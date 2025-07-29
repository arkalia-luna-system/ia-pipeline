#!/usr/bin/env python3
"""
🔍 ANALYSEUR AST DE BASE
========================
Module d'analyse AST pour extraire les informations de base
des fichiers Python. Utilisé par les autres modules d'analyse.
"""

import ast
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
import re

logger = logging.getLogger(__name__)


@dataclass
class ASTNodeInfo:
    """Informations extraites d'un nœud AST"""
    node_type: str
    name: str
    line_number: int
    complexity: int
    signature: str
    content: str


@dataclass
class FileAnalysis:
    """Analyse complète d'un fichier Python"""
    file_path: Path
    functions: List[ASTNodeInfo]
    classes: List[ASTNodeInfo]
    conditionals: List[ASTNodeInfo]
    loops: List[ASTNodeInfo]
    imports: List[str]
    total_lines: int
    complexity_score: float
    last_modified: datetime


class ASTAnalyzer:
    """Analyseur AST de base pour extraire les informations structurelles"""

    def __init__(self):
        self._cache = {}

    def analyze_file(self, file_path: Path) -> Optional[FileAnalysis]:
        """Analyser un fichier Python et extraire toutes les informations"""
        try:
            # Ignorer les fichiers cachés macOS
            if file_path.name.startswith('._'):
                return None

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            tree = ast.parse(content)

            functions = self._extract_functions(tree, content, file_path)
            classes = self._extract_classes(tree, content, file_path)
            conditionals = self._extract_conditionals(tree, content, file_path)
            loops = self._extract_loops(tree, content, file_path)
            imports = self._extract_imports(tree)

            complexity_score = self._calculate_complexity(tree)
            last_modified = datetime.fromtimestamp(file_path.stat().st_mtime)

            return FileAnalysis(
                file_path=file_path,
                functions=functions,
                classes=classes,
                conditionals=conditionals,
                loops=loops,
                imports=imports,
                total_lines=len(content.splitlines()),
                complexity_score=complexity_score,
                last_modified=last_modified
            )

        except Exception as e:
            logger.error(f"Erreur lors de l'analyse AST de {file_path}: {e}")
            return None

    def _extract_functions(
            self,
            tree: ast.AST,
            content: str,
            file_path: Path) -> List[ASTNodeInfo]:
        """Extraire toutes les fonctions du fichier"""
        functions = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = ASTNodeInfo(
                    node_type="function",
                    name=node.name,
                    line_number=node.lineno,
                    complexity=self._calculate_node_complexity(node),
                    signature=self._create_function_signature(node, content),
                    content=self._extract_node_content(node, content)
                )
                functions.append(func_info)

        return functions

    def _extract_classes(
            self,
            tree: ast.AST,
            content: str,
            file_path: Path) -> List[ASTNodeInfo]:
        """Extraire toutes les classes du fichier"""
        classes = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_info = ASTNodeInfo(
                    node_type="class",
                    name=node.name,
                    line_number=node.lineno,
                    complexity=self._calculate_node_complexity(node),
                    signature=self._create_class_signature(node, content),
                    content=self._extract_node_content(node, content)
                )
                classes.append(class_info)

        return classes

    def _extract_conditionals(
            self,
            tree: ast.AST,
            content: str,
            file_path: Path) -> List[ASTNodeInfo]:
        """Extraire toutes les structures conditionnelles"""
        conditionals = []

        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                cond_info = ASTNodeInfo(
                    node_type="conditional",
                    name=f"if_{node.lineno}",
                    line_number=node.lineno,
                    complexity=self._calculate_node_complexity(node),
                    signature=self._create_conditional_signature(
                        node,
                        content),
                    content=self._extract_node_content(
                        node,
                        content))
                conditionals.append(cond_info)

        return conditionals

    def _extract_loops(self, tree: ast.AST, content: str,
                       file_path: Path) -> List[ASTNodeInfo]:
        """Extraire toutes les boucles"""
        loops = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                loop_info = ASTNodeInfo(
                    node_type="loop",
                    name=f"{type(node).__name__.lower()}_{node.lineno}",
                    line_number=node.lineno,
                    complexity=self._calculate_node_complexity(node),
                    signature=self._create_loop_signature(node, content),
                    content=self._extract_node_content(node, content)
                )
                loops.append(loop_info)

        return loops

    def _extract_imports(self, tree: ast.AST) -> List[str]:
        """Extraire tous les imports"""
        imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")

        return imports

    def _create_function_signature(
            self,
            node: ast.FunctionDef,
            code: str) -> str:
        """Créer une signature unique pour une fonction"""
        # Extraire les paramètres
        args = []
        for arg in node.args.args:
            args.append(arg.arg)

        # Normaliser le code de la fonction
        func_code = self._extract_node_content(node, code)
        normalized = self._normalize_code(func_code)

        return f"function:{node.name}({','.join(args)}):{hash(normalized)}"

    def _create_class_signature(self, node: ast.ClassDef, code: str) -> str:
        """Créer une signature unique pour une classe"""
        # Extraire les méthodes
        methods = []
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                methods.append(child.name)

        # Normaliser le code de la classe
        class_code = self._extract_node_content(node, code)
        normalized = self._normalize_code(class_code)

        return f"class:{node.name}:{','.join(methods)}:{hash(normalized)}"

    def _create_conditional_signature(self, node: ast.If, code: str) -> str:
        """Créer une signature unique pour une condition"""
        cond_code = self._extract_node_content(node, code)
        normalized = self._normalize_code(cond_code)
        return f"conditional:{hash(normalized)}"

    def _create_loop_signature(self, node: ast.AST, code: str) -> str:
        """Créer une signature unique pour une boucle"""
        loop_code = self._extract_node_content(node, code)
        normalized = self._normalize_code(loop_code)
        return f"loop:{type(node).__name__}:{hash(normalized)}"

    def _extract_node_content(self, node: ast.AST, code: str) -> str:
        """Extraire le contenu d'un nœud AST"""
        lines = code.splitlines()
        start_line = getattr(node, 'lineno', 1) - 1
        end_line = getattr(node, 'end_lineno', start_line + 1)

        if end_line > len(lines):
            end_line = len(lines)

        return '\n'.join(lines[start_line:end_line])

    def _normalize_code(self, code: str) -> str:
        """Normaliser le code pour la comparaison"""
        # Supprimer les commentaires
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

        # Supprimer les espaces en début/fin
        code = code.strip()

        # Normaliser les espaces
        code = re.sub(r'\s+', ' ', code)

        # Supprimer les lignes vides
        code = re.sub(r'\n\s*\n', '\n', code)

        return code

    def _calculate_node_complexity(self, node: ast.AST) -> int:
        """Calculer la complexité cyclomatique d'un nœud"""
        complexity = 1

        for child in ast.walk(node):
            if isinstance(
                child,
                (ast.If,
                 ast.While,
                 ast.For,
                 ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1

        return complexity

    def _calculate_complexity(self, tree: ast.AST) -> float:
        """Calculer la complexité globale d'un arbre AST"""
        total_complexity = 0
        node_count = 0

        for node in ast.walk(tree):
            if isinstance(
                node,
                (ast.FunctionDef,
                 ast.ClassDef,
                 ast.If,
                 ast.While,
                 ast.For)):
                total_complexity += self._calculate_node_complexity(node)
                node_count += 1

        return total_complexity / max(node_count, 1)

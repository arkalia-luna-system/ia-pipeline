#!/usr/bin/env python3
"""
🏗️ ANALYSEUR D'ARCHITECTURE
============================
Module d'analyse d'architecture pour comprendre la structure
du projet, les dépendances et les relations entre modules.
"""

from dataclasses import dataclass
from datetime import datetime
import json
import logging
from pathlib import Path
import sqlite3
from typing import Any, Dict, List, Optional

import yaml

from .ast_analyzer import ASTAnalyzer, FileAnalysis


logger = logging.getLogger(__name__)


@dataclass
class ModuleAnalysis:
    """Analyse d'un module"""

    name: str
    path: str
    type: str
    size: int
    functions: List[str]
    classes: List[str]
    imports: List[str]
    dependencies: List[str]
    complexity: float
    issues: List[str]
    performance_score: float
    last_modified: datetime


@dataclass
class PerformanceIssue:
    """Problème de performance"""

    type: str
    location: str
    description: str
    impact: str
    suggestion: str


@dataclass
class ArchitectureMapping:
    """Mapping de l'architecture complète"""

    modules: Dict[str, ModuleAnalysis]
    dependencies: Dict[str, List[str]]
    duplicates: List[Any]  # DuplicateAnalysis
    performance_issues: List[PerformanceIssue]
    recommendations: List[str]


class ArchitectureAnalyzer:
    """Analyseur d'architecture pour comprendre la structure du projet"""

    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "architecture_analysis.db"
        self.config_path = self.root_path / "config" / "athalia_config.yaml"

        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialiser la base de données
        self._init_database()

        # Analyseur AST
        self.ast_analyzer = ASTAnalyzer()

        # Charger la configuration
        self.config = self._load_config()

        logger.info(f"🏗️ Architecture Analyzer initialisé dans {self.root_path}")

    def _init_database(self):
        """Initialiser la base de données d'architecture"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des modules
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS modules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    path TEXT NOT NULL,
                    type TEXT NOT NULL,
                    size INTEGER NOT NULL,
                    functions TEXT NOT NULL,
                    classes TEXT NOT NULL,
                    imports TEXT NOT NULL,
                    dependencies TEXT NOT NULL,
                    complexity REAL NOT NULL,
                    issues TEXT NOT NULL,
                    performance_score REAL NOT NULL,
                    last_modified TEXT NOT NULL,
                    analyzed_at TEXT NOT NULL
                )
            """
            )

            # Table des dépendances
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS dependencies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    module_name TEXT NOT NULL,
                    dependency_name TEXT NOT NULL,
                    dependency_type TEXT NOT NULL,
                    strength REAL DEFAULT 1.0,
                    created_at TEXT NOT NULL
                )
            """
            )

            # Table des problèmes de performance
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS performance_issues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_type TEXT NOT NULL,
                    location TEXT NOT NULL,
                    description TEXT NOT NULL,
                    impact TEXT NOT NULL,
                    suggestion TEXT NOT NULL,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT
                )
            """
            )

            conn.commit()

    def _load_config(self) -> Dict[str, Any]:
        """Charger la configuration"""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        return {}

    def analyze_entire_architecture(self) -> ArchitectureMapping:
        """Analyser l'architecture complète du projet"""
        logger.info("🏗️ Analyse de l'architecture complète...")

        # Analyser tous les modules
        modules = self._analyze_all_modules()

        # Détecter les doublons (utilise le pattern detector)
        duplicates = self._detect_duplicates(modules)

        # Analyser les performances
        performance_issues = self._analyze_performance(modules)

        # Construire le graphe de dépendances
        dependencies = self._build_dependency_graph(modules)

        # Générer les recommandations
        recommendations = self._generate_recommendations(
            modules, duplicates, performance_issues
        )

        # Créer le mapping d'architecture
        architecture = ArchitectureMapping(
            modules=modules,
            dependencies=dependencies,
            duplicates=duplicates,
            performance_issues=performance_issues,
            recommendations=recommendations,
        )

        # Sauvegarder l'analyse
        self._save_architecture_analysis(architecture)

        return architecture

    def _analyze_all_modules(self) -> Dict[str, ModuleAnalysis]:
        """Analyser tous les modules du projet"""
        modules = {}

        # Analyser les fichiers Python dans athalia_core (ignorer les fichiers
        # cachés)
        core_path = self.root_path / "athalia_core"
        if core_path.exists():
            for py_file in core_path.rglob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith("._"):
                    module_analysis = self._analyze_single_module(py_file, "core")
                    if module_analysis:
                        modules[module_analysis.name] = module_analysis

        # Analyser les fichiers Python dans tests (ignorer les fichiers cachés)
        tests_path = self.root_path / "tests"
        if tests_path.exists():
            for py_file in tests_path.rglob("*.py"):
                if not py_file.name.startswith("._"):
                    module_analysis = self._analyze_single_module(py_file, "test")
                    if module_analysis:
                        modules[module_analysis.name] = module_analysis

        # Analyser les fichiers Python dans setup (ignorer les fichiers cachés)
        setup_path = self.root_path / "setup"
        if setup_path.exists():
            for py_file in setup_path.rglob("*.py"):
                if not py_file.name.startswith("._"):
                    module_analysis = self._analyze_single_module(py_file, "setup")
                    if module_analysis:
                        modules[module_analysis.name] = module_analysis

        logger.info(f"📊 {len(modules)} modules analysés")
        return modules

    def _analyze_single_module(
        self, file_path: Path, module_type: str
    ) -> Optional[ModuleAnalysis]:
        """Analyser un module individuel"""
        try:
            # Analyser le fichier avec l'analyseur AST
            file_analysis = self.ast_analyzer.analyze_file(file_path)
            if not file_analysis:
                return None

            # Extraire les informations de base
            module_name = file_path.stem
            functions = [func.name for func in file_analysis.functions]
            classes = [cls.name for cls in file_analysis.classes]
            imports = file_analysis.imports

            # Analyser les dépendances
            dependencies = self._extract_dependencies(imports, module_type)

            # Détecter les problèmes
            issues = self._detect_module_issues(file_analysis)

            # Calculer le score de performance
            performance_score = self._calculate_performance_score(file_analysis)

            return ModuleAnalysis(
                name=module_name,
                path=str(file_path),
                type=module_type,
                size=file_analysis.total_lines,
                functions=functions,
                classes=classes,
                imports=imports,
                dependencies=dependencies,
                complexity=file_analysis.complexity_score,
                issues=issues,
                performance_score=performance_score,
                last_modified=file_analysis.last_modified,
            )

        except Exception as e:
            logger.error(f"Erreur lors de l'analyse du module {file_path}: {e}")
            return None

    def _extract_dependencies(self, imports: List[str], module_type: str) -> List[str]:
        """Extraire les dépendances d'un module"""
        dependencies = []

        for imp in imports:
            # Filtrer les imports internes au projet
            if imp.startswith("athalia_core."):
                dependencies.append(imp)
            elif imp.startswith("tests."):
                dependencies.append(imp)
            elif imp.startswith("setup."):
                dependencies.append(imp)
            # Ajouter les dépendances externes importantes
            elif imp in [
                "ast",
                "json",
                "logging",
                "sqlite3",
                "yaml",
                "pathlib",
            ]:
                dependencies.append(imp)

        return dependencies

    def _detect_module_issues(self, file_analysis: FileAnalysis) -> List[str]:
        """Détecter les problèmes dans un module"""
        issues = []

        # Vérifier la complexité
        if file_analysis.complexity_score > 10:
            issues.append(f"Complexité élevée: {file_analysis.complexity_score:.1f}")

        # Vérifier la taille
        if file_analysis.total_lines > 500:
            issues.append(f"Fichier très long: {file_analysis.total_lines} lignes")

        # Vérifier le nombre de fonctions
        if len(file_analysis.functions) > 20:
            issues.append(f"Trop de fonctions: {len(file_analysis.functions)}")

        # Vérifier le nombre de classes
        if len(file_analysis.classes) > 10:
            issues.append(f"Trop de classes: {len(file_analysis.classes)}")

        # Vérifier les imports
        if len(file_analysis.imports) > 30:
            issues.append(f"Trop d'imports: {len(file_analysis.imports)}")

        return issues

    def _calculate_performance_score(self, file_analysis: FileAnalysis) -> float:
        """Calculer un score de performance pour un module"""
        score = 100.0

        # Pénaliser la complexité
        if file_analysis.complexity_score > 5:
            score -= (file_analysis.complexity_score - 5) * 2

        # Pénaliser la taille
        if file_analysis.total_lines > 200:
            score -= (file_analysis.total_lines - 200) / 10

        # Pénaliser trop de fonctions
        if len(file_analysis.functions) > 10:
            score -= (len(file_analysis.functions) - 10) * 0.5

        # Pénaliser trop de classes
        if len(file_analysis.classes) > 5:
            score -= (len(file_analysis.classes) - 5) * 1

        return max(0.0, score)

    def _detect_duplicates(self, modules: Dict[str, ModuleAnalysis]) -> List[Any]:
        """Détecter les doublons entre modules"""
        # Cette fonction sera implémentée en utilisant le PatternDetector
        # Pour l'instant, retourner une liste vide
        return []

    def _analyze_performance(
        self, modules: Dict[str, ModuleAnalysis]
    ) -> List[PerformanceIssue]:
        """Analyser les problèmes de performance"""
        issues = []

        for module_name, module in modules.items():
            # Vérifier les scores de performance faibles
            if module.performance_score < 50:
                issue = PerformanceIssue(
                    type="low_performance",
                    location=module.path,
                    description=(
                        f"Module {module_name} a un score de performance faible: "
                        f"{module.performance_score:.1f}"
                    ),
                    impact="medium",
                    suggestion="Refactoriser pour réduire la complexité et la taille",
                )
                issues.append(issue)

            # Vérifier les modules très complexes
            if module.complexity > 15:
                issue = PerformanceIssue(
                    type="high_complexity",
                    location=module.path,
                    description=(
                        f"Module {module_name} très complexe: {module.complexity:.1f}"
                    ),
                    impact="high",
                    suggestion="Diviser en modules plus petits",
                )
                issues.append(issue)

        return issues

    def _build_dependency_graph(
        self, modules: Dict[str, ModuleAnalysis]
    ) -> Dict[str, List[str]]:
        """Construire le graphe de dépendances"""
        dependencies = {}

        for module_name, module in modules.items():
            dependencies[module_name] = module.dependencies

        return dependencies

    def _generate_recommendations(
        self,
        modules: Dict[str, ModuleAnalysis],
        duplicates: List[Any],
        performance_issues: List[PerformanceIssue],
    ) -> List[str]:
        """Générer des recommandations d'architecture"""
        recommendations = []

        # Recommandations basées sur les modules
        large_modules = [m for m in modules.values() if m.size > 300]
        if large_modules:
            recommendations.append(
                f"📦 {len(large_modules)} modules très grands détectés - "
                "considérer la division"
            )

        complex_modules = [m for m in modules.values() if m.complexity > 10]
        if complex_modules:
            recommendations.append(
                f"🧠 {len(complex_modules)} modules complexes - refactoring recommandé"
            )

        # Recommandations basées sur les performances
        if performance_issues:
            recommendations.append(
                f"⚡ {len(performance_issues)} problèmes de performance - "
                "optimisation nécessaire"
            )

        # Recommandations générales
        if len(modules) > 20:
            recommendations.append(
                "🏗️ Architecture complexe - documenter les dépendances"
            )

        return recommendations

    def _save_architecture_analysis(self, architecture: ArchitectureMapping):
        """Sauvegarder l'analyse d'architecture"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Sauvegarder les modules
            for module_name, module in architecture.modules.items():
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO modules
                    (name, path, type, size, functions, classes, imports, dependencies,
                     complexity, issues, performance_score, last_modified, analyzed_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        module.name,
                        module.path,
                        module.type,
                        module.size,
                        json.dumps(module.functions),
                        json.dumps(module.classes),
                        json.dumps(module.imports),
                        json.dumps(module.dependencies),
                        module.complexity,
                        json.dumps(module.issues),
                        module.performance_score,
                        module.last_modified.isoformat(),
                        datetime.now().isoformat(),
                    ),
                )

            # Sauvegarder les problèmes de performance
            for issue in architecture.performance_issues:
                cursor.execute(
                    """
                    INSERT INTO performance_issues
                    (issue_type, location, description, impact, suggestion, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        issue.type,
                        issue.location,
                        issue.description,
                        issue.impact,
                        issue.suggestion,
                        datetime.now().isoformat(),
                    ),
                )

            conn.commit()

    def get_optimization_plan(self) -> Dict[str, Any]:
        """Obtenir un plan d'optimisation basé sur l'analyse"""
        # Charger les données d'analyse
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Statistiques des modules
            cursor.execute("SELECT COUNT(*) FROM modules")
            total_modules = cursor.fetchone()[0]

            cursor.execute("SELECT AVG(complexity) FROM modules")
            avg_complexity = cursor.fetchone()[0] or 0

            cursor.execute("SELECT AVG(performance_score) FROM modules")
            avg_performance = cursor.fetchone()[0] or 0

            # Modules problématiques
            cursor.execute(
                "SELECT name, complexity, performance_score FROM modules "
                "WHERE complexity > 10 OR performance_score < 50"
            )
            problematic_modules = cursor.fetchall()

        return {
            "total_modules": total_modules,
            "average_complexity": avg_complexity,
            "average_performance": avg_performance,
            "problematic_modules": problematic_modules,
            "optimization_score": max(
                0, 100 - (avg_complexity * 2 + (100 - avg_performance) * 0.5)
            ),
        }

    def generate_intelligent_coordination(self) -> Dict[str, Any]:
        """Générer des recommandations de coordination intelligente"""
        optimization_plan = self.get_optimization_plan()

        coordination_plan = {
            "priority_tasks": [],
            "parallel_tasks": [],
            "dependencies": [],
            "estimated_time": 0,
        }

        # Tâches prioritaires basées sur l'analyse
        if optimization_plan["average_complexity"] > 8:
            coordination_plan["priority_tasks"].append(
                {
                    "task": "refactor_high_complexity_modules",
                    "description": "Refactoriser les modules très complexes",
                    "effort": "high",
                    "impact": "high",
                }
            )
            coordination_plan["estimated_time"] += 4  # heures

        if optimization_plan["average_performance"] < 70:
            coordination_plan["priority_tasks"].append(
                {
                    "task": "optimize_performance",
                    "description": "Optimiser les performances des modules",
                    "effort": "medium",
                    "impact": "medium",
                }
            )
            coordination_plan["estimated_time"] += 2  # heures

        return coordination_plan

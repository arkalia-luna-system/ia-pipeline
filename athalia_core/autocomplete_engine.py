#!/usr/bin/env python3
"""
Module autocomplete_engine pour Athalia
Moteur de complétion automatique intelligent
"""

from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import logging
import re
import ast
from collections import defaultdict

logger = logging.getLogger(__name__)


class AutocompleteEngine:
    """Moteur de complétion automatique"""

    def __init__(self, data_dir: str = ".autocomplete"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.suggestions = self.load_suggestions()
        self.context = {}

    def load_suggestions(self, suggestions_path: Optional[str] = None) -> Dict[str, List[str]]:
        """Charge les suggestions depuis un fichier"""
        default_suggestions = {
            "python": [
                "def", "class", "import", "from", "return", "if", "else", "elif",
                "for", "while", "try", "except", "finally", "with", "as",
                "True", "False", "None", "self", "super", "lambda", "yield",
                "async", "await", "raise", "assert", "del", "global", "nonlocal"
            ],
            "javascript": [
                "function", "const", "let", "var", "return", "if", "else",
                "for", "while", "try", "catch", "finally", "switch", "case",
                "default", "break", "continue", "throw", "class", "extends",
                "super", "new", "this", "async", "await", "export", "import"
            ],
            "html": [
                "<div>", "<span>", "<p>", "<h1>", "<h2>", "<h3>", "<h4>",
                "<h5>", "<h6>", "<ul>", "<ol>", "<li>", "<a>", "<img>",
                "<form>", "<input>", "<button>", "<table>", "<tr>", "<td>",
                "<th>", "<header>", "<footer>", "<nav>", "<section>", "<article>"
            ],
            "css": [
                "color", "background", "margin", "padding", "border", "width",
                "height", "display", "position", "float", "clear", "font-size",
                "font-weight", "text-align", "line-height", "opacity", "z-index"
            ]
        }
        
        if suggestions_path:
            try:
                with open(suggestions_path, 'r', encoding='utf-8') as f:
                    user_suggestions = json.load(f)
                    default_suggestions.update(user_suggestions)
            except Exception as e:
                logger.warning(f"Impossible de charger les suggestions {suggestions_path}: {e}")
        
        return default_suggestions

    def get_suggestions_for_context(self, context: str, partial: str) -> List[str]:
        """Récupère les suggestions pour un contexte donné"""
        try:
            if not context or context not in self.suggestions:
                return []
            
            suggestions = self.suggestions[context]
            filtered = self.filter_suggestions(suggestions, partial)
            ranked = self.rank_suggestions(filtered, partial)
            
            return ranked[:10]  # Limiter à 10 suggestions
            
        except Exception as e:
            logger.error(f"Erreur récupération suggestions: {e}")
            return []

    def filter_suggestions(self, suggestions: List[str], partial: str) -> List[str]:
        """Filtre les suggestions basées sur le texte partiel"""
        try:
            if not partial:
                return suggestions[:10]
            
            filtered = []
            partial_lower = partial.lower()
            
            for suggestion in suggestions:
                if partial_lower in suggestion.lower():
                    filtered.append(suggestion)
            
            return filtered
            
        except Exception as e:
            logger.error(f"Erreur filtrage suggestions: {e}")
            return []

    def rank_suggestions(self, suggestions: List[str], partial: str) -> List[str]:
        """Classe les suggestions par pertinence"""
        try:
            if not partial:
                return suggestions
            
            def score_suggestion(suggestion: str) -> int:
                suggestion_lower = suggestion.lower()
                partial_lower = partial.lower()
                
                # Score basé sur la position de la correspondance
                if suggestion_lower.startswith(partial_lower):
                    return 100  # Meilleur score pour les correspondances au début
                elif partial_lower in suggestion_lower:
                    return 50   # Score moyen pour les correspondances ailleurs
                else:
                    return 0    # Pas de correspondance
            
            # Trier par score décroissant
            ranked = sorted(suggestions, key=score_suggestion, reverse=True)
            return ranked
            
        except Exception as e:
            logger.error(f"Erreur classement suggestions: {e}")
            return suggestions

    def add_suggestion(self, context: str, suggestion: str) -> bool:
        """Ajoute une nouvelle suggestion"""
        try:
            if not context or not suggestion:
                return False
            
            if context not in self.suggestions:
                self.suggestions[context] = []
            
            if suggestion not in self.suggestions[context]:
                self.suggestions[context].append(suggestion)
            
            return True
            
        except Exception as e:
            logger.error(f"Erreur ajout suggestion: {e}")
            return False

    def remove_suggestion(self, context: str, suggestion: str) -> bool:
        """Supprime une suggestion"""
        try:
            if context in self.suggestions and suggestion in self.suggestions[context]:
                self.suggestions[context].remove(suggestion)
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Erreur suppression suggestion: {e}")
            return False

    def save_suggestions(self, suggestions_path: Optional[str] = None) -> bool:
        """Sauvegarde les suggestions dans un fichier"""
        try:
            if not suggestions_path:
                suggestions_path = self.data_dir / "suggestions.json"
            else:
                suggestions_path = Path(suggestions_path)
            
            with open(suggestions_path, 'w', encoding='utf-8') as f:
                json.dump(self.suggestions, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            logger.error(f"Erreur sauvegarde suggestions: {e}")
            return False

    def train_on_file(self, file_path: str) -> bool:
        """Entraîne le moteur sur un fichier"""
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                logger.error(f"Fichier non trouvé: {file_path}")
                return False
            
            # Détecter le langage basé sur l'extension
            language = self._detect_language(file_path)
            
            # Extraire les suggestions du fichier
            suggestions = self._extract_suggestions_from_file(file_path, language)
            
            # Ajouter les suggestions
            for suggestion in suggestions:
                self.add_suggestion(language, suggestion)
            
            return True
            
        except Exception as e:
            logger.error(f"Erreur entraînement fichier {file_path}: {e}")
            return False

    def train_on_directory(self, directory_path: str) -> bool:
        """Entraîne le moteur sur un répertoire"""
        try:
            directory_path = Path(directory_path)
            
            if not directory_path.exists() or not directory_path.is_dir():
                logger.error(f"Répertoire non trouvé: {directory_path}")
                return False
            
            # Parcourir tous les fichiers
            for file_path in directory_path.rglob("*"):
                if file_path.is_file():
                    self.train_on_file(str(file_path))
            
            return True
            
        except Exception as e:
            logger.error(f"Erreur entraînement répertoire {directory_path}: {e}")
            return False

    def get_context_suggestions(self) -> List[str]:
        """Récupère les suggestions basées sur le contexte actuel"""
        try:
            if not self.context:
                return []
            
            language = self.context.get("language", "")
            current_line = self.context.get("line", "")
            
            if language and current_line:
                return self.get_suggestions_for_context(language, current_line)
            
            return []
            
        except Exception as e:
            logger.error(f"Erreur suggestions contexte: {e}")
            return []

    def _detect_language(self, file_path: Path) -> str:
        """Détecte le langage basé sur l'extension du fichier"""
        extension = file_path.suffix.lower()
        
        language_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".html": "html",
            ".htm": "html",
            ".css": "css",
            ".scss": "scss",
            ".sass": "sass",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".h": "cpp",
            ".hpp": "cpp",
            ".php": "php",
            ".rb": "ruby",
            ".go": "go",
            ".rs": "rust",
            ".swift": "swift",
            ".kt": "kotlin",
            ".scala": "scala"
        }
        
        return language_map.get(extension, "text")

    def _extract_suggestions_from_file(self, file_path: Path, language: str) -> List[str]:
        """Extrait les suggestions d'un fichier"""
        try:
            suggestions = []
            
            if language == "python":
                suggestions = self._extract_python_suggestions(file_path)
            elif language == "javascript":
                suggestions = self._extract_javascript_suggestions(file_path)
            elif language == "html":
                suggestions = self._extract_html_suggestions(file_path)
            elif language == "css":
                suggestions = self._extract_css_suggestions(file_path)
            else:
                # Pour les autres langages, extraire les mots-clés
                suggestions = self._extract_generic_suggestions(file_path)
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction suggestions {file_path}: {e}")
            return []

    def _extract_python_suggestions(self, file_path: Path) -> List[str]:
        """Extrait les suggestions d'un fichier Python"""
        try:
            suggestions = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Analyser l'AST pour extraire les définitions
            try:
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        suggestions.append(node.name)
                    elif isinstance(node, ast.ClassDef):
                        suggestions.append(node.name)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            suggestions.append(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            suggestions.append(node.module)
                        for alias in node.names:
                            suggestions.append(alias.name)
                            
            except SyntaxError:
                # Si l'AST échoue, utiliser des regex
                suggestions.extend(self._extract_with_regex(content, r'def\s+(\w+)'))
                suggestions.extend(self._extract_with_regex(content, r'class\s+(\w+)'))
                suggestions.extend(self._extract_with_regex(content, r'import\s+(\w+)'))
                suggestions.extend(self._extract_with_regex(content, r'from\s+(\w+)'))
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction Python {file_path}: {e}")
            return []

    def _extract_javascript_suggestions(self, file_path: Path) -> List[str]:
        """Extrait les suggestions d'un fichier JavaScript"""
        try:
            suggestions = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les fonctions et variables
            suggestions.extend(self._extract_with_regex(content, r'function\s+(\w+)'))
            suggestions.extend(self._extract_with_regex(content, r'const\s+(\w+)'))
            suggestions.extend(self._extract_with_regex(content, r'let\s+(\w+)'))
            suggestions.extend(self._extract_with_regex(content, r'var\s+(\w+)'))
            suggestions.extend(self._extract_with_regex(content, r'class\s+(\w+)'))
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction JavaScript {file_path}: {e}")
            return []

    def _extract_html_suggestions(self, file_path: Path) -> List[str]:
        """Extrait les suggestions d'un fichier HTML"""
        try:
            suggestions = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les balises HTML
            suggestions.extend(self._extract_with_regex(content, r'<(\w+)'))
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction HTML {file_path}: {e}")
            return []

    def _extract_css_suggestions(self, file_path: Path) -> List[str]:
        """Extrait les suggestions d'un fichier CSS"""
        try:
            suggestions = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les propriétés CSS
            suggestions.extend(self._extract_with_regex(content, r'(\w+):'))
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction CSS {file_path}: {e}")
            return []

    def _extract_generic_suggestions(self, file_path: Path) -> List[str]:
        """Extrait les suggestions génériques d'un fichier"""
        try:
            suggestions = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraire les mots qui ressemblent à des identifiants
            suggestions.extend(self._extract_with_regex(content, r'\b(\w+)\s*='))
            suggestions.extend(self._extract_with_regex(content, r'\b(\w+)\s*\('))
            
            return suggestions
            
        except Exception as e:
            logger.error(f"Erreur extraction générique {file_path}: {e}")
            return []

    def _extract_with_regex(self, content: str, pattern: str) -> List[str]:
        """Extrait des suggestions avec une regex"""
        try:
            matches = re.findall(pattern, content)
            return list(set(matches))  # Supprimer les doublons
            
        except Exception as e:
            logger.error(f"Erreur regex {pattern}: {e}")
            return []


def get_suggestions(data_dir: str, context: str, partial: str) -> List[str]:
    """Fonction utilitaire pour obtenir des suggestions"""
    engine = AutocompleteEngine(data_dir)
    return engine.get_suggestions_for_context(context, partial)


def train_model(data_dir: str, file_path: str) -> bool:
    """Fonction utilitaire pour entraîner le modèle"""
    engine = AutocompleteEngine(data_dir)
    return engine.train_on_file(file_path)

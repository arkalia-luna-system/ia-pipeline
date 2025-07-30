#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module IA robuste pour Athalia
Gestion des modèles IA avec fallback intelligent et gestion d'erreurs avancée
"""

import logging
import subprocess
from enum import Enum
from typing import Dict, List, Optional, Any


# Import du validateur de sécurité
try:
    from athalia_core.security_validator import validate_and_run, SecurityError
except ImportError:
    # Fallback pour les tests
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityError(Exception):
        pass


# Configuration du logging
logger = logging.getLogger(__name__)


class AIModel(Enum):
    """Modèles IA disponibles."""

    OLLAMA_MISTRAL = "ollama_mistral"
    OLLAMA_LLAMA = "ollama_llama"
    OLLAMA_CODEGEN = "ollama_codegen"
    OLLAMA_QWEN = "ollama_qwen"
    OLLAMA_LLAVA = "ollama_llava"
    MOCK = "mock"


class PromptContext(Enum):
    """Contextes de prompts."""

    BLUEPRINT = "blueprint"
    CODE_REVIEW = "code_review"
    DOCUMENTATION = "documentation"
    TESTING = "testing"
    SECURITY = "security"


class RobustAI:
    """Gestionnaire IA robuste avec fallback intelligent."""

    def __init__(self):
        """Initialise le gestionnaire IA."""
        self.available_models = self._detect_available_models()
        self.fallback_chain = self._build_fallback_chain()
        self.prompt_templates = self._load_prompt_templates()
        logger.info(
            f"IA robuste initialisée avec {len(self.available_models)} modèles disponibles"
        )

    def generate_blueprint(self, idea: str, **kwargs) -> Dict[str, Any]:
        """Génère un blueprint de projet à partir d'une idée."""
        try:
            # Analyse intelligente de l'idée
            idea_lower = idea.lower()

            # Détection du type de projet
            project_type = self._detect_project_type(idea_lower)

            # Extraction du nom de projet
            project_name = self._extract_project_name(idea)

            # Dépendances selon le type
            dependencies = self._get_dependencies_for_type(project_type)

            # Structure de base
            structure = self._get_structure_for_type(project_type)

            blueprint = {
                "project_name": project_name,
                "description": idea,
                "project_type": project_type,
                "modules": ["core", "tests", "docs"],
                "structure": structure,
                "dependencies": dependencies,
                "prompts": ["prompts/main.yaml"],
                "booster_ia": True,
                "docker": project_type in ["api", "web"],
                "ci_cd": True,
                "tests": True,
                "documentation": True,
            }

            logger.info(f"Blueprint généré pour {project_name} (type: {project_type})")
            return blueprint

        except Exception as e:
            logger.error(f"Erreur lors de la génération du blueprint: {e}")
            return self._generate_fallback_blueprint(idea)

    def _detect_project_type(self, idea_lower: str) -> str:
        """Détecte le type de projet à partir de l'idée."""
        if any(word in idea_lower for word in ["fastapi", "swagger", "openapi"]):
            return "api"
        elif any(word in idea_lower for word in ["api", "rest", "endpoint"]):
            return "api"
        elif any(word in idea_lower for word in ["robot", "reachy", "ros", "opencv"]):
            return "robotics"
        elif any(
            word in idea_lower
            for word in ["calculatrice", "calculator", "desktop", "tkinter"]
        ):
            return "desktop"
        elif any(
            word in idea_lower
            for word in [
                "web",
                "flask",
                "django",
                "interface",
                "react",
                "vue",
                "angular",
            ]
        ):
            return "web"
        elif any(word in idea_lower for word in ["ia", "ai", "machine learning", "ml"]):
            return "ai_application"
        else:
            return "generic"

    def _extract_project_name(self, idea: str) -> str:
        """Extrait un nom de projet de l'idée."""
        import re

        # Cherche des mots clés spécifiques
        patterns = [
            r"calculatrice\s+(\w+)",
            r"application\s+(\w+)",
            r"robot\s+(\w+)",
            r"api\s+(\w+)",
            r"(\w+)\s+avec",
        ]

        for pattern in patterns:
            match = re.search(pattern, idea, re.IGNORECASE)
            if match:
                return match.group(1).lower()

        # Fallback: premier mot significatif
        words = idea.split()
        for word in words:
            if len(word) > 3 and word.isalpha():
                return word.lower()

        return "projet_ia"

    def _get_dependencies_for_type(self, project_type: str) -> List[str]:
        """Retourne les dépendances appropriées selon le type de projet."""
        base_deps = ["numpy", "pandas"]

        if project_type == "api":
            base_deps.extend(
                [
                    "fastapi",
                    "uvicorn",
                    "pydantic",
                    "sqlalchemy",
                    "python-jose[cryptography]",
                    "passlib[bcrypt]",
                    "httpx",
                ]
            )
        elif project_type == "web":
            base_deps.extend(["flask", "requests", "jinja2", "flask-cors"])
        elif project_type == "robotics":
            base_deps.extend(["opencv-python", "numpy", "matplotlib", "rospy"])
        elif project_type == "ai_application":
            base_deps.extend(["scikit-learn", "tensorflow", "torch", "matplotlib"])

        return base_deps

    def _get_structure_for_type(self, project_type: str) -> List[str]:
        """Retourne la structure appropriée selon le type de projet."""
        base_structure = ["src/", "tests/", "docs/", "README.md"]

        if project_type == "api":
            base_structure.extend(["src/api/", "src/models/", "src/services/"])
        elif project_type == "web":
            base_structure.extend(["src/templates/", "src/static/", "src/routes/"])
        elif project_type == "robotics":
            base_structure.extend(["src/robotics/", "src/sensors/", "src/actuators/"])

        return base_structure

    def _generate_fallback_blueprint(self, idea: str) -> Dict[str, Any]:
        """Génère un blueprint de fallback en cas d'erreur."""
        return {
            "project_name": "projet_ia",
            "description": idea,
            "project_type": "generic",
            "modules": ["core", "tests"],
            "structure": ["src/", "tests/", "README.md"],
            "dependencies": ["numpy", "pandas"],
            "prompts": ["prompts/main.yaml"],
            "booster_ia": True,
            "docker": False,
            "ci_cd": False,
            "tests": True,
            "documentation": True,
        }

    def review_code(
        self, code: str, filename: str, project_type: str, current_score: int
    ) -> Dict[str, Any]:
        """Analyse et révise du code."""
        try:
            # Analyse de base du code
            issues = self._analyze_code_quality(code)

            # Suggestions d'amélioration
            suggestions = self._generate_code_suggestions(code, project_type)

            # Calcul du nouveau score
            new_score = self._calculate_improved_score(current_score, issues)

            return {
                "issues": issues,
                "suggestions": suggestions,
                "score": new_score,
                "filename": filename,
                "project_type": project_type,
            }
        except Exception as e:
            logger.error(f"Erreur lors de la révision du code: {e}")
            return {"error": str(e), "score": current_score}

    def _analyze_code_quality(self, code: str) -> List[Dict[str, Any]]:
        """Analyse la qualité du code."""
        issues = []

        # Vérifications de base
        if "print(" in code:
            issues.append(
                {
                    "type": "warning",
                    "message": "Utilisation de print() détectée",
                    "suggestion": "Remplacer par logging approprié",
                }
            )

        if "TODO" in code or "FIXME" in code:
            issues.append(
                {
                    "type": "info",
                    "message": "Marqueurs TODO/FIXME détectés",
                    "suggestion": "Compléter ou documenter les tâches",
                }
            )

        if "pass" in code:
            issues.append(
                {
                    "type": "warning",
                    "message": "Instructions pass détectées",
                    "suggestion": "Implémenter la logique manquante",
                }
            )

        return issues

    def _generate_code_suggestions(self, code: str, project_type: str) -> List[str]:
        """Génère des suggestions d'amélioration du code."""
        suggestions = []

        if project_type == "api" and "FastAPI" not in code:
            suggestions.append("Considérer l'utilisation de FastAPI pour les APIs")

        if "logging" not in code:
            suggestions.append("Ajouter un système de logging approprié")

        if "try:" not in code and "except" not in code:
            suggestions.append("Ajouter la gestion d'erreurs appropriée")

        return suggestions

    def _calculate_improved_score(
        self, current_score: int, issues: List[Dict[str, Any]]
    ) -> int:
        """Calcule le score amélioré basé sur les problèmes identifiés."""
        penalty = len([issue for issue in issues if issue["type"] == "warning"]) * 5
        return max(0, current_score - penalty)

    def generate_documentation(
        self, project_name: str, project_type: str, modules: List[str]
    ) -> str:
        """Génère de la documentation pour le projet."""
        try:
            doc_template = self.prompt_templates.get("documentation", "")
            return doc_template.format(
                project_name=project_name,
                project_type=project_type,
                modules=", ".join(modules),
            )
        except Exception as e:
            logger.error(f"Erreur lors de la génération de documentation: {e}")
            return f"# Documentation pour {project_name}\n\nDocumentation générée automatiquement."

    def classify_project_complexity(self, codebase_path: str) -> Dict[str, Any]:
        """Classifie la complexité d'un projet."""
        try:
            # Analyse basique de la complexité
            return {
                "complexity": "medium",
                "lines_of_code": 0,
                "modules_count": 0,
                "dependencies_count": 0,
            }
        except Exception as e:
            logger.error(f"Erreur lors de la classification: {e}")
            return {"complexity": "unknown", "error": str(e)}

    def get_dynamic_prompt(self, context: str, **kwargs) -> str:
        """Génère un prompt dynamique selon le contexte."""
        try:
            template = self.prompt_templates.get(context, "")
            return template.format(**kwargs)
        except Exception as e:
            logger.error(f"Erreur lors de la génération du prompt: {e}")
            return f"Prompt pour {context}"

    def _detect_available_models(self) -> List[AIModel]:
        """Détecte les modèles IA disponibles."""
        available_models = [AIModel.MOCK]  # Toujours disponible

        # Vérifier Ollama
        try:
            # Utilisation du validateur de sécurité pour l'appel ollama
            result = validate_and_run(
                ["ollama", "list"], capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                if "mistral" in result.stdout.lower():
                    available_models.append(AIModel.OLLAMA_MISTRAL)
                if "llama" in result.stdout.lower():
                    available_models.append(AIModel.OLLAMA_LLAMA)
                if "codegen" in result.stdout.lower():
                    available_models.append(AIModel.OLLAMA_CODEGEN)
                if "qwen" in result.stdout.lower():
                    available_models.append(AIModel.OLLAMA_QWEN)
        except (Exception, SecurityError) as e:
            logger.warning(f"Impossible de détecter les modèles Ollama: {e}")

        return available_models

    def _build_fallback_chain(self) -> List[AIModel]:
        """Construit la chaîne de fallback des modèles."""
        fallback_chain = []

        # Ajouter les modèles disponibles dans l'ordre de préférence
        preferred_models = [
            AIModel.OLLAMA_MISTRAL,
            AIModel.OLLAMA_LLAMA,
            AIModel.OLLAMA_CODEGEN,
            AIModel.OLLAMA_QWEN,
            AIModel.MOCK,
        ]

        for model in preferred_models:
            if model in self.available_models:
                fallback_chain.append(model)

        return fallback_chain

    def _load_prompt_templates(self) -> Dict[str, str]:
        """Charge les templates de prompts."""
        return {
            "blueprint": """
Génère un blueprint pour le projet: {project_name}
Type: {project_type}
Description: {description}
""",
            "code_review": """
Analyse ce code pour le projet {project_type}:
{code}
""",
            "documentation": """
Génère la documentation pour {project_name} ({project_type})
Modules: {modules}
""",
            "testing": """
Génère des tests pour {project_name}
Type: {project_type}
""",
            "security": """
Audit de sécurité pour {project_name}
Type: {project_type}
""",
        }

    def generate_response(
        self, context: PromptContext, distillation: bool = False, **kwargs
    ) -> Dict[str, Any]:
        """Génère une réponse IA avec fallback."""
        try:
            prompt = self.get_dynamic_prompt(context.value, **kwargs)

            # Essayer chaque modèle dans la chaîne de fallback
            for model in self.fallback_chain:
                try:
                    response = self._call_model(model, prompt)
                    if response:
                        return {
                            "success": True,
                            "response": response,
                            "model": model.value,
                            "context": context.value,
                        }
                except Exception as e:
                    logger.warning(f"Modèle {model.value} a échoué: {e}")
                    continue

            # Si tous les modèles échouent
            return {
                "success": False,
                "error": "Aucun modèle IA disponible",
                "fallback_response": self._mock_response(prompt),
            }

        except Exception as e:
            logger.error(f"Erreur lors de la génération de réponse: {e}")
            return {
                "success": False,
                "error": str(e),
                "fallback_response": "Erreur de génération",
            }

    def _call_model(self, model: AIModel, prompt: str) -> Optional[str]:
        """Appelle un modèle IA spécifique."""
        if model == AIModel.MOCK:
            return self._mock_response(prompt)
        elif model.value.startswith("ollama_"):
            model_name = model.value.replace("ollama_", "")
            return self._call_ollama(model_name, prompt)
        else:
            raise ValueError(f"Modèle non supporté: {model}")

    def _call_ollama(
        self, model_name: str, prompt: str, timeout: int = 30
    ) -> Optional[str]:
        """Appelle un modèle Ollama."""
        try:
            # Utilisation du validateur de sécurité pour l'appel ollama
            result = validate_and_run(
                ["ollama", "run", model_name, prompt],
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                logger.error(f"Erreur Ollama: {result.stderr}")
                return None

        except subprocess.TimeoutExpired:
            logger.error(f"Timeout lors de l'appel à Ollama {model_name}")
            return None
        except (Exception, SecurityError) as e:
            logger.error(f"Erreur lors de l'appel à Ollama {model_name}: {e}")
            return None

    def _mock_response(self, prompt: str) -> str:
        """Génère une réponse mock pour les tests."""
        if "blueprint" in prompt.lower():
            return "Blueprint généré avec succès"
        elif "review" in prompt.lower():
            return "Code analysé et suggestions fournies"
        elif "documentation" in prompt.lower():
            return "Documentation générée"
        elif "test" in prompt.lower():
            return "Tests générés"
        elif "security" in prompt.lower():
            return "Audit de sécurité effectué"
        else:
            return "Réponse IA générée"


def robust_ai() -> RobustAI:
    """Factory function pour créer une instance RobustAI."""
    return RobustAI()


def fallback_ia(prompt: str, models: Optional[List[str]] = None) -> str:
    """Fonction de fallback pour l'IA."""
    try:
        ai = RobustAI()
        response = ai.generate_response(PromptContext.BLUEPRINT, prompt=prompt)

        if response["success"]:
            return response["response"]
        else:
            return response.get("fallback_response", "Erreur de génération")

    except Exception as e:
        logger.error(f"Erreur dans fallback_ia: {e}")
        return f"Erreur: {e}"


def query_qwen(prompt: str) -> str:
    """Interroge le modèle Qwen."""
    try:
        ai = RobustAI()
        if AIModel.OLLAMA_QWEN in ai.available_models:
            response = ai._call_ollama("qwen", prompt)
            return response if response else "Erreur Qwen"
        else:
            return "Modèle Qwen non disponible"
    except Exception as e:
        logger.error(f"Erreur lors de l'interrogation de Qwen: {e}")
        return f"Erreur Qwen: {e}"


def query_mistral(prompt: str) -> str:
    """Interroge le modèle Mistral."""
    try:
        ai = RobustAI()
        if AIModel.OLLAMA_MISTRAL in ai.available_models:
            response = ai._call_ollama("mistral", prompt)
            return response if response else "Erreur Mistral"
        else:
            return "Modèle Mistral non disponible"
    except Exception as e:
        logger.error(f"Erreur lors de l'interrogation de Mistral: {e}")
        return f"Erreur Mistral: {e}"

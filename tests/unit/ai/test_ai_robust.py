#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour le module IA robuste.
Couverture étendue avec tests d'intégration et de robustesse.
"""

from unittest.mock import Mock, patch

import pytest

from athalia_core.ai_robust import (
    AIModel,
    PromptContext,
    RobustAI,
    fallback_ia,
    query_mistral,
    query_qwen,
    robust_ai,
)


class TestRobustAI:
    """Tests complets pour l'IA robuste."""

    def setup_method(self):
        """Initialise l'IA robuste pour les tests - OPTIMISÉ."""
        self.ai = RobustAI()

        # Optimisé: Réduction de la consommation mémoire
        if hasattr(self.ai, "logger"):
            self.ai.logger.setLevel("ERROR")

    def test_detect_available_models(self):
        """Test la détection des modèles disponibles."""
        models = self.ai.available_models
        assert len(models) > 0
        assert AIModel.MOCK in models  # Mock toujours disponible
        assert isinstance(models, list)

    def test_build_fallback_chain(self):
        """Test la construction de la chaîne de fallback."""
        chain = self.ai.fallback_chain
        assert len(chain) > 0
        assert AIModel.MOCK in chain  # Mock toujours dans la chaîne
        assert isinstance(chain, list)

    def test_classify_project_complexity(self):
        """Test la classification de complexité des projets."""
        # Test simple
        assert (
            self.ai._classify_project_complexity("simple test f").get("complexity")
            == "f"
        )
        # Test medium
        assert (
            self.ai._classify_project_complexity("api web f").get("complexity") == "f"
        )
        # Test complex
        assert (
            self.ai._classify_project_complexity("ai neural f").get("complexity") == "f"
        )
        # Test default
        assert self.ai._classify_project_complexity("random f").get("complexity") == "f"

    def test_get_dynamic_prompt(self):
        """Test la génération de prompts dynamiques."""
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.BLUEPRINT, idea="test f", project_type="f", complexity="f"
        )
        assert "test f" in prompt
        assert "f" in prompt
        assert "f" in prompt
        assert "f" in prompt.lower()

    def test_generate_blueprint_with_mock(self):
        """Test la génération de blueprint avec fallback mock."""
        blueprint = self.ai.generate_bluelogger.info("test f")

        assert isinstance(blueprint, dict)
        assert "project_name" in blueprint
        assert "description" in blueprint
        assert "modules" in blueprint
        assert "structure" in blueprint
        assert "dependencies" in blueprint

    def test_review_code_with_mock(self):
        """Test la revue de code avec fallback mock."""
        code = """
def test_function():
    logger.info("f")
    return True
"""
        review = self.ai.review_code(
            code=code, filename="test.f(f", project_type="f", current_score=50
        )

        assert isinstance(review, dict)
        assert "score" in review
        assert "issues" in review
        assert "suggestions" in review

    def test_generate_documentation_with_mock(self):
        """Test la génération de documentation avec fallback mock."""
        doc = self.ai.generate_documentation(
            project_name="f", project_type="f", modules=["f", "f"]
        )

        assert isinstance(doc, str)
        assert "f" in doc
        assert "f" in doc or "f" in doc

    def test_call_ollama_timeout(self):
        """Test la gestion du timeout d'Ollama."""
        # Test avec un prompt qui devrait timeout
        result = self.ai._call_ollama(AIModel.OLLAMA_MISTRAL, "f", timeout=1)
        # Devrait retourner None en cas de timeout
        assert result is None or isinstance(result, str)

    def test_fallback_chain_behavior(self):
        """Test le comportement de la chaîne de fallback."""
        # Simuler un échec d'Ollama
        original_call = self.ai._call_ollama

        def mock_call_fail(model, prompt, timeout=60):
            return None

        self.ai._call_ollama = mock_call_fail

        try:
            # Devrait utiliser le mock en cas d'échec
            blueprint = self.ai.generate_bluelogger.info("test f")
            assert isinstance(blueprint, dict)
            assert "project_name" in blueprint
        finally:
            self.ai._call_ollama = original_call

    def test_extract_project_name(self):
        """Test l'extraction du nom de projet."""
        # Test avec pattern calculatrice
        name = self.ai._extract_project_name("calculatrice scientifique")
        assert name == "scientifique"

        # Test avec pattern application
        name = self.ai._extract_project_name("application gestion")
        assert name == "gestion"

        # Test avec pattern robot
        name = self.ai._extract_project_name("robot navigation")
        assert name == "navigation"

        # Test avec pattern api
        name = self.ai._extract_project_name("api utilisateurs")
        assert name == "utilisateurs"

        # Test avec pattern "avec"
        name = self.ai._extract_project_name("projet avec interface")
        assert name == "projet"

        # Test fallback
        name = self.ai._extract_project_name("simple test")
        assert name == "simple"

        # Test fallback final
        name = self.ai._extract_project_name("a b c")
        assert name == "projet_ia"

    def test_generate_blueprint_project_types(self):
        """Test la génération de blueprint pour différents types de projets."""
        # Test API
        blueprint = self.ai.generate_blueprint("api rest pour utilisateurs")
        assert blueprint["project_type"] == "api"
        assert "fastapi" in blueprint["dependencies"]
        assert "auth" in blueprint["modules"]

        # Test Web
        blueprint = self.ai.generate_blueprint("application web flask")
        assert blueprint["project_type"] == "web"
        assert "flask" in blueprint["dependencies"]
        assert "templates" in blueprint["modules"]

        # Test Robotics
        blueprint = self.ai.generate_blueprint("robot reachy navigation")
        assert blueprint["project_type"] == "robotics"
        assert "opencv-python" in blueprint["dependencies"]
        assert "vision" in blueprint["modules"]

        # Test Desktop
        blueprint = self.ai.generate_blueprint("calculatrice desktop")
        assert blueprint["project_type"] == "desktop"
        assert "tkinter" in blueprint["dependencies"]

        # Test AI
        blueprint = self.ai.generate_blueprint("application ia machine learning")
        assert blueprint["project_type"] == "ai_application"
        assert "scikit-learn" in blueprint["dependencies"]

        # Test Generic
        blueprint = self.ai.generate_blueprint("projet simple")
        assert blueprint["project_type"] == "generic"
        assert "numpy" in blueprint["dependencies"]

    def test_classify_project_complexity_method(self):
        """Test la méthode publique de classification."""
        result = self.ai.classify_project_complexity("test_path")
        assert isinstance(result, dict)
        assert "complexity" in result
        assert "score" in result

    def test_get_dynamic_prompt_method(self):
        """Test la méthode publique de prompt dynamique."""
        prompt = self.ai.get_dynamic_prompt("blueprint")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_get_dynamic_prompt_with_formatting_error(self):
        """Test la gestion d'erreur de formatage dans les prompts."""
        # Test avec des paramètres manquants
        prompt = self.ai._get_dynamic_prompt(PromptContext.BLUEPRINT, idea="test")
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_detect_available_models_with_ollama_error(self):
        """Test la détection avec erreur Ollama."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_validate.side_effect = Exception("Ollama error")
            ai = RobustAI()
            assert AIModel.MOCK in ai.available_models

    def test_detect_available_models_with_ollama_failure(self):
        """Test la détection avec échec Ollama."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_result = Mock()
            mock_result.returncode = 1
            mock_validate.return_value = mock_result
            ai = RobustAI()
            assert AIModel.MOCK in ai.available_models

    def test_detect_available_models_with_ollama_success(self):
        """Test la détection avec succès Ollama."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_result = Mock()
            mock_result.returncode = 0
            mock_result.stdout = "qwen mistral llava llama codegen"
            mock_validate.return_value = mock_result
            ai = RobustAI()
            assert AIModel.OLLAMA_QWEN in ai.available_models
            assert AIModel.OLLAMA_MISTRAL in ai.available_models

    def test_call_ollama_success(self):
        """Test l'appel Ollama réussi."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_result = Mock()
            mock_result.returncode = 0
            mock_result.stdout = "Réponse Ollama"
            mock_validate.return_value = mock_result

            result = self.ai._call_ollama("mistral", "test prompt")
            assert result == "Réponse Ollama"

    def test_call_ollama_failure(self):
        """Test l'appel Ollama échoué."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_result = Mock()
            mock_result.returncode = 1
            mock_result.stderr = "Erreur Ollama"
            mock_validate.return_value = mock_result

            result = self.ai._call_ollama("mistral", "test prompt")
            assert result is None

    def test_call_ollama_exception(self):
        """Test l'appel Ollama avec exception."""
        with patch("athalia_core.ai_robust.validate_and_run") as mock_validate:
            mock_validate.side_effect = Exception("Erreur système")

            result = self.ai._call_ollama("mistral", "test prompt")
            assert result is None

    def test_call_model_unsupported(self):
        """Test l'appel d'un modèle non supporté."""
        # Créer un enum personnalisé pour simuler un modèle non supporté
        from enum import Enum

        class UnsupportedModel(Enum):
            UNSUPPORTED = "unsupported"

        result = self.ai._call_model(UnsupportedModel.UNSUPPORTED, "test prompt")
        assert result is None

    def test_mock_response_blueprint(self):
        """Test la réponse mock pour blueprint."""
        response = self.ai._mock_response("blueprint test")
        assert "project_name" in response
        assert "projet_ia_exemple" in response

    def test_mock_response_code_review(self):
        """Test la réponse mock pour code review."""
        response = self.ai._mock_response("code_review test")
        assert "score" in response
        assert "issues" in response

    def test_mock_response_generic(self):
        """Test la réponse mock générique."""
        response = self.ai._mock_response("test prompt")
        assert "Réponse mock" in response

    def test_generate_response_success(self):
        """Test la génération de réponse réussie."""
        with patch.object(self.ai, "_call_model") as mock_call:
            mock_call.return_value = "Réponse réussie"

            result = self.ai.generate_response(
                PromptContext.BLUEPRINT,
                idea="test",
                project_type="test",
                complexity="simple",
            )

            assert result["success"] is True
            assert result["response"] == "Réponse réussie"
            assert "model" in result

    def test_generate_response_fallback(self):
        """Test la génération de réponse avec fallback."""
        with patch.object(self.ai, "_call_model") as mock_call:
            mock_call.return_value = None

            result = self.ai.generate_response(
                PromptContext.BLUEPRINT,
                idea="test",
                project_type="test",
                complexity="simple",
            )

            assert result["success"] is False
            assert result["model"] == "mock"
            assert "error" in result

    def test_generate_response_with_exception(self):
        """Test la génération de réponse avec exception."""
        with patch.object(self.ai, "_call_model") as mock_call:
            mock_call.side_effect = Exception("Erreur modèle")

            result = self.ai.generate_response(
                PromptContext.BLUEPRINT,
                idea="test",
                project_type="test",
                complexity="simple",
            )

            assert result["success"] is False
            assert result["model"] == "mock"


def test_robust_ai_integration():
    """Test d'intégration de l'IA robuste."""
    ai = RobustAI()

    # Test complet du workflow
    blueprint = ai.generate_bluelogger.info("api web f")
    assert isinstance(blueprint, dict)

    # Test avec contexte
    blueprint_with_context = ai.generate_bluelogger.info(
        "ai f", context={"project_type": "ai", "complexity": "high"}
    )
    assert isinstance(blueprint_with_context, dict)


def test_prompt_templates():
    """Test que tous les templates de prompts sont chargés."""
    ai = RobustAI()

    contexts = [
        PromptContext.BLUEPRINT,
        PromptContext.CODE_REVIEW,
        PromptContext.DOCUMENTATION,
        PromptContext.TESTING,
        PromptContext.SECURITY,
    ]

    for context in contexts:
        template = ai.prompt_templates.get(context.value)
        assert template is not None
        assert len(template) > 0
        assert isinstance(template, str)


def test_fallback_and_distillation_qwen_mistral():
    """Teste la génération de réponse avec fallback et distillation (Qwen/Mistral)."""
    ai = RobustAI()
    ai.available_models = [
        getattr(AIModel, "OLLAMA_QWEN", AIModel.MOCK),
        getattr(AIModel, "OLLAMA_MISTRAL", AIModel.MOCK),
        AIModel.MOCK,
    ]
    ai.fallback_chain = ai._build_fallback_chain()

    # Test fallback séquentiel
    result_fallback = ai.generate_response(
        PromptContext.BLUEPRINT,
        distillation=False,
        idea="test fallback",
        project_type="test",
        complexity="simple",
    )
    assert isinstance(result_fallback, dict)
    assert "model" in result_fallback
    assert "response" in result_fallback
    assert "success" in result_fallback
    assert "context" in result_fallback

    # Test distillation (maintenant géré différemment)
    result_distill = ai.generate_response(
        PromptContext.BLUEPRINT,
        distillation=True,
        idea="test distillation",
        project_type="test",
        complexity="simple",
    )
    assert isinstance(result_distill, dict)
    assert "model" in result_distill
    assert "response" in result_distill
    assert "success" in result_distill
    assert "context" in result_distill


def test_fallback_ia_qwen_mistral(monkeypatch):
    """Test de la fonction fallback_ia avec Qwen et Mistral."""
    from athalia_core.ai_robust import fallback_ia

    # Mock les requêtes pour Qwen et Mistral
    def mock_query_qwen(prompt):
        return "Réponse Qwen"

    def mock_query_mistral(prompt):
        return "Réponse Mistral"

    import athalia_core.ai_robust as ai_robust

    ai_robust.query_qwen = mock_query_qwen
    ai_robust.query_mistral = mock_query_mistral
    result = fallback_ia("Test prompt", models=["qwen", "mistral"])
    assert result == "Réponse Qwen"
    result2 = fallback_ia("Test prompt", models=["mistral"])
    assert result2 == "Réponse Mistral"


def test_robust_ai_factory():
    """Test de la fonction factory robust_ai."""
    ai = robust_ai()
    assert isinstance(ai, RobustAI)


def test_fallback_ia_default_models():
    """Test de fallback_ia avec les modèles par défaut."""
    with patch("athalia_core.ai_robust.query_qwen") as mock_qwen:
        mock_qwen.return_value = "Réponse Qwen"
        result = fallback_ia("Test prompt")
        assert result == "Réponse Qwen"


def test_fallback_ia_no_response():
    """Test de fallback_ia sans réponse."""
    with patch("athalia_core.ai_robust.query_qwen") as mock_qwen:
        mock_qwen.return_value = ""
        result = fallback_ia("Test prompt", models=["qwen", "mock"])
        assert result == "Réponse mock générée."


def test_fallback_ia_all_fail():
    """Test de fallback_ia avec tous les modèles qui échouent."""
    with patch("athalia_core.ai_robust.query_qwen") as mock_qwen:
        mock_qwen.return_value = ""
        result = fallback_ia("Test prompt", models=["qwen"])
        assert result == "[Aucune réponse IA]"


@patch("requests.post")
def test_query_qwen_success(mock_post):
    """Test de query_qwen avec succès."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"response": "Réponse Qwen"}
    mock_post.return_value = mock_response

    result = query_qwen("Test prompt")
    assert result == "Réponse Qwen"


@patch("requests.post")
def test_query_qwen_failure(mock_post):
    """Test de query_qwen avec échec."""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_post.return_value = mock_response

    result = query_qwen("Test prompt")
    assert result == ""


@patch("requests.post")
def test_query_qwen_exception(mock_post):
    """Test de query_qwen avec exception."""
    mock_post.side_effect = Exception("Erreur réseau")

    result = query_qwen("Test prompt")
    assert result == ""


@patch("requests.post")
def test_query_mistral_success(mock_post):
    """Test de query_mistral avec succès."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"response": "Réponse Mistral"}
    mock_post.return_value = mock_response

    result = query_mistral("Test prompt")
    assert result == "Réponse Mistral"


@patch("requests.post")
def test_query_mistral_failure(mock_post):
    """Test de query_mistral avec échec."""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_post.return_value = mock_response

    result = query_mistral("Test prompt")
    assert result == ""


@patch("requests.post")
def test_query_mistral_exception(mock_post):
    """Test de query_mistral avec exception."""
    mock_post.side_effect = Exception("Erreur réseau")

    result = query_mistral("Test prompt")
    assert result == ""


def test_ai_model_enum():
    """Test des valeurs de l'enum AIModel."""
    assert AIModel.OLLAMA_MISTRAL.value == "ollama_mistral"
    assert AIModel.OLLAMA_LLAMA.value == "ollama_llama"
    assert AIModel.OLLAMA_CODEGEN.value == "ollama_codegen"
    assert AIModel.OLLAMA_QWEN.value == "ollama_qwen"
    assert AIModel.OLLAMA_LLAVA.value == "ollama_llava"
    assert AIModel.MOCK.value == "mock"


def test_prompt_context_enum():
    """Test des valeurs de l'enum PromptContext."""
    assert PromptContext.BLUEPRINT.value == "blueprint"
    assert PromptContext.CODE_REVIEW.value == "code_review"
    assert PromptContext.DOCUMENTATION.value == "documentation"
    assert PromptContext.TESTING.value == "testing"
    assert PromptContext.SECURITY.value == "security"


def test_robust_ai_initialization():
    """Test de l'initialisation complète de RobustAI."""
    ai = RobustAI()

    assert hasattr(ai, "available_models")
    assert hasattr(ai, "fallback_chain")
    assert hasattr(ai, "prompt_templates")

    assert isinstance(ai.available_models, list)
    assert isinstance(ai.fallback_chain, list)
    assert isinstance(ai.prompt_templates, dict)

    assert len(ai.available_models) > 0
    assert len(ai.fallback_chain) > 0
    assert len(ai.prompt_templates) > 0


def test_blueprint_proxy_property():
    """Test de la propriété generate_bluelogger."""
    ai = RobustAI()
    proxy = ai.generate_bluelogger

    assert hasattr(proxy, "info")
    assert callable(proxy.info)

    # Test de l'appel via le proxy
    result = proxy.info("test project")
    assert isinstance(result, dict)
    assert "project_name" in result


def test_security_validator_import_fallback():
    """Test du fallback d'import du validateur de sécurité."""
    # Simuler l'absence du module security_validator
    import sys

    original_modules = sys.modules.copy()

    # Supprimer temporairement le module
    if "athalia_core.security_validator" in sys.modules:
        del sys.modules["athalia_core.security_validator"]

    try:
        # Recharger le module pour tester le fallback
        import importlib

        import athalia_core.ai_robust

        importlib.reload(athalia_core.ai_robust)

        # Vérifier que les fonctions de fallback sont disponibles
        assert hasattr(athalia_core.ai_robust, "validate_and_run")
        assert hasattr(athalia_core.ai_robust, "SecurityError")

        # Test que SecurityError est une exception
        assert issubclass(athalia_core.ai_robust.SecurityError, Exception)

    finally:
        # Restaurer les modules originaux
        sys.modules.clear()
        sys.modules.update(original_modules)


def test_security_error_handling():
    """Test de la gestion des erreurs de sécurité."""
    from athalia_core.ai_robust import SecurityError

    # Test que SecurityError peut être levée et attrapée
    try:
        raise SecurityError("Test d'erreur de sécurité")
    except SecurityError as e:
        assert str(e) == "Test d'erreur de sécurité"


def test_validate_and_run_fallback():
    """Test de la fonction validate_and_run de fallback."""
    from athalia_core.ai_robust import validate_and_run

    # Test que la fonction existe et peut être appelée
    assert callable(validate_and_run)

    # Test avec une commande simple
    result = validate_and_run(["echo", "test"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "test" in result.stdout


def test_classify_project_complexity_fallback():
    """Test de la méthode _classify_project_complexity avec fallback."""
    ai = RobustAI()

    # Test avec un chemin qui ne contient pas 'f'
    result = ai._classify_project_complexity("test_path")
    assert isinstance(result, dict)
    assert "complexity" in result


def test_main_block_execution():
    """Test de l'exécution du bloc main."""
    # Simuler l'exécution du bloc main
    ai = RobustAI()

    # Test que les modèles sont détectés
    models = ai.available_models
    assert len(models) > 0

    # Test de génération de réponse
    response = ai.generate_response(
        PromptContext.BLUEPRINT,
        idea="Assistant IA pour la gestion de projets",
        project_type="ai_assistant",
        complexity="medium",
    )
    assert isinstance(response, dict)
    assert "model" in response
    assert "response" in response


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov-report=term-missing"])

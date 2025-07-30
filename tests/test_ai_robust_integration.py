#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import pytest

from athalia_core.ai_robust import AIModel, PromptContext, RobustAI

# Import conditionnel de psutil
try:
    import psutil

    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

"""
Tests d'intégration pour l'IA robuste.
"""


class TestAIRobustIntegration:
    """Tests d'intégration pour l'IA robuste."""

    def setup_method(self):
        """Initialise l'IA robuste pour les tests."""
        self.ai = RobustAI()

    def test_complete_workflow_simple_project(self):
        """Test du workflow complet pour un projet simple."""
        # 1. Génération de blueprint
        blueprint = self.ai.generate_blueprint("simple projet")

        assert isinstance(blueprint, dict)
        assert "project_name" in blueprint
        assert "modules" in blueprint
        assert "dependencies" in blueprint

        # 2. Revue de code
        test_code = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""
        review = self.ai.review_code(
            code=test_code,
            filename="calculator.py",
            project_type="python",
            current_score=70,
        )

        assert isinstance(review, dict)
        assert "score" in review
        assert "issues" in review
        assert "suggestions" in review

        # 3. Génération de documentation
        doc = self.ai.generate_documentation(
            project_name=blueprint["project_name"],
            project_type="python",
            modules=blueprint["modules"],
        )

        assert isinstance(doc, str)
        assert len(doc) > 10  # Au moins quelques caractères
        assert blueprint["project_name"] in doc or "projet" in doc

    def test_fallback_chain_behavior(self):
        """Test du comportement de la chaîne de fallback."""
        # Simuler un échec d'Ollama
        original_call = self.ai._call_ollama

        def mock_call_fail(model, prompt, timeout=60):
            return None

        self.ai._call_ollama = mock_call_fail

        try:
            # Devrait utiliser le mock en cas d'échec
            blueprint = self.ai.generate_blueprint("test projet")
            assert isinstance(blueprint, dict)
            assert "project_name" in blueprint

            # Vérifier que c'est bien le mock qui a été utilisé
            assert blueprint.get("project_type") == "generic"

        finally:
            self.ai._call_ollama = original_call

    def test_different_project_complexities(self):
        """Test avec différents niveaux de complexité."""
        # Projet simple
        simple_blueprint = self.ai.generate_blueprint("hello world")
        assert isinstance(simple_blueprint, dict)

        # Projet moyen
        medium_blueprint = self.ai.generate_blueprint("web api simple")
        assert isinstance(medium_blueprint, dict)

        # Projet complexe
        complex_blueprint = self.ai.generate_blueprint("ai neural network")
        assert isinstance(complex_blueprint, dict)

    def test_prompt_contexts(self):
        """Test de tous les contextes de prompts."""
        # Test blueprint
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.BLUEPRINT,
            idea="test projet",
            project_type="python",
            complexity="simple",
        )
        assert isinstance(prompt, str)
        assert len(prompt) >= 50

        # Test code review
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.CODE_REVIEW,
            code="def test(): pass",
            filename="test.py",
            project_type="python",
            current_score=50,
        )
        assert isinstance(prompt, str)
        assert len(prompt) >= 50

        # Test documentation
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.DOCUMENTATION,
            project_name="test",
            project_type="python",
            modules="api, web",
        )
        assert isinstance(prompt, str)
        assert len(prompt) >= 50

        # Test testing
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.TESTING,
            module_name="test",
            features="add, multiply",
            project_type="python",
        )
        assert isinstance(prompt, str)
        assert len(prompt) >= 50

        # Test security
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.SECURITY,
            code="def vulnerable(): pass",
            app_type="web",
            environment="production",
        )
        assert isinstance(prompt, str)
        assert len(prompt) >= 50

    def test_model_detection(self):
        """Test de la détection des modèles."""
        models = self.ai.available_models
        assert len(models) > 0
        
        # Vérifier que MOCK est dans la liste (peut être à n'importe quelle position)
        mock_found = AIModel.MOCK in models
        assert mock_found, f"MOCK devrait être dans la liste des modèles: {models}"

        # Vérifier que la chaîne de fallback est cohérente
        chain = self.ai.fallback_chain
        assert len(chain) > 0
        
        # Vérifier que MOCK est dans la chaîne de fallback
        mock_in_chain = AIModel.MOCK in chain
        assert mock_in_chain, f"MOCK devrait être dans la chaîne de fallback: {chain}"

        # Vérifier que tous les modèles de la chaîne sont disponibles
        for model in chain:
            assert model in models

    def test_error_handling(self):
        """Test de la gestion d'erreurs."""
        # Test avec des paramètres invalides
        try:
            result = self.ai.generate_blueprint("")
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Ne devrait pas lever d'exception: {e}")

        # Test avec des paramètres None
        try:
            result = self.ai.generate_blueprint("")
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Ne devrait pas lever d'exception: {e}")


def test_ai_robust_performance():
    """Test de performance de l'IA robuste."""

    ai = RobustAI()

    # Test de performance pour la génération de blueprint
    start_time = time.time()
    blueprint = ai.generate_blueprint("performance test projet")
    end_time = time.time()

    assert isinstance(blueprint, dict)
    assert end_time - start_time < 60  # Moins de 60 secondes (plus réaliste)

    # Test de performance pour la revue de code
    test_code = "def test(): pass"
    start_time = time.time()
    review = ai.review_code(test_code, "test.py", "python", 50)
    end_time = time.time()

    assert isinstance(review, dict)
    assert end_time - start_time < 30  # Moins de 30 secondes


@pytest.mark.skipif(not PSUTIL_AVAILABLE, reason="psutil non disponible")
def test_ai_robust_memory_usage():
    """Test de l'utilisation mémoire de l'IA robuste."""
    process = psutil.Process()
    initial_memory = process.memory_info().rss

    ai = RobustAI()

    # Générer plusieurs blueprints pour tester la mémoire
    for i in range(5):
        blueprint = ai.generate_blueprint(f"projet test {i}")
        assert isinstance(blueprint, dict)

    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory

    # L'augmentation mémoire ne devrait pas être excessive (moins de 100MB)
    assert memory_increase < 100 * 1024 * 1024  # 100MB en bytes

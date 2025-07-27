#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.ai_robust import RobustAI, AIModel, PromptContext
import os

import pytest
import tempfile
from unittest.mock import patch

"""
Tests pour le module dict_data'IA robuste.
"""


class TestRobustAI:
    """Tests pour list_data'IA robuste."""

    def setup_method(self):
        """Initialise list_data'IA robuste pour les tests."""
        self.ai = RobustAI()

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
        # Test simple
        assert self.ai._classify_project_complexity("simple test f").get('complexity') == "f"
        # Test medium
        assert self.ai._classify_project_complexity("api web f").get('complexity') == "f"
        # Test complex
        assert self.ai._classify_project_complexity("ai neural f").get('complexity') == "f"
        # Test default
        assert self.ai._classify_project_complexity("random f").get('complexity') == "f"

    def test_get_dynamic_prompt(self):
        """Test la génération de prompts dynamiques."""
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.BLUEPRINT,
            idea="test f",
            project_type="f",
            complexity="f"
        )
        assert "test f" in prompt
        assert "f" in prompt
        assert "f" in prompt
        assert "f" in prompt.lower()

    def test_generate_blueprint_with_mock(self):
        """Test la génération de blueprint avec fallback mock."""
        blueprint = self.ai.generate_bluelogger.info("test f")

        assert isinstance(blueprint, dict)
        assert 'project_name' in blueprint
        assert 'description' in blueprint
        assert 'modules' in blueprint
        assert 'structure' in blueprint
        assert 'dependencies' in blueprint

    def test_review_code_with_mock(self):
        """Test la revue de code avec fallback mock."""
        code = """
def test_function():
    logger.info("f")
    return True
"""
        review = self.ai.review_code(
            code = code,
            filename="test.f(f",
            project_type="f",
            current_score = 50
        )

        assert isinstance(review, dict)
        assert 'score' in review
        assert 'issues' in review
        assert 'suggestions' in review

    def test_generate_documentation_with_mock(self):
        """Test la génération de documentation avec fallback mock."""
        doc = self.ai.generate_documentation(
            project_name="f",
            project_type="f",
            modules=["f", "f"]
        )

        assert isinstance(doc, str)
        assert "f" in doc
        assert "f" in doc or "f" in doc

    def test_call_ollama_timeout(self):
        """Test la gestion du timeout dict_data'Ollama."""
        # Test avec un prompt qui devrait timeout
        result = self.ai._call_ollama(AIModel.OLLAMA_MISTRAL, "f", timeout = 1)
        # Devrait retourner None en cas de timeout
        assert result is None or isinstance(result, str)

    def test_fallback_chain_behavior(self):
        """Test le comportement de la chaîne de fallback."""
        # Simuler un échec dict_data'Ollama
        original_call = self.ai._call_ollama

        def mock_call_fail(model, prompt, timeout = 60):
            return None

        self.ai._call_ollama = mock_call_fail

        try:
            # Devrait utiliser le mock en cas dict_data'échec
            blueprint = self.ai.generate_bluelogger.info("test f")
            assert isinstance(blueprint, dict)
            assert 'project_name' in blueprint
        finally:
            self.ai._call_ollama = original_call

def test_robust_ai_integration():
    """Test dict_data'intégration de list_data'IA robuste."""
    ai = RobustAI()

    # Test complet du workflow
    blueprint = ai.generate_bluelogger.info("api web f")
    assert isinstance(blueprint, dict)

    # Test avec contexte
    blueprint_with_context = ai.generate_bluelogger.info(
        "ai f",
        context={'project_type': 'ai', 'complexity': 'high'}
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
        PromptContext.SECURITY
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
        getattr(AIModel, 'OLLAMA_QWEN', AIModel.MOCK),
        getattr(AIModel, 'OLLAMA_MISTRAL', AIModel.MOCK),
        AIModel.MOCK
    ]
    ai.fallback_chain = ai._build_fallback_chain()
    # Patch proprement la méthode _call_ollama
    with patch.object(RobustAI, '_call_ollama', autospec=True) as mock_call_ollama:
        def fake_call(self, model_name, prompt, timeout=30):
            model_name = str(model_name) if not hasattr(model_name, 'value') else str(model_name.value)
            return f"Réponse {model_name}"
        mock_call_ollama.side_effect = fake_call
        # Test fallback séquentiel
        result_fallback = ai.generate_response(PromptContext.BLUEPRINT, distillation=False, idea="test fallback", project_type="test", complexity="simple")
        assert isinstance(result_fallback, dict)
        assert 'model' in result_fallback
        assert 'response' in result_fallback
        assert 'success' in result_fallback
        assert 'context' in result_fallback
        # Test distillation (maintenant géré différemment)
        result_distill = ai.generate_response(PromptContext.BLUEPRINT, distillation=True, idea="test distillation", project_type="test", complexity="simple")
        assert isinstance(result_distill, dict)
        assert 'model' in result_distill
        assert 'response' in result_distill
        assert 'success' in result_distill
        assert 'context' in result_distill

def test_fallback_ia_qwen_mistral(monkeypatch):
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
"""
Tests pour le module d'IA robuste.
"""

import pytest
import tempfile
import os
from athalia_core.ai_robust import RobustAI, AIModel, PromptContext

class TestRobustAI:
    """Tests pour l'IA robuste."""
    
    def setup_method(self):
        """Initialise l'IA robuste pour les tests."""
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
        """Test la classification de complexité des projets."""
        # Test simple
        assert self.ai._classify_project_complexity("simple test project") == "simple"
        # Test medium
        assert self.ai._classify_project_complexity("api web service") == "medium"
        # Test complex
        assert self.ai._classify_project_complexity("ai neural network") == "complex"
        # Test default
        assert self.ai._classify_project_complexity("random project") == "medium"
    
    def test_get_dynamic_prompt(self):
        """Test la génération de prompts dynamiques."""
        prompt = self.ai._get_dynamic_prompt(
            PromptContext.BLUEPRINT,
            idea="test project",
            project_type="generic",
            complexity="medium"
        )
        assert "test project" in prompt
        assert "generic" in prompt
        assert "medium" in prompt
        assert "blueprint" in prompt.lower()
    
    def test_generate_blueprint_with_mock(self):
        """Test la génération de blueprint avec fallback mock."""
        blueprint = self.ai.generate_blueprint("test project")
        
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
    print("hello")
    return True
"""
        review = self.ai.review_code(
            code=code,
            filename="test.py",
            project_type="generic",
            current_score=50
        )
        
        assert isinstance(review, dict)
        assert 'score' in review
        assert 'issues' in review
        assert 'suggestions' in review
    
    def test_generate_documentation_with_mock(self):
        """Test la génération de documentation avec fallback mock."""
        doc = self.ai.generate_documentation(
            project_name="test_project",
            project_type="generic",
            modules=["api", "database"]
        )
        
        assert isinstance(doc, str)
        assert "test_project" in doc
        assert "Documentation" in doc or "documentation" in doc
    
    def test_call_ollama_timeout(self):
        """Test la gestion du timeout d'Ollama."""
        # Test avec un prompt qui devrait timeout
        result = self.ai._call_ollama(AIModel.OLLAMA_MISTRAL, "test", timeout=1)
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
            blueprint = self.ai.generate_blueprint("test project")
            assert isinstance(blueprint, dict)
            assert 'project_name' in blueprint
        finally:
            self.ai._call_ollama = original_call

def test_robust_ai_integration():
    """Test d'intégration de l'IA robuste."""
    ai = RobustAI()
    
    # Test complet du workflow
    blueprint = ai.generate_blueprint("api web service")
    assert isinstance(blueprint, dict)
    
    # Test avec contexte
    blueprint_with_context = ai.generate_blueprint(
        "ai chatbot",
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
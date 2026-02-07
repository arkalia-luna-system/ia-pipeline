"""
Tests unitaires générés pour prompts
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import prompts
except ImportError:
    pytest.skip(f"Module prompts non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, '__init__')
    assert callable(getattr(prompts, '__init__'))

def test_vi_mode():
    """Test de la fonction vi_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'vi_mode')
    assert callable(getattr(prompts, 'vi_mode'))

def test_in_prompt_tokens():
    """Test de la fonction in_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'in_prompt_tokens')
    assert callable(getattr(prompts, 'in_prompt_tokens'))

def test__width():
    """Test de la fonction _width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, '_width')
    assert callable(getattr(prompts, '_width'))

def test_continuation_prompt_tokens():
    """Test de la fonction continuation_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'continuation_prompt_tokens')
    assert callable(getattr(prompts, 'continuation_prompt_tokens'))

def test_rewrite_prompt_tokens():
    """Test de la fonction rewrite_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'rewrite_prompt_tokens')
    assert callable(getattr(prompts, 'rewrite_prompt_tokens'))

def test_out_prompt_tokens():
    """Test de la fonction out_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'out_prompt_tokens')
    assert callable(getattr(prompts, 'out_prompt_tokens'))

def test_in_prompt_tokens():
    """Test de la fonction in_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'in_prompt_tokens')
    assert callable(getattr(prompts, 'in_prompt_tokens'))

def test_continuation_prompt_tokens():
    """Test de la fonction continuation_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'continuation_prompt_tokens')
    assert callable(getattr(prompts, 'continuation_prompt_tokens'))

def test_rewrite_prompt_tokens():
    """Test de la fonction rewrite_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'rewrite_prompt_tokens')
    assert callable(getattr(prompts, 'rewrite_prompt_tokens'))

def test_out_prompt_tokens():
    """Test de la fonction out_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'out_prompt_tokens')
    assert callable(getattr(prompts, 'out_prompt_tokens'))

def test_write_output_prompt():
    """Test de la fonction write_output_prompt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'write_output_prompt')
    assert callable(getattr(prompts, 'write_output_prompt'))

def test_write_format_data():
    """Test de la fonction write_format_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prompts, 'write_format_data')
    assert callable(getattr(prompts, 'write_format_data'))

class TestPrompts:
    """Tests pour la classe Prompts"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prompts, 'Prompts')
        assert isinstance(getattr(prompts, 'Prompts'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prompts, 'Prompts')
        for method_name in ['__init__', 'vi_mode', 'in_prompt_tokens', '_width', 'continuation_prompt_tokens', 'rewrite_prompt_tokens', 'out_prompt_tokens']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClassicPrompts:
    """Tests pour la classe ClassicPrompts"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prompts, 'ClassicPrompts')
        assert isinstance(getattr(prompts, 'ClassicPrompts'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prompts, 'ClassicPrompts')
        for method_name in ['in_prompt_tokens', 'continuation_prompt_tokens', 'rewrite_prompt_tokens', 'out_prompt_tokens']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRichPromptDisplayHook:
    """Tests pour la classe RichPromptDisplayHook"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prompts, 'RichPromptDisplayHook')
        assert isinstance(getattr(prompts, 'RichPromptDisplayHook'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prompts, 'RichPromptDisplayHook')
        for method_name in ['write_output_prompt', 'write_format_data']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

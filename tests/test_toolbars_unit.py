"""
Tests unitaires générés pour toolbars
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import toolbars
except ImportError:
    pytest.skip(f"Module toolbars non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test__get_display_before_text():
    """Test de la fonction _get_display_before_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_get_display_before_text')
    assert callable(getattr(toolbars, '_get_display_before_text'))

def test__build_key_bindings():
    """Test de la fonction _build_key_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_build_key_bindings')
    assert callable(getattr(toolbars, '_build_key_bindings'))

def test___pt_container__():
    """Test de la fonction __pt_container__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__pt_container__')
    assert callable(getattr(toolbars, '__pt_container__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test___pt_container__():
    """Test de la fonction __pt_container__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__pt_container__')
    assert callable(getattr(toolbars, '__pt_container__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test___pt_container__():
    """Test de la fonction __pt_container__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__pt_container__')
    assert callable(getattr(toolbars, '__pt_container__'))

def test_create_content():
    """Test de la fonction create_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'create_content')
    assert callable(getattr(toolbars, 'create_content'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test___pt_container__():
    """Test de la fonction __pt_container__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__pt_container__')
    assert callable(getattr(toolbars, '__pt_container__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__init__')
    assert callable(getattr(toolbars, '__init__'))

def test___pt_container__():
    """Test de la fonction __pt_container__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '__pt_container__')
    assert callable(getattr(toolbars, '__pt_container__'))

def test__cancel():
    """Test de la fonction _cancel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_cancel')
    assert callable(getattr(toolbars, '_cancel'))

def test__cancel_vi():
    """Test de la fonction _cancel_vi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_cancel_vi')
    assert callable(getattr(toolbars, '_cancel_vi'))

def test__focus_me():
    """Test de la fonction _focus_me"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_focus_me')
    assert callable(getattr(toolbars, '_focus_me'))

def test__focus_me_vi():
    """Test de la fonction _focus_me_vi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, '_focus_me_vi')
    assert callable(getattr(toolbars, '_focus_me_vi'))

def test_get_formatted_text():
    """Test de la fonction get_formatted_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'get_formatted_text')
    assert callable(getattr(toolbars, 'get_formatted_text'))

def test_is_searching():
    """Test de la fonction is_searching"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'is_searching')
    assert callable(getattr(toolbars, 'is_searching'))

def test_get_before_input():
    """Test de la fonction get_before_input"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'get_before_input')
    assert callable(getattr(toolbars, 'get_before_input'))

def test_get_line():
    """Test de la fonction get_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'get_line')
    assert callable(getattr(toolbars, 'get_line'))

def test_get_formatted_text():
    """Test de la fonction get_formatted_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toolbars, 'get_formatted_text')
    assert callable(getattr(toolbars, 'get_formatted_text'))

class TestFormattedTextToolbar:
    """Tests pour la classe FormattedTextToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'FormattedTextToolbar')
        assert isinstance(getattr(toolbars, 'FormattedTextToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'FormattedTextToolbar')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSystemToolbar:
    """Tests pour la classe SystemToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'SystemToolbar')
        assert isinstance(getattr(toolbars, 'SystemToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'SystemToolbar')
        for method_name in ['__init__', '_get_display_before_text', '_build_key_bindings', '__pt_container__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestArgToolbar:
    """Tests pour la classe ArgToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'ArgToolbar')
        assert isinstance(getattr(toolbars, 'ArgToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'ArgToolbar')
        for method_name in ['__init__', '__pt_container__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSearchToolbar:
    """Tests pour la classe SearchToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'SearchToolbar')
        assert isinstance(getattr(toolbars, 'SearchToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'SearchToolbar')
        for method_name in ['__init__', '__pt_container__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_CompletionsToolbarControl:
    """Tests pour la classe _CompletionsToolbarControl"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, '_CompletionsToolbarControl')
        assert isinstance(getattr(toolbars, '_CompletionsToolbarControl'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, '_CompletionsToolbarControl')
        for method_name in ['create_content']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCompletionsToolbar:
    """Tests pour la classe CompletionsToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'CompletionsToolbar')
        assert isinstance(getattr(toolbars, 'CompletionsToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'CompletionsToolbar')
        for method_name in ['__init__', '__pt_container__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestValidationToolbar:
    """Tests pour la classe ValidationToolbar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toolbars, 'ValidationToolbar')
        assert isinstance(getattr(toolbars, 'ValidationToolbar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toolbars, 'ValidationToolbar')
        for method_name in ['__init__', '__pt_container__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

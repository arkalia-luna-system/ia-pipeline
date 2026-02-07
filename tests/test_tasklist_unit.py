"""
Tests unitaires générés pour tasklist
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tasklist
except ImportError:
    pytest.skip(f"Module tasklist non importable")


def test_get_checkbox():
    """Test de la fonction get_checkbox"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'get_checkbox')
    assert callable(getattr(tasklist, 'get_checkbox'))

def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'makeExtension')
    assert callable(getattr(tasklist, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, '__init__')
    assert callable(getattr(tasklist, '__init__'))

def test_inline():
    """Test de la fonction inline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'inline')
    assert callable(getattr(tasklist, 'inline'))

def test_sub_paragraph():
    """Test de la fonction sub_paragraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'sub_paragraph')
    assert callable(getattr(tasklist, 'sub_paragraph'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'run')
    assert callable(getattr(tasklist, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, '__init__')
    assert callable(getattr(tasklist, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tasklist, 'extendMarkdown')
    assert callable(getattr(tasklist, 'extendMarkdown'))

class TestTasklistTreeprocessor:
    """Tests pour la classe TasklistTreeprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tasklist, 'TasklistTreeprocessor')
        assert isinstance(getattr(tasklist, 'TasklistTreeprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tasklist, 'TasklistTreeprocessor')
        for method_name in ['__init__', 'inline', 'sub_paragraph', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTasklistExtension:
    """Tests pour la classe TasklistExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tasklist, 'TasklistExtension')
        assert isinstance(getattr(tasklist, 'TasklistExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tasklist, 'TasklistExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

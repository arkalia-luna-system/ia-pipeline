"""
Tests unitaires générés pour codehilite
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import codehilite
except ImportError:
    pytest.skip(f"Module codehilite non importable")


def test_parse_hl_lines():
    """Test de la fonction parse_hl_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'parse_hl_lines')
    assert callable(getattr(codehilite, 'parse_hl_lines'))

def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'makeExtension')
    assert callable(getattr(codehilite, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, '__init__')
    assert callable(getattr(codehilite, '__init__'))

def test_hilite():
    """Test de la fonction hilite"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'hilite')
    assert callable(getattr(codehilite, 'hilite'))

def test__parseHeader():
    """Test de la fonction _parseHeader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, '_parseHeader')
    assert callable(getattr(codehilite, '_parseHeader'))

def test_code_unescape():
    """Test de la fonction code_unescape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'code_unescape')
    assert callable(getattr(codehilite, 'code_unescape'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'run')
    assert callable(getattr(codehilite, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, '__init__')
    assert callable(getattr(codehilite, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(codehilite, 'extendMarkdown')
    assert callable(getattr(codehilite, 'extendMarkdown'))

class TestCodeHilite:
    """Tests pour la classe CodeHilite"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(codehilite, 'CodeHilite')
        assert isinstance(getattr(codehilite, 'CodeHilite'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(codehilite, 'CodeHilite')
        for method_name in ['__init__', 'hilite', '_parseHeader']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHiliteTreeprocessor:
    """Tests pour la classe HiliteTreeprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(codehilite, 'HiliteTreeprocessor')
        assert isinstance(getattr(codehilite, 'HiliteTreeprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(codehilite, 'HiliteTreeprocessor')
        for method_name in ['code_unescape', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCodeHiliteExtension:
    """Tests pour la classe CodeHiliteExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(codehilite, 'CodeHiliteExtension')
        assert isinstance(getattr(codehilite, 'CodeHiliteExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(codehilite, 'CodeHiliteExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

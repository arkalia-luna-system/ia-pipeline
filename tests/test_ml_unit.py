"""
Tests unitaires générés pour ml
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ml
except ImportError:
    pytest.skip(f"Module ml non importable")


def test_stringy():
    """Test de la fonction stringy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ml, 'stringy')
    assert callable(getattr(ml, 'stringy'))

def test_long_id_callback():
    """Test de la fonction long_id_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ml, 'long_id_callback')
    assert callable(getattr(ml, 'long_id_callback'))

def test_end_id_callback():
    """Test de la fonction end_id_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ml, 'end_id_callback')
    assert callable(getattr(ml, 'end_id_callback'))

def test_id_callback():
    """Test de la fonction id_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ml, 'id_callback')
    assert callable(getattr(ml, 'id_callback'))

class TestSMLLexer:
    """Tests pour la classe SMLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ml, 'SMLLexer')
        assert isinstance(getattr(ml, 'SMLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ml, 'SMLLexer')
        for method_name in ['stringy', 'long_id_callback', 'end_id_callback', 'id_callback']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOcamlLexer:
    """Tests pour la classe OcamlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ml, 'OcamlLexer')
        assert isinstance(getattr(ml, 'OcamlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ml, 'OcamlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOpaLexer:
    """Tests pour la classe OpaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ml, 'OpaLexer')
        assert isinstance(getattr(ml, 'OpaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ml, 'OpaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestReasonLexer:
    """Tests pour la classe ReasonLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ml, 'ReasonLexer')
        assert isinstance(getattr(ml, 'ReasonLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ml, 'ReasonLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFStarLexer:
    """Tests pour la classe FStarLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ml, 'FStarLexer')
        assert isinstance(getattr(ml, 'FStarLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ml, 'FStarLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

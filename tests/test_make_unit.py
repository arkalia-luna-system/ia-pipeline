"""
Tests unitaires générés pour make
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import make
except ImportError:
    pytest.skip(f"Module make non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(make, 'get_tokens_unprocessed')
    assert callable(getattr(make, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(make, 'analyse_text')
    assert callable(getattr(make, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(make, 'analyse_text')
    assert callable(getattr(make, 'analyse_text'))

class TestMakefileLexer:
    """Tests pour la classe MakefileLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(make, 'MakefileLexer')
        assert isinstance(getattr(make, 'MakefileLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(make, 'MakefileLexer')
        for method_name in ['get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseMakefileLexer:
    """Tests pour la classe BaseMakefileLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(make, 'BaseMakefileLexer')
        assert isinstance(getattr(make, 'BaseMakefileLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(make, 'BaseMakefileLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCMakeLexer:
    """Tests pour la classe CMakeLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(make, 'CMakeLexer')
        assert isinstance(getattr(make, 'CMakeLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(make, 'CMakeLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

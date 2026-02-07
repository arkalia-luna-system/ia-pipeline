"""
Tests unitaires générés pour matlab
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import matlab
except ImportError:
    pytest.skip(f"Module matlab non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(matlab, 'analyse_text')
    assert callable(getattr(matlab, 'analyse_text'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(matlab, 'get_tokens_unprocessed')
    assert callable(getattr(matlab, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(matlab, 'analyse_text')
    assert callable(getattr(matlab, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(matlab, 'analyse_text')
    assert callable(getattr(matlab, 'analyse_text'))

class TestMatlabLexer:
    """Tests pour la classe MatlabLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(matlab, 'MatlabLexer')
        assert isinstance(getattr(matlab, 'MatlabLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(matlab, 'MatlabLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMatlabSessionLexer:
    """Tests pour la classe MatlabSessionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(matlab, 'MatlabSessionLexer')
        assert isinstance(getattr(matlab, 'MatlabSessionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(matlab, 'MatlabSessionLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOctaveLexer:
    """Tests pour la classe OctaveLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(matlab, 'OctaveLexer')
        assert isinstance(getattr(matlab, 'OctaveLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(matlab, 'OctaveLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestScilabLexer:
    """Tests pour la classe ScilabLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(matlab, 'ScilabLexer')
        assert isinstance(getattr(matlab, 'ScilabLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(matlab, 'ScilabLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

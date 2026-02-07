"""
Tests unitaires générés pour prolog
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import prolog
except ImportError:
    pytest.skip(f"Module prolog non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prolog, 'analyse_text')
    assert callable(getattr(prolog, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prolog, 'analyse_text')
    assert callable(getattr(prolog, 'analyse_text'))

class TestPrologLexer:
    """Tests pour la classe PrologLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prolog, 'PrologLexer')
        assert isinstance(getattr(prolog, 'PrologLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prolog, 'PrologLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLogtalkLexer:
    """Tests pour la classe LogtalkLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prolog, 'LogtalkLexer')
        assert isinstance(getattr(prolog, 'LogtalkLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prolog, 'LogtalkLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

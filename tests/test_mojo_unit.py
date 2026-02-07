"""
Tests unitaires générés pour mojo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mojo
except ImportError:
    pytest.skip(f"Module mojo non importable")


def test_innerstring_rules():
    """Test de la fonction innerstring_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mojo, 'innerstring_rules')
    assert callable(getattr(mojo, 'innerstring_rules'))

def test_fstring_rules():
    """Test de la fonction fstring_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mojo, 'fstring_rules')
    assert callable(getattr(mojo, 'fstring_rules'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mojo, 'analyse_text')
    assert callable(getattr(mojo, 'analyse_text'))

class TestMojoLexer:
    """Tests pour la classe MojoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mojo, 'MojoLexer')
        assert isinstance(getattr(mojo, 'MojoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mojo, 'MojoLexer')
        for method_name in ['innerstring_rules', 'fstring_rules', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour bdd
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bdd
except ImportError:
    pytest.skip(f"Module bdd non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bdd, 'analyse_text')
    assert callable(getattr(bdd, 'analyse_text'))

class TestBddLexer:
    """Tests pour la classe BddLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bdd, 'BddLexer')
        assert isinstance(getattr(bdd, 'BddLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bdd, 'BddLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

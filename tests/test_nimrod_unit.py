"""
Tests unitaires générés pour nimrod
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nimrod
except ImportError:
    pytest.skip(f"Module nimrod non importable")


def test_underscorize():
    """Test de la fonction underscorize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nimrod, 'underscorize')
    assert callable(getattr(nimrod, 'underscorize'))

class TestNimrodLexer:
    """Tests pour la classe NimrodLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nimrod, 'NimrodLexer')
        assert isinstance(getattr(nimrod, 'NimrodLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nimrod, 'NimrodLexer')
        for method_name in ['underscorize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour sdist
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sdist
except ImportError:
    pytest.skip(f"Module sdist non importable")


def test_add_defaults():
    """Test de la fonction add_defaults"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sdist, 'add_defaults')
    assert callable(getattr(sdist, 'add_defaults'))

class Testsdist:
    """Tests pour la classe sdist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sdist, 'sdist')
        assert isinstance(getattr(sdist, 'sdist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sdist, 'sdist')
        for method_name in ['add_defaults']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

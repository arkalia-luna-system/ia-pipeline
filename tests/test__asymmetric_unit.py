"""
Tests unitaires générés pour _asymmetric
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _asymmetric
except ImportError:
    pytest.skip(f"Module _asymmetric non importable")


def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asymmetric, 'name')
    assert callable(getattr(_asymmetric, 'name'))

class TestAsymmetricPadding:
    """Tests pour la classe AsymmetricPadding"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_asymmetric, 'AsymmetricPadding')
        assert isinstance(getattr(_asymmetric, 'AsymmetricPadding'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_asymmetric, 'AsymmetricPadding')
        for method_name in ['name']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

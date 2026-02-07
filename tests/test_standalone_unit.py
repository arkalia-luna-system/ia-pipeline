"""
Tests unitaires générés pour standalone
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import standalone
except ImportError:
    pytest.skip(f"Module standalone non importable")


def test_get_transforms():
    """Test de la fonction get_transforms"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(standalone, 'get_transforms')
    assert callable(getattr(standalone, 'get_transforms'))

class TestReader:
    """Tests pour la classe Reader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(standalone, 'Reader')
        assert isinstance(getattr(standalone, 'Reader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(standalone, 'Reader')
        for method_name in ['get_transforms']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

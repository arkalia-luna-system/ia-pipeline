"""
Tests unitaires générés pour overlay
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import overlay
except ImportError:
    pytest.skip(f"Module overlay non importable")


def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(overlay, '__hash__')
    assert callable(getattr(overlay, '__hash__'))

class TestHashableNamespace:
    """Tests pour la classe HashableNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(overlay, 'HashableNamespace')
        assert isinstance(getattr(overlay, 'HashableNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(overlay, 'HashableNamespace')
        for method_name in ['__hash__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

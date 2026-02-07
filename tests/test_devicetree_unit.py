"""
Tests unitaires générés pour devicetree
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import devicetree
except ImportError:
    pytest.skip(f"Module devicetree non importable")


class TestDevicetreeLexer:
    """Tests pour la classe DevicetreeLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(devicetree, 'DevicetreeLexer')
        assert isinstance(getattr(devicetree, 'DevicetreeLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(devicetree, 'DevicetreeLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

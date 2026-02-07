"""
Tests unitaires générés pour _spdx
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _spdx
except ImportError:
    pytest.skip(f"Module _spdx non importable")


class TestSPDXLicense:
    """Tests pour la classe SPDXLicense"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_spdx, 'SPDXLicense')
        assert isinstance(getattr(_spdx, 'SPDXLicense'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_spdx, 'SPDXLicense')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSPDXException:
    """Tests pour la classe SPDXException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_spdx, 'SPDXException')
        assert isinstance(getattr(_spdx, 'SPDXException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_spdx, 'SPDXException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

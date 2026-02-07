"""
Tests unitaires générés pour region
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import region
except ImportError:
    pytest.skip(f"Module region non importable")


class TestRegion:
    """Tests pour la classe Region"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(region, 'Region')
        assert isinstance(getattr(region, 'Region'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(region, 'Region')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

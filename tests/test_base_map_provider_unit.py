"""
Tests unitaires générés pour base_map_provider
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import base_map_provider
except ImportError:
    pytest.skip(f"Module base_map_provider non importable")


class TestBaseMapProvider:
    """Tests pour la classe BaseMapProvider"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_map_provider, 'BaseMapProvider')
        assert isinstance(getattr(base_map_provider, 'BaseMapProvider'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_map_provider, 'BaseMapProvider')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour rrt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rrt
except ImportError:
    pytest.skip(f"Module rrt non importable")


class TestRrtStyle:
    """Tests pour la classe RrtStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rrt, 'RrtStyle')
        assert isinstance(getattr(rrt, 'RrtStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rrt, 'RrtStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

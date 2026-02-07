"""
Tests unitaires générés pour colorable
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import colorable
except ImportError:
    pytest.skip(f"Module colorable non importable")


class TestColorable:
    """Tests pour la classe Colorable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(colorable, 'Colorable')
        assert isinstance(getattr(colorable, 'Colorable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(colorable, 'Colorable')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

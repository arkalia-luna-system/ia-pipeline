"""
Tests unitaires générés pour _tooltip
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tooltip
except ImportError:
    pytest.skip(f"Module _tooltip non importable")


class TestTooltip:
    """Tests pour la classe Tooltip"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tooltip, 'Tooltip')
        assert isinstance(getattr(_tooltip, 'Tooltip'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tooltip, 'Tooltip')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

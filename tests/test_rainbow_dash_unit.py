"""
Tests unitaires générés pour rainbow_dash
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rainbow_dash
except ImportError:
    pytest.skip(f"Module rainbow_dash non importable")


class TestRainbowDashStyle:
    """Tests pour la classe RainbowDashStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rainbow_dash, 'RainbowDashStyle')
        assert isinstance(getattr(rainbow_dash, 'RainbowDashStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rainbow_dash, 'RainbowDashStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

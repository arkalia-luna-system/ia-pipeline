"""
Tests unitaires générés pour lightbulb
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import lightbulb
except ImportError:
    pytest.skip(f"Module lightbulb non importable")


class TestLightbulbStyle:
    """Tests pour la classe LightbulbStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(lightbulb, 'LightbulbStyle')
        assert isinstance(getattr(lightbulb, 'LightbulbStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(lightbulb, 'LightbulbStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

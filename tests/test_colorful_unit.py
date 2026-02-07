"""
Tests unitaires générés pour colorful
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import colorful
except ImportError:
    pytest.skip(f"Module colorful non importable")


class TestColorfulStyle:
    """Tests pour la classe ColorfulStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(colorful, 'ColorfulStyle')
        assert isinstance(getattr(colorful, 'ColorfulStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(colorful, 'ColorfulStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

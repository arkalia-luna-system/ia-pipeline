"""
Tests unitaires générés pour inkpot
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import inkpot
except ImportError:
    pytest.skip(f"Module inkpot non importable")


class TestInkPotStyle:
    """Tests pour la classe InkPotStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(inkpot, 'InkPotStyle')
        assert isinstance(getattr(inkpot, 'InkPotStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(inkpot, 'InkPotStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

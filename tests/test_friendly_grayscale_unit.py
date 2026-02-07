"""
Tests unitaires générés pour friendly_grayscale
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import friendly_grayscale
except ImportError:
    pytest.skip(f"Module friendly_grayscale non importable")


class TestFriendlyGrayscaleStyle:
    """Tests pour la classe FriendlyGrayscaleStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(friendly_grayscale, 'FriendlyGrayscaleStyle')
        assert isinstance(getattr(friendly_grayscale, 'FriendlyGrayscaleStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(friendly_grayscale, 'FriendlyGrayscaleStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

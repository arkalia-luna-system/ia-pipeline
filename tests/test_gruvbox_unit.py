"""
Tests unitaires générés pour gruvbox
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gruvbox
except ImportError:
    pytest.skip(f"Module gruvbox non importable")


class TestGruvboxDarkStyle:
    """Tests pour la classe GruvboxDarkStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gruvbox, 'GruvboxDarkStyle')
        assert isinstance(getattr(gruvbox, 'GruvboxDarkStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gruvbox, 'GruvboxDarkStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGruvboxLightStyle:
    """Tests pour la classe GruvboxLightStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gruvbox, 'GruvboxLightStyle')
        assert isinstance(getattr(gruvbox, 'GruvboxLightStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gruvbox, 'GruvboxLightStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

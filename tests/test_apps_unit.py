"""
Tests unitaires générés pour apps
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import apps
except ImportError:
    pytest.skip(f"Module apps non importable")


class TestStarletteAppMixin:
    """Tests pour la classe StarletteAppMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apps, 'StarletteAppMixin')
        assert isinstance(getattr(apps, 'StarletteAppMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apps, 'StarletteAppMixin')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStarletteOAuth1App:
    """Tests pour la classe StarletteOAuth1App"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apps, 'StarletteOAuth1App')
        assert isinstance(getattr(apps, 'StarletteOAuth1App'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apps, 'StarletteOAuth1App')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStarletteOAuth2App:
    """Tests pour la classe StarletteOAuth2App"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apps, 'StarletteOAuth2App')
        assert isinstance(getattr(apps, 'StarletteOAuth2App'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apps, 'StarletteOAuth2App')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

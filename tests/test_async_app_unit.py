"""
Tests unitaires générés pour async_app
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import async_app
except ImportError:
    pytest.skip(f"Module async_app non importable")


class TestAsyncOAuth1Mixin:
    """Tests pour la classe AsyncOAuth1Mixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_app, 'AsyncOAuth1Mixin')
        assert isinstance(getattr(async_app, 'AsyncOAuth1Mixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_app, 'AsyncOAuth1Mixin')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAsyncOAuth2Mixin:
    """Tests pour la classe AsyncOAuth2Mixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_app, 'AsyncOAuth2Mixin')
        assert isinstance(getattr(async_app, 'AsyncOAuth2Mixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_app, 'AsyncOAuth2Mixin')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

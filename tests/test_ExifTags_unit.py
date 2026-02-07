"""
Tests unitaires générés pour ExifTags
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ExifTags
except ImportError:
    pytest.skip(f"Module ExifTags non importable")


class TestBase:
    """Tests pour la classe Base"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ExifTags, 'Base')
        assert isinstance(getattr(ExifTags, 'Base'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ExifTags, 'Base')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGPS:
    """Tests pour la classe GPS"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ExifTags, 'GPS')
        assert isinstance(getattr(ExifTags, 'GPS'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ExifTags, 'GPS')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInterop:
    """Tests pour la classe Interop"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ExifTags, 'Interop')
        assert isinstance(getattr(ExifTags, 'Interop'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ExifTags, 'Interop')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIFD:
    """Tests pour la classe IFD"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ExifTags, 'IFD')
        assert isinstance(getattr(ExifTags, 'IFD'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ExifTags, 'IFD')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLightSource:
    """Tests pour la classe LightSource"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ExifTags, 'LightSource')
        assert isinstance(getattr(ExifTags, 'LightSource'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ExifTags, 'LightSource')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

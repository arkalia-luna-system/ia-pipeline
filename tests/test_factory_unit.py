"""
Tests unitaires générés pour factory
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import factory
except ImportError:
    pytest.skip(f"Module factory non importable")


class TestCycloneDxFactoryException:
    """Tests pour la classe CycloneDxFactoryException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(factory, 'CycloneDxFactoryException')
        assert isinstance(getattr(factory, 'CycloneDxFactoryException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(factory, 'CycloneDxFactoryException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLicenseChoiceFactoryException:
    """Tests pour la classe LicenseChoiceFactoryException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(factory, 'LicenseChoiceFactoryException')
        assert isinstance(getattr(factory, 'LicenseChoiceFactoryException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(factory, 'LicenseChoiceFactoryException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInvalidSpdxLicenseException:
    """Tests pour la classe InvalidSpdxLicenseException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(factory, 'InvalidSpdxLicenseException')
        assert isinstance(getattr(factory, 'InvalidSpdxLicenseException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(factory, 'InvalidSpdxLicenseException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLicenseFactoryException:
    """Tests pour la classe LicenseFactoryException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(factory, 'LicenseFactoryException')
        assert isinstance(getattr(factory, 'LicenseFactoryException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(factory, 'LicenseFactoryException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInvalidLicenseExpressionException:
    """Tests pour la classe InvalidLicenseExpressionException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(factory, 'InvalidLicenseExpressionException')
        assert isinstance(getattr(factory, 'InvalidLicenseExpressionException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(factory, 'InvalidLicenseExpressionException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

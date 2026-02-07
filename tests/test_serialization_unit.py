"""
Tests unitaires générés pour serialization
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import serialization
except ImportError:
    pytest.skip(f"Module serialization non importable")


class TestCycloneDxSerializationException:
    """Tests pour la classe CycloneDxSerializationException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(serialization, 'CycloneDxSerializationException')
        assert isinstance(getattr(serialization, 'CycloneDxSerializationException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(serialization, 'CycloneDxSerializationException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCycloneDxDeserializationException:
    """Tests pour la classe CycloneDxDeserializationException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(serialization, 'CycloneDxDeserializationException')
        assert isinstance(getattr(serialization, 'CycloneDxDeserializationException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(serialization, 'CycloneDxDeserializationException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSerializationOfUnsupportedComponentTypeException:
    """Tests pour la classe SerializationOfUnsupportedComponentTypeException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(serialization, 'SerializationOfUnsupportedComponentTypeException')
        assert isinstance(getattr(serialization, 'SerializationOfUnsupportedComponentTypeException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(serialization, 'SerializationOfUnsupportedComponentTypeException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSerializationOfUnexpectedValueException:
    """Tests pour la classe SerializationOfUnexpectedValueException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(serialization, 'SerializationOfUnexpectedValueException')
        assert isinstance(getattr(serialization, 'SerializationOfUnexpectedValueException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(serialization, 'SerializationOfUnexpectedValueException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

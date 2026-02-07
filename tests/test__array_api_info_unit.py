"""
Tests unitaires générés pour _array_api_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _array_api_info
except ImportError:
    pytest.skip(f"Module _array_api_info non importable")


def test_capabilities():
    """Test de la fonction capabilities"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_api_info, 'capabilities')
    assert callable(getattr(_array_api_info, 'capabilities'))

def test_default_device():
    """Test de la fonction default_device"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_api_info, 'default_device')
    assert callable(getattr(_array_api_info, 'default_device'))

def test_default_dtypes():
    """Test de la fonction default_dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_api_info, 'default_dtypes')
    assert callable(getattr(_array_api_info, 'default_dtypes'))

def test_dtypes():
    """Test de la fonction dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_api_info, 'dtypes')
    assert callable(getattr(_array_api_info, 'dtypes'))

def test_devices():
    """Test de la fonction devices"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_api_info, 'devices')
    assert callable(getattr(_array_api_info, 'devices'))

class Test__array_namespace_info__:
    """Tests pour la classe __array_namespace_info__"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_array_api_info, '__array_namespace_info__')
        assert isinstance(getattr(_array_api_info, '__array_namespace_info__'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_array_api_info, '__array_namespace_info__')
        for method_name in ['capabilities', 'default_device', 'default_dtypes', 'dtypes', 'devices']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

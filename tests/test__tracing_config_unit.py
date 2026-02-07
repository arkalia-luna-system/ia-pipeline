"""
Tests unitaires générés pour _tracing_config
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tracing_config
except ImportError:
    pytest.skip(f"Module _tracing_config non importable")


def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'name')
    assert callable(getattr(_tracing_config, 'name'))

def test_build_attributes():
    """Test de la fonction build_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'build_attributes')
    assert callable(getattr(_tracing_config, 'build_attributes'))

def test_get_span_name():
    """Test de la fonction get_span_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'get_span_name')
    assert callable(getattr(_tracing_config, 'get_span_name'))

def test_get_span_kind():
    """Test de la fonction get_span_kind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'get_span_kind')
    assert callable(getattr(_tracing_config, 'get_span_kind'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, '__init__')
    assert callable(getattr(_tracing_config, '__init__'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'name')
    assert callable(getattr(_tracing_config, 'name'))

def test_build_attributes():
    """Test de la fonction build_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'build_attributes')
    assert callable(getattr(_tracing_config, 'build_attributes'))

def test_get_span_name():
    """Test de la fonction get_span_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'get_span_name')
    assert callable(getattr(_tracing_config, 'get_span_name'))

def test_get_span_kind():
    """Test de la fonction get_span_kind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, 'get_span_kind')
    assert callable(getattr(_tracing_config, 'get_span_kind'))

def test__get_destination_str():
    """Test de la fonction _get_destination_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, '_get_destination_str')
    assert callable(getattr(_tracing_config, '_get_destination_str'))

def test__get_operation_type():
    """Test de la fonction _get_operation_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tracing_config, '_get_operation_type')
    assert callable(getattr(_tracing_config, '_get_operation_type'))

class TestTracingConfig:
    """Tests pour la classe TracingConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tracing_config, 'TracingConfig')
        assert isinstance(getattr(_tracing_config, 'TracingConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tracing_config, 'TracingConfig')
        for method_name in ['name', 'build_attributes', 'get_span_name', 'get_span_kind']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExtraMessageRuntimeAttributes:
    """Tests pour la classe ExtraMessageRuntimeAttributes"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tracing_config, 'ExtraMessageRuntimeAttributes')
        assert isinstance(getattr(_tracing_config, 'ExtraMessageRuntimeAttributes'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tracing_config, 'ExtraMessageRuntimeAttributes')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMessageRuntimeTracingConfig:
    """Tests pour la classe MessageRuntimeTracingConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tracing_config, 'MessageRuntimeTracingConfig')
        assert isinstance(getattr(_tracing_config, 'MessageRuntimeTracingConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tracing_config, 'MessageRuntimeTracingConfig')
        for method_name in ['__init__', 'name', 'build_attributes', 'get_span_name', 'get_span_kind', '_get_destination_str', '_get_operation_type']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour _wrapped_document
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _wrapped_document
except ImportError:
    pytest.skip(f"Module _wrapped_document non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, '__init__')
    assert callable(getattr(_wrapped_document, '__init__'))

def test_wrapped():
    """Test de la fonction wrapped"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'wrapped')
    assert callable(getattr(_wrapped_document, 'wrapped'))

def test_wrap():
    """Test de la fonction wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'wrap')
    assert callable(getattr(_wrapped_document, 'wrap'))

def test_lines():
    """Test de la fonction lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'lines')
    assert callable(getattr(_wrapped_document, 'lines'))

def test_height():
    """Test de la fonction height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'height')
    assert callable(getattr(_wrapped_document, 'height'))

def test_wrap_range():
    """Test de la fonction wrap_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'wrap_range')
    assert callable(getattr(_wrapped_document, 'wrap_range'))

def test_offset_to_location():
    """Test de la fonction offset_to_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'offset_to_location')
    assert callable(getattr(_wrapped_document, 'offset_to_location'))

def test_location_to_offset():
    """Test de la fonction location_to_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'location_to_offset')
    assert callable(getattr(_wrapped_document, 'location_to_offset'))

def test_get_target_document_column():
    """Test de la fonction get_target_document_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'get_target_document_column')
    assert callable(getattr(_wrapped_document, 'get_target_document_column'))

def test_get_sections():
    """Test de la fonction get_sections"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'get_sections')
    assert callable(getattr(_wrapped_document, 'get_sections'))

def test_get_offsets():
    """Test de la fonction get_offsets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'get_offsets')
    assert callable(getattr(_wrapped_document, 'get_offsets'))

def test_get_tab_widths():
    """Test de la fonction get_tab_widths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrapped_document, 'get_tab_widths')
    assert callable(getattr(_wrapped_document, 'get_tab_widths'))

class TestWrappedDocument:
    """Tests pour la classe WrappedDocument"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_wrapped_document, 'WrappedDocument')
        assert isinstance(getattr(_wrapped_document, 'WrappedDocument'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_wrapped_document, 'WrappedDocument')
        for method_name in ['__init__', 'wrapped', 'wrap', 'lines', 'height', 'wrap_range', 'offset_to_location', 'location_to_offset', 'get_target_document_column', 'get_sections', 'get_offsets', 'get_tab_widths']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

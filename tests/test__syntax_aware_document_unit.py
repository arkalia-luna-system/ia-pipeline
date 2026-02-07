"""
Tests unitaires générés pour _syntax_aware_document
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _syntax_aware_document
except ImportError:
    pytest.skip(f"Module _syntax_aware_document non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, '__init__')
    assert callable(getattr(_syntax_aware_document, '__init__'))

def test_prepare_query():
    """Test de la fonction prepare_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, 'prepare_query')
    assert callable(getattr(_syntax_aware_document, 'prepare_query'))

def test_query_syntax_tree():
    """Test de la fonction query_syntax_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, 'query_syntax_tree')
    assert callable(getattr(_syntax_aware_document, 'query_syntax_tree'))

def test_replace_range():
    """Test de la fonction replace_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, 'replace_range')
    assert callable(getattr(_syntax_aware_document, 'replace_range'))

def test_get_line():
    """Test de la fonction get_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, 'get_line')
    assert callable(getattr(_syntax_aware_document, 'get_line'))

def test__location_to_byte_offset():
    """Test de la fonction _location_to_byte_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, '_location_to_byte_offset')
    assert callable(getattr(_syntax_aware_document, '_location_to_byte_offset'))

def test__location_to_point():
    """Test de la fonction _location_to_point"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, '_location_to_point')
    assert callable(getattr(_syntax_aware_document, '_location_to_point'))

def test__read_callable():
    """Test de la fonction _read_callable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_syntax_aware_document, '_read_callable')
    assert callable(getattr(_syntax_aware_document, '_read_callable'))

class TestSyntaxAwareDocumentError:
    """Tests pour la classe SyntaxAwareDocumentError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_syntax_aware_document, 'SyntaxAwareDocumentError')
        assert isinstance(getattr(_syntax_aware_document, 'SyntaxAwareDocumentError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_syntax_aware_document, 'SyntaxAwareDocumentError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSyntaxAwareDocument:
    """Tests pour la classe SyntaxAwareDocument"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_syntax_aware_document, 'SyntaxAwareDocument')
        assert isinstance(getattr(_syntax_aware_document, 'SyntaxAwareDocument'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_syntax_aware_document, 'SyntaxAwareDocument')
        for method_name in ['__init__', 'prepare_query', 'query_syntax_tree', 'replace_range', 'get_line', '_location_to_byte_offset', '_location_to_point', '_read_callable']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

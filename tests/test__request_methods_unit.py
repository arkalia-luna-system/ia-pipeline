"""
Tests unitaires générés pour _request_methods
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _request_methods
except ImportError:
    pytest.skip(f"Module _request_methods non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_request_methods, '__init__')
    assert callable(getattr(_request_methods, '__init__'))

def test_urlopen():
    """Test de la fonction urlopen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_request_methods, 'urlopen')
    assert callable(getattr(_request_methods, 'urlopen'))

def test_request():
    """Test de la fonction request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_request_methods, 'request')
    assert callable(getattr(_request_methods, 'request'))

def test_request_encode_url():
    """Test de la fonction request_encode_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_request_methods, 'request_encode_url')
    assert callable(getattr(_request_methods, 'request_encode_url'))

def test_request_encode_body():
    """Test de la fonction request_encode_body"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_request_methods, 'request_encode_body')
    assert callable(getattr(_request_methods, 'request_encode_body'))

class TestRequestMethods:
    """Tests pour la classe RequestMethods"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_request_methods, 'RequestMethods')
        assert isinstance(getattr(_request_methods, 'RequestMethods'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_request_methods, 'RequestMethods')
        for method_name in ['__init__', 'urlopen', 'request', 'request_encode_url', 'request_encode_body']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour _dispatch_key
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _dispatch_key
except ImportError:
    pytest.skip(f"Module _dispatch_key non importable")


def test_get_key_handler():
    """Test de la fonction get_key_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dispatch_key, 'get_key_handler')
    assert callable(getattr(_dispatch_key, 'get_key_handler'))

def test__raise_duplicate_key_handlers_error():
    """Test de la fonction _raise_duplicate_key_handlers_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dispatch_key, '_raise_duplicate_key_handlers_error')
    assert callable(getattr(_dispatch_key, '_raise_duplicate_key_handlers_error'))

if __name__ == "__main__":
    pytest.main([__file__])

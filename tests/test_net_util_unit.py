"""
Tests unitaires générés pour net_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import net_util
except ImportError:
    pytest.skip(f"Module net_util non importable")


def test_get_external_ip():
    """Test de la fonction get_external_ip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(net_util, 'get_external_ip')
    assert callable(getattr(net_util, 'get_external_ip'))

def test_get_internal_ip():
    """Test de la fonction get_internal_ip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(net_util, 'get_internal_ip')
    assert callable(getattr(net_util, 'get_internal_ip'))

def test__make_blocking_http_get():
    """Test de la fonction _make_blocking_http_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(net_util, '_make_blocking_http_get')
    assert callable(getattr(net_util, '_make_blocking_http_get'))

def test__looks_like_an_ip_adress():
    """Test de la fonction _looks_like_an_ip_adress"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(net_util, '_looks_like_an_ip_adress')
    assert callable(getattr(net_util, '_looks_like_an_ip_adress'))

if __name__ == "__main__":
    pytest.main([__file__])

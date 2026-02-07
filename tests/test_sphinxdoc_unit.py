"""
Tests unitaires générés pour sphinxdoc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sphinxdoc
except ImportError:
    pytest.skip(f"Module sphinxdoc non importable")


def test_setup():
    """Test de la fonction setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'setup')
    assert callable(getattr(sphinxdoc, 'setup'))

def test_interesting_default_value():
    """Test de la fonction interesting_default_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'interesting_default_value')
    assert callable(getattr(sphinxdoc, 'interesting_default_value'))

def test_format_aliases():
    """Test de la fonction format_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'format_aliases')
    assert callable(getattr(sphinxdoc, 'format_aliases'))

def test_class_config_rst_doc():
    """Test de la fonction class_config_rst_doc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'class_config_rst_doc')
    assert callable(getattr(sphinxdoc, 'class_config_rst_doc'))

def test_reverse_aliases():
    """Test de la fonction reverse_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'reverse_aliases')
    assert callable(getattr(sphinxdoc, 'reverse_aliases'))

def test_write_doc():
    """Test de la fonction write_doc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxdoc, 'write_doc')
    assert callable(getattr(sphinxdoc, 'write_doc'))

if __name__ == "__main__":
    pytest.main([__file__])

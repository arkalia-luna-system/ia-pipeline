"""
Tests unitaires générés pour frame
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import frame
except ImportError:
    pytest.skip(f"Module frame non importable")


def test_extract_vars():
    """Test de la fonction extract_vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frame, 'extract_vars')
    assert callable(getattr(frame, 'extract_vars'))

def test_extract_vars_above():
    """Test de la fonction extract_vars_above"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frame, 'extract_vars_above')
    assert callable(getattr(frame, 'extract_vars_above'))

def test_debugx():
    """Test de la fonction debugx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frame, 'debugx')
    assert callable(getattr(frame, 'debugx'))

def test_extract_module_locals():
    """Test de la fonction extract_module_locals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frame, 'extract_module_locals')
    assert callable(getattr(frame, 'extract_module_locals'))

if __name__ == "__main__":
    pytest.main([__file__])

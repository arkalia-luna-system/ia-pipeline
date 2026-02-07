"""
Tests unitaires générés pour page_navigation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import page_navigation
except ImportError:
    pytest.skip(f"Module page_navigation non importable")


def test_load_page_navigation_bindings():
    """Test de la fonction load_page_navigation_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(page_navigation, 'load_page_navigation_bindings')
    assert callable(getattr(page_navigation, 'load_page_navigation_bindings'))

def test_load_emacs_page_navigation_bindings():
    """Test de la fonction load_emacs_page_navigation_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(page_navigation, 'load_emacs_page_navigation_bindings')
    assert callable(getattr(page_navigation, 'load_emacs_page_navigation_bindings'))

def test_load_vi_page_navigation_bindings():
    """Test de la fonction load_vi_page_navigation_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(page_navigation, 'load_vi_page_navigation_bindings')
    assert callable(getattr(page_navigation, 'load_vi_page_navigation_bindings'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour open_in_editor
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import open_in_editor
except ImportError:
    pytest.skip(f"Module open_in_editor non importable")


def test_load_open_in_editor_bindings():
    """Test de la fonction load_open_in_editor_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(open_in_editor, 'load_open_in_editor_bindings')
    assert callable(getattr(open_in_editor, 'load_open_in_editor_bindings'))

def test_load_emacs_open_in_editor_bindings():
    """Test de la fonction load_emacs_open_in_editor_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(open_in_editor, 'load_emacs_open_in_editor_bindings')
    assert callable(getattr(open_in_editor, 'load_emacs_open_in_editor_bindings'))

def test_load_vi_open_in_editor_bindings():
    """Test de la fonction load_vi_open_in_editor_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(open_in_editor, 'load_vi_open_in_editor_bindings')
    assert callable(getattr(open_in_editor, 'load_vi_open_in_editor_bindings'))

if __name__ == "__main__":
    pytest.main([__file__])

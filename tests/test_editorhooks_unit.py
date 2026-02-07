"""
Tests unitaires générés pour editorhooks
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import editorhooks
except ImportError:
    pytest.skip(f"Module editorhooks non importable")


def test_install_editor():
    """Test de la fonction install_editor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'install_editor')
    assert callable(getattr(editorhooks, 'install_editor'))

def test_komodo():
    """Test de la fonction komodo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'komodo')
    assert callable(getattr(editorhooks, 'komodo'))

def test_scite():
    """Test de la fonction scite"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'scite')
    assert callable(getattr(editorhooks, 'scite'))

def test_notepadplusplus():
    """Test de la fonction notepadplusplus"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'notepadplusplus')
    assert callable(getattr(editorhooks, 'notepadplusplus'))

def test_jed():
    """Test de la fonction jed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'jed')
    assert callable(getattr(editorhooks, 'jed'))

def test_idle():
    """Test de la fonction idle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'idle')
    assert callable(getattr(editorhooks, 'idle'))

def test_mate():
    """Test de la fonction mate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'mate')
    assert callable(getattr(editorhooks, 'mate'))

def test_emacs():
    """Test de la fonction emacs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'emacs')
    assert callable(getattr(editorhooks, 'emacs'))

def test_gnuclient():
    """Test de la fonction gnuclient"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'gnuclient')
    assert callable(getattr(editorhooks, 'gnuclient'))

def test_crimson_editor():
    """Test de la fonction crimson_editor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'crimson_editor')
    assert callable(getattr(editorhooks, 'crimson_editor'))

def test_kate():
    """Test de la fonction kate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'kate')
    assert callable(getattr(editorhooks, 'kate'))

def test_call_editor():
    """Test de la fonction call_editor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editorhooks, 'call_editor')
    assert callable(getattr(editorhooks, 'call_editor'))

if __name__ == "__main__":
    pytest.main([__file__])

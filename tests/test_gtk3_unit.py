"""
Tests unitaires générés pour gtk3
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gtk3
except ImportError:
    pytest.skip(f"Module gtk3 non importable")


def test__main_quit():
    """Test de la fonction _main_quit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk3, '_main_quit')
    assert callable(getattr(gtk3, '_main_quit'))

def test_inputhook():
    """Test de la fonction inputhook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk3, 'inputhook')
    assert callable(getattr(gtk3, 'inputhook'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour ipython_console_highlighting
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ipython_console_highlighting
except ImportError:
    pytest.skip(f"Module ipython_console_highlighting non importable")


def test_setup():
    """Test de la fonction setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipython_console_highlighting, 'setup')
    assert callable(getattr(ipython_console_highlighting, 'setup'))

if __name__ == "__main__":
    pytest.main([__file__])

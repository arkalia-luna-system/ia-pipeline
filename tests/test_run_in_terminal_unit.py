"""
Tests unitaires générés pour run_in_terminal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import run_in_terminal
except ImportError:
    pytest.skip(f"Module run_in_terminal non importable")


def test_run_in_terminal():
    """Test de la fonction run_in_terminal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(run_in_terminal, 'run_in_terminal')
    assert callable(getattr(run_in_terminal, 'run_in_terminal'))

if __name__ == "__main__":
    pytest.main([__file__])

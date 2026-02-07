"""
Tests unitaires générés pour _line_split
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _line_split
except ImportError:
    pytest.skip(f"Module _line_split non importable")


def test_line_split():
    """Test de la fonction line_split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_line_split, 'line_split')
    assert callable(getattr(_line_split, 'line_split'))

if __name__ == "__main__":
    pytest.main([__file__])

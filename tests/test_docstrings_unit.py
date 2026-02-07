"""
Tests unitaires générés pour docstrings
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import docstrings
except ImportError:
    pytest.skip(f"Module docstrings non importable")


def test_make_flex_doc():
    """Test de la fonction make_flex_doc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(docstrings, 'make_flex_doc')
    assert callable(getattr(docstrings, 'make_flex_doc'))

if __name__ == "__main__":
    pytest.main([__file__])

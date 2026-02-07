"""
Tests unitaires générés pour sax
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sax
except ImportError:
    pytest.skip(f"Module sax non importable")


def test_to_sax():
    """Test de la fonction to_sax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sax, 'to_sax')
    assert callable(getattr(sax, 'to_sax'))

if __name__ == "__main__":
    pytest.main([__file__])

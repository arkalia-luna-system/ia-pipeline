"""
Tests unitaires générés pour spss
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import spss
except ImportError:
    pytest.skip(f"Module spss non importable")


def test_read_spss():
    """Test de la fonction read_spss"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(spss, 'read_spss')
    assert callable(getattr(spss, 'read_spss'))

if __name__ == "__main__":
    pytest.main([__file__])

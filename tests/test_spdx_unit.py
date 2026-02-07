"""
Tests unitaires générés pour spdx
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import spdx
except ImportError:
    pytest.skip(f"Module spdx non importable")


def test_is_supported_id():
    """Test de la fonction is_supported_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(spdx, 'is_supported_id')
    assert callable(getattr(spdx, 'is_supported_id'))

def test_fixup_id():
    """Test de la fonction fixup_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(spdx, 'fixup_id')
    assert callable(getattr(spdx, 'fixup_id'))

def test_is_compound_expression():
    """Test de la fonction is_compound_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(spdx, 'is_compound_expression')
    assert callable(getattr(spdx, 'is_compound_expression'))

if __name__ == "__main__":
    pytest.main([__file__])

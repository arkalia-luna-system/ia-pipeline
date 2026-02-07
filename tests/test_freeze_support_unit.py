"""
Tests unitaires générés pour freeze_support
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import freeze_support
except ImportError:
    pytest.skip(f"Module freeze_support non importable")


def test_freeze_includes():
    """Test de la fonction freeze_includes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(freeze_support, 'freeze_includes')
    assert callable(getattr(freeze_support, 'freeze_includes'))

def test__iter_all_modules():
    """Test de la fonction _iter_all_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(freeze_support, '_iter_all_modules')
    assert callable(getattr(freeze_support, '_iter_all_modules'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour rebuild
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rebuild
except ImportError:
    pytest.skip(f"Module rebuild non importable")


def test_rebuild():
    """Test de la fonction rebuild"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebuild, 'rebuild')
    assert callable(getattr(rebuild, 'rebuild'))

def test__run_zic():
    """Test de la fonction _run_zic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebuild, '_run_zic')
    assert callable(getattr(rebuild, '_run_zic'))

def test__print_on_nosuchfile():
    """Test de la fonction _print_on_nosuchfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebuild, '_print_on_nosuchfile')
    assert callable(getattr(rebuild, '_print_on_nosuchfile'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour uninit
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import uninit
except ImportError:
    pytest.skip(f"Module uninit non importable")


def test_insert_uninit_checks():
    """Test de la fonction insert_uninit_checks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninit, 'insert_uninit_checks')
    assert callable(getattr(uninit, 'insert_uninit_checks'))

def test_split_blocks_at_uninits():
    """Test de la fonction split_blocks_at_uninits"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninit, 'split_blocks_at_uninits')
    assert callable(getattr(uninit, 'split_blocks_at_uninits'))

def test_check_for_uninit_using_bitmap():
    """Test de la fonction check_for_uninit_using_bitmap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninit, 'check_for_uninit_using_bitmap')
    assert callable(getattr(uninit, 'check_for_uninit_using_bitmap'))

def test_update_register_assignments_to_set_bitmap():
    """Test de la fonction update_register_assignments_to_set_bitmap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninit, 'update_register_assignments_to_set_bitmap')
    assert callable(getattr(uninit, 'update_register_assignments_to_set_bitmap'))

if __name__ == "__main__":
    pytest.main([__file__])

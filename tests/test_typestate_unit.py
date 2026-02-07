"""
Tests unitaires générés pour typestate
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import typestate
except ImportError:
    pytest.skip(f"Module typestate non importable")


def test_reset_global_state():
    """Test de la fonction reset_global_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'reset_global_state')
    assert callable(getattr(typestate, 'reset_global_state'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, '__init__')
    assert callable(getattr(typestate, '__init__'))

def test_is_assumed_subtype():
    """Test de la fonction is_assumed_subtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'is_assumed_subtype')
    assert callable(getattr(typestate, 'is_assumed_subtype'))

def test_is_assumed_proper_subtype():
    """Test de la fonction is_assumed_proper_subtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'is_assumed_proper_subtype')
    assert callable(getattr(typestate, 'is_assumed_proper_subtype'))

def test_get_assumptions():
    """Test de la fonction get_assumptions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'get_assumptions')
    assert callable(getattr(typestate, 'get_assumptions'))

def test_reset_all_subtype_caches():
    """Test de la fonction reset_all_subtype_caches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'reset_all_subtype_caches')
    assert callable(getattr(typestate, 'reset_all_subtype_caches'))

def test_reset_subtype_caches_for():
    """Test de la fonction reset_subtype_caches_for"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'reset_subtype_caches_for')
    assert callable(getattr(typestate, 'reset_subtype_caches_for'))

def test_reset_all_subtype_caches_for():
    """Test de la fonction reset_all_subtype_caches_for"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'reset_all_subtype_caches_for')
    assert callable(getattr(typestate, 'reset_all_subtype_caches_for'))

def test_is_cached_subtype_check():
    """Test de la fonction is_cached_subtype_check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'is_cached_subtype_check')
    assert callable(getattr(typestate, 'is_cached_subtype_check'))

def test_is_cached_negative_subtype_check():
    """Test de la fonction is_cached_negative_subtype_check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'is_cached_negative_subtype_check')
    assert callable(getattr(typestate, 'is_cached_negative_subtype_check'))

def test_record_subtype_cache_entry():
    """Test de la fonction record_subtype_cache_entry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'record_subtype_cache_entry')
    assert callable(getattr(typestate, 'record_subtype_cache_entry'))

def test_record_negative_subtype_cache_entry():
    """Test de la fonction record_negative_subtype_cache_entry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'record_negative_subtype_cache_entry')
    assert callable(getattr(typestate, 'record_negative_subtype_cache_entry'))

def test_reset_protocol_deps():
    """Test de la fonction reset_protocol_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'reset_protocol_deps')
    assert callable(getattr(typestate, 'reset_protocol_deps'))

def test_record_protocol_subtype_check():
    """Test de la fonction record_protocol_subtype_check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'record_protocol_subtype_check')
    assert callable(getattr(typestate, 'record_protocol_subtype_check'))

def test__snapshot_protocol_deps():
    """Test de la fonction _snapshot_protocol_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, '_snapshot_protocol_deps')
    assert callable(getattr(typestate, '_snapshot_protocol_deps'))

def test_update_protocol_deps():
    """Test de la fonction update_protocol_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'update_protocol_deps')
    assert callable(getattr(typestate, 'update_protocol_deps'))

def test_add_all_protocol_deps():
    """Test de la fonction add_all_protocol_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typestate, 'add_all_protocol_deps')
    assert callable(getattr(typestate, 'add_all_protocol_deps'))

class TestTypeState:
    """Tests pour la classe TypeState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(typestate, 'TypeState')
        assert isinstance(getattr(typestate, 'TypeState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(typestate, 'TypeState')
        for method_name in ['__init__', 'is_assumed_subtype', 'is_assumed_proper_subtype', 'get_assumptions', 'reset_all_subtype_caches', 'reset_subtype_caches_for', 'reset_all_subtype_caches_for', 'is_cached_subtype_check', 'is_cached_negative_subtype_check', 'record_subtype_cache_entry', 'record_negative_subtype_cache_entry', 'reset_protocol_deps', 'record_protocol_subtype_check', '_snapshot_protocol_deps', 'update_protocol_deps', 'add_all_protocol_deps']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

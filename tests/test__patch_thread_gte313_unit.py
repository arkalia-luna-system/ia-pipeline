"""
Tests unitaires générés pour _patch_thread_gte313
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _patch_thread_gte313
except ImportError:
    pytest.skip(f"Module _patch_thread_gte313 non importable")


def test_patch_active_threads():
    """Test de la fonction patch_active_threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, 'patch_active_threads')
    assert callable(getattr(_patch_thread_gte313, 'patch_active_threads'))

def test_patch_threading_shutdown_on_main_thread_not_already_patched():
    """Test de la fonction patch_threading_shutdown_on_main_thread_not_already_patched"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, 'patch_threading_shutdown_on_main_thread_not_already_patched')
    assert callable(getattr(_patch_thread_gte313, 'patch_threading_shutdown_on_main_thread_not_already_patched'))

def test__shutdown():
    """Test de la fonction _shutdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, '_shutdown')
    assert callable(getattr(_patch_thread_gte313, '_shutdown'))

def test_is_done():
    """Test de la fonction is_done"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, 'is_done')
    assert callable(getattr(_patch_thread_gte313, 'is_done'))

def test__set_done():
    """Test de la fonction _set_done"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, '_set_done')
    assert callable(getattr(_patch_thread_gte313, '_set_done'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_gte313, 'join')
    assert callable(getattr(_patch_thread_gte313, 'join'))

class TestPatcher:
    """Tests pour la classe Patcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_patch_thread_gte313, 'Patcher')
        assert isinstance(getattr(_patch_thread_gte313, 'Patcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_patch_thread_gte313, 'Patcher')
        for method_name in ['patch_active_threads', 'patch_threading_shutdown_on_main_thread_not_already_patched']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFakeHandle:
    """Tests pour la classe FakeHandle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_patch_thread_gte313, 'FakeHandle')
        assert isinstance(getattr(_patch_thread_gte313, 'FakeHandle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_patch_thread_gte313, 'FakeHandle')
        for method_name in ['is_done', '_set_done', 'join']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

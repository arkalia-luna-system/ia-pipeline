"""
Tests unitaires générés pour _patch_thread_lt313
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _patch_thread_lt313
except ImportError:
    pytest.skip(f"Module _patch_thread_lt313 non importable")


def test_patch_active_threads():
    """Test de la fonction patch_active_threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_lt313, 'patch_active_threads')
    assert callable(getattr(_patch_thread_lt313, 'patch_active_threads'))

def test_patch_threading_shutdown_on_main_thread_not_already_patched():
    """Test de la fonction patch_threading_shutdown_on_main_thread_not_already_patched"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_lt313, 'patch_threading_shutdown_on_main_thread_not_already_patched')
    assert callable(getattr(_patch_thread_lt313, 'patch_threading_shutdown_on_main_thread_not_already_patched'))

def test__shutdown():
    """Test de la fonction _shutdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_patch_thread_lt313, '_shutdown')
    assert callable(getattr(_patch_thread_lt313, '_shutdown'))

class TestPatcher:
    """Tests pour la classe Patcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_patch_thread_lt313, 'Patcher')
        assert isinstance(getattr(_patch_thread_lt313, 'Patcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_patch_thread_lt313, 'Patcher')
        for method_name in ['patch_active_threads', 'patch_threading_shutdown_on_main_thread_not_already_patched']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

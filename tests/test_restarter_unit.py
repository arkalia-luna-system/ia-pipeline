"""
Tests unitaires générés pour restarter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import restarter
except ImportError:
    pytest.skip(f"Module restarter non importable")


def test__loop_default():
    """Test de la fonction _loop_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(restarter, '_loop_default')
    assert callable(getattr(restarter, '_loop_default'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(restarter, 'start')
    assert callable(getattr(restarter, 'start'))

def test_stop():
    """Test de la fonction stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(restarter, 'stop')
    assert callable(getattr(restarter, 'stop'))

class TestIOLoopKernelRestarter:
    """Tests pour la classe IOLoopKernelRestarter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(restarter, 'IOLoopKernelRestarter')
        assert isinstance(getattr(restarter, 'IOLoopKernelRestarter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(restarter, 'IOLoopKernelRestarter')
        for method_name in ['_loop_default', 'start', 'stop']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAsyncIOLoopKernelRestarter:
    """Tests pour la classe AsyncIOLoopKernelRestarter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(restarter, 'AsyncIOLoopKernelRestarter')
        assert isinstance(getattr(restarter, 'AsyncIOLoopKernelRestarter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(restarter, 'AsyncIOLoopKernelRestarter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

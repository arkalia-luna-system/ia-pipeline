"""
Tests unitaires générés pour filewrapper
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import filewrapper
except ImportError:
    pytest.skip(f"Module filewrapper non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, '__init__')
    assert callable(getattr(filewrapper, '__init__'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, '__getattr__')
    assert callable(getattr(filewrapper, '__getattr__'))

def test___is_fp_closed():
    """Test de la fonction __is_fp_closed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, '__is_fp_closed')
    assert callable(getattr(filewrapper, '__is_fp_closed'))

def test__close():
    """Test de la fonction _close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, '_close')
    assert callable(getattr(filewrapper, '_close'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, 'read')
    assert callable(getattr(filewrapper, 'read'))

def test__safe_read():
    """Test de la fonction _safe_read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filewrapper, '_safe_read')
    assert callable(getattr(filewrapper, '_safe_read'))

class TestCallbackFileWrapper:
    """Tests pour la classe CallbackFileWrapper"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(filewrapper, 'CallbackFileWrapper')
        assert isinstance(getattr(filewrapper, 'CallbackFileWrapper'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(filewrapper, 'CallbackFileWrapper')
        for method_name in ['__init__', '__getattr__', '__is_fp_closed', '_close', 'read', '_safe_read']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

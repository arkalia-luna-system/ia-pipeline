"""
Tests unitaires générés pour _imap
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _imap
except ImportError:
    pytest.skip(f"Module _imap non importable")


def test__raise_exc():
    """Test de la fonction _raise_exc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_raise_exc')
    assert callable(getattr(_imap, '_raise_exc'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '__init__')
    assert callable(getattr(_imap, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '__init__')
    assert callable(getattr(_imap, '__init__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '__iter__')
    assert callable(getattr(_imap, '__iter__'))

def test___next__():
    """Test de la fonction __next__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '__next__')
    assert callable(getattr(_imap, '__next__'))

def test__inext():
    """Test de la fonction _inext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_inext')
    assert callable(getattr(_imap, '_inext'))

def test__ispawn():
    """Test de la fonction _ispawn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_ispawn')
    assert callable(getattr(_imap, '_ispawn'))

def test__run():
    """Test de la fonction _run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_run')
    assert callable(getattr(_imap, '_run'))

def test__on_result():
    """Test de la fonction _on_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_on_result')
    assert callable(getattr(_imap, '_on_result'))

def test__on_finish():
    """Test de la fonction _on_finish"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_on_finish')
    assert callable(getattr(_imap, '_on_finish'))

def test__iqueue_value_for_success():
    """Test de la fonction _iqueue_value_for_success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_success')
    assert callable(getattr(_imap, '_iqueue_value_for_success'))

def test__iqueue_value_for_failure():
    """Test de la fonction _iqueue_value_for_failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_failure')
    assert callable(getattr(_imap, '_iqueue_value_for_failure'))

def test__iqueue_value_for_self_finished():
    """Test de la fonction _iqueue_value_for_self_finished"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_self_finished')
    assert callable(getattr(_imap, '_iqueue_value_for_self_finished'))

def test__iqueue_value_for_self_failure():
    """Test de la fonction _iqueue_value_for_self_failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_self_failure')
    assert callable(getattr(_imap, '_iqueue_value_for_self_failure'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '__init__')
    assert callable(getattr(_imap, '__init__'))

def test__inext():
    """Test de la fonction _inext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_inext')
    assert callable(getattr(_imap, '_inext'))

def test__iqueue_value_for_success():
    """Test de la fonction _iqueue_value_for_success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_success')
    assert callable(getattr(_imap, '_iqueue_value_for_success'))

def test__iqueue_value_for_failure():
    """Test de la fonction _iqueue_value_for_failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_failure')
    assert callable(getattr(_imap, '_iqueue_value_for_failure'))

def test__iqueue_value_for_self_finished():
    """Test de la fonction _iqueue_value_for_self_finished"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_self_finished')
    assert callable(getattr(_imap, '_iqueue_value_for_self_finished'))

def test__iqueue_value_for_self_failure():
    """Test de la fonction _iqueue_value_for_self_failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imap, '_iqueue_value_for_self_failure')
    assert callable(getattr(_imap, '_iqueue_value_for_self_failure'))

class TestFailure:
    """Tests pour la classe Failure"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_imap, 'Failure')
        assert isinstance(getattr(_imap, 'Failure'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_imap, 'Failure')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIMapUnordered:
    """Tests pour la classe IMapUnordered"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_imap, 'IMapUnordered')
        assert isinstance(getattr(_imap, 'IMapUnordered'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_imap, 'IMapUnordered')
        for method_name in ['__init__', '__iter__', '__next__', '_inext', '_ispawn', '_run', '_on_result', '_on_finish', '_iqueue_value_for_success', '_iqueue_value_for_failure', '_iqueue_value_for_self_finished', '_iqueue_value_for_self_failure']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIMap:
    """Tests pour la classe IMap"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_imap, 'IMap')
        assert isinstance(getattr(_imap, 'IMap'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_imap, 'IMap')
        for method_name in ['__init__', '_inext', '_iqueue_value_for_success', '_iqueue_value_for_failure', '_iqueue_value_for_self_finished', '_iqueue_value_for_self_failure']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

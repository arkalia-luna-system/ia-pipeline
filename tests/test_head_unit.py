"""
Tests unitaires générés pour head
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import head
except ImportError:
    pytest.skip(f"Module head non importable")


def test_strip_quotes():
    """Test de la fonction strip_quotes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'strip_quotes')
    assert callable(getattr(head, 'strip_quotes'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, '__init__')
    assert callable(getattr(head, '__init__'))

def test_orig_head():
    """Test de la fonction orig_head"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'orig_head')
    assert callable(getattr(head, 'orig_head'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'reset')
    assert callable(getattr(head, 'reset'))

def test_delete():
    """Test de la fonction delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'delete')
    assert callable(getattr(head, 'delete'))

def test_set_tracking_branch():
    """Test de la fonction set_tracking_branch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'set_tracking_branch')
    assert callable(getattr(head, 'set_tracking_branch'))

def test_tracking_branch():
    """Test de la fonction tracking_branch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'tracking_branch')
    assert callable(getattr(head, 'tracking_branch'))

def test_rename():
    """Test de la fonction rename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'rename')
    assert callable(getattr(head, 'rename'))

def test_checkout():
    """Test de la fonction checkout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'checkout')
    assert callable(getattr(head, 'checkout'))

def test__config_parser():
    """Test de la fonction _config_parser"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, '_config_parser')
    assert callable(getattr(head, '_config_parser'))

def test_config_reader():
    """Test de la fonction config_reader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'config_reader')
    assert callable(getattr(head, 'config_reader'))

def test_config_writer():
    """Test de la fonction config_writer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(head, 'config_writer')
    assert callable(getattr(head, 'config_writer'))

class TestHEAD:
    """Tests pour la classe HEAD"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(head, 'HEAD')
        assert isinstance(getattr(head, 'HEAD'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(head, 'HEAD')
        for method_name in ['__init__', 'orig_head', 'reset']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHead:
    """Tests pour la classe Head"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(head, 'Head')
        assert isinstance(getattr(head, 'Head'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(head, 'Head')
        for method_name in ['delete', 'set_tracking_branch', 'tracking_branch', 'rename', 'checkout', '_config_parser', 'config_reader', 'config_writer']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

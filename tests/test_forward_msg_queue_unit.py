"""
Tests unitaires générés pour forward_msg_queue
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import forward_msg_queue
except ImportError:
    pytest.skip(f"Module forward_msg_queue non importable")


def test__is_composable_message():
    """Test de la fonction _is_composable_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, '_is_composable_message')
    assert callable(getattr(forward_msg_queue, '_is_composable_message'))

def test__maybe_compose_delta_msgs():
    """Test de la fonction _maybe_compose_delta_msgs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, '_maybe_compose_delta_msgs')
    assert callable(getattr(forward_msg_queue, '_maybe_compose_delta_msgs'))

def test__update_script_finished_message():
    """Test de la fonction _update_script_finished_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, '_update_script_finished_message')
    assert callable(getattr(forward_msg_queue, '_update_script_finished_message'))

def test_on_before_enqueue_msg():
    """Test de la fonction on_before_enqueue_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'on_before_enqueue_msg')
    assert callable(getattr(forward_msg_queue, 'on_before_enqueue_msg'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, '__init__')
    assert callable(getattr(forward_msg_queue, '__init__'))

def test_get_debug():
    """Test de la fonction get_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'get_debug')
    assert callable(getattr(forward_msg_queue, 'get_debug'))

def test_is_empty():
    """Test de la fonction is_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'is_empty')
    assert callable(getattr(forward_msg_queue, 'is_empty'))

def test_enqueue():
    """Test de la fonction enqueue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'enqueue')
    assert callable(getattr(forward_msg_queue, 'enqueue'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'clear')
    assert callable(getattr(forward_msg_queue, 'clear'))

def test_flush():
    """Test de la fonction flush"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, 'flush')
    assert callable(getattr(forward_msg_queue, 'flush'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forward_msg_queue, '__len__')
    assert callable(getattr(forward_msg_queue, '__len__'))

class TestForwardMsgQueue:
    """Tests pour la classe ForwardMsgQueue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(forward_msg_queue, 'ForwardMsgQueue')
        assert isinstance(getattr(forward_msg_queue, 'ForwardMsgQueue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(forward_msg_queue, 'ForwardMsgQueue')
        for method_name in ['on_before_enqueue_msg', '__init__', 'get_debug', 'is_empty', 'enqueue', 'clear', 'flush', '__len__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

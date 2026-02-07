"""
Tests unitaires générés pour _zmq
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _zmq
except ImportError:
    pytest.skip(f"Module _zmq non importable")


def test__check_rc():
    """Test de la fonction _check_rc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_check_rc')
    assert callable(getattr(_zmq, '_check_rc'))

def test_free_python_msg():
    """Test de la fonction free_python_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'free_python_msg')
    assert callable(getattr(_zmq, 'free_python_msg'))

def test__copy_zmq_msg_bytes():
    """Test de la fonction _copy_zmq_msg_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_copy_zmq_msg_bytes')
    assert callable(getattr(_zmq, '_copy_zmq_msg_bytes'))

def test__asbuffer():
    """Test de la fonction _asbuffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_asbuffer')
    assert callable(getattr(_zmq, '_asbuffer'))

def test__c_addr():
    """Test de la fonction _c_addr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_c_addr')
    assert callable(getattr(_zmq, '_c_addr'))

def test__check_closed():
    """Test de la fonction _check_closed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_check_closed')
    assert callable(getattr(_zmq, '_check_closed'))

def test__check_closed_deep():
    """Test de la fonction _check_closed_deep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_check_closed_deep')
    assert callable(getattr(_zmq, '_check_closed_deep'))

def test__recv_frame():
    """Test de la fonction _recv_frame"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_recv_frame')
    assert callable(getattr(_zmq, '_recv_frame'))

def test__recv_copy():
    """Test de la fonction _recv_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_recv_copy')
    assert callable(getattr(_zmq, '_recv_copy'))

def test__send_frame():
    """Test de la fonction _send_frame"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_send_frame')
    assert callable(getattr(_zmq, '_send_frame'))

def test__send_copy():
    """Test de la fonction _send_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_send_copy')
    assert callable(getattr(_zmq, '_send_copy'))

def test__getsockopt():
    """Test de la fonction _getsockopt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_getsockopt')
    assert callable(getattr(_zmq, '_getsockopt'))

def test__setsockopt():
    """Test de la fonction _setsockopt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_setsockopt')
    assert callable(getattr(_zmq, '_setsockopt'))

def test_zmq_errno():
    """Test de la fonction zmq_errno"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'zmq_errno')
    assert callable(getattr(_zmq, 'zmq_errno'))

def test_strerror():
    """Test de la fonction strerror"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'strerror')
    assert callable(getattr(_zmq, 'strerror'))

def test_zmq_version_info():
    """Test de la fonction zmq_version_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'zmq_version_info')
    assert callable(getattr(_zmq, 'zmq_version_info'))

def test_has():
    """Test de la fonction has"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'has')
    assert callable(getattr(_zmq, 'has'))

def test_curve_keypair():
    """Test de la fonction curve_keypair"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'curve_keypair')
    assert callable(getattr(_zmq, 'curve_keypair'))

def test_curve_public():
    """Test de la fonction curve_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'curve_public')
    assert callable(getattr(_zmq, 'curve_public'))

def test_zmq_poll():
    """Test de la fonction zmq_poll"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'zmq_poll')
    assert callable(getattr(_zmq, 'zmq_poll'))

def test_proxy():
    """Test de la fonction proxy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'proxy')
    assert callable(getattr(_zmq, 'proxy'))

def test_proxy_steerable():
    """Test de la fonction proxy_steerable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'proxy_steerable')
    assert callable(getattr(_zmq, 'proxy_steerable'))

def test__mq_relay():
    """Test de la fonction _mq_relay"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_mq_relay')
    assert callable(getattr(_zmq, '_mq_relay'))

def test__mq_inline():
    """Test de la fonction _mq_inline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_mq_inline')
    assert callable(getattr(_zmq, '_mq_inline'))

def test_monitored_queue():
    """Test de la fonction monitored_queue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'monitored_queue')
    assert callable(getattr(_zmq, 'monitored_queue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__init__')
    assert callable(getattr(_zmq, '__init__'))

def test___dealloc__():
    """Test de la fonction __dealloc__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__dealloc__')
    assert callable(getattr(_zmq, '__dealloc__'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__copy__')
    assert callable(getattr(_zmq, '__copy__'))

def test_fast_copy():
    """Test de la fonction fast_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'fast_copy')
    assert callable(getattr(_zmq, 'fast_copy'))

def test___getbuffer__():
    """Test de la fonction __getbuffer__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__getbuffer__')
    assert callable(getattr(_zmq, '__getbuffer__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__len__')
    assert callable(getattr(_zmq, '__len__'))

def test_buffer():
    """Test de la fonction buffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'buffer')
    assert callable(getattr(_zmq, 'buffer'))

def test_bytes():
    """Test de la fonction bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'bytes')
    assert callable(getattr(_zmq, 'bytes'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'get')
    assert callable(getattr(_zmq, 'get'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'set')
    assert callable(getattr(_zmq, 'set'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__init__')
    assert callable(getattr(_zmq, '__init__'))

def test_underlying():
    """Test de la fonction underlying"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'underlying')
    assert callable(getattr(_zmq, 'underlying'))

def test__term():
    """Test de la fonction _term"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '_term')
    assert callable(getattr(_zmq, '_term'))

def test_term():
    """Test de la fonction term"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'term')
    assert callable(getattr(_zmq, 'term'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'set')
    assert callable(getattr(_zmq, 'set'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'get')
    assert callable(getattr(_zmq, 'get'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, '__init__')
    assert callable(getattr(_zmq, '__init__'))

def test_underlying():
    """Test de la fonction underlying"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'underlying')
    assert callable(getattr(_zmq, 'underlying'))

def test_closed():
    """Test de la fonction closed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'closed')
    assert callable(getattr(_zmq, 'closed'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'close')
    assert callable(getattr(_zmq, 'close'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'set')
    assert callable(getattr(_zmq, 'set'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'get')
    assert callable(getattr(_zmq, 'get'))

def test_bind():
    """Test de la fonction bind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'bind')
    assert callable(getattr(_zmq, 'bind'))

def test_connect():
    """Test de la fonction connect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'connect')
    assert callable(getattr(_zmq, 'connect'))

def test_unbind():
    """Test de la fonction unbind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'unbind')
    assert callable(getattr(_zmq, 'unbind'))

def test_disconnect():
    """Test de la fonction disconnect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'disconnect')
    assert callable(getattr(_zmq, 'disconnect'))

def test_monitor():
    """Test de la fonction monitor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'monitor')
    assert callable(getattr(_zmq, 'monitor'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'join')
    assert callable(getattr(_zmq, 'join'))

def test_leave():
    """Test de la fonction leave"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'leave')
    assert callable(getattr(_zmq, 'leave'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'send')
    assert callable(getattr(_zmq, 'send'))

def test_recv():
    """Test de la fonction recv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'recv')
    assert callable(getattr(_zmq, 'recv'))

def test_recv_into():
    """Test de la fonction recv_into"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_zmq, 'recv_into')
    assert callable(getattr(_zmq, 'recv_into'))

class TestFrame:
    """Tests pour la classe Frame"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_zmq, 'Frame')
        assert isinstance(getattr(_zmq, 'Frame'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_zmq, 'Frame')
        for method_name in ['__init__', '__dealloc__', '__copy__', 'fast_copy', '__getbuffer__', '__len__', 'buffer', 'bytes', 'get', 'set']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestContext:
    """Tests pour la classe Context"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_zmq, 'Context')
        assert isinstance(getattr(_zmq, 'Context'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_zmq, 'Context')
        for method_name in ['__init__', 'underlying', '_term', 'term', 'set', 'get']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSocket:
    """Tests pour la classe Socket"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_zmq, 'Socket')
        assert isinstance(getattr(_zmq, 'Socket'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_zmq, 'Socket')
        for method_name in ['__init__', 'underlying', 'closed', 'close', 'set', 'get', 'bind', 'connect', 'unbind', 'disconnect', 'monitor', 'join', 'leave', 'send', 'recv', 'recv_into']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

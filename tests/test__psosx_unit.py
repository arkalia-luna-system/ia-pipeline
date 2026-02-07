"""
Tests unitaires générés pour _psosx
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _psosx
except ImportError:
    pytest.skip(f"Module _psosx non importable")


def test_virtual_memory():
    """Test de la fonction virtual_memory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'virtual_memory')
    assert callable(getattr(_psosx, 'virtual_memory'))

def test_swap_memory():
    """Test de la fonction swap_memory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'swap_memory')
    assert callable(getattr(_psosx, 'swap_memory'))

def test_cpu_times():
    """Test de la fonction cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_times')
    assert callable(getattr(_psosx, 'cpu_times'))

def test_per_cpu_times():
    """Test de la fonction per_cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'per_cpu_times')
    assert callable(getattr(_psosx, 'per_cpu_times'))

def test_cpu_count_logical():
    """Test de la fonction cpu_count_logical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_count_logical')
    assert callable(getattr(_psosx, 'cpu_count_logical'))

def test_cpu_count_cores():
    """Test de la fonction cpu_count_cores"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_count_cores')
    assert callable(getattr(_psosx, 'cpu_count_cores'))

def test_cpu_stats():
    """Test de la fonction cpu_stats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_stats')
    assert callable(getattr(_psosx, 'cpu_stats'))

def test_cpu_freq():
    """Test de la fonction cpu_freq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_freq')
    assert callable(getattr(_psosx, 'cpu_freq'))

def test_disk_partitions():
    """Test de la fonction disk_partitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'disk_partitions')
    assert callable(getattr(_psosx, 'disk_partitions'))

def test_sensors_battery():
    """Test de la fonction sensors_battery"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'sensors_battery')
    assert callable(getattr(_psosx, 'sensors_battery'))

def test_net_connections():
    """Test de la fonction net_connections"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'net_connections')
    assert callable(getattr(_psosx, 'net_connections'))

def test_net_if_stats():
    """Test de la fonction net_if_stats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'net_if_stats')
    assert callable(getattr(_psosx, 'net_if_stats'))

def test_boot_time():
    """Test de la fonction boot_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'boot_time')
    assert callable(getattr(_psosx, 'boot_time'))

def test_users():
    """Test de la fonction users"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'users')
    assert callable(getattr(_psosx, 'users'))

def test_pids():
    """Test de la fonction pids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'pids')
    assert callable(getattr(_psosx, 'pids'))

def test_is_zombie():
    """Test de la fonction is_zombie"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'is_zombie')
    assert callable(getattr(_psosx, 'is_zombie'))

def test_wrap_exceptions():
    """Test de la fonction wrap_exceptions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'wrap_exceptions')
    assert callable(getattr(_psosx, 'wrap_exceptions'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'wrapper')
    assert callable(getattr(_psosx, 'wrapper'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, '__init__')
    assert callable(getattr(_psosx, '__init__'))

def test__get_kinfo_proc():
    """Test de la fonction _get_kinfo_proc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, '_get_kinfo_proc')
    assert callable(getattr(_psosx, '_get_kinfo_proc'))

def test__get_pidtaskinfo():
    """Test de la fonction _get_pidtaskinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, '_get_pidtaskinfo')
    assert callable(getattr(_psosx, '_get_pidtaskinfo'))

def test_oneshot_enter():
    """Test de la fonction oneshot_enter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'oneshot_enter')
    assert callable(getattr(_psosx, 'oneshot_enter'))

def test_oneshot_exit():
    """Test de la fonction oneshot_exit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'oneshot_exit')
    assert callable(getattr(_psosx, 'oneshot_exit'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'name')
    assert callable(getattr(_psosx, 'name'))

def test_exe():
    """Test de la fonction exe"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'exe')
    assert callable(getattr(_psosx, 'exe'))

def test_cmdline():
    """Test de la fonction cmdline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cmdline')
    assert callable(getattr(_psosx, 'cmdline'))

def test_environ():
    """Test de la fonction environ"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'environ')
    assert callable(getattr(_psosx, 'environ'))

def test_ppid():
    """Test de la fonction ppid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'ppid')
    assert callable(getattr(_psosx, 'ppid'))

def test_cwd():
    """Test de la fonction cwd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cwd')
    assert callable(getattr(_psosx, 'cwd'))

def test_uids():
    """Test de la fonction uids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'uids')
    assert callable(getattr(_psosx, 'uids'))

def test_gids():
    """Test de la fonction gids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'gids')
    assert callable(getattr(_psosx, 'gids'))

def test_terminal():
    """Test de la fonction terminal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'terminal')
    assert callable(getattr(_psosx, 'terminal'))

def test_memory_info():
    """Test de la fonction memory_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'memory_info')
    assert callable(getattr(_psosx, 'memory_info'))

def test_memory_full_info():
    """Test de la fonction memory_full_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'memory_full_info')
    assert callable(getattr(_psosx, 'memory_full_info'))

def test_cpu_times():
    """Test de la fonction cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'cpu_times')
    assert callable(getattr(_psosx, 'cpu_times'))

def test_create_time():
    """Test de la fonction create_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'create_time')
    assert callable(getattr(_psosx, 'create_time'))

def test_num_ctx_switches():
    """Test de la fonction num_ctx_switches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'num_ctx_switches')
    assert callable(getattr(_psosx, 'num_ctx_switches'))

def test_num_threads():
    """Test de la fonction num_threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'num_threads')
    assert callable(getattr(_psosx, 'num_threads'))

def test_open_files():
    """Test de la fonction open_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'open_files')
    assert callable(getattr(_psosx, 'open_files'))

def test_net_connections():
    """Test de la fonction net_connections"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'net_connections')
    assert callable(getattr(_psosx, 'net_connections'))

def test_num_fds():
    """Test de la fonction num_fds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'num_fds')
    assert callable(getattr(_psosx, 'num_fds'))

def test_wait():
    """Test de la fonction wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'wait')
    assert callable(getattr(_psosx, 'wait'))

def test_nice_get():
    """Test de la fonction nice_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'nice_get')
    assert callable(getattr(_psosx, 'nice_get'))

def test_nice_set():
    """Test de la fonction nice_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'nice_set')
    assert callable(getattr(_psosx, 'nice_set'))

def test_status():
    """Test de la fonction status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'status')
    assert callable(getattr(_psosx, 'status'))

def test_threads():
    """Test de la fonction threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psosx, 'threads')
    assert callable(getattr(_psosx, 'threads'))

class TestProcess:
    """Tests pour la classe Process"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_psosx, 'Process')
        assert isinstance(getattr(_psosx, 'Process'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_psosx, 'Process')
        for method_name in ['__init__', '_get_kinfo_proc', '_get_pidtaskinfo', 'oneshot_enter', 'oneshot_exit', 'name', 'exe', 'cmdline', 'environ', 'ppid', 'cwd', 'uids', 'gids', 'terminal', 'memory_info', 'memory_full_info', 'cpu_times', 'create_time', 'num_ctx_switches', 'num_threads', 'open_files', 'net_connections', 'num_fds', 'wait', 'nice_get', 'nice_set', 'status', 'threads']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

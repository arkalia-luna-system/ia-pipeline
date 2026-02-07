"""
Tests unitaires générés pour _pslinux
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _pslinux
except ImportError:
    pytest.skip(f"Module _pslinux non importable")


def test_readlink():
    """Test de la fonction readlink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'readlink')
    assert callable(getattr(_pslinux, 'readlink'))

def test_file_flags_to_mode():
    """Test de la fonction file_flags_to_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'file_flags_to_mode')
    assert callable(getattr(_pslinux, 'file_flags_to_mode'))

def test_is_storage_device():
    """Test de la fonction is_storage_device"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'is_storage_device')
    assert callable(getattr(_pslinux, 'is_storage_device'))

def test_set_scputimes_ntuple():
    """Test de la fonction set_scputimes_ntuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'set_scputimes_ntuple')
    assert callable(getattr(_pslinux, 'set_scputimes_ntuple'))

def test_calculate_avail_vmem():
    """Test de la fonction calculate_avail_vmem"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'calculate_avail_vmem')
    assert callable(getattr(_pslinux, 'calculate_avail_vmem'))

def test_virtual_memory():
    """Test de la fonction virtual_memory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'virtual_memory')
    assert callable(getattr(_pslinux, 'virtual_memory'))

def test_swap_memory():
    """Test de la fonction swap_memory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'swap_memory')
    assert callable(getattr(_pslinux, 'swap_memory'))

def test_cpu_times():
    """Test de la fonction cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_times')
    assert callable(getattr(_pslinux, 'cpu_times'))

def test_per_cpu_times():
    """Test de la fonction per_cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'per_cpu_times')
    assert callable(getattr(_pslinux, 'per_cpu_times'))

def test_cpu_count_logical():
    """Test de la fonction cpu_count_logical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_count_logical')
    assert callable(getattr(_pslinux, 'cpu_count_logical'))

def test_cpu_count_cores():
    """Test de la fonction cpu_count_cores"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_count_cores')
    assert callable(getattr(_pslinux, 'cpu_count_cores'))

def test_cpu_stats():
    """Test de la fonction cpu_stats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_stats')
    assert callable(getattr(_pslinux, 'cpu_stats'))

def test__cpu_get_cpuinfo_freq():
    """Test de la fonction _cpu_get_cpuinfo_freq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_cpu_get_cpuinfo_freq')
    assert callable(getattr(_pslinux, '_cpu_get_cpuinfo_freq'))

def test_net_connections():
    """Test de la fonction net_connections"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'net_connections')
    assert callable(getattr(_pslinux, 'net_connections'))

def test_net_io_counters():
    """Test de la fonction net_io_counters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'net_io_counters')
    assert callable(getattr(_pslinux, 'net_io_counters'))

def test_net_if_stats():
    """Test de la fonction net_if_stats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'net_if_stats')
    assert callable(getattr(_pslinux, 'net_if_stats'))

def test_disk_io_counters():
    """Test de la fonction disk_io_counters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'disk_io_counters')
    assert callable(getattr(_pslinux, 'disk_io_counters'))

def test_disk_partitions():
    """Test de la fonction disk_partitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'disk_partitions')
    assert callable(getattr(_pslinux, 'disk_partitions'))

def test_sensors_temperatures():
    """Test de la fonction sensors_temperatures"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'sensors_temperatures')
    assert callable(getattr(_pslinux, 'sensors_temperatures'))

def test_sensors_fans():
    """Test de la fonction sensors_fans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'sensors_fans')
    assert callable(getattr(_pslinux, 'sensors_fans'))

def test_sensors_battery():
    """Test de la fonction sensors_battery"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'sensors_battery')
    assert callable(getattr(_pslinux, 'sensors_battery'))

def test_users():
    """Test de la fonction users"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'users')
    assert callable(getattr(_pslinux, 'users'))

def test_boot_time():
    """Test de la fonction boot_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'boot_time')
    assert callable(getattr(_pslinux, 'boot_time'))

def test_pids():
    """Test de la fonction pids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'pids')
    assert callable(getattr(_pslinux, 'pids'))

def test_pid_exists():
    """Test de la fonction pid_exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'pid_exists')
    assert callable(getattr(_pslinux, 'pid_exists'))

def test_ppid_map():
    """Test de la fonction ppid_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ppid_map')
    assert callable(getattr(_pslinux, 'ppid_map'))

def test_wrap_exceptions():
    """Test de la fonction wrap_exceptions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'wrap_exceptions')
    assert callable(getattr(_pslinux, 'wrap_exceptions'))

def test_cpu_freq():
    """Test de la fonction cpu_freq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_freq')
    assert callable(getattr(_pslinux, 'cpu_freq'))

def test_cpu_freq():
    """Test de la fonction cpu_freq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_freq')
    assert callable(getattr(_pslinux, 'cpu_freq'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '__init__')
    assert callable(getattr(_pslinux, '__init__'))

def test_get_proc_inodes():
    """Test de la fonction get_proc_inodes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'get_proc_inodes')
    assert callable(getattr(_pslinux, 'get_proc_inodes'))

def test_get_all_inodes():
    """Test de la fonction get_all_inodes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'get_all_inodes')
    assert callable(getattr(_pslinux, 'get_all_inodes'))

def test_decode_address():
    """Test de la fonction decode_address"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'decode_address')
    assert callable(getattr(_pslinux, 'decode_address'))

def test_process_inet():
    """Test de la fonction process_inet"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'process_inet')
    assert callable(getattr(_pslinux, 'process_inet'))

def test_process_unix():
    """Test de la fonction process_unix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'process_unix')
    assert callable(getattr(_pslinux, 'process_unix'))

def test_retrieve():
    """Test de la fonction retrieve"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'retrieve')
    assert callable(getattr(_pslinux, 'retrieve'))

def test_read_procfs():
    """Test de la fonction read_procfs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'read_procfs')
    assert callable(getattr(_pslinux, 'read_procfs'))

def test_read_sysfs():
    """Test de la fonction read_sysfs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'read_sysfs')
    assert callable(getattr(_pslinux, 'read_sysfs'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '__init__')
    assert callable(getattr(_pslinux, '__init__'))

def test_ask_proc_partitions():
    """Test de la fonction ask_proc_partitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ask_proc_partitions')
    assert callable(getattr(_pslinux, 'ask_proc_partitions'))

def test_ask_sys_dev_block():
    """Test de la fonction ask_sys_dev_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ask_sys_dev_block')
    assert callable(getattr(_pslinux, 'ask_sys_dev_block'))

def test_ask_sys_class_block():
    """Test de la fonction ask_sys_class_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ask_sys_class_block')
    assert callable(getattr(_pslinux, 'ask_sys_class_block'))

def test_find():
    """Test de la fonction find"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'find')
    assert callable(getattr(_pslinux, 'find'))

def test_multi_bcat():
    """Test de la fonction multi_bcat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'multi_bcat')
    assert callable(getattr(_pslinux, 'multi_bcat'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'wrapper')
    assert callable(getattr(_pslinux, 'wrapper'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '__init__')
    assert callable(getattr(_pslinux, '__init__'))

def test__is_zombie():
    """Test de la fonction _is_zombie"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_is_zombie')
    assert callable(getattr(_pslinux, '_is_zombie'))

def test__raise_if_zombie():
    """Test de la fonction _raise_if_zombie"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_raise_if_zombie')
    assert callable(getattr(_pslinux, '_raise_if_zombie'))

def test__raise_if_not_alive():
    """Test de la fonction _raise_if_not_alive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_raise_if_not_alive')
    assert callable(getattr(_pslinux, '_raise_if_not_alive'))

def test__parse_stat_file():
    """Test de la fonction _parse_stat_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_parse_stat_file')
    assert callable(getattr(_pslinux, '_parse_stat_file'))

def test__read_status_file():
    """Test de la fonction _read_status_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_read_status_file')
    assert callable(getattr(_pslinux, '_read_status_file'))

def test__read_smaps_file():
    """Test de la fonction _read_smaps_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_read_smaps_file')
    assert callable(getattr(_pslinux, '_read_smaps_file'))

def test_oneshot_enter():
    """Test de la fonction oneshot_enter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'oneshot_enter')
    assert callable(getattr(_pslinux, 'oneshot_enter'))

def test_oneshot_exit():
    """Test de la fonction oneshot_exit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'oneshot_exit')
    assert callable(getattr(_pslinux, 'oneshot_exit'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'name')
    assert callable(getattr(_pslinux, 'name'))

def test_exe():
    """Test de la fonction exe"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'exe')
    assert callable(getattr(_pslinux, 'exe'))

def test_cmdline():
    """Test de la fonction cmdline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cmdline')
    assert callable(getattr(_pslinux, 'cmdline'))

def test_environ():
    """Test de la fonction environ"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'environ')
    assert callable(getattr(_pslinux, 'environ'))

def test_terminal():
    """Test de la fonction terminal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'terminal')
    assert callable(getattr(_pslinux, 'terminal'))

def test_cpu_times():
    """Test de la fonction cpu_times"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_times')
    assert callable(getattr(_pslinux, 'cpu_times'))

def test_cpu_num():
    """Test de la fonction cpu_num"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_num')
    assert callable(getattr(_pslinux, 'cpu_num'))

def test_wait():
    """Test de la fonction wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'wait')
    assert callable(getattr(_pslinux, 'wait'))

def test_create_time():
    """Test de la fonction create_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'create_time')
    assert callable(getattr(_pslinux, 'create_time'))

def test_memory_info():
    """Test de la fonction memory_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'memory_info')
    assert callable(getattr(_pslinux, 'memory_info'))

def test_cwd():
    """Test de la fonction cwd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cwd')
    assert callable(getattr(_pslinux, 'cwd'))

def test_num_ctx_switches():
    """Test de la fonction num_ctx_switches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'num_ctx_switches')
    assert callable(getattr(_pslinux, 'num_ctx_switches'))

def test_num_threads():
    """Test de la fonction num_threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'num_threads')
    assert callable(getattr(_pslinux, 'num_threads'))

def test_threads():
    """Test de la fonction threads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'threads')
    assert callable(getattr(_pslinux, 'threads'))

def test_nice_get():
    """Test de la fonction nice_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'nice_get')
    assert callable(getattr(_pslinux, 'nice_get'))

def test_nice_set():
    """Test de la fonction nice_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'nice_set')
    assert callable(getattr(_pslinux, 'nice_set'))

def test_status():
    """Test de la fonction status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'status')
    assert callable(getattr(_pslinux, 'status'))

def test_open_files():
    """Test de la fonction open_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'open_files')
    assert callable(getattr(_pslinux, 'open_files'))

def test_net_connections():
    """Test de la fonction net_connections"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'net_connections')
    assert callable(getattr(_pslinux, 'net_connections'))

def test_num_fds():
    """Test de la fonction num_fds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'num_fds')
    assert callable(getattr(_pslinux, 'num_fds'))

def test_ppid():
    """Test de la fonction ppid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ppid')
    assert callable(getattr(_pslinux, 'ppid'))

def test_uids():
    """Test de la fonction uids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'uids')
    assert callable(getattr(_pslinux, 'uids'))

def test_gids():
    """Test de la fonction gids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'gids')
    assert callable(getattr(_pslinux, 'gids'))

def test_io_counters():
    """Test de la fonction io_counters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'io_counters')
    assert callable(getattr(_pslinux, 'io_counters'))

def test__parse_smaps_rollup():
    """Test de la fonction _parse_smaps_rollup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_parse_smaps_rollup')
    assert callable(getattr(_pslinux, '_parse_smaps_rollup'))

def test__parse_smaps():
    """Test de la fonction _parse_smaps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_parse_smaps')
    assert callable(getattr(_pslinux, '_parse_smaps'))

def test_memory_full_info():
    """Test de la fonction memory_full_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'memory_full_info')
    assert callable(getattr(_pslinux, 'memory_full_info'))

def test_memory_maps():
    """Test de la fonction memory_maps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'memory_maps')
    assert callable(getattr(_pslinux, 'memory_maps'))

def test_cpu_affinity_get():
    """Test de la fonction cpu_affinity_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_affinity_get')
    assert callable(getattr(_pslinux, 'cpu_affinity_get'))

def test__get_eligible_cpus():
    """Test de la fonction _get_eligible_cpus"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, '_get_eligible_cpus')
    assert callable(getattr(_pslinux, '_get_eligible_cpus'))

def test_cpu_affinity_set():
    """Test de la fonction cpu_affinity_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'cpu_affinity_set')
    assert callable(getattr(_pslinux, 'cpu_affinity_set'))

def test_ionice_get():
    """Test de la fonction ionice_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ionice_get')
    assert callable(getattr(_pslinux, 'ionice_get'))

def test_ionice_set():
    """Test de la fonction ionice_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'ionice_set')
    assert callable(getattr(_pslinux, 'ionice_set'))

def test_rlimit():
    """Test de la fonction rlimit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'rlimit')
    assert callable(getattr(_pslinux, 'rlimit'))

def test_get_blocks():
    """Test de la fonction get_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pslinux, 'get_blocks')
    assert callable(getattr(_pslinux, 'get_blocks'))

class TestIOPriority:
    """Tests pour la classe IOPriority"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pslinux, 'IOPriority')
        assert isinstance(getattr(_pslinux, 'IOPriority'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pslinux, 'IOPriority')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Ipv6UnsupportedError:
    """Tests pour la classe _Ipv6UnsupportedError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pslinux, '_Ipv6UnsupportedError')
        assert isinstance(getattr(_pslinux, '_Ipv6UnsupportedError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pslinux, '_Ipv6UnsupportedError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNetConnections:
    """Tests pour la classe NetConnections"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pslinux, 'NetConnections')
        assert isinstance(getattr(_pslinux, 'NetConnections'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pslinux, 'NetConnections')
        for method_name in ['__init__', 'get_proc_inodes', 'get_all_inodes', 'decode_address', 'process_inet', 'process_unix', 'retrieve']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRootFsDeviceFinder:
    """Tests pour la classe RootFsDeviceFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pslinux, 'RootFsDeviceFinder')
        assert isinstance(getattr(_pslinux, 'RootFsDeviceFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pslinux, 'RootFsDeviceFinder')
        for method_name in ['__init__', 'ask_proc_partitions', 'ask_sys_dev_block', 'ask_sys_class_block', 'find']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProcess:
    """Tests pour la classe Process"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pslinux, 'Process')
        assert isinstance(getattr(_pslinux, 'Process'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pslinux, 'Process')
        for method_name in ['__init__', '_is_zombie', '_raise_if_zombie', '_raise_if_not_alive', '_parse_stat_file', '_read_status_file', '_read_smaps_file', 'oneshot_enter', 'oneshot_exit', 'name', 'exe', 'cmdline', 'environ', 'terminal', 'cpu_times', 'cpu_num', 'wait', 'create_time', 'memory_info', 'cwd', 'num_ctx_switches', 'num_threads', 'threads', 'nice_get', 'nice_set', 'status', 'open_files', 'net_connections', 'num_fds', 'ppid', 'uids', 'gids']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

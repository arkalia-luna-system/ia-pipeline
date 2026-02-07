"""
Tests unitaires générés pour shellapp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import shellapp
except ImportError:
    pytest.skip(f"Module shellapp non importable")


def test__user_ns_changed():
    """Test de la fonction _user_ns_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_user_ns_changed')
    assert callable(getattr(shellapp, '_user_ns_changed'))

def test_init_path():
    """Test de la fonction init_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, 'init_path')
    assert callable(getattr(shellapp, 'init_path'))

def test_init_shell():
    """Test de la fonction init_shell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, 'init_shell')
    assert callable(getattr(shellapp, 'init_shell'))

def test_init_gui_pylab():
    """Test de la fonction init_gui_pylab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, 'init_gui_pylab')
    assert callable(getattr(shellapp, 'init_gui_pylab'))

def test_init_extensions():
    """Test de la fonction init_extensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, 'init_extensions')
    assert callable(getattr(shellapp, 'init_extensions'))

def test_init_code():
    """Test de la fonction init_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, 'init_code')
    assert callable(getattr(shellapp, 'init_code'))

def test__run_exec_lines():
    """Test de la fonction _run_exec_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_run_exec_lines')
    assert callable(getattr(shellapp, '_run_exec_lines'))

def test__exec_file():
    """Test de la fonction _exec_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_exec_file')
    assert callable(getattr(shellapp, '_exec_file'))

def test__run_startup_files():
    """Test de la fonction _run_startup_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_run_startup_files')
    assert callable(getattr(shellapp, '_run_startup_files'))

def test__run_exec_files():
    """Test de la fonction _run_exec_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_run_exec_files')
    assert callable(getattr(shellapp, '_run_exec_files'))

def test__run_cmd_line_code():
    """Test de la fonction _run_cmd_line_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_run_cmd_line_code')
    assert callable(getattr(shellapp, '_run_cmd_line_code'))

def test__run_module():
    """Test de la fonction _run_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shellapp, '_run_module')
    assert callable(getattr(shellapp, '_run_module'))

class TestInteractiveShellApp:
    """Tests pour la classe InteractiveShellApp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shellapp, 'InteractiveShellApp')
        assert isinstance(getattr(shellapp, 'InteractiveShellApp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shellapp, 'InteractiveShellApp')
        for method_name in ['_user_ns_changed', 'init_path', 'init_shell', 'init_gui_pylab', 'init_extensions', 'init_code', '_run_exec_lines', '_exec_file', '_run_startup_files', '_run_exec_files', '_run_cmd_line_code', '_run_module']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

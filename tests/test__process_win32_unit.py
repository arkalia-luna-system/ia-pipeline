"""
Tests unitaires générés pour _process_win32
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _process_win32
except ImportError:
    pytest.skip(f"Module _process_win32 non importable")


def test__system_body():
    """Test de la fonction _system_body"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, '_system_body')
    assert callable(getattr(_process_win32, '_system_body'))

def test_system():
    """Test de la fonction system"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'system')
    assert callable(getattr(_process_win32, 'system'))

def test_getoutput():
    """Test de la fonction getoutput"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'getoutput')
    assert callable(getattr(_process_win32, 'getoutput'))

def test_check_pid():
    """Test de la fonction check_pid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'check_pid')
    assert callable(getattr(_process_win32, 'check_pid'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, '__enter__')
    assert callable(getattr(_process_win32, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, '__exit__')
    assert callable(getattr(_process_win32, '__exit__'))

def test_stdout_read():
    """Test de la fonction stdout_read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'stdout_read')
    assert callable(getattr(_process_win32, 'stdout_read'))

def test_stderr_read():
    """Test de la fonction stderr_read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'stderr_read')
    assert callable(getattr(_process_win32, 'stderr_read'))

def test_arg_split():
    """Test de la fonction arg_split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_process_win32, 'arg_split')
    assert callable(getattr(_process_win32, 'arg_split'))

class TestAvoidUNCPath:
    """Tests pour la classe AvoidUNCPath"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_process_win32, 'AvoidUNCPath')
        assert isinstance(getattr(_process_win32, 'AvoidUNCPath'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_process_win32, 'AvoidUNCPath')
        for method_name in ['__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour ipapp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ipapp
except ImportError:
    pytest.skip(f"Module ipapp non importable")


def test_load_default_config():
    """Test de la fonction load_default_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'load_default_config')
    assert callable(getattr(ipapp, 'load_default_config'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '__init__')
    assert callable(getattr(ipapp, '__init__'))

def test_make_report():
    """Test de la fonction make_report"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'make_report')
    assert callable(getattr(ipapp, 'make_report'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'start')
    assert callable(getattr(ipapp, 'start'))

def test__classes_default():
    """Test de la fonction _classes_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '_classes_default')
    assert callable(getattr(ipapp, '_classes_default'))

def test__quick_changed():
    """Test de la fonction _quick_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '_quick_changed')
    assert callable(getattr(ipapp, '_quick_changed'))

def test__force_interact_changed():
    """Test de la fonction _force_interact_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '_force_interact_changed')
    assert callable(getattr(ipapp, '_force_interact_changed'))

def test__file_to_run_changed():
    """Test de la fonction _file_to_run_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '_file_to_run_changed')
    assert callable(getattr(ipapp, '_file_to_run_changed'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'initialize')
    assert callable(getattr(ipapp, 'initialize'))

def test_init_shell():
    """Test de la fonction init_shell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'init_shell')
    assert callable(getattr(ipapp, 'init_shell'))

def test_init_banner():
    """Test de la fonction init_banner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'init_banner')
    assert callable(getattr(ipapp, 'init_banner'))

def test__pylab_changed():
    """Test de la fonction _pylab_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, '_pylab_changed')
    assert callable(getattr(ipapp, '_pylab_changed'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipapp, 'start')
    assert callable(getattr(ipapp, 'start'))

class TestIPAppCrashHandler:
    """Tests pour la classe IPAppCrashHandler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ipapp, 'IPAppCrashHandler')
        assert isinstance(getattr(ipapp, 'IPAppCrashHandler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ipapp, 'IPAppCrashHandler')
        for method_name in ['__init__', 'make_report']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLocateIPythonApp:
    """Tests pour la classe LocateIPythonApp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ipapp, 'LocateIPythonApp')
        assert isinstance(getattr(ipapp, 'LocateIPythonApp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ipapp, 'LocateIPythonApp')
        for method_name in ['start']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTerminalIPythonApp:
    """Tests pour la classe TerminalIPythonApp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ipapp, 'TerminalIPythonApp')
        assert isinstance(getattr(ipapp, 'TerminalIPythonApp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ipapp, 'TerminalIPythonApp')
        for method_name in ['_classes_default', '_quick_changed', '_force_interact_changed', '_file_to_run_changed', 'initialize', 'init_shell', 'init_banner', '_pylab_changed', 'start']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour local_script_runner
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import local_script_runner
except ImportError:
    pytest.skip(f"Module local_script_runner non importable")


def test_require_widgets_deltas():
    """Test de la fonction require_widgets_deltas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'require_widgets_deltas')
    assert callable(getattr(local_script_runner, 'require_widgets_deltas'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, '__init__')
    assert callable(getattr(local_script_runner, '__init__'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'join')
    assert callable(getattr(local_script_runner, 'join'))

def test_forward_msgs():
    """Test de la fonction forward_msgs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'forward_msgs')
    assert callable(getattr(local_script_runner, 'forward_msgs'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'run')
    assert callable(getattr(local_script_runner, 'run'))

def test_script_stopped():
    """Test de la fonction script_stopped"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'script_stopped')
    assert callable(getattr(local_script_runner, 'script_stopped'))

def test__on_script_finished():
    """Test de la fonction _on_script_finished"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, '_on_script_finished')
    assert callable(getattr(local_script_runner, '_on_script_finished'))

def test__new_module():
    """Test de la fonction _new_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, '_new_module')
    assert callable(getattr(local_script_runner, '_new_module'))

def test_record_event():
    """Test de la fonction record_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_script_runner, 'record_event')
    assert callable(getattr(local_script_runner, 'record_event'))

class TestLocalScriptRunner:
    """Tests pour la classe LocalScriptRunner"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(local_script_runner, 'LocalScriptRunner')
        assert isinstance(getattr(local_script_runner, 'LocalScriptRunner'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(local_script_runner, 'LocalScriptRunner')
        for method_name in ['__init__', 'join', 'forward_msgs', 'run', 'script_stopped', '_on_script_finished', '_new_module']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

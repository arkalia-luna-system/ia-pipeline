"""
Tests unitaires générés pour guisupport
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import guisupport
except ImportError:
    pytest.skip(f"Module guisupport non importable")


def test_get_app_wx():
    """Test de la fonction get_app_wx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'get_app_wx')
    assert callable(getattr(guisupport, 'get_app_wx'))

def test_is_event_loop_running_wx():
    """Test de la fonction is_event_loop_running_wx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'is_event_loop_running_wx')
    assert callable(getattr(guisupport, 'is_event_loop_running_wx'))

def test_start_event_loop_wx():
    """Test de la fonction start_event_loop_wx"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'start_event_loop_wx')
    assert callable(getattr(guisupport, 'start_event_loop_wx'))

def test_get_app_qt4():
    """Test de la fonction get_app_qt4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'get_app_qt4')
    assert callable(getattr(guisupport, 'get_app_qt4'))

def test_is_event_loop_running_qt4():
    """Test de la fonction is_event_loop_running_qt4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'is_event_loop_running_qt4')
    assert callable(getattr(guisupport, 'is_event_loop_running_qt4'))

def test_start_event_loop_qt4():
    """Test de la fonction start_event_loop_qt4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(guisupport, 'start_event_loop_qt4')
    assert callable(getattr(guisupport, 'start_event_loop_qt4'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour plugins_manager
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import plugins_manager
except ImportError:
    pytest.skip(f"Module plugins_manager non importable")


def test_list_plugins():
    """Test de la fonction list_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(plugins_manager, 'list_plugins')
    assert callable(getattr(plugins_manager, 'list_plugins'))

def test_load_plugin():
    """Test de la fonction load_plugin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(plugins_manager, 'load_plugin')
    assert callable(getattr(plugins_manager, 'load_plugin'))

def test_run_all_plugins():
    """Test de la fonction run_all_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(plugins_manager, 'run_all_plugins')
    assert callable(getattr(plugins_manager, 'run_all_plugins'))

if __name__ == "__main__":
    pytest.main([__file__])

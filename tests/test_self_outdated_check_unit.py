"""
Tests unitaires générés pour self_outdated_check
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import self_outdated_check
except ImportError:
    pytest.skip(f"Module self_outdated_check non importable")


def test__get_statefile_name():
    """Test de la fonction _get_statefile_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '_get_statefile_name')
    assert callable(getattr(self_outdated_check, '_get_statefile_name'))

def test__convert_date():
    """Test de la fonction _convert_date"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '_convert_date')
    assert callable(getattr(self_outdated_check, '_convert_date'))

def test_was_installed_by_pip():
    """Test de la fonction was_installed_by_pip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, 'was_installed_by_pip')
    assert callable(getattr(self_outdated_check, 'was_installed_by_pip'))

def test__get_current_remote_pip_version():
    """Test de la fonction _get_current_remote_pip_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '_get_current_remote_pip_version')
    assert callable(getattr(self_outdated_check, '_get_current_remote_pip_version'))

def test__self_version_check_logic():
    """Test de la fonction _self_version_check_logic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '_self_version_check_logic')
    assert callable(getattr(self_outdated_check, '_self_version_check_logic'))

def test_pip_self_version_check():
    """Test de la fonction pip_self_version_check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, 'pip_self_version_check')
    assert callable(getattr(self_outdated_check, 'pip_self_version_check'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '__init__')
    assert callable(getattr(self_outdated_check, '__init__'))

def test_key():
    """Test de la fonction key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, 'key')
    assert callable(getattr(self_outdated_check, 'key'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, 'get')
    assert callable(getattr(self_outdated_check, 'get'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, 'set')
    assert callable(getattr(self_outdated_check, 'set'))

def test___rich__():
    """Test de la fonction __rich__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(self_outdated_check, '__rich__')
    assert callable(getattr(self_outdated_check, '__rich__'))

class TestSelfCheckState:
    """Tests pour la classe SelfCheckState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(self_outdated_check, 'SelfCheckState')
        assert isinstance(getattr(self_outdated_check, 'SelfCheckState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(self_outdated_check, 'SelfCheckState')
        for method_name in ['__init__', 'key', 'get', 'set']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUpgradePrompt:
    """Tests pour la classe UpgradePrompt"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(self_outdated_check, 'UpgradePrompt')
        assert isinstance(getattr(self_outdated_check, 'UpgradePrompt'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(self_outdated_check, 'UpgradePrompt')
        for method_name in ['__rich__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

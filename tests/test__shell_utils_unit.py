"""
Tests unitaires générés pour _shell_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _shell_utils
except ImportError:
    pytest.skip(f"Module _shell_utils non importable")


def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'join')
    assert callable(getattr(_shell_utils, 'join'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'split')
    assert callable(getattr(_shell_utils, 'split'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'join')
    assert callable(getattr(_shell_utils, 'join'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'split')
    assert callable(getattr(_shell_utils, 'split'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'join')
    assert callable(getattr(_shell_utils, 'join'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_shell_utils, 'split')
    assert callable(getattr(_shell_utils, 'split'))

class TestCommandLineParser:
    """Tests pour la classe CommandLineParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_shell_utils, 'CommandLineParser')
        assert isinstance(getattr(_shell_utils, 'CommandLineParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_shell_utils, 'CommandLineParser')
        for method_name in ['join', 'split']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWindowsParser:
    """Tests pour la classe WindowsParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_shell_utils, 'WindowsParser')
        assert isinstance(getattr(_shell_utils, 'WindowsParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_shell_utils, 'WindowsParser')
        for method_name in ['join', 'split']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPosixParser:
    """Tests pour la classe PosixParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_shell_utils, 'PosixParser')
        assert isinstance(getattr(_shell_utils, 'PosixParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_shell_utils, 'PosixParser')
        for method_name in ['join', 'split']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

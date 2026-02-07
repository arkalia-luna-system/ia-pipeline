"""
Tests unitaires générés pour _completion_classes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _completion_classes
except ImportError:
    pytest.skip(f"Module _completion_classes non importable")


def test__sanitize_help_text():
    """Test de la fonction _sanitize_help_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, '_sanitize_help_text')
    assert callable(getattr(_completion_classes, '_sanitize_help_text'))

def test_completion_init():
    """Test de la fonction completion_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'completion_init')
    assert callable(getattr(_completion_classes, 'completion_init'))

def test_source_vars():
    """Test de la fonction source_vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'source_vars')
    assert callable(getattr(_completion_classes, 'source_vars'))

def test_get_completion_args():
    """Test de la fonction get_completion_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'get_completion_args')
    assert callable(getattr(_completion_classes, 'get_completion_args'))

def test_format_completion():
    """Test de la fonction format_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'format_completion')
    assert callable(getattr(_completion_classes, 'format_completion'))

def test_complete():
    """Test de la fonction complete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'complete')
    assert callable(getattr(_completion_classes, 'complete'))

def test_source_vars():
    """Test de la fonction source_vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'source_vars')
    assert callable(getattr(_completion_classes, 'source_vars'))

def test_get_completion_args():
    """Test de la fonction get_completion_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'get_completion_args')
    assert callable(getattr(_completion_classes, 'get_completion_args'))

def test_format_completion():
    """Test de la fonction format_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'format_completion')
    assert callable(getattr(_completion_classes, 'format_completion'))

def test_complete():
    """Test de la fonction complete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'complete')
    assert callable(getattr(_completion_classes, 'complete'))

def test_source_vars():
    """Test de la fonction source_vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'source_vars')
    assert callable(getattr(_completion_classes, 'source_vars'))

def test_get_completion_args():
    """Test de la fonction get_completion_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'get_completion_args')
    assert callable(getattr(_completion_classes, 'get_completion_args'))

def test_format_completion():
    """Test de la fonction format_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'format_completion')
    assert callable(getattr(_completion_classes, 'format_completion'))

def test_complete():
    """Test de la fonction complete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'complete')
    assert callable(getattr(_completion_classes, 'complete'))

def test_source_vars():
    """Test de la fonction source_vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'source_vars')
    assert callable(getattr(_completion_classes, 'source_vars'))

def test_get_completion_args():
    """Test de la fonction get_completion_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'get_completion_args')
    assert callable(getattr(_completion_classes, 'get_completion_args'))

def test_format_completion():
    """Test de la fonction format_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'format_completion')
    assert callable(getattr(_completion_classes, 'format_completion'))

def test_escape():
    """Test de la fonction escape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_classes, 'escape')
    assert callable(getattr(_completion_classes, 'escape'))

class TestBashComplete:
    """Tests pour la classe BashComplete"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_completion_classes, 'BashComplete')
        assert isinstance(getattr(_completion_classes, 'BashComplete'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_completion_classes, 'BashComplete')
        for method_name in ['source_vars', 'get_completion_args', 'format_completion', 'complete']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestZshComplete:
    """Tests pour la classe ZshComplete"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_completion_classes, 'ZshComplete')
        assert isinstance(getattr(_completion_classes, 'ZshComplete'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_completion_classes, 'ZshComplete')
        for method_name in ['source_vars', 'get_completion_args', 'format_completion', 'complete']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFishComplete:
    """Tests pour la classe FishComplete"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_completion_classes, 'FishComplete')
        assert isinstance(getattr(_completion_classes, 'FishComplete'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_completion_classes, 'FishComplete')
        for method_name in ['source_vars', 'get_completion_args', 'format_completion', 'complete']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPowerShellComplete:
    """Tests pour la classe PowerShellComplete"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_completion_classes, 'PowerShellComplete')
        assert isinstance(getattr(_completion_classes, 'PowerShellComplete'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_completion_classes, 'PowerShellComplete')
        for method_name in ['source_vars', 'get_completion_args', 'format_completion']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

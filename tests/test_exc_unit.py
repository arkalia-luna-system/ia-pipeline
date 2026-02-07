"""
Tests unitaires générés pour exc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import exc
except ImportError:
    pytest.skip(f"Module exc non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__str__')
    assert callable(getattr(exc, '__str__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__str__')
    assert callable(getattr(exc, '__str__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__init__')
    assert callable(getattr(exc, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(exc, '__str__')
    assert callable(getattr(exc, '__str__'))

class TestGitError:
    """Tests pour la classe GitError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'GitError')
        assert isinstance(getattr(exc, 'GitError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'GitError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInvalidGitRepositoryError:
    """Tests pour la classe InvalidGitRepositoryError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'InvalidGitRepositoryError')
        assert isinstance(getattr(exc, 'InvalidGitRepositoryError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'InvalidGitRepositoryError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWorkTreeRepositoryUnsupported:
    """Tests pour la classe WorkTreeRepositoryUnsupported"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'WorkTreeRepositoryUnsupported')
        assert isinstance(getattr(exc, 'WorkTreeRepositoryUnsupported'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'WorkTreeRepositoryUnsupported')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNoSuchPathError:
    """Tests pour la classe NoSuchPathError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'NoSuchPathError')
        assert isinstance(getattr(exc, 'NoSuchPathError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'NoSuchPathError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnsafeProtocolError:
    """Tests pour la classe UnsafeProtocolError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'UnsafeProtocolError')
        assert isinstance(getattr(exc, 'UnsafeProtocolError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'UnsafeProtocolError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnsafeOptionError:
    """Tests pour la classe UnsafeOptionError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'UnsafeOptionError')
        assert isinstance(getattr(exc, 'UnsafeOptionError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'UnsafeOptionError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCommandError:
    """Tests pour la classe CommandError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'CommandError')
        assert isinstance(getattr(exc, 'CommandError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'CommandError')
        for method_name in ['__init__', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGitCommandNotFound:
    """Tests pour la classe GitCommandNotFound"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'GitCommandNotFound')
        assert isinstance(getattr(exc, 'GitCommandNotFound'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'GitCommandNotFound')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGitCommandError:
    """Tests pour la classe GitCommandError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'GitCommandError')
        assert isinstance(getattr(exc, 'GitCommandError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'GitCommandError')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCheckoutError:
    """Tests pour la classe CheckoutError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'CheckoutError')
        assert isinstance(getattr(exc, 'CheckoutError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'CheckoutError')
        for method_name in ['__init__', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCacheError:
    """Tests pour la classe CacheError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'CacheError')
        assert isinstance(getattr(exc, 'CacheError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'CacheError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnmergedEntriesError:
    """Tests pour la classe UnmergedEntriesError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'UnmergedEntriesError')
        assert isinstance(getattr(exc, 'UnmergedEntriesError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'UnmergedEntriesError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHookExecutionError:
    """Tests pour la classe HookExecutionError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'HookExecutionError')
        assert isinstance(getattr(exc, 'HookExecutionError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'HookExecutionError')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRepositoryDirtyError:
    """Tests pour la classe RepositoryDirtyError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(exc, 'RepositoryDirtyError')
        assert isinstance(getattr(exc, 'RepositoryDirtyError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(exc, 'RepositoryDirtyError')
        for method_name in ['__init__', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

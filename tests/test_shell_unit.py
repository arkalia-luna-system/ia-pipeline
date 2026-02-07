"""
Tests unitaires générés pour shell
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import shell
except ImportError:
    pytest.skip(f"Module shell non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, 'analyse_text')
    assert callable(getattr(shell, 'analyse_text'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, 'get_tokens_unprocessed')
    assert callable(getattr(shell, 'get_tokens_unprocessed'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, 'get_tokens_unprocessed')
    assert callable(getattr(shell, 'get_tokens_unprocessed'))

def test__make_begin_state():
    """Test de la fonction _make_begin_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_begin_state')
    assert callable(getattr(shell, '_make_begin_state'))

def test__make_follow_state():
    """Test de la fonction _make_follow_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_follow_state')
    assert callable(getattr(shell, '_make_follow_state'))

def test__make_arithmetic_state():
    """Test de la fonction _make_arithmetic_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_arithmetic_state')
    assert callable(getattr(shell, '_make_arithmetic_state'))

def test__make_call_state():
    """Test de la fonction _make_call_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_call_state')
    assert callable(getattr(shell, '_make_call_state'))

def test__make_label_state():
    """Test de la fonction _make_label_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_label_state')
    assert callable(getattr(shell, '_make_label_state'))

def test__make_redirect_state():
    """Test de la fonction _make_redirect_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, '_make_redirect_state')
    assert callable(getattr(shell, '_make_redirect_state'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shell, 'analyse_text')
    assert callable(getattr(shell, 'analyse_text'))

class TestBashLexer:
    """Tests pour la classe BashLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'BashLexer')
        assert isinstance(getattr(shell, 'BashLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'BashLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSlurmBashLexer:
    """Tests pour la classe SlurmBashLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'SlurmBashLexer')
        assert isinstance(getattr(shell, 'SlurmBashLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'SlurmBashLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestShellSessionBaseLexer:
    """Tests pour la classe ShellSessionBaseLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'ShellSessionBaseLexer')
        assert isinstance(getattr(shell, 'ShellSessionBaseLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'ShellSessionBaseLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBashSessionLexer:
    """Tests pour la classe BashSessionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'BashSessionLexer')
        assert isinstance(getattr(shell, 'BashSessionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'BashSessionLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBatchLexer:
    """Tests pour la classe BatchLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'BatchLexer')
        assert isinstance(getattr(shell, 'BatchLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'BatchLexer')
        for method_name in ['_make_begin_state', '_make_follow_state', '_make_arithmetic_state', '_make_call_state', '_make_label_state', '_make_redirect_state']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMSDOSSessionLexer:
    """Tests pour la classe MSDOSSessionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'MSDOSSessionLexer')
        assert isinstance(getattr(shell, 'MSDOSSessionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'MSDOSSessionLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTcshLexer:
    """Tests pour la classe TcshLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'TcshLexer')
        assert isinstance(getattr(shell, 'TcshLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'TcshLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTcshSessionLexer:
    """Tests pour la classe TcshSessionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'TcshSessionLexer')
        assert isinstance(getattr(shell, 'TcshSessionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'TcshSessionLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPowerShellLexer:
    """Tests pour la classe PowerShellLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'PowerShellLexer')
        assert isinstance(getattr(shell, 'PowerShellLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'PowerShellLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPowerShellSessionLexer:
    """Tests pour la classe PowerShellSessionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'PowerShellSessionLexer')
        assert isinstance(getattr(shell, 'PowerShellSessionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'PowerShellSessionLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFishShellLexer:
    """Tests pour la classe FishShellLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'FishShellLexer')
        assert isinstance(getattr(shell, 'FishShellLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'FishShellLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExeclineLexer:
    """Tests pour la classe ExeclineLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shell, 'ExeclineLexer')
        assert isinstance(getattr(shell, 'ExeclineLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shell, 'ExeclineLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

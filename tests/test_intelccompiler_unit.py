"""
Tests unitaires générés pour intelccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import intelccompiler
except ImportError:
    pytest.skip(f"Module intelccompiler non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intelccompiler, '__init__')
    assert callable(getattr(intelccompiler, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intelccompiler, '__init__')
    assert callable(getattr(intelccompiler, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intelccompiler, '__init__')
    assert callable(getattr(intelccompiler, '__init__'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intelccompiler, 'initialize')
    assert callable(getattr(intelccompiler, 'initialize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intelccompiler, '__init__')
    assert callable(getattr(intelccompiler, '__init__'))

class TestIntelCCompiler:
    """Tests pour la classe IntelCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intelccompiler, 'IntelCCompiler')
        assert isinstance(getattr(intelccompiler, 'IntelCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intelccompiler, 'IntelCCompiler')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelItaniumCCompiler:
    """Tests pour la classe IntelItaniumCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intelccompiler, 'IntelItaniumCCompiler')
        assert isinstance(getattr(intelccompiler, 'IntelItaniumCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intelccompiler, 'IntelItaniumCCompiler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelEM64TCCompiler:
    """Tests pour la classe IntelEM64TCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intelccompiler, 'IntelEM64TCCompiler')
        assert isinstance(getattr(intelccompiler, 'IntelEM64TCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intelccompiler, 'IntelEM64TCCompiler')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelCCompilerW:
    """Tests pour la classe IntelCCompilerW"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intelccompiler, 'IntelCCompilerW')
        assert isinstance(getattr(intelccompiler, 'IntelCCompilerW'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intelccompiler, 'IntelCCompilerW')
        for method_name in ['__init__', 'initialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelEM64TCCompilerW:
    """Tests pour la classe IntelEM64TCCompilerW"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intelccompiler, 'IntelEM64TCCompilerW')
        assert isinstance(getattr(intelccompiler, 'IntelEM64TCCompilerW'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intelccompiler, 'IntelEM64TCCompilerW')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

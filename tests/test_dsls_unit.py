"""
Tests unitaires générés pour dsls
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dsls
except ImportError:
    pytest.skip(f"Module dsls non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, 'analyse_text')
    assert callable(getattr(dsls, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, '__init__')
    assert callable(getattr(dsls, '__init__'))

def test__reset_stringescapes():
    """Test de la fonction _reset_stringescapes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, '_reset_stringescapes')
    assert callable(getattr(dsls, '_reset_stringescapes'))

def test__string():
    """Test de la fonction _string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, '_string')
    assert callable(getattr(dsls, '_string'))

def test__stringescapes():
    """Test de la fonction _stringescapes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, '_stringescapes')
    assert callable(getattr(dsls, '_stringescapes'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, 'get_tokens_unprocessed')
    assert callable(getattr(dsls, 'get_tokens_unprocessed'))

def test_callback():
    """Test de la fonction callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dsls, 'callback')
    assert callable(getattr(dsls, 'callback'))

class TestProtoBufLexer:
    """Tests pour la classe ProtoBufLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'ProtoBufLexer')
        assert isinstance(getattr(dsls, 'ProtoBufLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'ProtoBufLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestThriftLexer:
    """Tests pour la classe ThriftLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'ThriftLexer')
        assert isinstance(getattr(dsls, 'ThriftLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'ThriftLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestZeekLexer:
    """Tests pour la classe ZeekLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'ZeekLexer')
        assert isinstance(getattr(dsls, 'ZeekLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'ZeekLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPuppetLexer:
    """Tests pour la classe PuppetLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'PuppetLexer')
        assert isinstance(getattr(dsls, 'PuppetLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'PuppetLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRslLexer:
    """Tests pour la classe RslLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'RslLexer')
        assert isinstance(getattr(dsls, 'RslLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'RslLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMscgenLexer:
    """Tests pour la classe MscgenLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'MscgenLexer')
        assert isinstance(getattr(dsls, 'MscgenLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'MscgenLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVGLLexer:
    """Tests pour la classe VGLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'VGLLexer')
        assert isinstance(getattr(dsls, 'VGLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'VGLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAlloyLexer:
    """Tests pour la classe AlloyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'AlloyLexer')
        assert isinstance(getattr(dsls, 'AlloyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'AlloyLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPanLexer:
    """Tests pour la classe PanLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'PanLexer')
        assert isinstance(getattr(dsls, 'PanLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'PanLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCrmshLexer:
    """Tests pour la classe CrmshLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'CrmshLexer')
        assert isinstance(getattr(dsls, 'CrmshLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'CrmshLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFlatlineLexer:
    """Tests pour la classe FlatlineLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'FlatlineLexer')
        assert isinstance(getattr(dsls, 'FlatlineLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'FlatlineLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSnowballLexer:
    """Tests pour la classe SnowballLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dsls, 'SnowballLexer')
        assert isinstance(getattr(dsls, 'SnowballLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dsls, 'SnowballLexer')
        for method_name in ['__init__', '_reset_stringescapes', '_string', '_stringescapes', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

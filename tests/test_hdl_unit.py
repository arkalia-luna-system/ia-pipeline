"""
Tests unitaires générés pour hdl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hdl
except ImportError:
    pytest.skip(f"Module hdl non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hdl, 'analyse_text')
    assert callable(getattr(hdl, 'analyse_text'))

class TestVerilogLexer:
    """Tests pour la classe VerilogLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hdl, 'VerilogLexer')
        assert isinstance(getattr(hdl, 'VerilogLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hdl, 'VerilogLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSystemVerilogLexer:
    """Tests pour la classe SystemVerilogLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hdl, 'SystemVerilogLexer')
        assert isinstance(getattr(hdl, 'SystemVerilogLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hdl, 'SystemVerilogLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVhdlLexer:
    """Tests pour la classe VhdlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hdl, 'VhdlLexer')
        assert isinstance(getattr(hdl, 'VhdlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hdl, 'VhdlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

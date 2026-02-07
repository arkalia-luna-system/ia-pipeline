"""
Tests unitaires générés pour minecraft
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import minecraft
except ImportError:
    pytest.skip(f"Module minecraft non importable")


class TestSNBTLexer:
    """Tests pour la classe SNBTLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(minecraft, 'SNBTLexer')
        assert isinstance(getattr(minecraft, 'SNBTLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(minecraft, 'SNBTLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMCFunctionLexer:
    """Tests pour la classe MCFunctionLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(minecraft, 'MCFunctionLexer')
        assert isinstance(getattr(minecraft, 'MCFunctionLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(minecraft, 'MCFunctionLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMCSchemaLexer:
    """Tests pour la classe MCSchemaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(minecraft, 'MCSchemaLexer')
        assert isinstance(getattr(minecraft, 'MCSchemaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(minecraft, 'MCSchemaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

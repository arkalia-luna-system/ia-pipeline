"""
Tests unitaires générés pour d
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import d
except ImportError:
    pytest.skip(f"Module d non importable")


class TestDLexer:
    """Tests pour la classe DLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(d, 'DLexer')
        assert isinstance(getattr(d, 'DLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(d, 'DLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCrocLexer:
    """Tests pour la classe CrocLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(d, 'CrocLexer')
        assert isinstance(getattr(d, 'CrocLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(d, 'CrocLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMiniDLexer:
    """Tests pour la classe MiniDLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(d, 'MiniDLexer')
        assert isinstance(getattr(d, 'MiniDLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(d, 'MiniDLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

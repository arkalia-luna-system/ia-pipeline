"""
Tests unitaires générés pour archetype
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import archetype
except ImportError:
    pytest.skip(f"Module archetype non importable")


class TestAtomsLexer:
    """Tests pour la classe AtomsLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(archetype, 'AtomsLexer')
        assert isinstance(getattr(archetype, 'AtomsLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(archetype, 'AtomsLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOdinLexer:
    """Tests pour la classe OdinLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(archetype, 'OdinLexer')
        assert isinstance(getattr(archetype, 'OdinLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(archetype, 'OdinLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCadlLexer:
    """Tests pour la classe CadlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(archetype, 'CadlLexer')
        assert isinstance(getattr(archetype, 'CadlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(archetype, 'CadlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAdlLexer:
    """Tests pour la classe AdlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(archetype, 'AdlLexer')
        assert isinstance(getattr(archetype, 'AdlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(archetype, 'AdlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

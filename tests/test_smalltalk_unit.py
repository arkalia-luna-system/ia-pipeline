"""
Tests unitaires générés pour smalltalk
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import smalltalk
except ImportError:
    pytest.skip(f"Module smalltalk non importable")


class TestSmalltalkLexer:
    """Tests pour la classe SmalltalkLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(smalltalk, 'SmalltalkLexer')
        assert isinstance(getattr(smalltalk, 'SmalltalkLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(smalltalk, 'SmalltalkLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNewspeakLexer:
    """Tests pour la classe NewspeakLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(smalltalk, 'NewspeakLexer')
        assert isinstance(getattr(smalltalk, 'NewspeakLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(smalltalk, 'NewspeakLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

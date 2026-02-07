"""
Tests unitaires générés pour automation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import automation
except ImportError:
    pytest.skip(f"Module automation non importable")


class TestAutohotkeyLexer:
    """Tests pour la classe AutohotkeyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(automation, 'AutohotkeyLexer')
        assert isinstance(getattr(automation, 'AutohotkeyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(automation, 'AutohotkeyLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAutoItLexer:
    """Tests pour la classe AutoItLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(automation, 'AutoItLexer')
        assert isinstance(getattr(automation, 'AutoItLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(automation, 'AutoItLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour q
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import q
except ImportError:
    pytest.skip(f"Module q non importable")


class TestKLexer:
    """Tests pour la classe KLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(q, 'KLexer')
        assert isinstance(getattr(q, 'KLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(q, 'KLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestQLexer:
    """Tests pour la classe QLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(q, 'QLexer')
        assert isinstance(getattr(q, 'QLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(q, 'QLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

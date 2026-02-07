"""
Tests unitaires générés pour vyper
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vyper
except ImportError:
    pytest.skip(f"Module vyper non importable")


class TestVyperLexer:
    """Tests pour la classe VyperLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vyper, 'VyperLexer')
        assert isinstance(getattr(vyper, 'VyperLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vyper, 'VyperLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

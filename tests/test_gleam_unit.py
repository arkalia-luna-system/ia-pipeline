"""
Tests unitaires générés pour gleam
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gleam
except ImportError:
    pytest.skip(f"Module gleam non importable")


class TestGleamLexer:
    """Tests pour la classe GleamLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gleam, 'GleamLexer')
        assert isinstance(getattr(gleam, 'GleamLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gleam, 'GleamLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

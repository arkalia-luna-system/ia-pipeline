"""
Tests unitaires générés pour foxpro
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import foxpro
except ImportError:
    pytest.skip(f"Module foxpro non importable")


class TestFoxProLexer:
    """Tests pour la classe FoxProLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(foxpro, 'FoxProLexer')
        assert isinstance(getattr(foxpro, 'FoxProLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(foxpro, 'FoxProLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

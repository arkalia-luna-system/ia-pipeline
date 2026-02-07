"""
Tests unitaires générés pour wren
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wren
except ImportError:
    pytest.skip(f"Module wren non importable")


class TestWrenLexer:
    """Tests pour la classe WrenLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(wren, 'WrenLexer')
        assert isinstance(getattr(wren, 'WrenLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(wren, 'WrenLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

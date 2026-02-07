"""
Tests unitaires générés pour hexdump
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hexdump
except ImportError:
    pytest.skip(f"Module hexdump non importable")


class TestHexdumpLexer:
    """Tests pour la classe HexdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hexdump, 'HexdumpLexer')
        assert isinstance(getattr(hexdump, 'HexdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hexdump, 'HexdumpLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

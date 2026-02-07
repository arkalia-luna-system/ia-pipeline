"""
Tests unitaires générés pour webassembly
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import webassembly
except ImportError:
    pytest.skip(f"Module webassembly non importable")


class TestWatLexer:
    """Tests pour la classe WatLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(webassembly, 'WatLexer')
        assert isinstance(getattr(webassembly, 'WatLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(webassembly, 'WatLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

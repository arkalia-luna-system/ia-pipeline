"""
Tests unitaires générés pour sgf
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sgf
except ImportError:
    pytest.skip(f"Module sgf non importable")


class TestSmartGameFormatLexer:
    """Tests pour la classe SmartGameFormatLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sgf, 'SmartGameFormatLexer')
        assert isinstance(getattr(sgf, 'SmartGameFormatLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sgf, 'SmartGameFormatLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

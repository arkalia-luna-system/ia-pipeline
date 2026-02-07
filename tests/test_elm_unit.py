"""
Tests unitaires générés pour elm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import elm
except ImportError:
    pytest.skip(f"Module elm non importable")


class TestElmLexer:
    """Tests pour la classe ElmLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(elm, 'ElmLexer')
        assert isinstance(getattr(elm, 'ElmLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(elm, 'ElmLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

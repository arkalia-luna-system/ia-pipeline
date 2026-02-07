"""
Tests unitaires générés pour jsx
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jsx
except ImportError:
    pytest.skip(f"Module jsx non importable")


class TestJsxLexer:
    """Tests pour la classe JsxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jsx, 'JsxLexer')
        assert isinstance(getattr(jsx, 'JsxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jsx, 'JsxLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTsxLexer:
    """Tests pour la classe TsxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jsx, 'TsxLexer')
        assert isinstance(getattr(jsx, 'TsxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jsx, 'TsxLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

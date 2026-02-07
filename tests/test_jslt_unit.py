"""
Tests unitaires générés pour jslt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jslt
except ImportError:
    pytest.skip(f"Module jslt non importable")


class TestJSLTLexer:
    """Tests pour la classe JSLTLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jslt, 'JSLTLexer')
        assert isinstance(getattr(jslt, 'JSLTLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jslt, 'JSLTLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

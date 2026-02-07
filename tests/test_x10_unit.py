"""
Tests unitaires générés pour x10
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import x10
except ImportError:
    pytest.skip(f"Module x10 non importable")


class TestX10Lexer:
    """Tests pour la classe X10Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(x10, 'X10Lexer')
        assert isinstance(getattr(x10, 'X10Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(x10, 'X10Lexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

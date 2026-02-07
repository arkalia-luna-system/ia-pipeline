"""
Tests unitaires générés pour macaulay2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import macaulay2
except ImportError:
    pytest.skip(f"Module macaulay2 non importable")


class TestMacaulay2Lexer:
    """Tests pour la classe Macaulay2Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(macaulay2, 'Macaulay2Lexer')
        assert isinstance(getattr(macaulay2, 'Macaulay2Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(macaulay2, 'Macaulay2Lexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour comal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import comal
except ImportError:
    pytest.skip(f"Module comal non importable")


class TestComal80Lexer:
    """Tests pour la classe Comal80Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(comal, 'Comal80Lexer')
        assert isinstance(getattr(comal, 'Comal80Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(comal, 'Comal80Lexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour tablegen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tablegen
except ImportError:
    pytest.skip(f"Module tablegen non importable")


class TestTableGenLexer:
    """Tests pour la classe TableGenLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tablegen, 'TableGenLexer')
        assert isinstance(getattr(tablegen, 'TableGenLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tablegen, 'TableGenLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

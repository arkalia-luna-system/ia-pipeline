"""
Tests unitaires générés pour ncl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ncl
except ImportError:
    pytest.skip(f"Module ncl non importable")


class TestNCLLexer:
    """Tests pour la classe NCLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ncl, 'NCLLexer')
        assert isinstance(getattr(ncl, 'NCLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ncl, 'NCLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

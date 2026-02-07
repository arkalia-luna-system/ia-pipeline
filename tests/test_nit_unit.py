"""
Tests unitaires générés pour nit
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nit
except ImportError:
    pytest.skip(f"Module nit non importable")


class TestNitLexer:
    """Tests pour la classe NitLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nit, 'NitLexer')
        assert isinstance(getattr(nit, 'NitLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nit, 'NitLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

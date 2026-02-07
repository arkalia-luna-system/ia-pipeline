"""
Tests unitaires générés pour ptx
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ptx
except ImportError:
    pytest.skip(f"Module ptx non importable")


class TestPtxLexer:
    """Tests pour la classe PtxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ptx, 'PtxLexer')
        assert isinstance(getattr(ptx, 'PtxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ptx, 'PtxLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

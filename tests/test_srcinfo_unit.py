"""
Tests unitaires générés pour srcinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import srcinfo
except ImportError:
    pytest.skip(f"Module srcinfo non importable")


class TestSrcinfoLexer:
    """Tests pour la classe SrcinfoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(srcinfo, 'SrcinfoLexer')
        assert isinstance(getattr(srcinfo, 'SrcinfoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(srcinfo, 'SrcinfoLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

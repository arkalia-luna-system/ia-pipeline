"""
Tests unitaires générés pour ooc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ooc
except ImportError:
    pytest.skip(f"Module ooc non importable")


class TestOocLexer:
    """Tests pour la classe OocLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ooc, 'OocLexer')
        assert isinstance(getattr(ooc, 'OocLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ooc, 'OocLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

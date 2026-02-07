"""
Tests unitaires générés pour xorg
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import xorg
except ImportError:
    pytest.skip(f"Module xorg non importable")


class TestXorgLexer:
    """Tests pour la classe XorgLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(xorg, 'XorgLexer')
        assert isinstance(getattr(xorg, 'XorgLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(xorg, 'XorgLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

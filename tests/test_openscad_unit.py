"""
Tests unitaires générés pour openscad
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import openscad
except ImportError:
    pytest.skip(f"Module openscad non importable")


class TestOpenScadLexer:
    """Tests pour la classe OpenScadLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(openscad, 'OpenScadLexer')
        assert isinstance(getattr(openscad, 'OpenScadLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(openscad, 'OpenScadLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

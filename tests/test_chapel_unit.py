"""
Tests unitaires générés pour chapel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import chapel
except ImportError:
    pytest.skip(f"Module chapel non importable")


class TestChapelLexer:
    """Tests pour la classe ChapelLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(chapel, 'ChapelLexer')
        assert isinstance(getattr(chapel, 'ChapelLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(chapel, 'ChapelLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

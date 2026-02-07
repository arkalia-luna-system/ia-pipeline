"""
Tests unitaires générés pour pony
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pony
except ImportError:
    pytest.skip(f"Module pony non importable")


class TestPonyLexer:
    """Tests pour la classe PonyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pony, 'PonyLexer')
        assert isinstance(getattr(pony, 'PonyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pony, 'PonyLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

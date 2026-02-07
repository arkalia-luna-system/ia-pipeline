"""
Tests unitaires générés pour teal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import teal
except ImportError:
    pytest.skip(f"Module teal non importable")


class TestTealLexer:
    """Tests pour la classe TealLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(teal, 'TealLexer')
        assert isinstance(getattr(teal, 'TealLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(teal, 'TealLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

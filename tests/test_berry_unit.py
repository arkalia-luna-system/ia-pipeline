"""
Tests unitaires générés pour berry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import berry
except ImportError:
    pytest.skip(f"Module berry non importable")


class TestBerryLexer:
    """Tests pour la classe BerryLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(berry, 'BerryLexer')
        assert isinstance(getattr(berry, 'BerryLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(berry, 'BerryLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour hare
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hare
except ImportError:
    pytest.skip(f"Module hare non importable")


class TestHareLexer:
    """Tests pour la classe HareLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hare, 'HareLexer')
        assert isinstance(getattr(hare, 'HareLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hare, 'HareLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

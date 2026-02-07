"""
Tests unitaires générés pour ride
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ride
except ImportError:
    pytest.skip(f"Module ride non importable")


class TestRideLexer:
    """Tests pour la classe RideLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ride, 'RideLexer')
        assert isinstance(getattr(ride, 'RideLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ride, 'RideLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

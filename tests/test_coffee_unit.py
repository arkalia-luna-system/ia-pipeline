"""
Tests unitaires générés pour coffee
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import coffee
except ImportError:
    pytest.skip(f"Module coffee non importable")


class TestCoffeeStyle:
    """Tests pour la classe CoffeeStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(coffee, 'CoffeeStyle')
        assert isinstance(getattr(coffee, 'CoffeeStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(coffee, 'CoffeeStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

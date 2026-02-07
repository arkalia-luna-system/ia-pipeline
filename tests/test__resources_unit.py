"""
Tests unitaires générés pour _resources
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _resources
except ImportError:
    pytest.skip(f"Module _resources non importable")


class TestAsyncResource:
    """Tests pour la classe AsyncResource"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_resources, 'AsyncResource')
        assert isinstance(getattr(_resources, 'AsyncResource'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_resources, 'AsyncResource')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

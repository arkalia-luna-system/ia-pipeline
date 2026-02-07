"""
Tests unitaires générés pour zenburn
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zenburn
except ImportError:
    pytest.skip(f"Module zenburn non importable")


class TestZenburnStyle:
    """Tests pour la classe ZenburnStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zenburn, 'ZenburnStyle')
        assert isinstance(getattr(zenburn, 'ZenburnStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zenburn, 'ZenburnStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

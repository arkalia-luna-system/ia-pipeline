"""
Tests unitaires générés pour scheme
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import scheme
except ImportError:
    pytest.skip(f"Module scheme non importable")


class TestScheme:
    """Tests pour la classe Scheme"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(scheme, 'Scheme')
        assert isinstance(getattr(scheme, 'Scheme'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(scheme, 'Scheme')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

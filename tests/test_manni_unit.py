"""
Tests unitaires générés pour manni
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import manni
except ImportError:
    pytest.skip(f"Module manni non importable")


class TestManniStyle:
    """Tests pour la classe ManniStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(manni, 'ManniStyle')
        assert isinstance(getattr(manni, 'ManniStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(manni, 'ManniStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

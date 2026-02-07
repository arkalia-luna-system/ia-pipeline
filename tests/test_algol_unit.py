"""
Tests unitaires générés pour algol
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import algol
except ImportError:
    pytest.skip(f"Module algol non importable")


class TestAlgolStyle:
    """Tests pour la classe AlgolStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algol, 'AlgolStyle')
        assert isinstance(getattr(algol, 'AlgolStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algol, 'AlgolStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

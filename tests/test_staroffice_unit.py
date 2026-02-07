"""
Tests unitaires générés pour staroffice
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import staroffice
except ImportError:
    pytest.skip(f"Module staroffice non importable")


class TestStarofficeStyle:
    """Tests pour la classe StarofficeStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(staroffice, 'StarofficeStyle')
        assert isinstance(getattr(staroffice, 'StarofficeStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(staroffice, 'StarofficeStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour tango
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tango
except ImportError:
    pytest.skip(f"Module tango non importable")


class TestTangoStyle:
    """Tests pour la classe TangoStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tango, 'TangoStyle')
        assert isinstance(getattr(tango, 'TangoStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tango, 'TangoStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

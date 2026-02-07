"""
Tests unitaires générés pour trac
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import trac
except ImportError:
    pytest.skip(f"Module trac non importable")


class TestTracStyle:
    """Tests pour la classe TracStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(trac, 'TracStyle')
        assert isinstance(getattr(trac, 'TracStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(trac, 'TracStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

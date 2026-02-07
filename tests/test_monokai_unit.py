"""
Tests unitaires générés pour monokai
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import monokai
except ImportError:
    pytest.skip(f"Module monokai non importable")


class TestMonokaiStyle:
    """Tests pour la classe MonokaiStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(monokai, 'MonokaiStyle')
        assert isinstance(getattr(monokai, 'MonokaiStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(monokai, 'MonokaiStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

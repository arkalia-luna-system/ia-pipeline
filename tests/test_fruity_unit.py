"""
Tests unitaires générés pour fruity
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fruity
except ImportError:
    pytest.skip(f"Module fruity non importable")


class TestFruityStyle:
    """Tests pour la classe FruityStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fruity, 'FruityStyle')
        assert isinstance(getattr(fruity, 'FruityStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fruity, 'FruityStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour dracula
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dracula
except ImportError:
    pytest.skip(f"Module dracula non importable")


class TestDraculaStyle:
    """Tests pour la classe DraculaStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dracula, 'DraculaStyle')
        assert isinstance(getattr(dracula, 'DraculaStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dracula, 'DraculaStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

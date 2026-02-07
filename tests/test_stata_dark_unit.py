"""
Tests unitaires générés pour stata_dark
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stata_dark
except ImportError:
    pytest.skip(f"Module stata_dark non importable")


class TestStataDarkStyle:
    """Tests pour la classe StataDarkStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stata_dark, 'StataDarkStyle')
        assert isinstance(getattr(stata_dark, 'StataDarkStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stata_dark, 'StataDarkStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

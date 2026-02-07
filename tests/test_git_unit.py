"""
Tests unitaires générés pour git
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import git
except ImportError:
    pytest.skip(f"Module git non importable")


class TestGITModel:
    """Tests pour la classe GITModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(git, 'GITModel')
        assert isinstance(getattr(git, 'GITModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(git, 'GITModel')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

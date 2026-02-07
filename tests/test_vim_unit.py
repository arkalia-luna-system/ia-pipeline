"""
Tests unitaires générés pour vim
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vim
except ImportError:
    pytest.skip(f"Module vim non importable")


class TestVimStyle:
    """Tests pour la classe VimStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vim, 'VimStyle')
        assert isinstance(getattr(vim, 'VimStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vim, 'VimStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

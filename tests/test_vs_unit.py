"""
Tests unitaires générés pour vs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vs
except ImportError:
    pytest.skip(f"Module vs non importable")


class TestVisualStudioStyle:
    """Tests pour la classe VisualStudioStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vs, 'VisualStudioStyle')
        assert isinstance(getattr(vs, 'VisualStudioStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vs, 'VisualStudioStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

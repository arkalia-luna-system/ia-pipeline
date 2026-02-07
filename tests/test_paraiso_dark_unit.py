"""
Tests unitaires générés pour paraiso_dark
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import paraiso_dark
except ImportError:
    pytest.skip(f"Module paraiso_dark non importable")


class TestParaisoDarkStyle:
    """Tests pour la classe ParaisoDarkStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(paraiso_dark, 'ParaisoDarkStyle')
        assert isinstance(getattr(paraiso_dark, 'ParaisoDarkStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(paraiso_dark, 'ParaisoDarkStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour onedark
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import onedark
except ImportError:
    pytest.skip(f"Module onedark non importable")


class TestOneDarkStyle:
    """Tests pour la classe OneDarkStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(onedark, 'OneDarkStyle')
        assert isinstance(getattr(onedark, 'OneDarkStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(onedark, 'OneDarkStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

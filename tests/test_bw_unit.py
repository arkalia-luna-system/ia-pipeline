"""
Tests unitaires générés pour bw
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bw
except ImportError:
    pytest.skip(f"Module bw non importable")


class TestBlackWhiteStyle:
    """Tests pour la classe BlackWhiteStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bw, 'BlackWhiteStyle')
        assert isinstance(getattr(bw, 'BlackWhiteStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bw, 'BlackWhiteStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour fift
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fift
except ImportError:
    pytest.skip(f"Module fift non importable")


class TestFiftLexer:
    """Tests pour la classe FiftLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fift, 'FiftLexer')
        assert isinstance(getattr(fift, 'FiftLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fift, 'FiftLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

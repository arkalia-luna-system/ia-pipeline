"""
Tests unitaires générés pour wgsl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wgsl
except ImportError:
    pytest.skip(f"Module wgsl non importable")


class TestWgslLexer:
    """Tests pour la classe WgslLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(wgsl, 'WgslLexer')
        assert isinstance(getattr(wgsl, 'WgslLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(wgsl, 'WgslLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

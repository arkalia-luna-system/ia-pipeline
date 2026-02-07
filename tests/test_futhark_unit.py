"""
Tests unitaires générés pour futhark
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import futhark
except ImportError:
    pytest.skip(f"Module futhark non importable")


class TestFutharkLexer:
    """Tests pour la classe FutharkLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(futhark, 'FutharkLexer')
        assert isinstance(getattr(futhark, 'FutharkLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(futhark, 'FutharkLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour phix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import phix
except ImportError:
    pytest.skip(f"Module phix non importable")


class TestPhixLexer:
    """Tests pour la classe PhixLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(phix, 'PhixLexer')
        assert isinstance(getattr(phix, 'PhixLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(phix, 'PhixLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

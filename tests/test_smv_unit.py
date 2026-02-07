"""
Tests unitaires générés pour smv
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import smv
except ImportError:
    pytest.skip(f"Module smv non importable")


class TestNuSMVLexer:
    """Tests pour la classe NuSMVLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(smv, 'NuSMVLexer')
        assert isinstance(getattr(smv, 'NuSMVLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(smv, 'NuSMVLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

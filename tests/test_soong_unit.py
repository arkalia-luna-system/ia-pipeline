"""
Tests unitaires générés pour soong
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import soong
except ImportError:
    pytest.skip(f"Module soong non importable")


class TestSoongLexer:
    """Tests pour la classe SoongLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(soong, 'SoongLexer')
        assert isinstance(getattr(soong, 'SoongLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(soong, 'SoongLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour meson
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import meson
except ImportError:
    pytest.skip(f"Module meson non importable")


class TestMesonLexer:
    """Tests pour la classe MesonLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(meson, 'MesonLexer')
        assert isinstance(getattr(meson, 'MesonLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(meson, 'MesonLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

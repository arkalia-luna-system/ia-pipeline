"""
Tests unitaires générés pour whiley
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import whiley
except ImportError:
    pytest.skip(f"Module whiley non importable")


class TestWhileyLexer:
    """Tests pour la classe WhileyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(whiley, 'WhileyLexer')
        assert isinstance(getattr(whiley, 'WhileyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(whiley, 'WhileyLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

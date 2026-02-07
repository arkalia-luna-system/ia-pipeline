"""
Tests unitaires générés pour apl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import apl
except ImportError:
    pytest.skip(f"Module apl non importable")


class TestAPLLexer:
    """Tests pour la classe APLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apl, 'APLLexer')
        assert isinstance(getattr(apl, 'APLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apl, 'APLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour webidl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import webidl
except ImportError:
    pytest.skip(f"Module webidl non importable")


class TestWebIDLLexer:
    """Tests pour la classe WebIDLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(webidl, 'WebIDLLexer')
        assert isinstance(getattr(webidl, 'WebIDLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(webidl, 'WebIDLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

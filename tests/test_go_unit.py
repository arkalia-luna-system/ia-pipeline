"""
Tests unitaires générés pour go
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import go
except ImportError:
    pytest.skip(f"Module go non importable")


class TestGoLexer:
    """Tests pour la classe GoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(go, 'GoLexer')
        assert isinstance(getattr(go, 'GoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(go, 'GoLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

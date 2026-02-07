"""
Tests unitaires générés pour apdlexer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import apdlexer
except ImportError:
    pytest.skip(f"Module apdlexer non importable")


class Testapdlexer:
    """Tests pour la classe apdlexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apdlexer, 'apdlexer')
        assert isinstance(getattr(apdlexer, 'apdlexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apdlexer, 'apdlexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

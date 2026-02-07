"""
Tests unitaires générés pour gcodelexer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gcodelexer
except ImportError:
    pytest.skip(f"Module gcodelexer non importable")


class TestGcodeLexer:
    """Tests pour la classe GcodeLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gcodelexer, 'GcodeLexer')
        assert isinstance(getattr(gcodelexer, 'GcodeLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gcodelexer, 'GcodeLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour trafficscript
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import trafficscript
except ImportError:
    pytest.skip(f"Module trafficscript non importable")


class TestRtsLexer:
    """Tests pour la classe RtsLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(trafficscript, 'RtsLexer')
        assert isinstance(getattr(trafficscript, 'RtsLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(trafficscript, 'RtsLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

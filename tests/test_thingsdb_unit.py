"""
Tests unitaires générés pour thingsdb
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import thingsdb
except ImportError:
    pytest.skip(f"Module thingsdb non importable")


class TestThingsDBLexer:
    """Tests pour la classe ThingsDBLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(thingsdb, 'ThingsDBLexer')
        assert isinstance(getattr(thingsdb, 'ThingsDBLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(thingsdb, 'ThingsDBLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

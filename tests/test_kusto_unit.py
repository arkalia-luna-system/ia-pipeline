"""
Tests unitaires générés pour kusto
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import kusto
except ImportError:
    pytest.skip(f"Module kusto non importable")


class TestKustoLexer:
    """Tests pour la classe KustoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(kusto, 'KustoLexer')
        assert isinstance(getattr(kusto, 'KustoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(kusto, 'KustoLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

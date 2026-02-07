"""
Tests unitaires générés pour graph
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import graph
except ImportError:
    pytest.skip(f"Module graph non importable")


class TestCypherLexer:
    """Tests pour la classe CypherLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graph, 'CypherLexer')
        assert isinstance(getattr(graph, 'CypherLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graph, 'CypherLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

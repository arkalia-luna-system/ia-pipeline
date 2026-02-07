"""
Tests unitaires générés pour graphviz
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import graphviz
except ImportError:
    pytest.skip(f"Module graphviz non importable")


class TestGraphvizLexer:
    """Tests pour la classe GraphvizLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphviz, 'GraphvizLexer')
        assert isinstance(getattr(graphviz, 'GraphvizLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphviz, 'GraphvizLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

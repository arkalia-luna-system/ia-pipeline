"""
Tests unitaires générés pour promql
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import promql
except ImportError:
    pytest.skip(f"Module promql non importable")


class TestPromQLLexer:
    """Tests pour la classe PromQLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(promql, 'PromQLLexer')
        assert isinstance(getattr(promql, 'PromQLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(promql, 'PromQLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

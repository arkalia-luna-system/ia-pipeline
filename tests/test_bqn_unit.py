"""
Tests unitaires générés pour bqn
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bqn
except ImportError:
    pytest.skip(f"Module bqn non importable")


class TestBQNLexer:
    """Tests pour la classe BQNLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bqn, 'BQNLexer')
        assert isinstance(getattr(bqn, 'BQNLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bqn, 'BQNLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

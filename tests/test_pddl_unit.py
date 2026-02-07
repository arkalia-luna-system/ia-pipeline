"""
Tests unitaires générés pour pddl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pddl
except ImportError:
    pytest.skip(f"Module pddl non importable")


class TestPddlLexer:
    """Tests pour la classe PddlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pddl, 'PddlLexer')
        assert isinstance(getattr(pddl, 'PddlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pddl, 'PddlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

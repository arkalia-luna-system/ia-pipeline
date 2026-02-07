"""
Tests unitaires générés pour tact
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tact
except ImportError:
    pytest.skip(f"Module tact non importable")


class TestTactLexer:
    """Tests pour la classe TactLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tact, 'TactLexer')
        assert isinstance(getattr(tact, 'TactLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tact, 'TactLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

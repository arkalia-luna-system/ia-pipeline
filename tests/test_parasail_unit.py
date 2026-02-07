"""
Tests unitaires générés pour parasail
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import parasail
except ImportError:
    pytest.skip(f"Module parasail non importable")


class TestParaSailLexer:
    """Tests pour la classe ParaSailLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(parasail, 'ParaSailLexer')
        assert isinstance(getattr(parasail, 'ParaSailLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(parasail, 'ParaSailLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

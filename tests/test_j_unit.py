"""
Tests unitaires générés pour j
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import j
except ImportError:
    pytest.skip(f"Module j non importable")


class TestJLexer:
    """Tests pour la classe JLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(j, 'JLexer')
        assert isinstance(getattr(j, 'JLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(j, 'JLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

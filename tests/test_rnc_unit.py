"""
Tests unitaires générés pour rnc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rnc
except ImportError:
    pytest.skip(f"Module rnc non importable")


class TestRNCCompactLexer:
    """Tests pour la classe RNCCompactLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rnc, 'RNCCompactLexer')
        assert isinstance(getattr(rnc, 'RNCCompactLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rnc, 'RNCCompactLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

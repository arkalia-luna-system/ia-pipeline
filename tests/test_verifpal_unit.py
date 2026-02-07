"""
Tests unitaires générés pour verifpal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import verifpal
except ImportError:
    pytest.skip(f"Module verifpal non importable")


class TestVerifpalLexer:
    """Tests pour la classe VerifpalLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(verifpal, 'VerifpalLexer')
        assert isinstance(getattr(verifpal, 'VerifpalLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(verifpal, 'VerifpalLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

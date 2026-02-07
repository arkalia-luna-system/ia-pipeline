"""
Tests unitaires générés pour freefem
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import freefem
except ImportError:
    pytest.skip(f"Module freefem non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(freefem, 'get_tokens_unprocessed')
    assert callable(getattr(freefem, 'get_tokens_unprocessed'))

class TestFreeFemLexer:
    """Tests pour la classe FreeFemLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(freefem, 'FreeFemLexer')
        assert isinstance(getattr(freefem, 'FreeFemLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(freefem, 'FreeFemLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

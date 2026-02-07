"""
Tests unitaires générés pour fantom
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fantom
except ImportError:
    pytest.skip(f"Module fantom non importable")


def test_s():
    """Test de la fonction s"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fantom, 's')
    assert callable(getattr(fantom, 's'))

class TestFantomLexer:
    """Tests pour la classe FantomLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fantom, 'FantomLexer')
        assert isinstance(getattr(fantom, 'FantomLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fantom, 'FantomLexer')
        for method_name in ['s']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

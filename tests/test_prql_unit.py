"""
Tests unitaires générés pour prql
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import prql
except ImportError:
    pytest.skip(f"Module prql non importable")


def test_innerstring_rules():
    """Test de la fonction innerstring_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prql, 'innerstring_rules')
    assert callable(getattr(prql, 'innerstring_rules'))

def test_fstring_rules():
    """Test de la fonction fstring_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(prql, 'fstring_rules')
    assert callable(getattr(prql, 'fstring_rules'))

class TestPrqlLexer:
    """Tests pour la classe PrqlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(prql, 'PrqlLexer')
        assert isinstance(getattr(prql, 'PrqlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(prql, 'PrqlLexer')
        for method_name in ['innerstring_rules', 'fstring_rules']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

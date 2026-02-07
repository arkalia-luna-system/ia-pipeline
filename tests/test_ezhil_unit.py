"""
Tests unitaires générés pour ezhil
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ezhil
except ImportError:
    pytest.skip(f"Module ezhil non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ezhil, 'analyse_text')
    assert callable(getattr(ezhil, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ezhil, '__init__')
    assert callable(getattr(ezhil, '__init__'))

class TestEzhilLexer:
    """Tests pour la classe EzhilLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ezhil, 'EzhilLexer')
        assert isinstance(getattr(ezhil, 'EzhilLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ezhil, 'EzhilLexer')
        for method_name in ['analyse_text', '__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

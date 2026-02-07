"""
Tests unitaires générés pour asn1
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asn1
except ImportError:
    pytest.skip(f"Module asn1 non importable")


def test_word_sequences():
    """Test de la fonction word_sequences"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asn1, 'word_sequences')
    assert callable(getattr(asn1, 'word_sequences'))

class TestAsn1Lexer:
    """Tests pour la classe Asn1Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asn1, 'Asn1Lexer')
        assert isinstance(getattr(asn1, 'Asn1Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asn1, 'Asn1Lexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

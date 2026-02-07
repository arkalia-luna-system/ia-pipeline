"""
Tests unitaires générés pour maxima
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import maxima
except ImportError:
    pytest.skip(f"Module maxima non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(maxima, 'analyse_text')
    assert callable(getattr(maxima, 'analyse_text'))

class TestMaximaLexer:
    """Tests pour la classe MaximaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(maxima, 'MaximaLexer')
        assert isinstance(getattr(maxima, 'MaximaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(maxima, 'MaximaLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

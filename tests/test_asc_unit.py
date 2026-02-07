"""
Tests unitaires générés pour asc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asc
except ImportError:
    pytest.skip(f"Module asc non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asc, 'analyse_text')
    assert callable(getattr(asc, 'analyse_text'))

class TestAscLexer:
    """Tests pour la classe AscLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asc, 'AscLexer')
        assert isinstance(getattr(asc, 'AscLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asc, 'AscLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

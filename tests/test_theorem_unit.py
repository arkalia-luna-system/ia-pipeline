"""
Tests unitaires générés pour theorem
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import theorem
except ImportError:
    pytest.skip(f"Module theorem non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(theorem, 'analyse_text')
    assert callable(getattr(theorem, 'analyse_text'))

class TestCoqLexer:
    """Tests pour la classe CoqLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(theorem, 'CoqLexer')
        assert isinstance(getattr(theorem, 'CoqLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(theorem, 'CoqLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIsabelleLexer:
    """Tests pour la classe IsabelleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(theorem, 'IsabelleLexer')
        assert isinstance(getattr(theorem, 'IsabelleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(theorem, 'IsabelleLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

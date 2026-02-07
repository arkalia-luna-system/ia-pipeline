"""
Tests unitaires générés pour forth
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import forth
except ImportError:
    pytest.skip(f"Module forth non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forth, 'analyse_text')
    assert callable(getattr(forth, 'analyse_text'))

class TestForthLexer:
    """Tests pour la classe ForthLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(forth, 'ForthLexer')
        assert isinstance(getattr(forth, 'ForthLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(forth, 'ForthLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

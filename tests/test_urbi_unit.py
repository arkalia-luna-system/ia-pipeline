"""
Tests unitaires générés pour urbi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import urbi
except ImportError:
    pytest.skip(f"Module urbi non importable")


def test_blob_callback():
    """Test de la fonction blob_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(urbi, 'blob_callback')
    assert callable(getattr(urbi, 'blob_callback'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(urbi, 'analyse_text')
    assert callable(getattr(urbi, 'analyse_text'))

class TestUrbiscriptLexer:
    """Tests pour la classe UrbiscriptLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(urbi, 'UrbiscriptLexer')
        assert isinstance(getattr(urbi, 'UrbiscriptLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(urbi, 'UrbiscriptLexer')
        for method_name in ['blob_callback', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

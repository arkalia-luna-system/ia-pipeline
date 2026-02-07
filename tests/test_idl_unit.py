"""
Tests unitaires générés pour idl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import idl
except ImportError:
    pytest.skip(f"Module idl non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(idl, 'analyse_text')
    assert callable(getattr(idl, 'analyse_text'))

class TestIDLLexer:
    """Tests pour la classe IDLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(idl, 'IDLLexer')
        assert isinstance(getattr(idl, 'IDLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(idl, 'IDLLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

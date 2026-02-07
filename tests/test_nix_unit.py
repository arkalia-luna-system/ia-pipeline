"""
Tests unitaires générés pour nix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nix
except ImportError:
    pytest.skip(f"Module nix non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nix, 'analyse_text')
    assert callable(getattr(nix, 'analyse_text'))

class TestNixLexer:
    """Tests pour la classe NixLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nix, 'NixLexer')
        assert isinstance(getattr(nix, 'NixLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nix, 'NixLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour floscript
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import floscript
except ImportError:
    pytest.skip(f"Module floscript non importable")


def test_innerstring_rules():
    """Test de la fonction innerstring_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(floscript, 'innerstring_rules')
    assert callable(getattr(floscript, 'innerstring_rules'))

class TestFloScriptLexer:
    """Tests pour la classe FloScriptLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(floscript, 'FloScriptLexer')
        assert isinstance(getattr(floscript, 'FloScriptLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(floscript, 'FloScriptLexer')
        for method_name in ['innerstring_rules']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour jsonnet
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jsonnet
except ImportError:
    pytest.skip(f"Module jsonnet non importable")


def test_string_rules():
    """Test de la fonction string_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jsonnet, 'string_rules')
    assert callable(getattr(jsonnet, 'string_rules'))

def test_quoted_field_name():
    """Test de la fonction quoted_field_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jsonnet, 'quoted_field_name')
    assert callable(getattr(jsonnet, 'quoted_field_name'))

class TestJsonnetLexer:
    """Tests pour la classe JsonnetLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jsonnet, 'JsonnetLexer')
        assert isinstance(getattr(jsonnet, 'JsonnetLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jsonnet, 'JsonnetLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

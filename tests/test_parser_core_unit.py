"""
Tests unitaires générés pour parser_core
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import parser_core
except ImportError:
    pytest.skip(f"Module parser_core non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(parser_core, '__init__')
    assert callable(getattr(parser_core, '__init__'))

def test_process():
    """Test de la fonction process"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(parser_core, 'process')
    assert callable(getattr(parser_core, 'process'))

class TestParserCore:
    """Tests pour la classe ParserCore"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(parser_core, 'ParserCore')
        assert isinstance(getattr(parser_core, 'ParserCore'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(parser_core, 'ParserCore')
        for method_name in ['__init__', 'process']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

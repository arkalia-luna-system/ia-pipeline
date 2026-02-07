"""
Tests unitaires générés pour maple
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import maple
except ImportError:
    pytest.skip(f"Module maple non importable")


def test_delayed_callback():
    """Test de la fonction delayed_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(maple, 'delayed_callback')
    assert callable(getattr(maple, 'delayed_callback'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(maple, 'analyse_text')
    assert callable(getattr(maple, 'analyse_text'))

class TestMapleLexer:
    """Tests pour la classe MapleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(maple, 'MapleLexer')
        assert isinstance(getattr(maple, 'MapleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(maple, 'MapleLexer')
        for method_name in ['delayed_callback', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

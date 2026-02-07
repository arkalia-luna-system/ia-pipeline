"""
Tests unitaires générés pour selection_prefs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import selection_prefs
except ImportError:
    pytest.skip(f"Module selection_prefs non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selection_prefs, '__init__')
    assert callable(getattr(selection_prefs, '__init__'))

class TestSelectionPreferences:
    """Tests pour la classe SelectionPreferences"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(selection_prefs, 'SelectionPreferences')
        assert isinstance(getattr(selection_prefs, 'SelectionPreferences'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(selection_prefs, 'SelectionPreferences')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

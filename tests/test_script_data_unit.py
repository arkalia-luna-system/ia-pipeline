"""
Tests unitaires générés pour script_data
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import script_data
except ImportError:
    pytest.skip(f"Module script_data non importable")


def test___post_init__():
    """Test de la fonction __post_init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(script_data, '__post_init__')
    assert callable(getattr(script_data, '__post_init__'))

class TestScriptData:
    """Tests pour la classe ScriptData"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(script_data, 'ScriptData')
        assert isinstance(getattr(script_data, 'ScriptData'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(script_data, 'ScriptData')
        for method_name in ['__post_init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

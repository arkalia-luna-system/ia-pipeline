"""
Tests unitaires générés pour resource
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import resource
except ImportError:
    pytest.skip(f"Module resource non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(resource, 'analyse_text')
    assert callable(getattr(resource, 'analyse_text'))

class TestResourceLexer:
    """Tests pour la classe ResourceLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(resource, 'ResourceLexer')
        assert isinstance(getattr(resource, 'ResourceLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(resource, 'ResourceLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

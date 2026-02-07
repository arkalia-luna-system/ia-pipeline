"""
Tests unitaires générés pour supercollider
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import supercollider
except ImportError:
    pytest.skip(f"Module supercollider non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(supercollider, 'analyse_text')
    assert callable(getattr(supercollider, 'analyse_text'))

class TestSuperColliderLexer:
    """Tests pour la classe SuperColliderLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(supercollider, 'SuperColliderLexer')
        assert isinstance(getattr(supercollider, 'SuperColliderLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(supercollider, 'SuperColliderLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

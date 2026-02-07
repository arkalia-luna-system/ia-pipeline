"""
Tests unitaires générés pour backwards
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import backwards
except ImportError:
    pytest.skip(f"Module backwards non importable")


def test_hook():
    """Test de la fonction hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backwards, 'hook')
    assert callable(getattr(backwards, 'hook'))

class TestBackwardsCompatConfig:
    """Tests pour la classe BackwardsCompatConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(backwards, 'BackwardsCompatConfig')
        assert isinstance(getattr(backwards, 'BackwardsCompatConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(backwards, 'BackwardsCompatConfig')
        for method_name in ['hook']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

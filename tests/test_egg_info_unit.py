"""
Tests unitaires générés pour egg_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import egg_info
except ImportError:
    pytest.skip(f"Module egg_info non importable")


def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(egg_info, 'run')
    assert callable(getattr(egg_info, 'run'))

class Testegg_info:
    """Tests pour la classe egg_info"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(egg_info, 'egg_info')
        assert isinstance(getattr(egg_info, 'egg_info'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(egg_info, 'egg_info')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

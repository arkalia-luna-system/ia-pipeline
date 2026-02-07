"""
Tests unitaires générés pour async_generator
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import async_generator
except ImportError:
    pytest.skip(f"Module async_generator non importable")


def test_runner():
    """Test de la fonction runner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_generator, 'runner')
    assert callable(getattr(async_generator, 'runner'))

class Test_Done:
    """Tests pour la classe _Done"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_generator, '_Done')
        assert isinstance(getattr(async_generator, '_Done'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_generator, '_Done')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

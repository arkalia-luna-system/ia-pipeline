"""
Tests unitaires générés pour background
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import background
except ImportError:
    pytest.skip(f"Module background non importable")


def test_add_task():
    """Test de la fonction add_task"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(background, 'add_task')
    assert callable(getattr(background, 'add_task'))

class TestBackgroundTasks:
    """Tests pour la classe BackgroundTasks"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(background, 'BackgroundTasks')
        assert isinstance(getattr(background, 'BackgroundTasks'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(background, 'BackgroundTasks')
        for method_name in ['add_task']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour horizontal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import horizontal
except ImportError:
    pytest.skip(f"Module horizontal non importable")


def test_arrange():
    """Test de la fonction arrange"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(horizontal, 'arrange')
    assert callable(getattr(horizontal, 'arrange'))

class TestHorizontalLayout:
    """Tests pour la classe HorizontalLayout"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(horizontal, 'HorizontalLayout')
        assert isinstance(getattr(horizontal, 'HorizontalLayout'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(horizontal, 'HorizontalLayout')
        for method_name in ['arrange']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

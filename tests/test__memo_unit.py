"""
Tests unitaires générés pour _memo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _memo
except ImportError:
    pytest.skip(f"Module _memo non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_memo, '__init__')
    assert callable(getattr(_memo, '__init__'))

class TestTypeCheckMemo:
    """Tests pour la classe TypeCheckMemo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_memo, 'TypeCheckMemo')
        assert isinstance(getattr(_memo, 'TypeCheckMemo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_memo, 'TypeCheckMemo')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

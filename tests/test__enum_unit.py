"""
Tests unitaires générés pour _enum
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _enum
except ImportError:
    pytest.skip(f"Module _enum non importable")


def test__generate_next_value_():
    """Test de la fonction _generate_next_value_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_enum, '_generate_next_value_')
    assert callable(getattr(_enum, '_generate_next_value_'))

class TestNoAutoEnum:
    """Tests pour la classe NoAutoEnum"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_enum, 'NoAutoEnum')
        assert isinstance(getattr(_enum, 'NoAutoEnum'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_enum, 'NoAutoEnum')
        for method_name in ['_generate_next_value_']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

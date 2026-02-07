"""
Tests unitaires générés pour convert_namedtuple_to_dataclass
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import convert_namedtuple_to_dataclass
except ImportError:
    pytest.skip(f"Module convert_namedtuple_to_dataclass non importable")


def test_leave_ClassDef():
    """Test de la fonction leave_ClassDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(convert_namedtuple_to_dataclass, 'leave_ClassDef')
    assert callable(getattr(convert_namedtuple_to_dataclass, 'leave_ClassDef'))

class TestConvertNamedTupleToDataclassCommand:
    """Tests pour la classe ConvertNamedTupleToDataclassCommand"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(convert_namedtuple_to_dataclass, 'ConvertNamedTupleToDataclassCommand')
        assert isinstance(getattr(convert_namedtuple_to_dataclass, 'ConvertNamedTupleToDataclassCommand'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(convert_namedtuple_to_dataclass, 'ConvertNamedTupleToDataclassCommand')
        for method_name in ['leave_ClassDef']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

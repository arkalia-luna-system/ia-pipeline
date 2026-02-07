"""
Tests unitaires générés pour _gather_global_names
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _gather_global_names
except ImportError:
    pytest.skip(f"Module _gather_global_names non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, '__init__')
    assert callable(getattr(_gather_global_names, '__init__'))

def test_visit_ClassDef():
    """Test de la fonction visit_ClassDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'visit_ClassDef')
    assert callable(getattr(_gather_global_names, 'visit_ClassDef'))

def test_leave_ClassDef():
    """Test de la fonction leave_ClassDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'leave_ClassDef')
    assert callable(getattr(_gather_global_names, 'leave_ClassDef'))

def test_visit_FunctionDef():
    """Test de la fonction visit_FunctionDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'visit_FunctionDef')
    assert callable(getattr(_gather_global_names, 'visit_FunctionDef'))

def test_leave_FunctionDef():
    """Test de la fonction leave_FunctionDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'leave_FunctionDef')
    assert callable(getattr(_gather_global_names, 'leave_FunctionDef'))

def test_visit_Assign():
    """Test de la fonction visit_Assign"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'visit_Assign')
    assert callable(getattr(_gather_global_names, 'visit_Assign'))

def test_visit_AnnAssign():
    """Test de la fonction visit_AnnAssign"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_global_names, 'visit_AnnAssign')
    assert callable(getattr(_gather_global_names, 'visit_AnnAssign'))

class TestGatherGlobalNamesVisitor:
    """Tests pour la classe GatherGlobalNamesVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_gather_global_names, 'GatherGlobalNamesVisitor')
        assert isinstance(getattr(_gather_global_names, 'GatherGlobalNamesVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_gather_global_names, 'GatherGlobalNamesVisitor')
        for method_name in ['__init__', 'visit_ClassDef', 'leave_ClassDef', 'visit_FunctionDef', 'leave_FunctionDef', 'visit_Assign', 'visit_AnnAssign']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

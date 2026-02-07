"""
Tests unitaires générés pour _gather_string_annotation_names
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _gather_string_annotation_names
except ImportError:
    pytest.skip(f"Module _gather_string_annotation_names non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, '__init__')
    assert callable(getattr(_gather_string_annotation_names, '__init__'))

def test_visit_Annotation():
    """Test de la fonction visit_Annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'visit_Annotation')
    assert callable(getattr(_gather_string_annotation_names, 'visit_Annotation'))

def test_leave_Annotation():
    """Test de la fonction leave_Annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'leave_Annotation')
    assert callable(getattr(_gather_string_annotation_names, 'leave_Annotation'))

def test_visit_Subscript():
    """Test de la fonction visit_Subscript"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'visit_Subscript')
    assert callable(getattr(_gather_string_annotation_names, 'visit_Subscript'))

def test_visit_Call():
    """Test de la fonction visit_Call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'visit_Call')
    assert callable(getattr(_gather_string_annotation_names, 'visit_Call'))

def test_leave_Call():
    """Test de la fonction leave_Call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'leave_Call')
    assert callable(getattr(_gather_string_annotation_names, 'leave_Call'))

def test_visit_ConcatenatedString():
    """Test de la fonction visit_ConcatenatedString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'visit_ConcatenatedString')
    assert callable(getattr(_gather_string_annotation_names, 'visit_ConcatenatedString'))

def test_visit_SimpleString():
    """Test de la fonction visit_SimpleString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'visit_SimpleString')
    assert callable(getattr(_gather_string_annotation_names, 'visit_SimpleString'))

def test_handle_any_string():
    """Test de la fonction handle_any_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_gather_string_annotation_names, 'handle_any_string')
    assert callable(getattr(_gather_string_annotation_names, 'handle_any_string'))

class TestGatherNamesFromStringAnnotationsVisitor:
    """Tests pour la classe GatherNamesFromStringAnnotationsVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_gather_string_annotation_names, 'GatherNamesFromStringAnnotationsVisitor')
        assert isinstance(getattr(_gather_string_annotation_names, 'GatherNamesFromStringAnnotationsVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_gather_string_annotation_names, 'GatherNamesFromStringAnnotationsVisitor')
        for method_name in ['__init__', 'visit_Annotation', 'leave_Annotation', 'visit_Subscript', 'visit_Call', 'leave_Call', 'visit_ConcatenatedString', 'visit_SimpleString', 'handle_any_string']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

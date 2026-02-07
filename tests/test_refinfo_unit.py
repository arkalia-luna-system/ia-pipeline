"""
Tests unitaires générés pour refinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import refinfo
except ImportError:
    pytest.skip(f"Module refinfo non importable")


def test_type_fullname():
    """Test de la fonction type_fullname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'type_fullname')
    assert callable(getattr(refinfo, 'type_fullname'))

def test_get_undocumented_ref_info_json():
    """Test de la fonction get_undocumented_ref_info_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'get_undocumented_ref_info_json')
    assert callable(getattr(refinfo, 'get_undocumented_ref_info_json'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, '__init__')
    assert callable(getattr(refinfo, '__init__'))

def test_visit_name_expr():
    """Test de la fonction visit_name_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'visit_name_expr')
    assert callable(getattr(refinfo, 'visit_name_expr'))

def test_visit_member_expr():
    """Test de la fonction visit_member_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'visit_member_expr')
    assert callable(getattr(refinfo, 'visit_member_expr'))

def test_visit_func_def():
    """Test de la fonction visit_func_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'visit_func_def')
    assert callable(getattr(refinfo, 'visit_func_def'))

def test_record_ref_expr():
    """Test de la fonction record_ref_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(refinfo, 'record_ref_expr')
    assert callable(getattr(refinfo, 'record_ref_expr'))

class TestRefInfoVisitor:
    """Tests pour la classe RefInfoVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(refinfo, 'RefInfoVisitor')
        assert isinstance(getattr(refinfo, 'RefInfoVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(refinfo, 'RefInfoVisitor')
        for method_name in ['__init__', 'visit_name_expr', 'visit_member_expr', 'visit_func_def', 'record_ref_expr']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour columns
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import columns
except ImportError:
    pytest.skip(f"Module columns non importable")


def test_tabulate():
    """Test de la fonction tabulate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, 'tabulate')
    assert callable(getattr(columns, 'tabulate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, '__init__')
    assert callable(getattr(columns, '__init__'))

def test_is_manifest():
    """Test de la fonction is_manifest"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, 'is_manifest')
    assert callable(getattr(columns, 'is_manifest'))

def test_format():
    """Test de la fonction format"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, 'format')
    assert callable(getattr(columns, 'format'))

def test__format_vuln():
    """Test de la fonction _format_vuln"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, '_format_vuln')
    assert callable(getattr(columns, '_format_vuln'))

def test__format_fix_versions():
    """Test de la fonction _format_fix_versions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, '_format_fix_versions')
    assert callable(getattr(columns, '_format_fix_versions'))

def test__format_skipped_dep():
    """Test de la fonction _format_skipped_dep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, '_format_skipped_dep')
    assert callable(getattr(columns, '_format_skipped_dep'))

def test__format_applied_fix():
    """Test de la fonction _format_applied_fix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(columns, '_format_applied_fix')
    assert callable(getattr(columns, '_format_applied_fix'))

class TestColumnsFormat:
    """Tests pour la classe ColumnsFormat"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(columns, 'ColumnsFormat')
        assert isinstance(getattr(columns, 'ColumnsFormat'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(columns, 'ColumnsFormat')
        for method_name in ['__init__', 'is_manifest', 'format', '_format_vuln', '_format_fix_versions', '_format_skipped_dep', '_format_applied_fix']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

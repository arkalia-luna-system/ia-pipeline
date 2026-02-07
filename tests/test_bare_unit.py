"""
Tests unitaires générés pour bare
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bare
except ImportError:
    pytest.skip(f"Module bare non importable")


def test_render_vulnerabilities():
    """Test de la fonction render_vulnerabilities"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bare, 'render_vulnerabilities')
    assert callable(getattr(bare, 'render_vulnerabilities'))

def test_render_licenses():
    """Test de la fonction render_licenses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bare, 'render_licenses')
    assert callable(getattr(bare, 'render_licenses'))

def test_render_announcements():
    """Test de la fonction render_announcements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bare, 'render_announcements')
    assert callable(getattr(bare, 'render_announcements'))

class TestBareReport:
    """Tests pour la classe BareReport"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bare, 'BareReport')
        assert isinstance(getattr(bare, 'BareReport'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bare, 'BareReport')
        for method_name in ['render_vulnerabilities', 'render_licenses', 'render_announcements']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

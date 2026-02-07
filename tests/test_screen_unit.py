"""
Tests unitaires générés pour screen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import screen
except ImportError:
    pytest.skip(f"Module screen non importable")


def test___build_announcements_section():
    """Test de la fonction __build_announcements_section"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(screen, '__build_announcements_section')
    assert callable(getattr(screen, '__build_announcements_section'))

def test_render_vulnerabilities():
    """Test de la fonction render_vulnerabilities"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(screen, 'render_vulnerabilities')
    assert callable(getattr(screen, 'render_vulnerabilities'))

def test_render_licenses():
    """Test de la fonction render_licenses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(screen, 'render_licenses')
    assert callable(getattr(screen, 'render_licenses'))

def test_render_announcements():
    """Test de la fonction render_announcements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(screen, 'render_announcements')
    assert callable(getattr(screen, 'render_announcements'))

class TestScreenReport:
    """Tests pour la classe ScreenReport"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(screen, 'ScreenReport')
        assert isinstance(getattr(screen, 'ScreenReport'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(screen, 'ScreenReport')
        for method_name in ['__build_announcements_section', 'render_vulnerabilities', 'render_licenses', 'render_announcements']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour qt_screenshot
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import qt_screenshot
except ImportError:
    pytest.skip(f"Module qt_screenshot non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, '__init__')
    assert callable(getattr(qt_screenshot, '__init__'))

def test_capture():
    """Test de la fonction capture"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'capture')
    assert callable(getattr(qt_screenshot, 'capture'))

def test_on_loaded():
    """Test de la fonction on_loaded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'on_loaded')
    assert callable(getattr(qt_screenshot, 'on_loaded'))

def test_export_pdf():
    """Test de la fonction export_pdf"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'export_pdf')
    assert callable(getattr(qt_screenshot, 'export_pdf'))

def test_export_png():
    """Test de la fonction export_png"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'export_png')
    assert callable(getattr(qt_screenshot, 'export_png'))

def test_get_data():
    """Test de la fonction get_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'get_data')
    assert callable(getattr(qt_screenshot, 'get_data'))

def test_cleanup():
    """Test de la fonction cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_screenshot, 'cleanup')
    assert callable(getattr(qt_screenshot, 'cleanup'))

class TestQtScreenshot:
    """Tests pour la classe QtScreenshot"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(qt_screenshot, 'QtScreenshot')
        assert isinstance(getattr(qt_screenshot, 'QtScreenshot'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(qt_screenshot, 'QtScreenshot')
        for method_name in ['__init__', 'capture', 'on_loaded', 'export_pdf', 'export_png', 'get_data']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour qt_exporter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import qt_exporter
except ImportError:
    pytest.skip(f"Module qt_exporter non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_exporter, '_file_extension_default')
    assert callable(getattr(qt_exporter, '_file_extension_default'))

def test__check_launch_reqs():
    """Test de la fonction _check_launch_reqs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_exporter, '_check_launch_reqs')
    assert callable(getattr(qt_exporter, '_check_launch_reqs'))

def test__run_pyqtwebengine():
    """Test de la fonction _run_pyqtwebengine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_exporter, '_run_pyqtwebengine')
    assert callable(getattr(qt_exporter, '_run_pyqtwebengine'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_exporter, 'from_notebook_node')
    assert callable(getattr(qt_exporter, 'from_notebook_node'))

class TestQtExporter:
    """Tests pour la classe QtExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(qt_exporter, 'QtExporter')
        assert isinstance(getattr(qt_exporter, 'QtExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(qt_exporter, 'QtExporter')
        for method_name in ['_file_extension_default', '_check_launch_reqs', '_run_pyqtwebengine', 'from_notebook_node']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

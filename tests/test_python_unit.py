"""
Tests unitaires générés pour python
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import python
except ImportError:
    pytest.skip(f"Module python non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(python, '_file_extension_default')
    assert callable(getattr(python, '_file_extension_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(python, '_template_name_default')
    assert callable(getattr(python, '_template_name_default'))

class TestPythonExporter:
    """Tests pour la classe PythonExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(python, 'PythonExporter')
        assert isinstance(getattr(python, 'PythonExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(python, 'PythonExporter')
        for method_name in ['_file_extension_default', '_template_name_default']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour notebook
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import notebook
except ImportError:
    pytest.skip(f"Module notebook non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(notebook, '_file_extension_default')
    assert callable(getattr(notebook, '_file_extension_default'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(notebook, 'from_notebook_node')
    assert callable(getattr(notebook, 'from_notebook_node'))

class TestNotebookExporter:
    """Tests pour la classe NotebookExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(notebook, 'NotebookExporter')
        assert isinstance(getattr(notebook, 'NotebookExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(notebook, 'NotebookExporter')
        for method_name in ['_file_extension_default', 'from_notebook_node']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour script
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import script
except ImportError:
    pytest.skip(f"Module script non importable")


def test__template_file_default():
    """Test de la fonction _template_file_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(script, '_template_file_default')
    assert callable(getattr(script, '_template_file_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(script, '_template_name_default')
    assert callable(getattr(script, '_template_name_default'))

def test__get_language_exporter():
    """Test de la fonction _get_language_exporter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(script, '_get_language_exporter')
    assert callable(getattr(script, '_get_language_exporter'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(script, 'from_notebook_node')
    assert callable(getattr(script, 'from_notebook_node'))

class TestScriptExporter:
    """Tests pour la classe ScriptExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(script, 'ScriptExporter')
        assert isinstance(getattr(script, 'ScriptExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(script, 'ScriptExporter')
        for method_name in ['_template_file_default', '_template_name_default', '_get_language_exporter', 'from_notebook_node']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

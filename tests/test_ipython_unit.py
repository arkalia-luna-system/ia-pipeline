"""
Tests unitaires générés pour ipython
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ipython
except ImportError:
    pytest.skip(f"Module ipython non importable")


def test_load_ipython_extension():
    """Test de la fonction load_ipython_extension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipython, 'load_ipython_extension')
    assert callable(getattr(ipython, 'load_ipython_extension'))

def test_dotenv():
    """Test de la fonction dotenv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ipython, 'dotenv')
    assert callable(getattr(ipython, 'dotenv'))

class TestIPythonDotEnv:
    """Tests pour la classe IPythonDotEnv"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ipython, 'IPythonDotEnv')
        assert isinstance(getattr(ipython, 'IPythonDotEnv'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ipython, 'IPythonDotEnv')
        for method_name in ['dotenv']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

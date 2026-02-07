"""
Tests unitaires générés pour __pip-runner__
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import __pip-runner__
except ImportError:
    pytest.skip(f"Module __pip-runner__ non importable")


def test_version_str():
    """Test de la fonction version_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__pip-runner__, 'version_str')
    assert callable(getattr(__pip-runner__, 'version_str'))

def test_find_spec():
    """Test de la fonction find_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__pip-runner__, 'find_spec')
    assert callable(getattr(__pip-runner__, 'find_spec'))

class TestPipImportRedirectingFinder:
    """Tests pour la classe PipImportRedirectingFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(__pip-runner__, 'PipImportRedirectingFinder')
        assert isinstance(getattr(__pip-runner__, 'PipImportRedirectingFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(__pip-runner__, 'PipImportRedirectingFinder')
        for method_name in ['find_spec']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

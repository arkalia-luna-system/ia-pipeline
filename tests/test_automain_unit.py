"""
Tests unitaires générés pour automain
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import automain
except ImportError:
    pytest.skip(f"Module automain non importable")


def test_automain():
    """Test de la fonction automain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(automain, 'automain')
    assert callable(getattr(automain, 'automain'))

def test_automain_decorator():
    """Test de la fonction automain_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(automain, 'automain_decorator')
    assert callable(getattr(automain, 'automain_decorator'))

class TestAutomainRequiresModuleError:
    """Tests pour la classe AutomainRequiresModuleError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(automain, 'AutomainRequiresModuleError')
        assert isinstance(getattr(automain, 'AutomainRequiresModuleError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(automain, 'AutomainRequiresModuleError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

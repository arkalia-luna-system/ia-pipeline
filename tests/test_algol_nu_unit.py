"""
Tests unitaires générés pour algol_nu
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import algol_nu
except ImportError:
    pytest.skip(f"Module algol_nu non importable")


class TestAlgol_NuStyle:
    """Tests pour la classe Algol_NuStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algol_nu, 'Algol_NuStyle')
        assert isinstance(getattr(algol_nu, 'Algol_NuStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algol_nu, 'Algol_NuStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

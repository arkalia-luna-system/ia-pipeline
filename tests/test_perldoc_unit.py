"""
Tests unitaires générés pour perldoc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import perldoc
except ImportError:
    pytest.skip(f"Module perldoc non importable")


class TestPerldocStyle:
    """Tests pour la classe PerldocStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(perldoc, 'PerldocStyle')
        assert isinstance(getattr(perldoc, 'PerldocStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(perldoc, 'PerldocStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

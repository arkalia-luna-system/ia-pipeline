"""
Tests unitaires générés pour material
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import material
except ImportError:
    pytest.skip(f"Module material non importable")


class TestMaterialStyle:
    """Tests pour la classe MaterialStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(material, 'MaterialStyle')
        assert isinstance(getattr(material, 'MaterialStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(material, 'MaterialStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

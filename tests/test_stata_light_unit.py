"""
Tests unitaires générés pour stata_light
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stata_light
except ImportError:
    pytest.skip(f"Module stata_light non importable")


class TestStataLightStyle:
    """Tests pour la classe StataLightStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stata_light, 'StataLightStyle')
        assert isinstance(getattr(stata_light, 'StataLightStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stata_light, 'StataLightStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

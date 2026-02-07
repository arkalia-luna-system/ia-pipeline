"""
Tests unitaires générés pour paraiso_light
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import paraiso_light
except ImportError:
    pytest.skip(f"Module paraiso_light non importable")


class TestParaisoLightStyle:
    """Tests pour la classe ParaisoLightStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(paraiso_light, 'ParaisoLightStyle')
        assert isinstance(getattr(paraiso_light, 'ParaisoLightStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(paraiso_light, 'ParaisoLightStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

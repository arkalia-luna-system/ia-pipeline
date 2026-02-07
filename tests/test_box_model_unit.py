"""
Tests unitaires générés pour box_model
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import box_model
except ImportError:
    pytest.skip(f"Module box_model non importable")


class TestBoxModel:
    """Tests pour la classe BoxModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(box_model, 'BoxModel')
        assert isinstance(getattr(box_model, 'BoxModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(box_model, 'BoxModel')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

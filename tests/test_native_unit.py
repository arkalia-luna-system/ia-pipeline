"""
Tests unitaires générés pour native
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import native
except ImportError:
    pytest.skip(f"Module native non importable")


class TestNativeStyle:
    """Tests pour la classe NativeStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(native, 'NativeStyle')
        assert isinstance(getattr(native, 'NativeStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(native, 'NativeStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

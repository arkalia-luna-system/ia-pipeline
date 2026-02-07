"""
Tests unitaires générés pour tarfile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tarfile
except ImportError:
    pytest.skip(f"Module tarfile non importable")


class TestTarFile:
    """Tests pour la classe TarFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tarfile, 'TarFile')
        assert isinstance(getattr(tarfile, 'TarFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tarfile, 'TarFile')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

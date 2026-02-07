"""
Tests unitaires générés pour bdist_rpm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bdist_rpm
except ImportError:
    pytest.skip(f"Module bdist_rpm non importable")


def test__make_spec_file():
    """Test de la fonction _make_spec_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bdist_rpm, '_make_spec_file')
    assert callable(getattr(bdist_rpm, '_make_spec_file'))

class Testbdist_rpm:
    """Tests pour la classe bdist_rpm"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bdist_rpm, 'bdist_rpm')
        assert isinstance(getattr(bdist_rpm, 'bdist_rpm'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bdist_rpm, 'bdist_rpm')
        for method_name in ['_make_spec_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

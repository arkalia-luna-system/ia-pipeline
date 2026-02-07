"""
Tests unitaires générés pour dist_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dist_info
except ImportError:
    pytest.skip(f"Module dist_info non importable")


def test_initialize_options():
    """Test de la fonction initialize_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dist_info, 'initialize_options')
    assert callable(getattr(dist_info, 'initialize_options'))

def test_finalize_options():
    """Test de la fonction finalize_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dist_info, 'finalize_options')
    assert callable(getattr(dist_info, 'finalize_options'))

def test__maybe_bkp_dir():
    """Test de la fonction _maybe_bkp_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dist_info, '_maybe_bkp_dir')
    assert callable(getattr(dist_info, '_maybe_bkp_dir'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dist_info, 'run')
    assert callable(getattr(dist_info, 'run'))

class Testdist_info:
    """Tests pour la classe dist_info"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dist_info, 'dist_info')
        assert isinstance(getattr(dist_info, 'dist_info'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dist_info, 'dist_info')
        for method_name in ['initialize_options', 'finalize_options', '_maybe_bkp_dir', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

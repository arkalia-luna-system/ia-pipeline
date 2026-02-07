"""
Tests unitaires générés pour stubinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stubinfo
except ImportError:
    pytest.skip(f"Module stubinfo non importable")


def test_is_legacy_bundled_package():
    """Test de la fonction is_legacy_bundled_package"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubinfo, 'is_legacy_bundled_package')
    assert callable(getattr(stubinfo, 'is_legacy_bundled_package'))

def test_approved_stub_package_exists():
    """Test de la fonction approved_stub_package_exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubinfo, 'approved_stub_package_exists')
    assert callable(getattr(stubinfo, 'approved_stub_package_exists'))

def test_stub_distribution_name():
    """Test de la fonction stub_distribution_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubinfo, 'stub_distribution_name')
    assert callable(getattr(stubinfo, 'stub_distribution_name'))

if __name__ == "__main__":
    pytest.main([__file__])

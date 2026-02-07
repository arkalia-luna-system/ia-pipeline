"""
Tests unitaires générés pour cleanup
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cleanup
except ImportError:
    pytest.skip(f"Module cleanup non importable")


def test_clean_old_tests_and_caches():
    """Test de la fonction clean_old_tests_and_caches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup, 'clean_old_tests_and_caches')
    assert callable(getattr(cleanup, 'clean_old_tests_and_caches'))

def test_clean_macos_files():
    """Test de la fonction clean_macos_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup, 'clean_macos_files')
    assert callable(getattr(cleanup, 'clean_macos_files'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour ci
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ci
except ImportError:
    pytest.skip(f"Module ci non importable")


def test_generate_github_ci_yaml():
    """Test de la fonction generate_github_ci_yaml"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ci, 'generate_github_ci_yaml')
    assert callable(getattr(ci, 'generate_github_ci_yaml'))

def test_add_coverage_badge():
    """Test de la fonction add_coverage_badge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ci, 'add_coverage_badge')
    assert callable(getattr(ci, 'add_coverage_badge'))

if __name__ == "__main__":
    pytest.main([__file__])

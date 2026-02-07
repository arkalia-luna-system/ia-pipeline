"""
Tests unitaires générés pour _error_tools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _error_tools
except ImportError:
    pytest.skip(f"Module _error_tools non importable")


def test_friendly_list():
    """Test de la fonction friendly_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_error_tools, 'friendly_list')
    assert callable(getattr(_error_tools, 'friendly_list'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour version
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import version
except ImportError:
    pytest.skip(f"Module version non importable")


def test_check_version():
    """Test de la fonction check_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(version, 'check_version')
    assert callable(getattr(version, 'check_version'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour wheel_editable
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wheel_editable
except ImportError:
    pytest.skip(f"Module wheel_editable non importable")


def test_build_wheel_editable():
    """Test de la fonction build_wheel_editable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wheel_editable, 'build_wheel_editable')
    assert callable(getattr(wheel_editable, 'build_wheel_editable'))

if __name__ == "__main__":
    pytest.main([__file__])

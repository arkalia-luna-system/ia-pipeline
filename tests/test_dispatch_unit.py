"""
Tests unitaires générés pour dispatch
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dispatch
except ImportError:
    pytest.skip(f"Module dispatch non importable")


def test_should_extension_dispatch():
    """Test de la fonction should_extension_dispatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dispatch, 'should_extension_dispatch')
    assert callable(getattr(dispatch, 'should_extension_dispatch'))

if __name__ == "__main__":
    pytest.main([__file__])

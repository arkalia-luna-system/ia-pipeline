"""
Tests unitaires générés pour strip-prefix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import strip-prefix
except ImportError:
    pytest.skip(f"Module strip-prefix non importable")


def test_strip_prefix():
    """Test de la fonction strip_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strip-prefix, 'strip_prefix')
    assert callable(getattr(strip-prefix, 'strip_prefix'))

if __name__ == "__main__":
    pytest.main([__file__])

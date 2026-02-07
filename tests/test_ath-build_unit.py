"""
Tests unitaires générés pour ath-build
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ath-build
except ImportError:
    pytest.skip(f"Module ath-build non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-build, 'main')
    assert callable(getattr(ath-build, 'main'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour athalia_unified
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import athalia_unified
except ImportError:
    pytest.skip(f"Module athalia_unified non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(athalia_unified, 'main')
    assert callable(getattr(athalia_unified, 'main'))

if __name__ == "__main__":
    pytest.main([__file__])

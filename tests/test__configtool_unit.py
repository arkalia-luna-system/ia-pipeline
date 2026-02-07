"""
Tests unitaires générés pour _configtool
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _configtool
except ImportError:
    pytest.skip(f"Module _configtool non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_configtool, 'main')
    assert callable(getattr(_configtool, 'main'))

if __name__ == "__main__":
    pytest.main([__file__])

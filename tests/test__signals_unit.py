"""
Tests unitaires générés pour _signals
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _signals
except ImportError:
    pytest.skip(f"Module _signals non importable")


def test_open_signal_receiver():
    """Test de la fonction open_signal_receiver"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_signals, 'open_signal_receiver')
    assert callable(getattr(_signals, 'open_signal_receiver'))

if __name__ == "__main__":
    pytest.main([__file__])

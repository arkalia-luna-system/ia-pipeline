"""
Tests unitaires générés pour easter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import easter
except ImportError:
    pytest.skip(f"Module easter non importable")


def test_easter():
    """Test de la fonction easter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(easter, 'easter')
    assert callable(getattr(easter, 'easter'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour autolink
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import autolink
except ImportError:
    pytest.skip(f"Module autolink non importable")


def test_autolink():
    """Test de la fonction autolink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autolink, 'autolink')
    assert callable(getattr(autolink, 'autolink'))

if __name__ == "__main__":
    pytest.main([__file__])

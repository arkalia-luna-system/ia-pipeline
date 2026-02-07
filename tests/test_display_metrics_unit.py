"""
Tests unitaires générés pour display_metrics
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import display_metrics
except ImportError:
    pytest.skip(f"Module display_metrics non importable")


def test_display_metrics():
    """Test de la fonction display_metrics"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(display_metrics, 'display_metrics')
    assert callable(getattr(display_metrics, 'display_metrics'))

if __name__ == "__main__":
    pytest.main([__file__])

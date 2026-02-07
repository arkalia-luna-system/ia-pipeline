"""
Tests unitaires générés pour create_badge
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import create_badge
except ImportError:
    pytest.skip(f"Module create_badge non importable")


def test_create_metrics_badge():
    """Test de la fonction create_metrics_badge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(create_badge, 'create_metrics_badge')
    assert callable(getattr(create_badge, 'create_metrics_badge'))

if __name__ == "__main__":
    pytest.main([__file__])

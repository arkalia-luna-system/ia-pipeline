"""
Tests unitaires générés pour app_debug
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import app_debug
except ImportError:
    pytest.skip(f"Module app_debug non importable")


def test_flask_debug_true():
    """Test de la fonction flask_debug_true"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(app_debug, 'flask_debug_true')
    assert callable(getattr(app_debug, 'flask_debug_true'))

if __name__ == "__main__":
    pytest.main([__file__])

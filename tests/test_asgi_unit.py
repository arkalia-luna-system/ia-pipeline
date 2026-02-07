"""
Tests unitaires générés pour asgi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asgi
except ImportError:
    pytest.skip(f"Module asgi non importable")


def test_make_asgi_app():
    """Test de la fonction make_asgi_app"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asgi, 'make_asgi_app')
    assert callable(getattr(asgi, 'make_asgi_app'))

if __name__ == "__main__":
    pytest.main([__file__])

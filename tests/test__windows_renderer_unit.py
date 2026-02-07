"""
Tests unitaires générés pour _windows_renderer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _windows_renderer
except ImportError:
    pytest.skip(f"Module _windows_renderer non importable")


def test_legacy_windows_render():
    """Test de la fonction legacy_windows_render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_windows_renderer, 'legacy_windows_render')
    assert callable(getattr(_windows_renderer, 'legacy_windows_render'))

if __name__ == "__main__":
    pytest.main([__file__])

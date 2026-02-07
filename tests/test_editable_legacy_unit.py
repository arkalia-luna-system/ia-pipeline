"""
Tests unitaires générés pour editable_legacy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import editable_legacy
except ImportError:
    pytest.skip(f"Module editable_legacy non importable")


def test_install_editable():
    """Test de la fonction install_editable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(editable_legacy, 'install_editable')
    assert callable(getattr(editable_legacy, 'install_editable'))

if __name__ == "__main__":
    pytest.main([__file__])

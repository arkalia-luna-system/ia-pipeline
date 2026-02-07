"""
Tests unitaires générés pour widgets
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import widgets
except ImportError:
    pytest.skip(f"Module widgets non importable")


def test_register_widget():
    """Test de la fonction register_widget"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(widgets, 'register_widget')
    assert callable(getattr(widgets, 'register_widget'))

def test_register_widget_from_metadata():
    """Test de la fonction register_widget_from_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(widgets, 'register_widget_from_metadata')
    assert callable(getattr(widgets, 'register_widget_from_metadata'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour dataframe_demo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dataframe_demo
except ImportError:
    pytest.skip(f"Module dataframe_demo non importable")


def test_data_frame_demo():
    """Test de la fonction data_frame_demo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe_demo, 'data_frame_demo')
    assert callable(getattr(dataframe_demo, 'data_frame_demo'))

def test_get_un_data():
    """Test de la fonction get_un_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe_demo, 'get_un_data')
    assert callable(getattr(dataframe_demo, 'get_un_data'))

if __name__ == "__main__":
    pytest.main([__file__])

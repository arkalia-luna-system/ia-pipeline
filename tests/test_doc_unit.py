"""
Tests unitaires générés pour doc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import doc
except ImportError:
    pytest.skip(f"Module doc non importable")


def test_create_section_header():
    """Test de la fonction create_section_header"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc, 'create_section_header')
    assert callable(getattr(doc, 'create_section_header'))

def test_window_agg_numba_parameters():
    """Test de la fonction window_agg_numba_parameters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc, 'window_agg_numba_parameters')
    assert callable(getattr(doc, 'window_agg_numba_parameters'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour direct_url_helpers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import direct_url_helpers
except ImportError:
    pytest.skip(f"Module direct_url_helpers non importable")


def test_direct_url_as_pep440_direct_reference():
    """Test de la fonction direct_url_as_pep440_direct_reference"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url_helpers, 'direct_url_as_pep440_direct_reference')
    assert callable(getattr(direct_url_helpers, 'direct_url_as_pep440_direct_reference'))

def test_direct_url_for_editable():
    """Test de la fonction direct_url_for_editable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url_helpers, 'direct_url_for_editable')
    assert callable(getattr(direct_url_helpers, 'direct_url_for_editable'))

def test_direct_url_from_link():
    """Test de la fonction direct_url_from_link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url_helpers, 'direct_url_from_link')
    assert callable(getattr(direct_url_helpers, 'direct_url_from_link'))

if __name__ == "__main__":
    pytest.main([__file__])

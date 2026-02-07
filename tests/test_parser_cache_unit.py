"""
Tests unitaires générés pour parser_cache
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import parser_cache
except ImportError:
    pytest.skip(f"Module parser_cache non importable")


def test_get_yield_exprs():
    """Test de la fonction get_yield_exprs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(parser_cache, 'get_yield_exprs')
    assert callable(getattr(parser_cache, 'get_yield_exprs'))

if __name__ == "__main__":
    pytest.main([__file__])

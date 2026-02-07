"""
Tests unitaires générés pour introspect
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import introspect
except ImportError:
    pytest.skip(f"Module introspect non importable")


def test_opt_func_info():
    """Test de la fonction opt_func_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(introspect, 'opt_func_info')
    assert callable(getattr(introspect, 'opt_func_info'))

if __name__ == "__main__":
    pytest.main([__file__])

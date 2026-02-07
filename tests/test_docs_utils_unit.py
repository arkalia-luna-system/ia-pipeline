"""
Tests unitaires générés pour docs_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import docs_utils
except ImportError:
    pytest.skip(f"Module docs_utils non importable")


def test_get_url():
    """Test de la fonction get_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(docs_utils, 'get_url')
    assert callable(getattr(docs_utils, 'get_url'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour calls
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import calls
except ImportError:
    pytest.skip(f"Module calls non importable")


def test_gen_blacklist():
    """Test de la fonction gen_blacklist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(calls, 'gen_blacklist')
    assert callable(getattr(calls, 'gen_blacklist'))

if __name__ == "__main__":
    pytest.main([__file__])

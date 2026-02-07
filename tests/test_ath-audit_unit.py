"""
Tests unitaires générés pour ath-audit
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ath-audit
except ImportError:
    pytest.skip(f"Module ath-audit non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-audit, 'main')
    assert callable(getattr(ath-audit, 'main'))

if __name__ == "__main__":
    pytest.main([__file__])

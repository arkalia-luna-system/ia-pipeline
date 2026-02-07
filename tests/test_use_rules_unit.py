"""
Tests unitaires générés pour use_rules
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import use_rules
except ImportError:
    pytest.skip(f"Module use_rules non importable")


def test_buildusevars():
    """Test de la fonction buildusevars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(use_rules, 'buildusevars')
    assert callable(getattr(use_rules, 'buildusevars'))

def test_buildusevar():
    """Test de la fonction buildusevar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(use_rules, 'buildusevar')
    assert callable(getattr(use_rules, 'buildusevar'))

if __name__ == "__main__":
    pytest.main([__file__])

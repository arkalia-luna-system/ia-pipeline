"""
Tests unitaires générés pour rules
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rules
except ImportError:
    pytest.skip(f"Module rules non importable")


def test_buildmodule():
    """Test de la fonction buildmodule"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rules, 'buildmodule')
    assert callable(getattr(rules, 'buildmodule'))

def test_buildapi():
    """Test de la fonction buildapi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rules, 'buildapi')
    assert callable(getattr(rules, 'buildapi'))

if __name__ == "__main__":
    pytest.main([__file__])

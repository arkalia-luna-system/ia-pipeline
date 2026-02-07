"""
Tests d'intégration générés automatiquement pour _once
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _once
except ImportError:
    pytest.skip(f"Module _once non importable")

def test__once_integration():
    """Test d'intégration pour _once"""
    # TODO: Implémenter les tests d'intégration spécifiques
    assert True

if __name__ == "__main__":
    pytest.main([__file__])

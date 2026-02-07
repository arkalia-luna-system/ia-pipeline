"""
Tests unitaires générés pour athalia_launcher
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import athalia_launcher
except ImportError:
    pytest.skip(f"Module athalia_launcher non importable")


def test_launch_script():
    """Test de la fonction launch_script"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(athalia_launcher, 'launch_script')
    assert callable(getattr(athalia_launcher, 'launch_script'))

def test_list_available_scripts():
    """Test de la fonction list_available_scripts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(athalia_launcher, 'list_available_scripts')
    assert callable(getattr(athalia_launcher, 'list_available_scripts'))

if __name__ == "__main__":
    pytest.main([__file__])

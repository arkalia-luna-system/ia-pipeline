"""
Tests unitaires générés pour project_classifier
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import project_classifier
except ImportError:
    pytest.skip(f"Module project_classifier non importable")


def test_classify_project():
    """Test de la fonction classify_project"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project_classifier, 'classify_project')
    assert callable(getattr(project_classifier, 'classify_project'))

def test_get_project_name():
    """Test de la fonction get_project_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project_classifier, 'get_project_name')
    assert callable(getattr(project_classifier, 'get_project_name'))

def test_classify_project_intelligent():
    """Test de la fonction classify_project_intelligent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project_classifier, 'classify_project_intelligent')
    assert callable(getattr(project_classifier, 'classify_project_intelligent'))

if __name__ == "__main__":
    pytest.main([__file__])

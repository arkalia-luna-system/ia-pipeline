"""
Tests unitaires générés pour docs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import docs
except ImportError:
    pytest.skip(f"Module docs non importable")


def test_get_swagger_ui_html():
    """Test de la fonction get_swagger_ui_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(docs, 'get_swagger_ui_html')
    assert callable(getattr(docs, 'get_swagger_ui_html'))

def test_get_redoc_html():
    """Test de la fonction get_redoc_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(docs, 'get_redoc_html')
    assert callable(getattr(docs, 'get_redoc_html'))

def test_get_swagger_ui_oauth2_redirect_html():
    """Test de la fonction get_swagger_ui_oauth2_redirect_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(docs, 'get_swagger_ui_oauth2_redirect_html')
    assert callable(getattr(docs, 'get_swagger_ui_oauth2_redirect_html'))

if __name__ == "__main__":
    pytest.main([__file__])

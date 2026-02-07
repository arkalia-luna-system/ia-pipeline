"""
Tests unitaires générés pour languages
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import languages
except ImportError:
    pytest.skip(f"Module languages non importable")


def test_get_official_languages():
    """Test de la fonction get_official_languages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(languages, 'get_official_languages')
    assert callable(getattr(languages, 'get_official_languages'))

def test_get_territory_language_info():
    """Test de la fonction get_territory_language_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(languages, 'get_territory_language_info')
    assert callable(getattr(languages, 'get_territory_language_info'))

if __name__ == "__main__":
    pytest.main([__file__])

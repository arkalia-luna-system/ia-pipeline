"""
Tests unitaires générés pour artistic_templates
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import artistic_templates
except ImportError:
    pytest.skip(f"Module artistic_templates non importable")


def test_get_artistic_templates():
    """Test de la fonction get_artistic_templates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(artistic_templates, 'get_artistic_templates')
    assert callable(getattr(artistic_templates, 'get_artistic_templates'))

if __name__ == "__main__":
    pytest.main([__file__])

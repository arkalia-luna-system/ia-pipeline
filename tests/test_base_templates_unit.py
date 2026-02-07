"""
Tests unitaires générés pour base_templates
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import base_templates
except ImportError:
    pytest.skip(f"Module base_templates non importable")


def test_get_base_templates():
    """Test de la fonction get_base_templates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_templates, 'get_base_templates')
    assert callable(getattr(base_templates, 'get_base_templates'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour jinja2_templates
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jinja2_templates
except ImportError:
    pytest.skip(f"Module jinja2_templates non importable")


def test_jinja2_autoescape_false():
    """Test de la fonction jinja2_autoescape_false"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jinja2_templates, 'jinja2_autoescape_false')
    assert callable(getattr(jinja2_templates, 'jinja2_autoescape_false'))

if __name__ == "__main__":
    pytest.main([__file__])

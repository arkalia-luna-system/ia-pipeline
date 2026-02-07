"""
Tests unitaires générés pour text_join
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import text_join
except ImportError:
    pytest.skip(f"Module text_join non importable")


def test_text_join():
    """Test de la fonction text_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_join, 'text_join')
    assert callable(getattr(text_join, 'text_join'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour html_inline
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import html_inline
except ImportError:
    pytest.skip(f"Module html_inline non importable")


def test_isLetter():
    """Test de la fonction isLetter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html_inline, 'isLetter')
    assert callable(getattr(html_inline, 'isLetter'))

def test_html_inline():
    """Test de la fonction html_inline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html_inline, 'html_inline')
    assert callable(getattr(html_inline, 'html_inline'))

if __name__ == "__main__":
    pytest.main([__file__])

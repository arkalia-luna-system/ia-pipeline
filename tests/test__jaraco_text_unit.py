"""
Tests unitaires générés pour _jaraco_text
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _jaraco_text
except ImportError:
    pytest.skip(f"Module _jaraco_text non importable")


def test__nonblank():
    """Test de la fonction _nonblank"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_jaraco_text, '_nonblank')
    assert callable(getattr(_jaraco_text, '_nonblank'))

def test_yield_lines():
    """Test de la fonction yield_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_jaraco_text, 'yield_lines')
    assert callable(getattr(_jaraco_text, 'yield_lines'))

def test__():
    """Test de la fonction _"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_jaraco_text, '_')
    assert callable(getattr(_jaraco_text, '_'))

def test_drop_comment():
    """Test de la fonction drop_comment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_jaraco_text, 'drop_comment')
    assert callable(getattr(_jaraco_text, 'drop_comment'))

def test_join_continuation():
    """Test de la fonction join_continuation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_jaraco_text, 'join_continuation')
    assert callable(getattr(_jaraco_text, 'join_continuation'))

if __name__ == "__main__":
    pytest.main([__file__])

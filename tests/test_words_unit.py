"""
Tests unitaires générés pour words
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import words
except ImportError:
    pytest.skip(f"Module words non importable")


def test_generate_corpus_id():
    """Test de la fonction generate_corpus_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(words, 'generate_corpus_id')
    assert callable(getattr(words, 'generate_corpus_id'))

if __name__ == "__main__":
    pytest.main([__file__])

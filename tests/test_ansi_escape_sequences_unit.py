"""
Tests unitaires générés pour ansi_escape_sequences
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ansi_escape_sequences
except ImportError:
    pytest.skip(f"Module ansi_escape_sequences non importable")


def test__get_reverse_ansi_sequences():
    """Test de la fonction _get_reverse_ansi_sequences"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ansi_escape_sequences, '_get_reverse_ansi_sequences')
    assert callable(getattr(ansi_escape_sequences, '_get_reverse_ansi_sequences'))

if __name__ == "__main__":
    pytest.main([__file__])

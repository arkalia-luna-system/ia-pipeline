"""
Tests unitaires générés pour regexopt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import regexopt
except ImportError:
    pytest.skip(f"Module regexopt non importable")


def test_make_charset():
    """Test de la fonction make_charset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(regexopt, 'make_charset')
    assert callable(getattr(regexopt, 'make_charset'))

def test_regex_opt_inner():
    """Test de la fonction regex_opt_inner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(regexopt, 'regex_opt_inner')
    assert callable(getattr(regexopt, 'regex_opt_inner'))

def test_regex_opt():
    """Test de la fonction regex_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(regexopt, 'regex_opt')
    assert callable(getattr(regexopt, 'regex_opt'))

if __name__ == "__main__":
    pytest.main([__file__])

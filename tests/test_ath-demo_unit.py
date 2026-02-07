"""
Tests unitaires générés pour ath-demo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ath-demo
except ImportError:
    pytest.skip(f"Module ath-demo non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-demo, 'main')
    assert callable(getattr(ath-demo, 'main'))

def test_run_quickcheck():
    """Test de la fonction run_quickcheck"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-demo, 'run_quickcheck')
    assert callable(getattr(ath-demo, 'run_quickcheck'))

def test_run_security_test():
    """Test de la fonction run_security_test"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-demo, 'run_security_test')
    assert callable(getattr(ath-demo, 'run_security_test'))

def test_run_structure_check():
    """Test de la fonction run_structure_check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-demo, 'run_structure_check')
    assert callable(getattr(ath-demo, 'run_structure_check'))

if __name__ == "__main__":
    pytest.main([__file__])

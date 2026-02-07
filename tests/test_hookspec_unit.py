"""
Tests unitaires générés pour hookspec
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hookspec
except ImportError:
    pytest.skip(f"Module hookspec non importable")


def test_pytest_benchmark_scale_unit():
    """Test de la fonction pytest_benchmark_scale_unit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_scale_unit')
    assert callable(getattr(hookspec, 'pytest_benchmark_scale_unit'))

def test_pytest_benchmark_generate_machine_info():
    """Test de la fonction pytest_benchmark_generate_machine_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_generate_machine_info')
    assert callable(getattr(hookspec, 'pytest_benchmark_generate_machine_info'))

def test_pytest_benchmark_update_machine_info():
    """Test de la fonction pytest_benchmark_update_machine_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_update_machine_info')
    assert callable(getattr(hookspec, 'pytest_benchmark_update_machine_info'))

def test_pytest_benchmark_generate_commit_info():
    """Test de la fonction pytest_benchmark_generate_commit_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_generate_commit_info')
    assert callable(getattr(hookspec, 'pytest_benchmark_generate_commit_info'))

def test_pytest_benchmark_update_commit_info():
    """Test de la fonction pytest_benchmark_update_commit_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_update_commit_info')
    assert callable(getattr(hookspec, 'pytest_benchmark_update_commit_info'))

def test_pytest_benchmark_group_stats():
    """Test de la fonction pytest_benchmark_group_stats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_group_stats')
    assert callable(getattr(hookspec, 'pytest_benchmark_group_stats'))

def test_pytest_benchmark_generate_json():
    """Test de la fonction pytest_benchmark_generate_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_generate_json')
    assert callable(getattr(hookspec, 'pytest_benchmark_generate_json'))

def test_pytest_benchmark_update_json():
    """Test de la fonction pytest_benchmark_update_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_update_json')
    assert callable(getattr(hookspec, 'pytest_benchmark_update_json'))

def test_pytest_benchmark_compare_machine_info():
    """Test de la fonction pytest_benchmark_compare_machine_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hookspec, 'pytest_benchmark_compare_machine_info')
    assert callable(getattr(hookspec, 'pytest_benchmark_compare_machine_info'))

if __name__ == "__main__":
    pytest.main([__file__])

"""
Tests unitaires générés pour django_sql_injection
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import django_sql_injection
except ImportError:
    pytest.skip(f"Module django_sql_injection non importable")


def test_keywords2dict():
    """Test de la fonction keywords2dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(django_sql_injection, 'keywords2dict')
    assert callable(getattr(django_sql_injection, 'keywords2dict'))

def test_django_extra_used():
    """Test de la fonction django_extra_used"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(django_sql_injection, 'django_extra_used')
    assert callable(getattr(django_sql_injection, 'django_extra_used'))

def test_django_rawsql_used():
    """Test de la fonction django_rawsql_used"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(django_sql_injection, 'django_rawsql_used')
    assert callable(getattr(django_sql_injection, 'django_rawsql_used'))

if __name__ == "__main__":
    pytest.main([__file__])

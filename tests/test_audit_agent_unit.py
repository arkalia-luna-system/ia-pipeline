"""
Tests unitaires générés pour audit_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import audit_agent
except ImportError:
    pytest.skip(f"Module audit_agent non importable")


def test_query_qwen():
    """Test de la fonction query_qwen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(audit_agent, 'query_qwen')
    assert callable(getattr(audit_agent, 'query_qwen'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(audit_agent, '__init__')
    assert callable(getattr(audit_agent, '__init__'))

def test_act():
    """Test de la fonction act"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(audit_agent, 'act')
    assert callable(getattr(audit_agent, 'act'))

class TestAuditAgent:
    """Tests pour la classe AuditAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(audit_agent, 'AuditAgent')
        assert isinstance(getattr(audit_agent, 'AuditAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(audit_agent, 'AuditAgent')
        for method_name in ['__init__', 'act']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

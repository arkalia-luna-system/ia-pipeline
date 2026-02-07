"""
Tests unitaires générés pour _task
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _task
except ImportError:
    pytest.skip(f"Module _task non importable")


def test_run_stream():
    """Test de la fonction run_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_task, 'run_stream')
    assert callable(getattr(_task, 'run_stream'))

class TestTaskResult:
    """Tests pour la classe TaskResult"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_task, 'TaskResult')
        assert isinstance(getattr(_task, 'TaskResult'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_task, 'TaskResult')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTaskRunner:
    """Tests pour la classe TaskRunner"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_task, 'TaskRunner')
        assert isinstance(getattr(_task, 'TaskRunner'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_task, 'TaskRunner')
        for method_name in ['run_stream']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

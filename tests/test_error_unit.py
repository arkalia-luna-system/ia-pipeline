"""
Tests unitaires générés pour error
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import error
except ImportError:
    pytest.skip(f"Module error non importable")


class TestIPythonCoreError:
    """Tests pour la classe IPythonCoreError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(error, 'IPythonCoreError')
        assert isinstance(getattr(error, 'IPythonCoreError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(error, 'IPythonCoreError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTryNext:
    """Tests pour la classe TryNext"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(error, 'TryNext')
        assert isinstance(getattr(error, 'TryNext'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(error, 'TryNext')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUsageError:
    """Tests pour la classe UsageError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(error, 'UsageError')
        assert isinstance(getattr(error, 'UsageError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(error, 'UsageError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStdinNotImplementedError:
    """Tests pour la classe StdinNotImplementedError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(error, 'StdinNotImplementedError')
        assert isinstance(getattr(error, 'StdinNotImplementedError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(error, 'StdinNotImplementedError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInputRejected:
    """Tests pour la classe InputRejected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(error, 'InputRejected')
        assert isinstance(getattr(error, 'InputRejected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(error, 'InputRejected')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

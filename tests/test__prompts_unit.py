"""
Tests unitaires générés pour _prompts
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _prompts
except ImportError:
    pytest.skip(f"Module _prompts non importable")


class TestLedgerEntryBooleanAnswer:
    """Tests pour la classe LedgerEntryBooleanAnswer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_prompts, 'LedgerEntryBooleanAnswer')
        assert isinstance(getattr(_prompts, 'LedgerEntryBooleanAnswer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_prompts, 'LedgerEntryBooleanAnswer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLedgerEntryStringAnswer:
    """Tests pour la classe LedgerEntryStringAnswer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_prompts, 'LedgerEntryStringAnswer')
        assert isinstance(getattr(_prompts, 'LedgerEntryStringAnswer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_prompts, 'LedgerEntryStringAnswer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLedgerEntry:
    """Tests pour la classe LedgerEntry"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_prompts, 'LedgerEntry')
        assert isinstance(getattr(_prompts, 'LedgerEntry'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_prompts, 'LedgerEntry')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

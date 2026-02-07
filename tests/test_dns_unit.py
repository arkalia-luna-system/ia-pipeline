"""
Tests unitaires générés pour dns
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dns
except ImportError:
    pytest.skip(f"Module dns non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dns, 'analyse_text')
    assert callable(getattr(dns, 'analyse_text'))

class TestDnsZoneLexer:
    """Tests pour la classe DnsZoneLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dns, 'DnsZoneLexer')
        assert isinstance(getattr(dns, 'DnsZoneLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dns, 'DnsZoneLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

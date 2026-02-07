"""
Tests unitaires générés pour ldap
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ldap
except ImportError:
    pytest.skip(f"Module ldap non importable")


class TestLdifLexer:
    """Tests pour la classe LdifLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ldap, 'LdifLexer')
        assert isinstance(getattr(ldap, 'LdifLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ldap, 'LdifLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLdaprcLexer:
    """Tests pour la classe LdaprcLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ldap, 'LdaprcLexer')
        assert isinstance(getattr(ldap, 'LdaprcLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ldap, 'LdaprcLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

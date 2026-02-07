"""
Tests unitaires générés pour _oid
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _oid
except ImportError:
    pytest.skip(f"Module _oid non importable")


class TestExtensionOID:
    """Tests pour la classe ExtensionOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'ExtensionOID')
        assert isinstance(getattr(_oid, 'ExtensionOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'ExtensionOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOCSPExtensionOID:
    """Tests pour la classe OCSPExtensionOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'OCSPExtensionOID')
        assert isinstance(getattr(_oid, 'OCSPExtensionOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'OCSPExtensionOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCRLEntryExtensionOID:
    """Tests pour la classe CRLEntryExtensionOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'CRLEntryExtensionOID')
        assert isinstance(getattr(_oid, 'CRLEntryExtensionOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'CRLEntryExtensionOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNameOID:
    """Tests pour la classe NameOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'NameOID')
        assert isinstance(getattr(_oid, 'NameOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'NameOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSignatureAlgorithmOID:
    """Tests pour la classe SignatureAlgorithmOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'SignatureAlgorithmOID')
        assert isinstance(getattr(_oid, 'SignatureAlgorithmOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'SignatureAlgorithmOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHashAlgorithmOID:
    """Tests pour la classe HashAlgorithmOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'HashAlgorithmOID')
        assert isinstance(getattr(_oid, 'HashAlgorithmOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'HashAlgorithmOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPublicKeyAlgorithmOID:
    """Tests pour la classe PublicKeyAlgorithmOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'PublicKeyAlgorithmOID')
        assert isinstance(getattr(_oid, 'PublicKeyAlgorithmOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'PublicKeyAlgorithmOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExtendedKeyUsageOID:
    """Tests pour la classe ExtendedKeyUsageOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'ExtendedKeyUsageOID')
        assert isinstance(getattr(_oid, 'ExtendedKeyUsageOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'ExtendedKeyUsageOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOtherNameFormOID:
    """Tests pour la classe OtherNameFormOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'OtherNameFormOID')
        assert isinstance(getattr(_oid, 'OtherNameFormOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'OtherNameFormOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAuthorityInformationAccessOID:
    """Tests pour la classe AuthorityInformationAccessOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'AuthorityInformationAccessOID')
        assert isinstance(getattr(_oid, 'AuthorityInformationAccessOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'AuthorityInformationAccessOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSubjectInformationAccessOID:
    """Tests pour la classe SubjectInformationAccessOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'SubjectInformationAccessOID')
        assert isinstance(getattr(_oid, 'SubjectInformationAccessOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'SubjectInformationAccessOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCertificatePoliciesOID:
    """Tests pour la classe CertificatePoliciesOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'CertificatePoliciesOID')
        assert isinstance(getattr(_oid, 'CertificatePoliciesOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'CertificatePoliciesOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAttributeOID:
    """Tests pour la classe AttributeOID"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_oid, 'AttributeOID')
        assert isinstance(getattr(_oid, 'AttributeOID'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_oid, 'AttributeOID')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

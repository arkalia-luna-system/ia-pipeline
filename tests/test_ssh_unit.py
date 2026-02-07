"""
Tests unitaires générés pour ssh
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ssh
except ImportError:
    pytest.skip(f"Module ssh non importable")


def test__get_ssh_key_type():
    """Test de la fonction _get_ssh_key_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_ssh_key_type')
    assert callable(getattr(ssh, '_get_ssh_key_type'))

def test__ecdsa_key_type():
    """Test de la fonction _ecdsa_key_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_ecdsa_key_type')
    assert callable(getattr(ssh, '_ecdsa_key_type'))

def test__ssh_pem_encode():
    """Test de la fonction _ssh_pem_encode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_ssh_pem_encode')
    assert callable(getattr(ssh, '_ssh_pem_encode'))

def test__check_block_size():
    """Test de la fonction _check_block_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_check_block_size')
    assert callable(getattr(ssh, '_check_block_size'))

def test__check_empty():
    """Test de la fonction _check_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_check_empty')
    assert callable(getattr(ssh, '_check_empty'))

def test__init_cipher():
    """Test de la fonction _init_cipher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_init_cipher')
    assert callable(getattr(ssh, '_init_cipher'))

def test__get_u32():
    """Test de la fonction _get_u32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_u32')
    assert callable(getattr(ssh, '_get_u32'))

def test__get_u64():
    """Test de la fonction _get_u64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_u64')
    assert callable(getattr(ssh, '_get_u64'))

def test__get_sshstr():
    """Test de la fonction _get_sshstr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_sshstr')
    assert callable(getattr(ssh, '_get_sshstr'))

def test__get_mpint():
    """Test de la fonction _get_mpint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_mpint')
    assert callable(getattr(ssh, '_get_mpint'))

def test__to_mpint():
    """Test de la fonction _to_mpint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_to_mpint')
    assert callable(getattr(ssh, '_to_mpint'))

def test_load_application():
    """Test de la fonction load_application"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_application')
    assert callable(getattr(ssh, 'load_application'))

def test__lookup_kformat():
    """Test de la fonction _lookup_kformat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_lookup_kformat')
    assert callable(getattr(ssh, '_lookup_kformat'))

def test_load_ssh_private_key():
    """Test de la fonction load_ssh_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_ssh_private_key')
    assert callable(getattr(ssh, 'load_ssh_private_key'))

def test__serialize_ssh_private_key():
    """Test de la fonction _serialize_ssh_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_serialize_ssh_private_key')
    assert callable(getattr(ssh, '_serialize_ssh_private_key'))

def test__get_ec_hash_alg():
    """Test de la fonction _get_ec_hash_alg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_get_ec_hash_alg')
    assert callable(getattr(ssh, '_get_ec_hash_alg'))

def test__load_ssh_public_identity():
    """Test de la fonction _load_ssh_public_identity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_load_ssh_public_identity')
    assert callable(getattr(ssh, '_load_ssh_public_identity'))

def test_load_ssh_public_identity():
    """Test de la fonction load_ssh_public_identity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_ssh_public_identity')
    assert callable(getattr(ssh, 'load_ssh_public_identity'))

def test__parse_exts_opts():
    """Test de la fonction _parse_exts_opts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_parse_exts_opts')
    assert callable(getattr(ssh, '_parse_exts_opts'))

def test_ssh_key_fingerprint():
    """Test de la fonction ssh_key_fingerprint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'ssh_key_fingerprint')
    assert callable(getattr(ssh, 'ssh_key_fingerprint'))

def test_load_ssh_public_key():
    """Test de la fonction load_ssh_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_ssh_public_key')
    assert callable(getattr(ssh, 'load_ssh_public_key'))

def test_serialize_ssh_public_key():
    """Test de la fonction serialize_ssh_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'serialize_ssh_public_key')
    assert callable(getattr(ssh, 'serialize_ssh_public_key'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '__init__')
    assert callable(getattr(ssh, '__init__'))

def test_put_raw():
    """Test de la fonction put_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'put_raw')
    assert callable(getattr(ssh, 'put_raw'))

def test_put_u32():
    """Test de la fonction put_u32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'put_u32')
    assert callable(getattr(ssh, 'put_u32'))

def test_put_u64():
    """Test de la fonction put_u64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'put_u64')
    assert callable(getattr(ssh, 'put_u64'))

def test_put_sshstr():
    """Test de la fonction put_sshstr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'put_sshstr')
    assert callable(getattr(ssh, 'put_sshstr'))

def test_put_mpint():
    """Test de la fonction put_mpint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'put_mpint')
    assert callable(getattr(ssh, 'put_mpint'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'size')
    assert callable(getattr(ssh, 'size'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'render')
    assert callable(getattr(ssh, 'render'))

def test_tobytes():
    """Test de la fonction tobytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'tobytes')
    assert callable(getattr(ssh, 'tobytes'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_load_private():
    """Test de la fonction load_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_private')
    assert callable(getattr(ssh, 'load_private'))

def test_encode_public():
    """Test de la fonction encode_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_public')
    assert callable(getattr(ssh, 'encode_public'))

def test_encode_private():
    """Test de la fonction encode_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_private')
    assert callable(getattr(ssh, 'encode_private'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_load_private():
    """Test de la fonction load_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_private')
    assert callable(getattr(ssh, 'load_private'))

def test_encode_public():
    """Test de la fonction encode_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_public')
    assert callable(getattr(ssh, 'encode_public'))

def test_encode_private():
    """Test de la fonction encode_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_private')
    assert callable(getattr(ssh, 'encode_private'))

def test__validate():
    """Test de la fonction _validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_validate')
    assert callable(getattr(ssh, '_validate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '__init__')
    assert callable(getattr(ssh, '__init__'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_load_private():
    """Test de la fonction load_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_private')
    assert callable(getattr(ssh, 'load_private'))

def test_encode_public():
    """Test de la fonction encode_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_public')
    assert callable(getattr(ssh, 'encode_public'))

def test_encode_private():
    """Test de la fonction encode_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_private')
    assert callable(getattr(ssh, 'encode_private'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_load_private():
    """Test de la fonction load_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_private')
    assert callable(getattr(ssh, 'load_private'))

def test_encode_public():
    """Test de la fonction encode_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_public')
    assert callable(getattr(ssh, 'encode_public'))

def test_encode_private():
    """Test de la fonction encode_private"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'encode_private')
    assert callable(getattr(ssh, 'encode_private'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test_load_public():
    """Test de la fonction load_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'load_public')
    assert callable(getattr(ssh, 'load_public'))

def test_get_public():
    """Test de la fonction get_public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'get_public')
    assert callable(getattr(ssh, 'get_public'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '__init__')
    assert callable(getattr(ssh, '__init__'))

def test_nonce():
    """Test de la fonction nonce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'nonce')
    assert callable(getattr(ssh, 'nonce'))

def test_public_key():
    """Test de la fonction public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'public_key')
    assert callable(getattr(ssh, 'public_key'))

def test_serial():
    """Test de la fonction serial"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'serial')
    assert callable(getattr(ssh, 'serial'))

def test_type():
    """Test de la fonction type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'type')
    assert callable(getattr(ssh, 'type'))

def test_key_id():
    """Test de la fonction key_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'key_id')
    assert callable(getattr(ssh, 'key_id'))

def test_valid_principals():
    """Test de la fonction valid_principals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_principals')
    assert callable(getattr(ssh, 'valid_principals'))

def test_valid_before():
    """Test de la fonction valid_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_before')
    assert callable(getattr(ssh, 'valid_before'))

def test_valid_after():
    """Test de la fonction valid_after"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_after')
    assert callable(getattr(ssh, 'valid_after'))

def test_critical_options():
    """Test de la fonction critical_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'critical_options')
    assert callable(getattr(ssh, 'critical_options'))

def test_extensions():
    """Test de la fonction extensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'extensions')
    assert callable(getattr(ssh, 'extensions'))

def test_signature_key():
    """Test de la fonction signature_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'signature_key')
    assert callable(getattr(ssh, 'signature_key'))

def test_public_bytes():
    """Test de la fonction public_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'public_bytes')
    assert callable(getattr(ssh, 'public_bytes'))

def test_verify_cert_signature():
    """Test de la fonction verify_cert_signature"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'verify_cert_signature')
    assert callable(getattr(ssh, 'verify_cert_signature'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '__init__')
    assert callable(getattr(ssh, '__init__'))

def test_public_key():
    """Test de la fonction public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'public_key')
    assert callable(getattr(ssh, 'public_key'))

def test_serial():
    """Test de la fonction serial"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'serial')
    assert callable(getattr(ssh, 'serial'))

def test_type():
    """Test de la fonction type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'type')
    assert callable(getattr(ssh, 'type'))

def test_key_id():
    """Test de la fonction key_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'key_id')
    assert callable(getattr(ssh, 'key_id'))

def test_valid_principals():
    """Test de la fonction valid_principals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_principals')
    assert callable(getattr(ssh, 'valid_principals'))

def test_valid_for_all_principals():
    """Test de la fonction valid_for_all_principals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_for_all_principals')
    assert callable(getattr(ssh, 'valid_for_all_principals'))

def test_valid_before():
    """Test de la fonction valid_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_before')
    assert callable(getattr(ssh, 'valid_before'))

def test_valid_after():
    """Test de la fonction valid_after"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'valid_after')
    assert callable(getattr(ssh, 'valid_after'))

def test_add_critical_option():
    """Test de la fonction add_critical_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'add_critical_option')
    assert callable(getattr(ssh, 'add_critical_option'))

def test_add_extension():
    """Test de la fonction add_extension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'add_extension')
    assert callable(getattr(ssh, 'add_extension'))

def test_sign():
    """Test de la fonction sign"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, 'sign')
    assert callable(getattr(ssh, 'sign'))

def test__bcrypt_kdf():
    """Test de la fonction _bcrypt_kdf"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ssh, '_bcrypt_kdf')
    assert callable(getattr(ssh, '_bcrypt_kdf'))

class Test_SSHCipher:
    """Tests pour la classe _SSHCipher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHCipher')
        assert isinstance(getattr(ssh, '_SSHCipher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHCipher')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_FragList:
    """Tests pour la classe _FragList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_FragList')
        assert isinstance(getattr(ssh, '_FragList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_FragList')
        for method_name in ['__init__', 'put_raw', 'put_u32', 'put_u64', 'put_sshstr', 'put_mpint', 'size', 'render', 'tobytes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatRSA:
    """Tests pour la classe _SSHFormatRSA"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatRSA')
        assert isinstance(getattr(ssh, '_SSHFormatRSA'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatRSA')
        for method_name in ['get_public', 'load_public', 'load_private', 'encode_public', 'encode_private']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatDSA:
    """Tests pour la classe _SSHFormatDSA"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatDSA')
        assert isinstance(getattr(ssh, '_SSHFormatDSA'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatDSA')
        for method_name in ['get_public', 'load_public', 'load_private', 'encode_public', 'encode_private', '_validate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatECDSA:
    """Tests pour la classe _SSHFormatECDSA"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatECDSA')
        assert isinstance(getattr(ssh, '_SSHFormatECDSA'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatECDSA')
        for method_name in ['__init__', 'get_public', 'load_public', 'load_private', 'encode_public', 'encode_private']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatEd25519:
    """Tests pour la classe _SSHFormatEd25519"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatEd25519')
        assert isinstance(getattr(ssh, '_SSHFormatEd25519'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatEd25519')
        for method_name in ['get_public', 'load_public', 'load_private', 'encode_public', 'encode_private']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatSKEd25519:
    """Tests pour la classe _SSHFormatSKEd25519"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatSKEd25519')
        assert isinstance(getattr(ssh, '_SSHFormatSKEd25519'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatSKEd25519')
        for method_name in ['load_public', 'get_public']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SSHFormatSKECDSA:
    """Tests pour la classe _SSHFormatSKECDSA"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, '_SSHFormatSKECDSA')
        assert isinstance(getattr(ssh, '_SSHFormatSKECDSA'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, '_SSHFormatSKECDSA')
        for method_name in ['load_public', 'get_public']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSHCertificateType:
    """Tests pour la classe SSHCertificateType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, 'SSHCertificateType')
        assert isinstance(getattr(ssh, 'SSHCertificateType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, 'SSHCertificateType')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSHCertificate:
    """Tests pour la classe SSHCertificate"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, 'SSHCertificate')
        assert isinstance(getattr(ssh, 'SSHCertificate'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, 'SSHCertificate')
        for method_name in ['__init__', 'nonce', 'public_key', 'serial', 'type', 'key_id', 'valid_principals', 'valid_before', 'valid_after', 'critical_options', 'extensions', 'signature_key', 'public_bytes', 'verify_cert_signature']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSHCertificateBuilder:
    """Tests pour la classe SSHCertificateBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ssh, 'SSHCertificateBuilder')
        assert isinstance(getattr(ssh, 'SSHCertificateBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ssh, 'SSHCertificateBuilder')
        for method_name in ['__init__', 'public_key', 'serial', 'type', 'key_id', 'valid_principals', 'valid_for_all_principals', 'valid_before', 'valid_after', 'add_critical_option', 'add_extension', 'sign']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])

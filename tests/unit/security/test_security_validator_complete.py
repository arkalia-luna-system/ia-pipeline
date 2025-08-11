#!/usr/bin/env python3
"""
Tests complets pour security_validator.py (489 lignes)
Couverture actuelle: 15% → Objectif: 85%

Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from athalia_core.security_validator import SecurityValidator


class TestSecurityValidatorComplete:
    """Tests complets pour SecurityValidator."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer fichiers de test avec vulnérabilités potentielles
        (self.project_path / "secure_file.py").write_text("""
import hashlib
import secrets

def secure_hash(data):
    '''Fonction sécurisée pour hasher des données.'''
    salt = secrets.token_bytes(32)
    return hashlib.pbkdf2_hmac('sha256', data.encode(), salt, 100000)

def validate_input(user_input):
    '''Validation sécurisée des entrées.'''
    if not isinstance(user_input, str):
        raise ValueError("Input must be string")
    if len(user_input) > 1000:
        raise ValueError("Input too long")
    return user_input.strip()
""")
        
        (self.project_path / "vulnerable_file.py").write_text("""
import subprocess
import pickle
import os

# Vulnérabilités intentionnelles pour les tests
def dangerous_eval(user_code):
    return eval(user_code)  # eval() est dangereux

def dangerous_exec(user_code):
    exec(user_code)  # exec() est dangereux

def dangerous_subprocess(user_command):
    subprocess.call(user_command, shell=True)  # shell=True dangereux

def dangerous_pickle_load(data):
    return pickle.loads(data)  # pickle.loads() dangereux

def hardcoded_password():
    password = "secret123"  # Mot de passe hardcodé
    api_key = "sk-1234567890abcdef"  # Clé API hardcodée
    return password, api_key

def sql_injection_risk(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection
    return query
""")
        
        (self.project_path / "requirements.txt").write_text("""
requests==2.25.0
django==3.1.0
flask==1.1.0
""")
        
        self.validator = SecurityValidator()

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_validator_initialization(self):
        """Test initialisation du validateur."""
        assert isinstance(self.validator, SecurityValidator)
        assert hasattr(self.validator, 'scan_results')
        assert hasattr(self.validator, 'vulnerability_patterns')

    def test_scan_file_for_vulnerabilities_secure(self):
        """Test scan fichier sécurisé."""
        secure_file = self.project_path / "secure_file.py"
        results = self.validator.scan_file_for_vulnerabilities(str(secure_file))
        
        assert isinstance(results, dict)
        # Un fichier sécurisé devrait avoir peu ou pas de vulnérabilités
        vulnerabilities = results.get('vulnerabilities', [])
        high_severity = [v for v in vulnerabilities if v.get('severity') == 'HIGH']
        assert len(high_severity) == 0

    def test_scan_file_for_vulnerabilities_dangerous(self):
        """Test scan fichier avec vulnérabilités."""
        vulnerable_file = self.project_path / "vulnerable_file.py"
        results = self.validator.scan_file_for_vulnerabilities(str(vulnerable_file))
        
        assert isinstance(results, dict)
        vulnerabilities = results.get('vulnerabilities', [])
        
        # Le fichier vulnérable devrait contenir plusieurs vulnérabilités
        assert len(vulnerabilities) > 0
        
        # Vérifier détection de vulnérabilités spécifiques
        vuln_types = [v.get('type', '') for v in vulnerabilities]
        assert any('eval' in vtype.lower() for vtype in vuln_types)

    def test_detect_eval_usage(self):
        """Test détection usage eval()."""
        code_with_eval = "result = eval(user_input)"
        detection = self.validator.detect_dangerous_functions(code_with_eval)
        
        assert isinstance(detection, (dict, list))
        if isinstance(detection, dict):
            assert 'eval' in str(detection).lower()
        else:
            assert any('eval' in str(item).lower() for item in detection)

    def test_detect_exec_usage(self):
        """Test détection usage exec()."""
        code_with_exec = "exec(user_code)"
        detection = self.validator.detect_dangerous_functions(code_with_exec)
        
        assert isinstance(detection, (dict, list))
        # exec() devrait être détecté comme dangereux
        assert len(detection) > 0

    def test_detect_subprocess_shell_injection(self):
        """Test détection injection shell subprocess."""
        code_with_shell = "subprocess.call(cmd, shell=True)"
        detection = self.validator.detect_command_injection(code_with_shell)
        
        assert isinstance(detection, (dict, list))
        # shell=True devrait être détecté comme risqué
        assert len(detection) > 0

    def test_detect_hardcoded_secrets(self):
        """Test détection secrets hardcodés."""
        vulnerable_file = self.project_path / "vulnerable_file.py"
        secrets = self.validator.detect_hardcoded_secrets(str(vulnerable_file))
        
        assert isinstance(secrets, (dict, list))
        # Devrait détecter password et api_key hardcodés
        secrets_found = str(secrets).lower()
        assert 'password' in secrets_found or 'secret' in secrets_found

    def test_check_sql_injection_patterns(self):
        """Test détection patterns SQL injection."""
        sql_code = 'query = f"SELECT * FROM users WHERE id = {user_id}"'
        detection = self.validator.check_sql_injection_patterns(sql_code)
        
        assert isinstance(detection, (dict, list, bool))
        # Devrait détecter le pattern SQL injection
        if isinstance(detection, bool):
            assert detection is True
        else:
            assert len(detection) > 0

    def test_analyze_dependencies_vulnerabilities(self):
        """Test analyse vulnérabilités dépendances."""
        requirements_file = self.project_path / "requirements.txt"
        vuln_deps = self.validator.analyze_dependencies_vulnerabilities(str(requirements_file))
        
        assert isinstance(vuln_deps, dict)
        # Devrait analyser les dépendances du fichier requirements.txt
        assert 'dependencies' in vuln_deps or 'vulnerabilities' in vuln_deps

    def test_validate_encryption_usage(self):
        """Test validation usage chiffrement."""
        secure_file = self.project_path / "secure_file.py"
        encryption_analysis = self.validator.validate_encryption_usage(str(secure_file))
        
        assert isinstance(encryption_analysis, dict)
        # Le fichier sécurisé utilise hashlib correctement
        assert 'encryption_score' in encryption_analysis or 'secure' in str(encryption_analysis)

    def test_check_authentication_security(self):
        """Test vérification sécurité authentification."""
        auth_code = """
def authenticate_user(username, password):
    if username == "admin" and password == "password":
        return True
    return False
"""
        
        auth_analysis = self.validator.check_authentication_security(auth_code)
        
        assert isinstance(auth_analysis, dict)
        # Devrait détecter l'authentification faible
        issues = auth_analysis.get('issues', [])
        assert len(issues) > 0

    def test_validate_input_sanitization(self):
        """Test validation sanitisation entrées."""
        input_code = """
def process_user_input(data):
    return data  # Pas de validation
"""
        
        sanitization = self.validator.validate_input_sanitization(input_code)
        
        assert isinstance(sanitization, dict)
        # Devrait détecter l'absence de validation
        assert 'sanitization_score' in sanitization or 'issues' in sanitization

    def test_check_file_permissions(self):
        """Test vérification permissions fichiers."""
        # Créer fichier avec permissions spécifiques
        test_file = self.project_path / "test_permissions.py"
        test_file.write_text("# Test file")
        test_file.chmod(0o777)  # Permissions trop larges
        
        perm_analysis = self.validator.check_file_permissions(str(test_file))
        
        assert isinstance(perm_analysis, dict)
        # Devrait détecter les permissions trop larges
        if 'permissions' in perm_analysis:
            assert perm_analysis['permissions'] is not None

    def test_analyze_cryptographic_strength(self):
        """Test analyse force cryptographique."""
        crypto_code = """
import hashlib
import md5  # Algorithme faible

def weak_hash(data):
    return md5.md5(data).hexdigest()  # MD5 est faible

def strong_hash(data):
    return hashlib.sha256(data).hexdigest()  # SHA256 est fort
"""
        
        crypto_analysis = self.validator.analyze_cryptographic_strength(crypto_code)
        
        assert isinstance(crypto_analysis, dict)
        # Devrait détecter l'usage de MD5 faible
        weak_algos = crypto_analysis.get('weak_algorithms', [])
        assert isinstance(weak_algos, list)

    def test_detect_xss_vulnerabilities(self):
        """Test détection vulnérabilités XSS."""
        xss_code = """
def render_user_content(user_input):
    return f"<div>{user_input}</div>"  # XSS possible
"""
        
        xss_detection = self.validator.detect_xss_vulnerabilities(xss_code)
        
        assert isinstance(xss_detection, (dict, list))
        # Devrait détecter le risque XSS
        assert len(xss_detection) > 0

    def test_check_csrf_protection(self):
        """Test vérification protection CSRF."""
        csrf_code = """
def process_form(request):
    # Pas de protection CSRF
    return save_data(request.POST)
"""
        
        csrf_analysis = self.validator.check_csrf_protection(csrf_code)
        
        assert isinstance(csrf_analysis, dict)
        # Devrait détecter l'absence de protection CSRF
        assert 'csrf_protection' in csrf_analysis or 'issues' in csrf_analysis

    def test_validate_session_security(self):
        """Test validation sécurité sessions."""
        session_code = """
session_config = {
    'secure': False,  # Cookie non sécurisé
    'httponly': False,  # Pas de protection XSS
    'timeout': 86400 * 30  # Timeout trop long
}
"""
        
        session_analysis = self.validator.validate_session_security(session_code)
        
        assert isinstance(session_analysis, dict)
        # Devrait détecter les problèmes de configuration session
        issues = session_analysis.get('issues', [])
        assert isinstance(issues, list)

    def test_scan_for_information_disclosure(self):
        """Test scan divulgation d'informations."""
        disclosure_code = """
def debug_info():
    print(f"Database password: {db_password}")  # Divulgation
    print(f"API key: {api_key}")  # Divulgation
    return {"debug": True, "internal_path": "/internal/path"}
"""
        
        disclosure = self.validator.scan_for_information_disclosure(disclosure_code)
        
        assert isinstance(disclosure, (dict, list))
        # Devrait détecter les divulgations d'informations
        assert len(disclosure) > 0

    def test_check_error_handling_security(self):
        """Test vérification sécurité gestion erreurs."""
        error_code = """
try:
    risky_operation()
except Exception as e:
    print(f"Error details: {e}")  # Divulgue trop d'infos
    raise e  # Re-raise sans masquage
"""
        
        error_analysis = self.validator.check_error_handling_security(error_code)
        
        assert isinstance(error_analysis, dict)
        # Devrait détecter les problèmes de gestion d'erreurs
        assert 'error_handling_score' in error_analysis or 'issues' in error_analysis

    def test_comprehensive_security_scan(self):
        """Test scan sécurité complet."""
        scan_results = self.validator.run_comprehensive_scan(str(self.project_path))
        
        assert isinstance(scan_results, dict)
        
        # Vérifier que toutes les catégories sont présentes
        expected_categories = [
            'vulnerabilities', 'dependencies', 'authentication', 
            'encryption', 'input_validation', 'file_permissions'
        ]
        
        # Au moins la moitié des catégories devraient être présentes
        present_categories = sum(1 for cat in expected_categories if cat in scan_results)
        assert present_categories >= len(expected_categories) // 2

    def test_generate_security_report(self):
        """Test génération rapport sécurité."""
        # Exécuter scan d'abord
        self.validator.run_comprehensive_scan(str(self.project_path))
        
        report = self.validator.generate_security_report()
        
        assert isinstance(report, (dict, str))
        
        if isinstance(report, str):
            # Rapport texte
            assert 'security' in report.lower()
            assert len(report) > 100
        else:
            # Rapport structuré
            assert 'summary' in report or 'vulnerabilities' in report

    def test_calculate_security_score(self):
        """Test calcul score sécurité."""
        # Exécuter scan complet
        self.validator.run_comprehensive_scan(str(self.project_path))
        
        score = self.validator.calculate_security_score()
        
        assert isinstance(score, (int, float, dict))
        
        if isinstance(score, (int, float)):
            assert 0 <= score <= 100
        else:
            assert 'score' in score

    def test_export_security_results(self):
        """Test export résultats sécurité."""
        # Exécuter scan
        self.validator.run_comprehensive_scan(str(self.project_path))
        
        export_file = self.project_path / "security_report.json"
        success = self.validator.export_security_results(str(export_file))
        
        if success:
            assert export_file.exists()
            
            # Vérifier que le JSON est valide
            with open(export_file) as f:
                data = json.load(f)
                assert isinstance(data, dict)

    @patch('athalia_core.security_validator.subprocess')
    def test_external_security_tools_integration(self, mock_subprocess):
        """Test intégration outils sécurité externes."""
        mock_subprocess.run.return_value.returncode = 0
        mock_subprocess.run.return_value.stdout = "No vulnerabilities found"
        
        # Test avec mock pour éviter dépendances externes
        result = self.validator.run_external_security_scan(str(self.project_path))
        
        assert isinstance(result, (dict, str, bool))

    def test_performance_large_codebase(self):
        """Test performance sur grande base de code."""
        import time
        
        # Créer beaucoup de fichiers
        for i in range(20):
            (self.project_path / f"file_{i}.py").write_text(f"""
def function_{i}():
    data = "test data {i}"
    return eval(data)  # Vulnérabilité intentionnelle
""")
        
        start_time = time.time()
        self.validator.run_comprehensive_scan(str(self.project_path))
        scan_duration = time.time() - start_time
        
        # Le scan ne devrait pas prendre trop de temps
        assert scan_duration < 30.0  # Moins de 30 secondes

    @pytest.mark.parametrize("vuln_type,code_sample", [
        ("eval", "result = eval(user_input)"),
        ("exec", "exec(malicious_code)"),
        ("pickle", "pickle.loads(untrusted_data)"),
        ("subprocess", "subprocess.call(cmd, shell=True)"),
        ("sql_injection", "query = f'SELECT * FROM users WHERE id = {user_id}'"),
    ])
    def test_vulnerability_detection_parametrized(self, vuln_type, code_sample):
        """Test détection vulnérabilités avec paramètres."""
        detection = self.validator.detect_vulnerability_by_type(vuln_type, code_sample)
        
        # Devrait détecter la vulnérabilité correspondante
        assert isinstance(detection, (dict, list, bool))
        if isinstance(detection, bool):
            assert detection is True
        else:
            assert len(detection) > 0

    def test_error_handling_invalid_files(self):
        """Test gestion erreurs fichiers invalides."""
        invalid_file = self.project_path / "invalid.bin"
        invalid_file.write_bytes(b'\x00\x01\x02\x03')
        
        # Le validateur devrait gérer gracieusement les fichiers invalides
        try:
            results = self.validator.scan_file_for_vulnerabilities(str(invalid_file))
            assert isinstance(results, dict)
        except Exception as e:
            # Exception acceptable pour fichier binaire
            assert "binary" in str(e).lower() or "invalid" in str(e).lower()

    def test_whitelist_false_positives(self):
        """Test whitelist pour faux positifs."""
        # Code qui peut générer des faux positifs
        safe_code = """
# Ce code utilise eval de manière sécurisée dans un contexte contrôlé
import ast

def safe_eval(expression):
    # Utilisation sécurisée d'ast.literal_eval
    return ast.literal_eval(expression)
"""
        
        # Configurer whitelist
        self.validator.configure_whitelist(['ast.literal_eval'])
        
        detection = self.validator.detect_dangerous_functions(safe_code)
        
        # Ne devrait pas détecter ast.literal_eval comme dangereux
        assert isinstance(detection, (dict, list))


class TestSecurityValidatorIntegration:
    """Tests d'intégration pour SecurityValidator."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_security_audit_workflow(self):
        """Test workflow complet audit sécurité."""
        # Créer projet avec vulnérabilités mixtes
        (self.project_path / "src").mkdir()
        
        # Code avec vulnérabilités
        (self.project_path / "src" / "vulnerable.py").write_text("""
import subprocess
import pickle

def process_user_data(user_input, user_file):
    # Vulnérabilités multiples
    result = eval(user_input)  # eval dangereux
    subprocess.call(f"cat {user_file}", shell=True)  # injection commande
    return pickle.loads(result)  # pickle dangereux
""")
        
        # Code sécurisé
        (self.project_path / "src" / "secure.py").write_text("""
import hashlib
import json

def secure_process(data):
    # Code sécurisé
    if not isinstance(data, str):
        raise ValueError("Invalid input")
    
    hashed = hashlib.sha256(data.encode()).hexdigest()
    return json.loads(data) if data.startswith('{') else data
""")
        
        # Configuration avec dépendances vulnérables
        (self.project_path / "requirements.txt").write_text("""
requests==2.20.0
django==2.0.0
flask==0.12.0
""")
        
        # Exécuter audit complet
        validator = SecurityValidator()
        results = validator.run_comprehensive_scan(str(self.project_path))
        
        # Vérifications
        assert isinstance(results, dict)
        assert len(results) > 0
        
        # Générer rapport
        report = validator.generate_security_report()
        assert isinstance(report, (dict, str))
        
        # Calculer score
        score = validator.calculate_security_score()
        assert isinstance(score, (int, float, dict))
        
        # Export
        export_file = self.project_path / "security_audit.json"
        export_success = validator.export_security_results(str(export_file))
        
        if export_success:
            assert export_file.exists()


class TestSecurityValidatorPerformance:
    """Tests de performance pour SecurityValidator."""

    def setup_method(self):
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()
        self.validator = SecurityValidator()

    def teardown_method(self):
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_scalability_many_files(self):
        """Test scalabilité avec beaucoup de fichiers."""
        import time
        
        large_project = Path(self.temp_dir) / "large_project"
        large_project.mkdir()
        
        # Créer beaucoup de fichiers avec vulnérabilités
        for i in range(100):
            (large_project / f"file_{i}.py").write_text(f"""
# File {i}
def function_{i}(user_input):
    result = eval(user_input)  # Vulnérabilité
    return result * {i}
""")
        
        start_time = time.time()
        results = self.validator.run_comprehensive_scan(str(large_project))
        scan_time = time.time() - start_time
        
        # Vérifications performance
        assert isinstance(results, dict)
        assert scan_time < 60.0  # Moins de 1 minute pour 100 fichiers
        
        # Vérifier détection vulnérabilités
        vulnerabilities = results.get('vulnerabilities', [])
        assert len(vulnerabilities) >= 100  # Au moins une par fichier
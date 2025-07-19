#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le système d'audit intelligent Athalia
"""
import os
import shutil
import tempfile
import pytest

try:
    from athalia_core.audit import ProjectAuditor, audit_project_intelligent, generate_audit_report
except ImportError:
    ProjectAuditor = None
    audit_project_intelligent = None
    generate_audit_report = None


class TestAuditIntelligent:
    """Tests pour l'audit intelligent."""

    def setup_method(self):
        """Prépare un projet de test pour l'audit."""
        self.test_dir = tempfile.mkdtemp()
        self.create_test_project()

    def teardown_method(self):
        """Nettoie après les tests."""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def create_test_project(self):
        """Crée un projet de test avec des problèmes connus."""
        os.makedirs(os.path.join(self.test_dir, 'src'), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, 'tests'), exist_ok=True)
        # Fichier main.py avec problèmes
        main_content = '''"""
Module principal avec problèmes.
"""

# Problème de sécurité
password = "f"
api_key = "sk-f"

# Problème de performance
def slow_function():
    result = []
    for index in range(100):
        result.append(index)
    return result

# Problème de logging
def debug_function():
    import logging
    logging.info("Debug f")
    return True

# Appel shell risqué
def run_command():
    import os
    os.system("ls -f")
    return True

if __name__ == "__main__":
    debug_function()
    run_command()
'''
        with open(os.path.join(self.test_dir, 'main.py'), 'w') as file_handle:
            file_handle.write(main_content)
        # Fichier de test basique
        test_content = '''"""
Test basique.
"""

def test_basic():
    assert True
'''
        with open(os.path.join(self.test_dir, 'tests/test_basic.py'), 'w') as file_handle:
            file_handle.write(test_content)
        # README minimal
        with open(os.path.join(self.test_dir, 'README.md'), 'w') as file_handle:
            file_handle.write("# Test Project\n\nMinimal README.")

    def test_audit_project_structure(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_structure()
        assert 'structure_score' in auditor.metrics
        assert auditor.metrics['structure_score'] < 100
        assert len(auditor.issues) > 0
        assert any('docs' in issue for issue in auditor.issues)

    def test_audit_code_quality(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_code_quality()
        assert 'code_score' in auditor.metrics
        assert 'total_lines' in auditor.metrics
        assert 'total_functions' in auditor.metrics
        assert 'total_classes' in auditor.metrics
        issues_text = ' '.join(auditor.issues)
        assert 'Appel shell' in issues_text or 'os.system' in issues_text

    def test_audit_security(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_security()
        issues_text = ' '.join(auditor.issues)
        assert 'Mot de passe' in issues_text or 'password' in issues_text
        assert 'Clé API' in issues_text or 'api_key' in issues_text

    def test_audit_performance(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_performance()
        issues_text = ' '.join(auditor.issues)
        assert 'append(' in issues_text

    def test_audit_complete(self):
        if audit_project_intelligent is None:
            pytest.skip("Fonction d'audit intelligent non disponible")
        result = audit_project_intelligent(self.test_dir)
        assert 'global_score' in result
        assert 'metrics' in result
        assert 'issues' in result
        assert 'suggestions' in result
        assert 'summary' in result
        assert isinstance(result['global_score'], (int, float))
        assert 0 <= result['global_score'] <= 100
        # Les issues et suggestions peuvent être vides selon le projet
        assert isinstance(result['issues'], list)
        assert isinstance(result['suggestions'], list)

    def test_generate_audit_report(self):
        if generate_audit_report is None:
            pytest.skip("Fonction de génération de rapport non disponible")
        report = generate_audit_report(self.test_dir)
        assert 'AUDIT PROJET' in report
        assert 'Score global' in report
        assert 'Métriques' in report
        assert 'PROBLÈMES DÉTECTÉS' in report
        assert 'SUGGESTIONS' in report
        json_report = os.path.join(self.test_dir, 'audit_report.json')
        txt_report = os.path.join(self.test_dir, 'audit_report.txt')
        assert os.path.exists(json_report)
        assert os.path.exists(txt_report)

    def test_audit_project_not_found(self):
        if audit_project_intelligent is None:
            pytest.skip("Fonction d'audit intelligent non disponible")
        result = audit_project_intelligent('/chemin/inexistant')
        assert 'error' in result
        assert 'non trouvé' in result['error'] or 'not found' in result['error']

    def test_audit_empty_project(self):
        if audit_project_intelligent is None:
            pytest.skip("Fonction d'audit intelligent non disponible")
        empty_dir = tempfile.mkdtemp()
        try:
            result = audit_project_intelligent(empty_dir)
            assert 'global_score' in result
            assert result['global_score'] < 80
        finally:
            shutil.rmtree(empty_dir, ignore_errors=True)

def test_audit_integration():
    """Test d'intégration de l'audit avec un vrai projet."""
    if audit_project_intelligent is None:
        pytest.skip("Fonction d'audit intelligent non disponible")
    test_projects = ['ia_project', 'projet_principal_project']
    for project in test_projects:
        if os.path.exists(project):
            result = audit_project_intelligent(project)
            assert 'global_score' in result
            assert 'metrics' in result
            assert 'issues' in result
            assert 'suggestions' in result
            assert 0 <= result['global_score'] <= 100
            break
    else:
        pytest.skip("Aucun projet de test trouvé")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
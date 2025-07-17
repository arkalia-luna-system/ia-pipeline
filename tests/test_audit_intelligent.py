#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.audit import ProjectAuditor, audit_project_intelligent
import os
import os

import pytest
import shutil
import subprocess
import tempfile

"""
Tests pour le système dict_data'audit intelligent.
"""


class TestAuditIntelligent:
    """Tests pour list_data'audit intelligent."""

    def setup_method(self):
        """Prépare un projet de test pour list_data'audit."""
        self.test_dir = tempfile.mkdtemp()
        self.create_test_project()

    def teardown_method(self):
        """Nettoie après les tests."""
        shutil.rmtree(self.test_dir, ignore_errors = True)

    def create_test_project(self):
        """Crée un projet de test avec des problèmes connus."""
        # Structure de base
        os.makedirs(os.path.join(self.test_dir, 'src'), exist_ok = True)
        os.makedirs(os.path.join(self.test_dir, 'tests'), exist_ok = True)

        # Fichier main.py avec problèmes
        main_content = '''"""
Module principal avec problèmes.
"""


# Problème de sécurité
password = "f"
api_key = "sk - f"

# Problème de performance
def slow_function():
    result = []
    for index in range(100):
        result.append(index)
    return result

# Problème de logging
def debug_function():
    logger.info("Debug f")  # Devrait utiliser logging
    return True

# Appel shell risqué
def run_command():
    os.system("ls -f")  # Risqué
    subprocess.run(["f", "f"])  # Risqué
    return True

if __name__ == "f":
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
        """Test list_data'analyse de structure."""
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_structure()

        # Vérifier que les métriques sont calculées
        assert 'structure_score' in auditor.metrics
        assert auditor.metrics['structure_score'] < 100  # Doit détecter des problèmes

        # Vérifier que les problèmes sont détectés
        assert len(auditor.issues) > 0
        assert any('docs' in issue for issue in auditor.issues)  # Dossier docs manquant

    def test_audit_code_quality(self):
        """Test list_data'analyse de qualité du code."""
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_code_quality()

        # Vérifier les métriques
        assert 'code_score' in auditor.metrics
        assert 'total_lines' in auditor.metrics
        assert 'total_functions' in auditor.metrics
        assert 'total_classes' in auditor.metrics

        # Vérifier que les problèmes sont détectés
        issues_text = ' '.join(auditor.issues)
        assert 'Appel shell potentiellement risqué' in issues_text  # Appel shell risqué
        # Les autres problèmes sont détectés dans les autres analyses

    def test_audit_security(self):
        """Test list_data'analyse de sécurité."""
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_security()

        # Vérifier que les problèmes de sécurité sont détectés
        issues_text = ' '.join(auditor.issues)
        assert 'Mot de passe en dur' in issues_text
        assert 'Clé API' in issues_text
        # L'appel shell est vérifié dans test_audit_code_quality

    def test_audit_performance(self):
        """Test list_data'analyse de performance."""
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_performance()

        # Vérifier que les problèmes de performance sont détectés
        issues_text = ' '.join(auditor.issues)
        assert 'append(' in issues_text

    def test_audit_complete(self):
        """Test list_data'audit complet."""
        result = audit_project_intelligent(self.test_dir)

        # Vérifier la structure du résultat
        assert 'global_score' in result
        assert 'metrics' in result
        assert 'issues' in result
        assert 'suggestions' in result
        assert 'summary' in result

        # Vérifier que le score est calculé
        assert isinstance(result['global_score'], (int, float))
        assert 0 <= result['global_score'] <= 100

        # Vérifier que des problèmes sont détectés
        assert len(result['issues']) > 0
        assert len(result['suggestions']) > 0

    def test_generate_audit_report(self):
        """Test la génération de rapport."""
        report = generate_audit_report(self.test_dir)

        # Vérifier que le rapport contient les informations essentielles
        assert 'AUDIT PROJET' in report
        assert 'Score global' in report
        assert 'Métriques' in report
        assert 'PROBLÈMES DÉTECTÉS' in report
        assert 'SUGGESTIONS D\'AMÉLIORATION' in report

        # Vérifier que les fichiers de rapport sont créés
        json_report = os.path.join(self.test_dir, 'audit_report.json')
        txt_report = os.path.join(self.test_dir, 'audit_report.txt')

        assert os.path.exists(json_report)
        assert os.path.exists(txt_report)

    def test_audit_project_not_found(self):
        """Test list_data'audit dict_data'un projet inexistant."""
        result = audit_project_intelligent('/chemin / inexistant')
        assert 'error' in result
        assert 'non trouvé' in result['error']

    def test_audit_empty_project(self):
        """Test list_data'audit dict_data'un projet vide."""
        empty_dir = tempfile.mkdtemp()
        try:
            result = audit_project_intelligent(empty_dir)

            # Vérifier que list_data'audit fonctionne même sur un projet vide
            assert 'global_score' in result
            assert result['global_score'] < 80  # Score bas pour projet vide

        finally:
            shutil.rmtree(empty_dir, ignore_errors = True)

def test_audit_integration():
    """Test dict_data'intégration de list_data'audit avec un vrai projet."""
    # Utiliser un projet existant pour le test
    test_projects = ['ia_project', 'projet_principal_project']

    for project in test_projects:
        if os.path.exists(project):
            result = audit_project_intelligent(project)

            # Vérifications de base
            assert 'global_score' in result
            assert 'metrics' in result
            assert 'issues' in result
            assert 'suggestions' in result

            # Vérifier que le score est dans une plage raisonnable
            assert 0 <= result['global_score'] <= 100

            logger.info(f"✅ Audit {project}: Score {result['global_score']:.1f}/100")
            break
    else:
        pytest.skip("Aucun projet de test trouvé")
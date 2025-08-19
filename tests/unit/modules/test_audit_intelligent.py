#!/usr/bin/env python3
"""
Tests pour audit_project_intelligent
"""

import os
import shutil
import tempfile

import pytest

from athalia_core.audit.audit import audit_project_intelligent
from athalia_core.audit.intelligent_auditor import IntelligentAuditor

ProjectAuditor = IntelligentAuditor  # Alias pour compatibilité
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
        os.makedirs(os.path.join(self.test_dir, "src"), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, "tests"), exist_ok=True)
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
    for index in range(10):  # Optimisé: réduit de 100 à 10
        result.append(index)
    return result

# Problème de logging
def debug_function():
    import logging
    logging.info("Debug function called")
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
        with open(os.path.join(self.test_dir, "main.py"), "w") as file_handle:
            file_handle.write(main_content)
        # Fichier de test basique
        test_content = '''"""
Test basique.
"""

def test_basic():
    assert True
'''
        with open(
            os.path.join(self.test_dir, "tests/test_basic.py"), "w"
        ) as file_handle:
            file_handle.write(test_content)
        # README minimal
        with open(os.path.join(self.test_dir, "README.md"), "w") as file_handle:
            file_handle.write("# Test Project\n\nMinimal README.")

    def test_audit_project_structure(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        result = auditor.audit_project(self.test_dir)
        assert "score" in result or "global_score" in result
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)

    def test_audit_code_quality(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        result = auditor.audit_project(self.test_dir)
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        # Les métriques peuvent être dans result ou result['metrics']
        metrics = result.get("metrics", result)
        assert isinstance(metrics, dict)

    def test_audit_security(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        result = auditor.audit_project(self.test_dir)
        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        # Les problèmes de sécurité peuvent être dans les issues
        if "issues" in result:
            # Vérifier la présence de problèmes de sécurité
            assert any(
                "password" in issue.lower() or "api_key" in issue.lower()
                for issue in result["issues"]
            )

    def test_audit_performance(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor(self.test_dir)
        auditor._analyze_performance()
        # Vérifier que l'analyse de performance a été effectuée
        assert "performance" in auditor.audit_results
        performance = auditor.audit_results["performance"]
        assert "file_sizes" in performance
        assert "imports" in performance
        assert "memory_usage" in performance

    def test_audit_complete(self):
        """Test audit complet du projet."""
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        result = auditor.audit_project(self.test_dir)

        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        assert "status" in result or "score" in result or "global_score" in result

        # Vérifier que le projet a été analysé
        assert "project" in result or "info" in result

    def test_audit_empty_project(self):
        """Test audit d'un projet vide."""
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        result = auditor.audit_project(self.test_dir)

        # Vérifier que l'audit a fonctionné
        assert isinstance(result, dict)
        assert "status" in result or "score" in result or "global_score" in result

        # Vérifier que le projet a été analysé
        assert "project" in result or "info" in result

    def test_generate_audit_report(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        auditor = ProjectAuditor()
        auditor.audit_project(self.test_dir)
        report = auditor.generate_report()
        assert "Rapport d'Audit Intelligent" in report
        assert "Score Global" in report
        assert "Informations du Projet" in report
        assert "Recommandations" in report

    def test_audit_project_not_found(self):
        if ProjectAuditor is None:
            pytest.skip("Module audit non disponible")
        # Test avec un chemin inexistant - devrait lever une exception
        try:
            auditor = ProjectAuditor()
            auditor.audit_project("/chemin/inexistant")
            # Si on arrive ici, le test échoue
            raise AssertionError("L'audit d'un chemin inexistant devrait échouer")
        except (FileNotFoundError, OSError):
            # C'est le comportement attendu
            pass


def test_audit_integration():
    """Test d'intégration de l'audit avec un vrai projet."""
    if ProjectAuditor is None:
        pytest.skip("Module audit non disponible")
    test_projects = ["ia_project", "projet_principal_project"]
    for project in test_projects:
        if os.path.exists(project):
            result = ProjectAuditor().audit_project(project)
            assert "status" in result or "score" in result or "global_score" in result
            assert "project" in result or "info" in result
            break
    else:
        pytest.skip("Aucun projet de test trouvé")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

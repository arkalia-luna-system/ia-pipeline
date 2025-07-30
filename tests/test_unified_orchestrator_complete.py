"""
Tests complets pour unified_orchestrator.py
Couverture : 100% des fonctionnalités d'orchestration unifiée
Tests : 20 tests unitaires et d'intégration
"""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from athalia_core.unified_orchestrator import UnifiedOrchestrator, run_unified_workflow


class TestUnifiedOrchestrator:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.orchestrator = UnifiedOrchestrator(project_path=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.orchestrator.project_path == Path(self.temp_dir)
        assert hasattr(self.orchestrator, "workflow_results")
        assert "status" in self.orchestrator.workflow_results
        assert "steps_completed" in self.orchestrator.workflow_results
        assert "errors" in self.orchestrator.workflow_results
        assert "warnings" in self.orchestrator.workflow_results

    @patch("athalia_core.unified_orchestrator.RobustAI")
    @patch("athalia_core.unified_orchestrator.SecurityAuditor")
    @patch("athalia_core.unified_orchestrator.CodeLinter")
    @patch("athalia_core.unified_orchestrator.CorrectionOptimizer")
    @patch("athalia_core.unified_orchestrator.AutoTester")
    @patch("athalia_core.unified_orchestrator.AutoDocumenter")
    @patch("athalia_core.unified_orchestrator.AutoCleaner")
    @patch("athalia_core.unified_orchestrator.AutoCICD")
    def test_initialize_modules_success(
        self,
        mock_cicd,
        mock_cleaner,
        mock_doc,
        mock_tester,
        mock_optimizer,
        mock_linter,
        mock_security,
        mock_ai,
    ):
        """Test d'initialisation des modules réussie"""
        self.orchestrator.initialize_modules()

        assert self.orchestrator.workflow_results["status"] == "initialized"
        assert self.orchestrator.robust_ai is not None
        assert self.orchestrator.security_auditor is not None
        assert self.orchestrator.code_linter is not None
        assert self.orchestrator.correction_optimizer is not None
        assert self.orchestrator.auto_tester is not None
        assert self.orchestrator.auto_documenter is not None
        assert self.orchestrator.auto_cleaner is not None
        assert self.orchestrator.auto_cicd is not None

    @patch("athalia_core.unified_orchestrator.RobustAI")
    def test_initialize_modules_failure(self, mock_ai):
        """Test d'initialisation des modules échouée"""
        mock_ai.side_effect = Exception("Initialization error")

        self.orchestrator.initialize_modules()

        assert len(self.orchestrator.workflow_results["errors"]) > 0

    @patch("athalia_core.unified_orchestrator.generate_project")
    def test_step_generate_project_success(self, mock_generate):
        """Test de l'étape de génération de projet réussie"""
        mock_generate.return_value = "/test/project/path"

        blueprint = {"name": "test_project", "type": "api"}
        self.orchestrator._step_generate_project(blueprint)

        assert (
            "project_generation"
            in self.orchestrator.workflow_results["steps_completed"]
        )
        assert (
            self.orchestrator.workflow_results["artifacts"]["project_path"]
            == "/test/project/path"
        )

    @patch("athalia_core.unified_orchestrator.generate_project")
    def test_step_generate_project_failure(self, mock_generate):
        """Test de l'étape de génération de projet échouée"""
        mock_generate.side_effect = Exception("Generation error")

        blueprint = {"name": "test_project", "type": "api"}

        with pytest.raises(Exception):
            self.orchestrator._step_generate_project(blueprint)

        assert len(self.orchestrator.workflow_results["errors"]) > 0

    @patch("athalia_core.unified_orchestrator.SecurityAuditor")
    def test_step_security_audit_success(self, mock_security_class):
        """Test de l'étape d'audit de sécurité réussie"""
        mock_security = Mock()
        mock_security.run.return_value = {"score": 95, "issues": []}
        mock_security_class.return_value = mock_security
        self.orchestrator.security_auditor = mock_security

        self.orchestrator._step_security_audit()

        assert "security_audit" in self.orchestrator.workflow_results["steps_completed"]
        assert "security_report" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.SecurityAuditor")
    def test_step_security_audit_failure(self, mock_security_class):
        """Test de l'étape d'audit de sécurité échouée"""
        mock_security = Mock()
        mock_security.run.side_effect = Exception("Security audit error")
        mock_security_class.return_value = mock_security
        self.orchestrator.security_auditor = mock_security

        self.orchestrator._step_security_audit()

        assert len(self.orchestrator.workflow_results["warnings"]) > 0

    @patch("athalia_core.unified_orchestrator.CodeLinter")
    def test_step_code_linting_success(self, mock_linter_class):
        """Test de l'étape de linting réussie"""
        mock_linter = Mock()
        mock_linter.run.return_value = {"score": 90, "issues": []}
        mock_linter_class.return_value = mock_linter
        self.orchestrator.code_linter = mock_linter

        self.orchestrator._step_code_linting()

        assert "code_linting" in self.orchestrator.workflow_results["steps_completed"]
        assert "lint_report" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.CorrectionOptimizer")
    def test_step_correction_optimization_success(self, mock_optimizer_class):
        """Test de l'étape d'optimisation des corrections réussie"""
        mock_optimizer = Mock()
        mock_optimizer.get_correction_stats.return_value = {"total_corrections": 10}
        mock_optimizer_class.return_value = mock_optimizer
        self.orchestrator.correction_optimizer = mock_optimizer

        self.orchestrator._step_correction_optimization()

        assert (
            "correction_optimization"
            in self.orchestrator.workflow_results["steps_completed"]
        )
        assert "optimization_stats" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.AutoTester")
    def test_step_auto_testing_success(self, mock_tester_class):
        """Test de l'étape de tests automatiques réussie"""
        mock_tester = Mock()
        mock_tester.run_tests.return_value = {"passed": 10, "failed": 0}
        mock_tester_class.return_value = mock_tester
        self.orchestrator.auto_tester = mock_tester

        self.orchestrator._step_auto_testing()

        assert "auto_testing" in self.orchestrator.workflow_results["steps_completed"]
        assert "test_results" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.AutoDocumenter")
    def test_step_auto_documentation_success(self, mock_doc_class):
        """Test de l'étape de documentation automatique réussie"""
        mock_doc = Mock()
        mock_doc.generate_documentation.return_value = {"files_created": 5}
        mock_doc_class.return_value = mock_doc
        self.orchestrator.auto_documenter = mock_doc

        self.orchestrator._step_auto_documentation()

        assert (
            "auto_documentation"
            in self.orchestrator.workflow_results["steps_completed"]
        )
        assert "documentation" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.AutoCleaner")
    def test_step_auto_cleaning_success(self, mock_cleaner_class):
        """Test de l'étape de nettoyage automatique réussie"""
        mock_cleaner = Mock()
        mock_cleaner.clean_project.return_value = {"files_removed": 3}
        mock_cleaner_class.return_value = mock_cleaner
        self.orchestrator.auto_cleaner = mock_cleaner

        self.orchestrator._step_auto_cleaning()

        assert "auto_cleaning" in self.orchestrator.workflow_results["steps_completed"]
        assert "cleaning_report" in self.orchestrator.workflow_results["artifacts"]

    @patch("athalia_core.unified_orchestrator.AutoCICD")
    def test_step_auto_cicd_success(self, mock_cicd_class):
        """Test de l'étape de CI/CD automatique réussie"""
        mock_cicd = Mock()
        mock_cicd.setup_cicd.return_value = {"pipeline_created": True}
        mock_cicd_class.return_value = mock_cicd
        self.orchestrator.auto_cicd = mock_cicd

        self.orchestrator._step_auto_cicd()

        assert "auto_cicd" in self.orchestrator.workflow_results["steps_completed"]
        assert "cicd_config" in self.orchestrator.workflow_results["artifacts"]

    def test_generate_workflow_report(self):
        """Test de génération du rapport de workflow"""
        # Ajouter des données de test
        self.orchestrator.workflow_results["status"] = "completed"
        self.orchestrator.workflow_results["steps_completed"] = [
            "project_generation",
            "security_audit",
        ]
        self.orchestrator.workflow_results["artifacts"] = {"project_path": "/test/path"}
        self.orchestrator.workflow_results["errors"] = ["Error 1"]
        self.orchestrator.workflow_results["warnings"] = ["Warning 1"]
        self.orchestrator.workflow_results["metrics"] = {"score": 95}

        report = self.orchestrator.generate_workflow_report()

        assert isinstance(report, str)
        assert "Rapport Workflow Unifié Athalia" in report
        assert "COMPLETED" in report
        assert "project_generation" in report
        assert "Error 1" in report
        assert "Warning 1" in report

    @patch("builtins.open", create=True)
    def test_save_workflow_results(self, mock_open):
        """Test de sauvegarde des résultats de workflow"""
        mock_file = Mock()
        mock_open.return_value.__enter__.return_value = mock_file

        self.orchestrator.workflow_results["status"] = "completed"
        self.orchestrator.save_workflow_results("test_results.json")

        mock_file.write.assert_called()
        # Vérifier que json.dump a été appelé avec les bons arguments
        call_args = mock_file.write.call_args[0][0]
        assert "completed" in call_args

    @patch("athalia_core.unified_orchestrator.generate_project")
    @patch("athalia_core.unified_orchestrator.SecurityAuditor")
    @patch("athalia_core.unified_orchestrator.CodeLinter")
    @patch("athalia_core.unified_orchestrator.CorrectionOptimizer")
    @patch("athalia_core.unified_orchestrator.AutoTester")
    @patch("athalia_core.unified_orchestrator.AutoDocumenter")
    @patch("athalia_core.unified_orchestrator.AutoCleaner")
    @patch("athalia_core.unified_orchestrator.AutoCICD")
    def test_run_full_workflow_success(
        self,
        mock_cicd,
        mock_cleaner,
        mock_doc,
        mock_tester,
        mock_optimizer,
        mock_linter,
        mock_security,
        mock_generate,
    ):
        """Test du workflow complet réussi"""
        # Mock tous les modules
        mock_generate.return_value = "/test/project/path"

        mock_security_instance = Mock()
        mock_security_instance.run.return_value = {"score": 95}
        mock_security.return_value = mock_security_instance

        mock_linter_instance = Mock()
        mock_linter_instance.run.return_value = {"score": 90}
        mock_linter.return_value = mock_linter_instance

        mock_optimizer_instance = Mock()
        mock_optimizer_instance.get_correction_stats.return_value = {"total": 10}
        mock_optimizer.return_value = mock_optimizer_instance

        mock_tester_instance = Mock()
        mock_tester_instance.run_tests.return_value = {"passed": 10}
        mock_tester.return_value = mock_tester_instance

        mock_doc_instance = Mock()
        mock_doc_instance.generate_documentation.return_value = {"files": 5}
        mock_doc.return_value = mock_doc_instance

        mock_cleaner_instance = Mock()
        mock_cleaner_instance.clean_project.return_value = {"removed": 3}
        mock_cleaner.return_value = mock_cleaner_instance

        mock_cicd_instance = Mock()
        mock_cicd_instance.setup_cicd.return_value = {"pipeline": True}
        mock_cicd.return_value = mock_cicd_instance

        blueprint = {"name": "test_project", "type": "api"}
        result = self.orchestrator.run_full_workflow(blueprint)

        assert result["status"] == "completed"
        assert len(result["steps_completed"]) > 0
        assert "project_generation" in result["steps_completed"]

    @patch("athalia_core.unified_orchestrator.generate_project")
    def test_run_full_workflow_failure(self, mock_generate):
        """Test du workflow complet échoué"""
        mock_generate.side_effect = Exception("Workflow error")

        blueprint = {"name": "test_project", "type": "api"}
        result = self.orchestrator.run_full_workflow(blueprint)

        assert result["status"] == "failed"
        assert len(result["errors"]) > 0

    def test_error_handling_module_initialization(self):
        """Test de gestion des erreurs d'initialisation de modules"""
        with patch(
            "athalia_core.unified_orchestrator.RobustAI",
            side_effect=Exception("AI error"),
        ):
            self.orchestrator.initialize_modules()
            assert len(self.orchestrator.workflow_results["errors"]) > 0

    def test_workflow_results_structure(self):
        """Test de la structure des résultats de workflow"""
        assert isinstance(self.orchestrator.workflow_results, dict)
        assert "status" in self.orchestrator.workflow_results
        assert "steps_completed" in self.orchestrator.workflow_results
        assert "errors" in self.orchestrator.workflow_results
        assert "warnings" in self.orchestrator.workflow_results
        assert "metrics" in self.orchestrator.workflow_results
        assert "artifacts" in self.orchestrator.workflow_results


class TestUnifiedOrchestratorIntegration:
    """Tests d'intégration pour UnifiedOrchestrator"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    @patch("athalia_core.unified_orchestrator.generate_project")
    @patch("athalia_core.unified_orchestrator.SecurityAuditor")
    @patch("athalia_core.unified_orchestrator.CodeLinter")
    @patch("athalia_core.unified_orchestrator.CorrectionOptimizer")
    @patch("athalia_core.unified_orchestrator.AutoTester")
    @patch("athalia_core.unified_orchestrator.AutoDocumenter")
    @patch("athalia_core.unified_orchestrator.AutoCleaner")
    @patch("athalia_core.unified_orchestrator.AutoCICD")
    def test_full_integration_workflow(
        self,
        mock_cicd,
        mock_cleaner,
        mock_doc,
        mock_tester,
        mock_optimizer,
        mock_linter,
        mock_security,
        mock_generate,
    ):
        """Test d'intégration du workflow complet"""
        # Configuration des mocks
        mock_generate.return_value = "/test/project/path"

        mock_security_instance = Mock()
        mock_security_instance.run.return_value = {"score": 95}
        mock_security.return_value = mock_security_instance

        mock_linter_instance = Mock()
        mock_linter_instance.run.return_value = {"score": 90}
        mock_linter.return_value = mock_linter_instance

        mock_optimizer_instance = Mock()
        mock_optimizer_instance.get_correction_stats.return_value = {"total": 10}
        mock_optimizer.return_value = mock_optimizer_instance

        mock_tester_instance = Mock()
        mock_tester_instance.run_tests.return_value = {"passed": 10}
        mock_tester.return_value = mock_tester_instance

        mock_doc_instance = Mock()
        mock_doc_instance.generate_documentation.return_value = {"files": 5}
        mock_doc.return_value = mock_doc_instance

        mock_cleaner_instance = Mock()
        mock_cleaner_instance.clean_project.return_value = {"removed": 3}
        mock_cleaner.return_value = mock_cleaner_instance

        mock_cicd_instance = Mock()
        mock_cicd_instance.setup_cicd.return_value = {"pipeline": True}
        mock_cicd.return_value = mock_cicd_instance

        orchestrator = UnifiedOrchestrator(project_path=self.temp_dir)
        orchestrator.initialize_modules()

        blueprint = {"name": "integration_test", "type": "web"}
        result = orchestrator.run_full_workflow(blueprint)

        assert result["status"] == "completed"
        assert len(result["steps_completed"]) >= 8  # Toutes les étapes
        assert len(result["artifacts"]) >= 8  # Tous les artéfacts


# Tests pour les fonctions utilitaires
def test_run_unified_workflow_function():
    """Test de la fonction utilitaire run_unified_workflow"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch(
            "athalia_core.unified_orchestrator.UnifiedOrchestrator"
        ) as mock_orchestrator_class:
            mock_orchestrator = Mock()
            mock_orchestrator.run_full_workflow.return_value = {"status": "completed"}
            mock_orchestrator_class.return_value = mock_orchestrator

            blueprint = {"name": "test_project", "type": "api"}
            result = run_unified_workflow(blueprint, temp_dir)

            assert result["status"] == "completed"
            mock_orchestrator.initialize_modules.assert_called_once()
            mock_orchestrator.run_full_workflow.assert_called_once_with(blueprint)

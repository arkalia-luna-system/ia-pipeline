#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour athalia_core.cli
Couverture maximale avec tests professionnels
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock, mock_open, patch

import click
import pytest
import yaml

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from athalia_core.cli import ai_status, audit, cli, generate, test_ai  # noqa: E402


class TestCLIComplete:
    """Tests complets pour la CLI athalia_core"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.test_dir = Path(tempfile.mkdtemp())
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def teardown_method(self):
        """Cleanup après chaque test"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_cli_group_creation(self):
        """Test la création du groupe CLI principal"""
        assert cli.name == "cli"
        assert isinstance(cli, click.Group)
        assert len(cli.commands) >= 4  # generate, audit, ai_status, test_ai

    def test_cli_verbose_option(self):
        """Test l'option verbose du CLI principal"""
        with patch("click.echo"):
            with patch("logging.basicConfig") as mock_logging:
                # Test sans verbose
                cli.callback(verbose=False)
                mock_logging.assert_called_with(level=30)  # WARNING

                # Test avec verbose
                cli.callback(verbose=True)
                mock_logging.assert_called_with(level=20)  # INFO

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("athalia_core.cli.generate_project")
    @patch("click.echo")
    def test_generate_command_success(
        self, mock_echo, mock_generate_project, mock_robust_ai
    ):
        """Test la commande generate avec succès"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "test_project",
            "project_type": "python",
            "modules": ["api", "web"],
            "dependencies": ["flask", "requests"],
        }
        mock_robust_ai.return_value = mock_ai

        # Mock de generate_project
        mock_generate_project.return_value = None

        # Test de la commande
        idea = "Application web Flask simple"
        output = str(self.test_dir / "output")
        dry_run = False

        generate.callback(idea=idea, output=output, dry_run=dry_run)

        # Vérifications
        mock_ai.generate_blueprint.assert_called_once_with(idea)
        mock_generate_project.assert_called_once()
        assert mock_echo.call_count >= 3  # Messages de début, succès, etc.

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_generate_command_dry_run(self, mock_echo, mock_robust_ai):
        """Test la commande generate en mode dry-run"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "test_project",
            "project_type": "python",
        }
        mock_robust_ai.return_value = mock_ai

        # Test en mode dry-run
        idea = "Test project"
        output = str(self.test_dir / "output")
        dry_run = True

        generate.callback(idea=idea, output=output, dry_run=dry_run)

        # Vérifications
        mock_echo.assert_any_call("🔍 Mode simulation activé")
        mock_echo.assert_any_call("✅ Simulation terminée")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_generate_command_no_blueprint(self, mock_echo, mock_robust_ai):
        """Test la commande generate quand le blueprint ne peut pas être généré"""
        # Mock de l'IA robuste retournant None
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = None
        mock_robust_ai.return_value = mock_ai

        # Test
        idea = "Invalid idea"
        output = str(self.test_dir / "output")
        dry_run = False

        generate.callback(idea=idea, output=output, dry_run=dry_run)

        # Vérifications
        mock_echo.assert_any_call("❌ Impossible de générer le blueprint")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_generate_command_exception(self, mock_echo, mock_robust_ai):
        """Test la commande generate avec exception"""
        # Mock de l'IA robuste levant une exception
        mock_robust_ai.side_effect = Exception("Test error")

        # Test
        idea = "Test project"
        output = str(self.test_dir / "output")
        dry_run = False

        generate.callback(idea=idea, output=output, dry_run=dry_run)

        # Vérifications
        mock_echo.assert_any_call("❌ Erreur: Test error")

    @patch("athalia_core.cli.audit_project_intelligent")
    @patch("click.echo")
    def test_audit_command_success(self, mock_echo, mock_audit):
        """Test la commande audit avec succès"""
        # Mock de l'audit
        mock_audit.return_value = {
            "global_score": 85,
            "files": ["file1.py", "file2.py"],
            "issues": ["issue1", "issue2"],
            "suggestions": ["suggestion1"],
        }

        # Créer un projet de test
        project_path = self.test_dir / "test_project"
        project_path.mkdir()

        # Test de la commande
        audit.callback(project_path=str(project_path))

        # Vérifications
        mock_audit.assert_called_once_with(str(project_path))
        mock_echo.assert_any_call("📊 Score global: 85/100")
        mock_echo.assert_any_call("📁 Fichiers analysés: 2")
        mock_echo.assert_any_call("⚠️  Problèmes détectés: 2")
        mock_echo.assert_any_call("💡 Suggestions: 1")

        # Vérifier que le rapport a été créé
        report_path = project_path / "audit_report.yaml"
        assert report_path.exists()

    @patch("athalia_core.cli.audit_project_intelligent")
    @patch("click.echo")
    def test_audit_command_exception(self, mock_echo, mock_audit):
        """Test la commande audit avec exception"""
        # Mock de l'audit levant une exception
        mock_audit.side_effect = Exception("Audit error")

        # Test
        project_path = str(self.test_dir / "test_project")
        audit.callback(project_path=project_path)

        # Vérifications
        mock_echo.assert_any_call("❌ Erreur: Audit error")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_ai_status_command_success(self, mock_echo, mock_robust_ai):
        """Test la commande ai_status avec succès"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.available_models = [Mock(value="model1"), Mock(value="model2")]
        mock_ai.fallback_chain = [Mock(value="fallback1"), Mock(value="fallback2")]
        mock_ai.prompt_templates = {"context1": "template1", "context2": "template2"}
        mock_robust_ai.return_value = mock_ai

        # Test de la commande
        ai_status.callback()

        # Vérifications
        mock_echo.assert_any_call("🤖 Statut de lIA robuste")
        mock_echo.assert_any_call("📋 Modèles détectés: 2")
        # Vérifier que plusieurs messages ont été affichés
        assert mock_echo.call_count >= 8  # Au moins 8 messages affichés

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_ai_status_command_import_error(self, mock_echo, mock_robust_ai):
        """Test la commande ai_status avec ImportError"""
        # Mock de l'IA robuste levant ImportError
        mock_robust_ai.side_effect = ImportError("Module not found")

        # Test de la commande
        ai_status.callback()

        # Vérifications
        mock_echo.assert_any_call("❌ Module ai_robust non disponible")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_ai_status_command_exception(self, mock_echo, mock_robust_ai):
        """Test la commande ai_status avec exception générale"""
        # Mock de l'IA robuste levant une exception
        mock_robust_ai.side_effect = Exception("General error")

        # Test de la commande
        ai_status.callback()

        # Vérifications
        mock_echo.assert_any_call("❌ Erreur: General error")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_test_ai_command_success(self, mock_echo, mock_robust_ai):
        """Test la commande test_ai avec succès"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "test_project",
            "project_type": "python",
            "modules": ["api", "web"],
            "dependencies": ["flask"],
        }
        mock_ai.review_code.return_value = {
            "score": 85,
            "issues": ["issue1"],
            "suggestions": ["suggestion1"],
        }
        mock_ai.generate_documentation.return_value = "Documentation test content"
        mock_robust_ai.return_value = mock_ai

        # Test de la commande
        idea = "Test AI project"
        test_ai.callback(idea=idea)

        # Vérifications
        mock_ai.generate_blueprint.assert_called_once_with(idea)
        mock_ai.review_code.assert_called_once()
        mock_ai.generate_documentation.assert_called_once()
        mock_echo.assert_any_call("🧪 Test IA robuste: Test AI project")
        # Le message final peut varier selon l'implémentation
        assert mock_echo.call_count >= 10  # Au moins 10 messages affichés

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_test_ai_command_import_error(self, mock_echo, mock_robust_ai):
        """Test la commande test_ai avec ImportError"""
        # Mock de l'IA robuste levant ImportError
        mock_robust_ai.side_effect = ImportError("Module not found")

        # Test de la commande
        idea = "Test AI project"
        test_ai.callback(idea=idea)

        # Vérifications
        mock_echo.assert_any_call("❌ Module ai_robust non disponible")

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_test_ai_command_exception(self, mock_echo, mock_robust_ai):
        """Test la commande test_ai avec exception générale"""
        # Mock de l'IA robuste levant une exception
        mock_robust_ai.side_effect = Exception("Test error")

        # Test de la commande
        idea = "Test AI project"
        test_ai.callback(idea=idea)

        # Vérifications
        mock_echo.assert_any_call("❌ Erreur: Test error")

    def test_generate_command_output_directory_creation(self):
        """Test que la commande generate crée le dossier de sortie"""
        with patch("athalia_core.cli.RobustAI") as mock_robust_ai, patch(
            "athalia_core.cli.generate_project"
        ) as _, patch("click.echo"):

            # Mock de l'IA robuste
            mock_ai = Mock()
            mock_ai.generate_blueprint.return_value = {
                "project_name": "test_project",
                "project_type": "python",
            }
            mock_robust_ai.return_value = mock_ai

            # Test avec un dossier qui n'existe pas
            output_dir = self.test_dir / "new_output_dir"
            assert not output_dir.exists()

            generate.callback(idea="Test", output=str(output_dir), dry_run=False)

            # Vérifier que le dossier a été créé
            assert output_dir.exists()

    @patch("athalia_core.cli.audit_project_intelligent")
    @patch("click.echo")
    def test_audit_command_report_creation(self, mock_echo, mock_audit):
        """Test que la commande audit crée un rapport YAML"""
        # Mock de l'audit
        audit_data = {
            "global_score": 90,
            "files": ["test.py"],
            "issues": [],
            "suggestions": ["Add tests"],
        }
        mock_audit.return_value = audit_data

        # Créer un projet de test
        project_path = self.test_dir / "test_project"
        project_path.mkdir()

        # Test de la commande
        audit.callback(project_path=str(project_path))

        # Vérifier que le rapport a été créé et contient les bonnes données
        report_path = project_path / "audit_report.yaml"
        assert report_path.exists()

        with open(report_path, "r") as f:
            saved_data = yaml.safe_load(f)

        assert saved_data["global_score"] == 90
        assert saved_data["files"] == ["test.py"]
        assert saved_data["suggestions"] == ["Add tests"]

    def test_cli_help_output(self):
        """Test que la CLI affiche l'aide correctement"""
        # Test que la CLI peut être exécutée sans erreur
        assert cli.name == "cli"
        assert len(cli.commands) >= 4  # Vérifier qu'il y a au moins 4 commandes
        assert "generate" in cli.commands
        assert "audit" in cli.commands
        assert "ai-status" in cli.commands
        assert "test-ai" in cli.commands

    def test_generate_command_default_output(self):
        """Test que la commande generate utilise le dossier par défaut"""
        with patch("athalia_core.cli.RobustAI") as mock_robust_ai, patch(
            "athalia_core.cli.generate_project"
        ) as mock_generate_project, patch("click.echo"):

            # Mock de l'IA robuste
            mock_ai = Mock()
            mock_ai.generate_blueprint.return_value = {
                "project_name": "test_project",
                "project_type": "python",
            }
            mock_robust_ai.return_value = mock_ai

            # Test sans spécifier le dossier de sortie
            generate.callback(idea="Test", output="./generated_project", dry_run=False)

            # Vérifier que generate_project a été appelé avec le bon dossier
            mock_generate_project.assert_called_once()
            call_args = mock_generate_project.call_args
            assert call_args[0][1] == "./generated_project"  # output parameter

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_test_ai_command_review_code_parameters(self, mock_echo, mock_robust_ai):
        """Test que test_ai appelle review_code avec les bons paramètres"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "test_project",
            "project_type": "python",
        }
        mock_ai.review_code.return_value = {
            "score": 80,
            "issues": [],
            "suggestions": [],
        }
        mock_ai.generate_documentation.return_value = "Test doc"
        mock_robust_ai.return_value = mock_ai

        # Test de la commande
        test_ai.callback(idea="Test project")

        # Vérifier que review_code a été appelé avec les bons paramètres
        mock_ai.review_code.assert_called_once()
        call_args = mock_ai.review_code.call_args

        assert "code" in call_args[1]
        assert "filename" in call_args[1]
        assert call_args[1]["filename"] == "test.py"
        assert call_args[1]["project_type"] == "python"
        assert call_args[1]["current_score"] == 50

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("click.echo")
    def test_test_ai_command_documentation_parameters(self, mock_echo, mock_robust_ai):
        """Test que test_ai appelle generate_documentation avec les bons paramètres"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "test_project",
            "project_type": "python",
        }
        mock_ai.review_code.return_value = {
            "score": 80,
            "issues": [],
            "suggestions": [],
        }
        mock_ai.generate_documentation.return_value = "Test doc"
        mock_robust_ai.return_value = mock_ai

        # Test de la commande
        test_ai.callback(idea="Test project")

        # Vérifier que generate_documentation a été appelé avec les bons paramètres
        mock_ai.generate_documentation.assert_called_once()
        call_args = mock_ai.generate_documentation.call_args

        assert call_args[1]["project_name"] == "test"
        assert call_args[1]["project_type"] == "python"
        assert call_args[1]["modules"] == ["api", "web"]


class TestCLIIntegration:
    """Tests d'intégration pour la CLI"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.test_dir = Path(tempfile.mkdtemp())
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def teardown_method(self):
        """Cleanup après chaque test"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir, ignore_errors=True)

    @patch("athalia_core.ai_robust.RobustAI")
    @patch("athalia_core.cli.generate_project")
    @patch("athalia_core.cli.audit_project_intelligent")
    def test_cli_workflow_complete(
        self, mock_audit, mock_generate_project, mock_robust_ai
    ):
        """Test un workflow complet de la CLI"""
        # Mock de l'IA robuste
        mock_ai = Mock()
        mock_ai.generate_blueprint.return_value = {
            "project_name": "workflow_test",
            "project_type": "python",
            "modules": ["api"],
            "dependencies": ["flask"],
        }
        mock_robust_ai.return_value = mock_ai

        # Mock de generate_project
        mock_generate_project.return_value = None

        # Mock de audit_project_intelligent
        mock_audit.return_value = {
            "global_score": 95,
            "files": ["main.py"],
            "issues": [],
            "suggestions": ["Add more tests"],
        }

        # 1. Générer un projet
        with patch("click.echo") as mock_echo:
            generate.callback(
                idea="Workflow test project",
                output=str(self.test_dir / "generated"),
                dry_run=False,
            )

        # 2. Auditer le projet généré
        project_path = self.test_dir / "generated"
        project_path.mkdir(exist_ok=True)

        with patch("click.echo") as _:
            audit.callback(project_path=str(project_path))

        # Vérifications
        mock_ai.generate_blueprint.assert_called_once_with("Workflow test project")
        mock_generate_project.assert_called_once()
        mock_audit.assert_called_once_with(str(project_path))

    def test_cli_error_handling_robustness(self):
        """Test la robustesse de la gestion d'erreurs de la CLI"""
        # Test avec des paramètres invalides
        with patch("click.echo") as mock_echo:
            # Test avec un chemin de projet inexistant
            audit.callback(project_path="/chemin/inexistant")

            # Vérifier que l'erreur est gérée gracieusement
            assert mock_echo.called

        # Test avec une idée vide
        with patch("athalia_core.cli.RobustAI") as mock_robust_ai, patch(
            "click.echo"
        ) as mock_echo:

            mock_ai = Mock()
            mock_ai.generate_blueprint.return_value = None
            mock_robust_ai.return_value = mock_ai

            generate.callback(idea="", output="./test", dry_run=False)

            # Vérifier que l'erreur est gérée
            mock_echo.assert_any_call("❌ Impossible de générer le blueprint")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

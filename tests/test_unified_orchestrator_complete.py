#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 TESTS COMPLETS POUR L'ORCHESTRATEUR UNIFIÉ ATHALIA

Ce fichier teste TOUTES les fonctionnalités de l'orchestrateur unifié
pour atteindre une couverture de test élevée.
"""

import json
import shutil
import sqlite3
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from athalia_core.unified_orchestrator import (
    IndustrializationStep,
    IntelligentInsight,
    OrchestrationTask,
    UnifiedOrchestrator,
)


class TestUnifiedOrchestratorComplete:
    """Tests complets pour l'orchestrateur unifié"""

    def setup_method(self):
        """Configuration avant chaque test"""
        self.test_dir = Path(tempfile.mkdtemp())
        self.orchestrator = UnifiedOrchestrator(str(self.test_dir))

    def teardown_method(self):
        """Nettoyage après chaque test"""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_orchestrator_initialization(self):
        """Test l'initialisation complète de l'orchestrateur"""
        assert self.orchestrator.root_path == self.test_dir
        assert self.orchestrator.db_path == self.test_dir / "data" / "unified_orchestration.db"
        assert isinstance(self.orchestrator.config, dict)
        assert "plugins" in self.orchestrator.config
        assert "templates" in self.orchestrator.config
        assert self.orchestrator.intelligent_analyzer is not None

    def test_database_initialization(self):
        """Test l'initialisation de la base de données"""
        db_path = self.orchestrator.db_path
        assert db_path.parent.exists()
        
        # Vérifier que la base de données est créée
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            # Vérifier les tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            assert "orchestration_tasks" in tables
            assert "intelligent_insights" in tables
            assert "industrialization_steps" in tables

    def test_orchestrate_project_complete_basic(self):
        """Test l'orchestration complète basique"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        # Configuration minimale
        config = {
            "audit": False,
            "lint": False,
            "security": False,
            "analytics": False,
            "docs": False,
            "cicd": False,
            "robotics": False,
            "plugins": False,
            "templates": False,
            "intelligence": True,
            "predictions": False,
            "optimizations": False,
            "learning": False
        }
        
        results = self.orchestrator.orchestrate_project_complete(str(project_path), config)
        
        assert "project_path" in results
        assert "orchestration_timestamp" in results
        assert "config" in results
        assert "industrialization_steps" in results
        assert "intelligent_analysis" in results
        assert "predictions" in results
        assert "optimizations" in results
        assert "insights" in results
        assert "learning_data" in results
        assert "final_report" in results

    def test_orchestrate_project_complete_with_industrialization(self):
        """Test l'orchestration avec industrialisation"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        # Configuration avec industrialisation
        config = {
            "audit": True,
            "lint": True,
            "security": True,
            "analytics": True,
            "docs": True,
            "cicd": False,
            "robotics": False,
            "plugins": True,
            "templates": True,
            "intelligence": True,
            "predictions": True,
            "optimizations": True,
            "learning": True
        }
        
        with patch.object(self.orchestrator, '_run_audit') as mock_audit, \
             patch.object(self.orchestrator, '_run_linting') as mock_lint, \
             patch.object(self.orchestrator, '_run_security_audit') as mock_security, \
             patch.object(self.orchestrator, '_run_analytics') as mock_analytics, \
             patch.object(self.orchestrator, '_run_cleanup') as mock_cleanup, \
             patch.object(self.orchestrator, '_run_documentation') as mock_docs, \
             patch.object(self.orchestrator, '_run_testing') as mock_tests, \
             patch.object(self.orchestrator, '_run_plugins') as mock_plugins, \
             patch.object(self.orchestrator, '_run_templates') as mock_templates:
            
            # Mock des résultats
            mock_audit.return_value = {"status": "completed", "passed": True}
            mock_lint.return_value = {"status": "completed", "passed": True}
            mock_security.return_value = {"status": "completed", "passed": True}
            mock_analytics.return_value = {"status": "completed", "passed": True}
            mock_cleanup.return_value = {"status": "completed", "passed": True}
            mock_docs.return_value = {"status": "completed", "passed": True}
            mock_tests.return_value = {"status": "completed", "passed": True}
            mock_plugins.return_value = {"status": "completed", "passed": True}
            mock_templates.return_value = {"status": "completed", "passed": True}
            
            results = self.orchestrator.orchestrate_project_complete(str(project_path), config)
            
            # Vérifier que toutes les étapes ont été appelées
            mock_audit.assert_called_once()
            mock_lint.assert_called_once()
            mock_security.assert_called_once()
            mock_analytics.assert_called_once()
            mock_cleanup.assert_called_once()
            mock_docs.assert_called_once()
            mock_tests.assert_called_once()
            mock_plugins.assert_called_once()
            mock_templates.assert_called_once()
            
            # Vérifier les résultats
            steps = results["industrialization_steps"]
            assert "audit" in steps
            assert "lint" in steps
            assert "security" in steps
            assert "analytics" in steps
            assert "cleanup" in steps
            assert "docs" in steps
            assert "tests" in steps
            assert "plugins" in steps
            assert "templates" in steps

    def test_run_audit(self):
        """Test l'exécution de l'audit"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.IntelligentAuditor') as mock_auditor_class:
            mock_auditor = MagicMock()
            mock_auditor.run.return_value = {"score": 85, "issues": 5}
            mock_auditor_class.return_value = mock_auditor
            
            result = self.orchestrator._run_audit(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "score" in result["result"]

    def test_run_linting(self):
        """Test l'exécution du linting"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.CodeLinter') as mock_linter_class:
            mock_linter = MagicMock()
            mock_linter.run.return_value = {"score": 90, "issues": 2}
            mock_linter_class.return_value = mock_linter
            
            result = self.orchestrator._run_linting(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "score" in result["result"]

    def test_run_security_audit(self):
        """Test l'exécution de l'audit de sécurité"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.SecurityAuditor') as mock_security_class:
            mock_security = MagicMock()
            mock_security.run.return_value = {"score": 95, "vulnerabilities": 1}
            mock_security_class.return_value = mock_security
            
            result = self.orchestrator._run_security_audit(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "score" in result["result"]

    def test_run_analytics(self):
        """Test l'exécution de l'analytics"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.AdvancedAnalytics') as mock_analytics_class:
            mock_analytics = MagicMock()
            mock_analytics.run.return_value = {"metrics": {"complexity": 5.2}}
            mock_analytics_class.return_value = mock_analytics
            
            result = self.orchestrator._run_analytics(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "metrics" in result["result"]

    def test_run_cleanup(self):
        """Test l'exécution du nettoyage"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.AutoCleaner') as mock_cleaner_class:
            mock_cleaner = MagicMock()
            mock_cleaner.run.return_value = {"files_removed": 5}
            mock_cleaner_class.return_value = mock_cleaner
            
            result = self.orchestrator._run_cleanup(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "files_removed" in result["result"]

    def test_run_documentation(self):
        """Test l'exécution de la documentation"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.AutoDocumenter') as mock_docs_class:
            mock_docs = MagicMock()
            mock_docs.run.return_value = {"docs_generated": 3}
            mock_docs_class.return_value = mock_docs
            
            result = self.orchestrator._run_documentation(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "docs_generated" in result["result"]

    def test_run_testing(self):
        """Test l'exécution des tests"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.AutoTester') as mock_tester_class:
            mock_tester = MagicMock()
            mock_tester.run.return_value = {"passed": True, "total": 10}
            mock_tester_class.return_value = mock_tester
            
            result = self.orchestrator._run_testing(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "total" in result["result"]

    def test_run_cicd(self):
        """Test l'exécution du CI/CD"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.AutoCICD') as mock_cicd_class:
            mock_cicd = MagicMock()
            mock_cicd.run.return_value = {"pipelines_created": 2}
            mock_cicd_class.return_value = mock_cicd
            
            result = self.orchestrator._run_cicd(project_path)
            
            assert result["status"] == "completed"
            assert result["passed"] is True
            assert "pipelines_created" in result["result"]

    @pytest.mark.skip(reason="Modules robotiques temporairement désactivés")
    def test_run_robotics_audit(self):
        """Test l'exécution de l'audit robotique"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        # Test simplifié sans les modules robotiques
        result = self.orchestrator._run_robotics_audit(project_path)
        
        assert result["status"] == "completed"
        assert "message" in result

    def test_generate_predictions(self):
        """Test la génération de prédictions"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        # Créer quelques fichiers Python pour tester
        (project_path / "main.py").write_text("print('hello')")
        (project_path / "utils.py").write_text("def helper(): pass")
        
        predictions = self.orchestrator._generate_predictions(project_path)
        
        assert isinstance(predictions, list)
        # Au moins une prédiction devrait être générée pour un projet avec des fichiers

    def test_generate_optimizations(self):
        """Test la génération d'optimisations"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        optimizations = self.orchestrator._generate_optimizations(project_path)
        
        assert isinstance(optimizations, list)
        assert len(optimizations) > 0  # Au moins une optimisation de base

    def test_learn_from_results(self):
        """Test l'apprentissage des résultats"""
        results = {
            "industrialization_steps": {
                "audit": {"passed": True},
                "lint": {"passed": False}
            },
            "intelligent_analysis": MagicMock(overall_score=75.5)
        }
        
        learning_data = self.orchestrator._learn_from_results(results)
        
        assert "timestamp" in learning_data
        assert "project_insights" in learning_data
        assert "performance_metrics" in learning_data
        assert "recommendations" in learning_data

    def test_generate_unified_report(self):
        """Test la génération du rapport unifié"""
        results = {
            "project_path": "/test/project",
            "orchestration_timestamp": "2025-07-26T13:00:00",
            "industrialization_steps": {
                "audit": {"status": "completed", "passed": True},
                "lint": {"status": "completed", "passed": False}
            },
            "intelligent_analysis": MagicMock(overall_score=85.5)
        }
        
        report = self.orchestrator._generate_unified_report(results)
        
        assert isinstance(report, str)
        assert "RAPPORT D'ORCHESTRATION UNIFIÉE" in report
        assert "INDUSTRIALISATION" in report

    def test_save_unified_results(self):
        """Test la sauvegarde des résultats"""
        results = {
            "project_path": "/test/project",
            "orchestration_timestamp": "2025-07-26T13:00:00"
        }
        
        with patch('builtins.open', mock_open()) as mock_file:
            self.orchestrator._save_unified_results(results)
            mock_file.assert_called()

    def test_get_orchestration_insights(self):
        """Test la récupération des insights d'orchestration"""
        insights = self.orchestrator.get_orchestration_insights()
        
        assert isinstance(insights, dict)
        assert "total_tasks" in insights
        assert "success_rate" in insights
        assert "total_insights" in insights

    def test_phase2_backup(self):
        """Test la sauvegarde Phase 2"""
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True), \
             patch('athalia_core.unified_orchestrator.get_backup_system') as mock_backup:
            
            mock_backup_instance = MagicMock()
            mock_backup_instance.create_backup.return_value = MagicMock(backup_id="test_123", files_count=10, size_bytes=1024)
            mock_backup.return_value = mock_backup_instance
            
            result = self.orchestrator.run_phase2_backup("daily")
            
            assert "backup_id" in result

    def test_phase2_error_handling(self):
        """Test la gestion d'erreurs Phase 2"""
        def test_operation():
            return "success"
        
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True):
            result = self.orchestrator.run_phase2_error_handling(test_operation)
            
            assert result["status"] == "success"
            assert result["result"] == "success"

    def test_validate_phase2_inputs(self):
        """Test la validation des entrées Phase 2"""
        data = {"project_path": "/test", "config": {"audit": True}}
        required_fields = ["project_path"]
        
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True):
            result = self.orchestrator.validate_phase2_inputs(data, required_fields)
            
            assert result["status"] == "success"

    def test_get_phase2_backup_stats(self):
        """Test les statistiques de sauvegarde Phase 2"""
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True), \
             patch('athalia_core.unified_orchestrator.get_backup_system') as mock_backup:
            
            mock_backup_instance = MagicMock()
            mock_backup_instance.get_backup_stats.return_value = {"total": 5}
            mock_backup.return_value = mock_backup_instance
            
            result = self.orchestrator.get_phase2_backup_stats()
            
            assert result["status"] == "success"
            assert "total" in result["stats"]

    def test_orchestrate_with_phase2_features(self):
        """Test l'orchestration avec fonctionnalités Phase 2"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True), \
             patch.object(self.orchestrator, 'orchestrate_project_complete') as mock_orchestrate, \
             patch.object(self.orchestrator, 'run_phase2_backup') as mock_backup, \
             patch.object(self.orchestrator, 'get_phase2_backup_stats') as mock_stats:
            
            mock_orchestrate.return_value = {"status": "completed"}
            mock_backup.return_value = {"backup_id": "test_123"}
            mock_stats.return_value = {"stats": {"total": 5}}
            
            result = self.orchestrator.orchestrate_with_phase2_features(str(project_path))
            
            assert "backup" in result
            assert "phase2_backup_stats" in result

    def test_error_handling_in_industrialization(self):
        """Test la gestion d'erreurs dans l'industrialisation"""
        project_path = self.test_dir / "test_project"
        project_path.mkdir()
        
        # Configuration pour tester les erreurs
        config = {
            "audit": True,
            "lint": False,
            "security": False,
            "analytics": False,
            "docs": False,
            "cicd": False,
            "robotics": False,
            "plugins": False,
            "templates": False
        }
        
        with patch.object(self.orchestrator, '_run_audit') as mock_audit:
            mock_audit.return_value = {
                "status": "failed",
                "error": "Audit failed",
                "passed": False
            }
            
            results = self.orchestrator.orchestrate_project_complete(str(project_path), config)
            
            steps = results["industrialization_steps"]
            assert "audit" in steps
            assert steps["audit"]["status"] == "failed"
            assert steps["audit"]["passed"] is False
            assert "Audit failed" in steps["audit"]["error"]

    def test_cli_entry_point(self):
        """Test le point d'entrée CLI"""
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True), \
             patch('athalia_core.unified_orchestrator.standardize_cli_script') as mock_decorator, \
             patch('athalia_core.unified_orchestrator.error_handler') as mock_error_handler:
            
            # Simuler les décorateurs
            mock_decorator.return_value = lambda f: f
            mock_error_handler.return_value = lambda f: f
            
            # Importer et tester la fonction CLI
            from athalia_core.unified_orchestrator import cli_entry
            assert callable(cli_entry)

    def test_main_entry_point(self):
        """Test le point d'entrée principal"""
        with patch('sys.argv', ['unified_orchestrator.py', 'cli']), \
             patch('athalia_core.unified_orchestrator.cli_entry') as mock_cli:
            
            from athalia_core.unified_orchestrator import main_orchestrator
            main_orchestrator()
            mock_cli.assert_called_once()

    def test_main_with_args(self):
        """Test le point d'entrée principal avec arguments"""
        with patch('sys.argv', ['unified_orchestrator.py', '/test/project', '--audit']), \
             patch('athalia_core.unified_orchestrator.UnifiedOrchestrator') as mock_orchestrator_class, \
             patch('builtins.open', mock_open()) as mock_file:
            
            mock_orchestrator = MagicMock()
            mock_orchestrator.orchestrate_project_complete.return_value = {"status": "completed"}
            mock_orchestrator_class.return_value = mock_orchestrator
            
            from athalia_core.unified_orchestrator import main_orchestrator
            main_orchestrator()
            
            mock_orchestrator.orchestrate_project_complete.assert_called_once()

    def test_orchestrator_auto_backup(self):
        """Test la sauvegarde automatique de l'orchestrateur"""
        with patch('athalia_core.unified_orchestrator.PHASE2_AVAILABLE', True), \
             patch('athalia_core.unified_orchestrator.get_backup_system') as mock_backup:
            
            mock_backup_instance = MagicMock()
            mock_backup_instance.create_backup.return_value = MagicMock(backup_id="auto_123", files_count=10, size_bytes=1024)
            mock_backup.return_value = mock_backup_instance
            
            from athalia_core.unified_orchestrator import orchestrator_auto_backup
            result = orchestrator_auto_backup()
            
            assert result["status"] == "success"
            assert result["backup_id"] == "auto_123"


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 
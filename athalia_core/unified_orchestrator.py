#!/usr/bin/env python3
"""
Orchestrateur unifié pour Athalia
Coordination centralisée de tous les modules
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# Imports des modules Athalia
from .ai_robust import RobustAI
from .auto_cicd import AutoCICD
from .auto_cleaner import AutoCleaner
from .auto_documenter import AutoDocumenter
from .auto_tester import AutoTester
from .code_linter import CodeLinter
from .correction_optimizer import CorrectionOptimizer
from .generation import generate_project
from .security_auditor import SecurityAuditor

logger = logging.getLogger(__name__)


class UnifiedOrchestrator:
    """Orchestrateur unifié pour Athalia"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.workflow_results = {
            "status": "idle",
            "steps_completed": [],
            "errors": [],
            "warnings": [],
            "metrics": {},
            "artifacts": {},
        }

        # Initialiser les modules
        self.robust_ai = None
        self.security_auditor = None
        self.code_linter = None
        self.correction_optimizer = None
        self.auto_tester = None
        self.auto_documenter = None
        self.auto_cleaner = None
        self.auto_cicd = None

    def initialize_modules(self):
        """Initialise tous les modules"""
        try:
            self.robust_ai = RobustAI()
            self.security_auditor = SecurityAuditor(str(self.project_path))
            self.code_linter = CodeLinter(str(self.project_path))
            self.correction_optimizer = CorrectionOptimizer()
            self.auto_tester = AutoTester(str(self.project_path))
            self.auto_documenter = AutoDocumenter(str(self.project_path))
            self.auto_cleaner = AutoCleaner(str(self.project_path))
            self.auto_cicd = AutoCICD(str(self.project_path))

            self.workflow_results["status"] = "initialized"
            logger.info("✅ Tous les modules initialisés")

        except Exception as e:
            self.workflow_results["errors"].append(
                f"Erreur initialisation modules: {e}"
            )
            logger.error(f"❌ Erreur initialisation: {e}")

    def run_full_workflow(self, blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute le workflow complet"""
        logger.info("🚀 Démarrage du workflow unifié")
        self.workflow_results["status"] = "running"

        try:
            # Étape 1: Génération du projet
            self._step_generate_project(blueprint)

            # Étape 2: Audit de sécurité
            self._step_security_audit()

            # Étape 3: Linting du code
            self._step_code_linting()

            # Étape 4: Optimisation des corrections
            self._step_correction_optimization()

            # Étape 5: Tests automatiques
            self._step_auto_testing()

            # Étape 6: Documentation automatique
            self._step_auto_documentation()

            # Étape 7: Nettoyage automatique
            self._step_auto_cleaning()

            # Étape 8: CI/CD automatique
            self._step_auto_cicd()

            self.workflow_results["status"] = "completed"
            logger.info("✅ Workflow terminé avec succès")

        except Exception as e:
            self.workflow_results["status"] = "failed"
            self.workflow_results["errors"].append(f"Erreur workflow: {e}")
            logger.error(f"❌ Erreur workflow: {e}")

        return self.workflow_results

    def _step_generate_project(self, blueprint: Dict[str, Any]):
        """Étape 1: Génération du projet"""
        logger.info("📁 Génération du projet...")

        try:
            project_path = generate_project(blueprint, self.project_path)
            self.workflow_results["steps_completed"].append("project_generation")
            self.workflow_results["artifacts"]["project_path"] = project_path
            logger.info(f"✅ Projet généré: {project_path}")

        except Exception as e:
            self.workflow_results["errors"].append(f"Erreur génération projet: {e}")
            raise

    def _step_security_audit(self):
        """Étape 2: Audit de sécurité"""
        logger.info("🔒 Audit de sécurité...")

        try:
            if self.security_auditor:
                security_results = self.security_auditor.run()
                self.workflow_results["steps_completed"].append("security_audit")
                self.workflow_results["artifacts"]["security_report"] = security_results
                logger.info("✅ Audit de sécurité terminé")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur audit sécurité: {e}")

    def _step_code_linting(self):
        """Étape 3: Linting du code"""
        logger.info("📏 Linting du code...")

        try:
            if self.code_linter:
                lint_results = self.code_linter.run()
                self.workflow_results["steps_completed"].append("code_linting")
                self.workflow_results["artifacts"]["lint_report"] = lint_results
                logger.info("✅ Linting terminé")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur linting: {e}")

    def _step_correction_optimization(self):
        """Étape 4: Optimisation des corrections"""
        logger.info("🔧 Optimisation des corrections...")

        try:
            if self.correction_optimizer:
                # Optimiser les corrections basées sur les rapports précédents
                optimization_results = self.correction_optimizer.get_correction_stats()
                self.workflow_results["steps_completed"].append(
                    "correction_optimization"
                )
                self.workflow_results["artifacts"][
                    "optimization_stats"
                ] = optimization_results
                logger.info("✅ Optimisation terminée")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur optimisation: {e}")

    def _step_auto_testing(self):
        """Étape 5: Tests automatiques"""
        logger.info("🧪 Tests automatiques...")

        try:
            if self.auto_tester:
                test_results = self.auto_tester.run_tests()
                self.workflow_results["steps_completed"].append("auto_testing")
                self.workflow_results["artifacts"]["test_results"] = test_results
                logger.info("✅ Tests automatiques terminés")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur tests automatiques: {e}")

    def _step_auto_documentation(self):
        """Étape 6: Documentation automatique"""
        logger.info("📚 Documentation automatique...")

        try:
            if self.auto_documenter:
                doc_results = self.auto_documenter.generate_documentation()
                self.workflow_results["steps_completed"].append("auto_documentation")
                self.workflow_results["artifacts"]["documentation"] = doc_results
                logger.info("✅ Documentation générée")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur documentation: {e}")

    def _step_auto_cleaning(self):
        """Étape 7: Nettoyage automatique"""
        logger.info("🧹 Nettoyage automatique...")

        try:
            if self.auto_cleaner:
                clean_results = self.auto_cleaner.clean_project()
                self.workflow_results["steps_completed"].append("auto_cleaning")
                self.workflow_results["artifacts"]["cleaning_report"] = clean_results
                logger.info("✅ Nettoyage terminé")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur nettoyage: {e}")

    def _step_auto_cicd(self):
        """Étape 8: CI/CD automatique"""
        logger.info("🚀 Configuration CI/CD...")

        try:
            if self.auto_cicd:
                cicd_results = self.auto_cicd.setup_cicd()
                self.workflow_results["steps_completed"].append("auto_cicd")
                self.workflow_results["artifacts"]["cicd_config"] = cicd_results
                logger.info("✅ CI/CD configuré")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur CI/CD: {e}")

    def generate_workflow_report(self) -> str:
        """Génère un rapport du workflow"""
        report = []
        report.append("# Rapport Workflow Unifié Athalia")
        report.append("")

        report.append(f"## Statut: {self.workflow_results['status'].upper()}")
        report.append(f"## Date: {datetime.now().isoformat()}")
        report.append("")

        report.append("## Étapes Complétées")
        for step in self.workflow_results["steps_completed"]:
            report.append(f"- ✅ {step}")
        report.append("")

        if self.workflow_results["artifacts"]:
            report.append("## Artéfacts Générés")
            for artifact, value in self.workflow_results["artifacts"].items():
                report.append(f"- **{artifact}**: {type(value).__name__}")
        report.append("")

        if self.workflow_results["errors"]:
            report.append("## Erreurs")
            for error in self.workflow_results["errors"]:
                report.append(f"- ❌ {error}")
            report.append("")

        if self.workflow_results["warnings"]:
            report.append("## Avertissements")
            for warning in self.workflow_results["warnings"]:
                report.append(f"- ⚠️ {warning}")
            report.append("")

        if self.workflow_results["metrics"]:
            report.append("## Métriques")
            for metric, value in self.workflow_results["metrics"].items():
                report.append(f"- **{metric}**: {value}")

        return "\n".join(report)

    def save_workflow_results(self, output_path: str = "workflow_results.json"):
        """Sauvegarde les résultats du workflow"""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(self.workflow_results, f, indent=2, default=str)
            logger.info(f"✅ Résultats sauvegardés: {output_path}")
        except Exception as e:
            logger.error(f"❌ Erreur sauvegarde: {e}")


def run_unified_workflow(
    blueprint: Dict[str, Any], project_path: str = "."
) -> Dict[str, Any]:
    """Fonction utilitaire pour exécuter le workflow unifié"""
    orchestrator = UnifiedOrchestrator(project_path)
    orchestrator.initialize_modules()
    return orchestrator.run_full_workflow(blueprint)

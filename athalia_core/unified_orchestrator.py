#!/usr/bin/env python3
"""
Orchestrateur unifié pour Athalia
Coordination centralisée de tous les modules
"""

from datetime import datetime
import json
import logging
from pathlib import Path
from typing import Any, Dict

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

# Imports des modules avancés
try:
    from .advanced_modules.auto_correction_advanced import AutoCorrectionAvancee
    ADVANCED_MODULES_AVAILABLE = True
except ImportError:
    ADVANCED_MODULES_AVAILABLE = False
    logger.warning("⚠️ Modules avancés non disponibles - mode fallback activé")

# Imports des nouveaux modules IA et distillation
try:
    from .agents.unified_agent import UnifiedAgent
    from .agents.context_prompt import ContextPromptAgent
    from .agents.audit_agent import AuditAgent
    from .distillation.quality_scorer import QualityScorer
    from .distillation.response_distiller import ResponseDistiller
    from .distillation.code_genetics import CodeGenetics

    AI_MODULES_AVAILABLE = True
except ImportError:
    AI_MODULES_AVAILABLE = False
    logger.warning("⚠️ Modules IA non disponibles - mode fallback activé")


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

        # Initialiser les modules IA et distillation
        self.unified_agent = None
        self.context_agent = None
        self.audit_agent = None
        self.quality_scorer = None
        self.response_distiller = None
        self.code_genetics = None
        
        # Initialiser les modules avancés
        self.auto_correction_advanced = None

    def initialize_modules(self):
        """Initialise tous les modules"""
        try:
            # Modules de base
            self.robust_ai = RobustAI()
            self.security_auditor = SecurityAuditor(str(self.project_path))
            self.code_linter = CodeLinter(str(self.project_path))
            self.correction_optimizer = CorrectionOptimizer()
            self.auto_tester = AutoTester(str(self.project_path))
            self.auto_documenter = AutoDocumenter(str(self.project_path))
            self.auto_cleaner = AutoCleaner(str(self.project_path))
            self.auto_cicd = AutoCICD()

            # Modules IA et distillation (si disponibles)
            if AI_MODULES_AVAILABLE:
                try:
                    self.unified_agent = UnifiedAgent()
                    self.context_agent = ContextPromptAgent()
                    self.audit_agent = AuditAgent()
                    self.quality_scorer = QualityScorer()
                    self.response_distiller = ResponseDistiller()
                    self.code_genetics = CodeGenetics()
                    logger.info("✅ Modules IA et distillation initialisés")
                except Exception as e:
                    logger.warning(f"⚠️ Erreur initialisation modules IA: {e}")

            # Modules avancés (si disponibles)
            if ADVANCED_MODULES_AVAILABLE:
                try:
                    self.auto_correction_advanced = AutoCorrectionAvancee(str(self.project_path))
                    logger.info("✅ Modules avancés initialisés")
                except Exception as e:
                    logger.warning(f"⚠️ Erreur initialisation modules avancés: {e}")

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
            # Étape 1: Classification intelligente du projet
            self._step_intelligent_classification(blueprint)

            # Étape 2: Génération du projet
            self._step_generate_project(blueprint)

            # Étape 3: Amélioration IA intelligente
            self._step_ai_enhancement(blueprint)

            # Étape 4: Audit de sécurité
            self._step_security_audit()

            # Étape 5: Linting du code
            self._step_code_linting()

            # Étape 6: Auto-correction avancée
            self._step_advanced_auto_correction()

            # Étape 7: Optimisation des corrections
            self._step_correction_optimization()

            # Étape 8: Tests automatiques
            self._step_auto_testing()

            # Étape 9: Documentation automatique
            self._step_auto_documentation()

            # Étape 10: Nettoyage automatique
            self._step_auto_cleaning()

            # Étape 11: CI/CD automatique
            self._step_auto_cicd()

            self.workflow_results["status"] = "completed"
            logger.info("✅ Workflow terminé avec succès")

        except Exception as e:
            self.workflow_results["status"] = "failed"
            self.workflow_results["errors"].append(f"Erreur workflow: {e}")
            logger.error(f"❌ Erreur workflow: {e}")

        return self.workflow_results

    def _step_intelligent_classification(self, blueprint: Dict[str, Any]):
        """Étape 1: Classification intelligente du projet"""
        logger.info("🧠 Classification intelligente du projet...")

        try:
            if AI_MODULES_AVAILABLE and self.context_agent:
                # Utiliser l'agent de contexte pour classifier le projet
                description = blueprint.get("description", "")
                project_name = blueprint.get("project_name", "")

                classification_prompt = f"""
                Analyse ce projet et détermine son type :
                Nom: {project_name}
                Description: {description}
                
                Types possibles: api, web, game, artistic, robotics, data, mobile, iot, generic
                
                Retourne uniquement le type de projet.
                """

                try:
                    project_type = self.context_agent.act(classification_prompt)
                    if project_type and project_type.strip():
                        blueprint["project_type"] = project_type.strip()
                        logger.info(f"✅ Type détecté intelligemment: {project_type}")
                    else:
                        logger.warning(
                            "⚠️ Classification IA échouée, utilisation du type par défaut"
                        )
                except Exception as e:
                    logger.warning(f"⚠️ Erreur classification IA: {e}")

            self.workflow_results["steps_completed"].append(
                "intelligent_classification"
            )
            self.workflow_results["artifacts"]["project_type"] = blueprint.get(
                "project_type", "generic"
            )

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur classification: {e}")

    def _step_generate_project(self, blueprint: Dict[str, Any]):
        """Étape 2: Génération du projet"""
        logger.info("📁 Génération du projet...")

        try:
            project_path = generate_project(blueprint, self.project_path)
            self.workflow_results["steps_completed"].append("project_generation")
            self.workflow_results["artifacts"]["project_path"] = project_path
            logger.info(f"✅ Projet généré: {project_path}")

        except Exception as e:
            self.workflow_results["errors"].append(f"Erreur génération projet: {e}")
            raise

    def _step_ai_enhancement(self, blueprint: Dict[str, Any]):
        """Étape 3: Amélioration IA intelligente"""
        logger.info("🤖 Amélioration IA intelligente...")

        try:
            if AI_MODULES_AVAILABLE and self.unified_agent and self.quality_scorer:
                project_path = self.workflow_results["artifacts"].get("project_path")
                if project_path:
                    main_file = Path(project_path) / "src" / "main.py"
                    if main_file.exists():
                        # Lire le code généré
                        with open(main_file, "r", encoding="utf-8") as f:
                            original_code = f.read()

                        # Améliorer le code avec l'agent IA
                        enhancement_prompt = f"""
                        Améliore ce code Python pour le rendre ultra-avancé :
                        
                        Type de projet: {blueprint.get('project_type', 'generic')}
                        Description: {blueprint.get('description', '')}
                        
                        Code actuel:
                        {original_code}
                        
                        Améliore ce code avec :
                        1. Fonctionnalités avancées spécifiques au type de projet
                        2. Architecture moderne et scalable
                        3. Gestion d'erreurs robuste
                        4. Performance optimisée
                        5. Code de production professionnel
                        
                        Retourne UNIQUEMENT le code Python amélioré.
                        """

                        try:
                            enhanced_code = self.unified_agent.act(enhancement_prompt)
                            if enhanced_code and self._validate_code(enhanced_code):
                                # Sauvegarder et appliquer l'amélioration
                                backup_file = main_file.with_suffix(".py.backup")
                                with open(backup_file, "w", encoding="utf-8") as f:
                                    f.write(original_code)

                                with open(main_file, "w", encoding="utf-8") as f:
                                    f.write(enhanced_code)

                                # Évaluer la qualité
                                quality_score = self.quality_scorer.score_code(
                                    enhanced_code
                                )
                                logger.info(
                                    f"✅ Code amélioré avec score qualité: {quality_score}"
                                )

                                self.workflow_results["artifacts"]["ai_enhancement"] = {
                                    "quality_score": quality_score,
                                    "backup_file": str(backup_file),
                                }
                            else:
                                logger.warning(
                                    "⚠️ Amélioration IA invalide, code original conservé"
                                )
                        except Exception as e:
                            logger.warning(f"⚠️ Erreur amélioration IA: {e}")

            self.workflow_results["steps_completed"].append("ai_enhancement")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur amélioration IA: {e}")

    def _step_advanced_auto_correction(self):
        """Étape 6: Auto-correction avancée"""
        logger.info("🔧 Auto-correction avancée...")

        try:
            if ADVANCED_MODULES_AVAILABLE and self.auto_correction_advanced:
                # Lancer l'auto-correction avancée
                resultats = self.auto_correction_advanced.analyser_et_corriger(dry_run=False)
                
                # Enregistrer les résultats
                self.workflow_results["steps_completed"].append("advanced_auto_correction")
                self.workflow_results["artifacts"]["auto_correction_results"] = resultats
                
                # Afficher les statistiques
                corrections_count = len(resultats.get("corrections_appliquees", []))
                suggestions_count = len(resultats.get("suggestions", []))
                fichiers_traites = resultats.get("fichiers_traites", 0)
                
                logger.info(f"✅ Auto-correction avancée terminée:")
                logger.info(f"  - Fichiers traités: {fichiers_traites}")
                logger.info(f"  - Corrections appliquées: {corrections_count}")
                logger.info(f"  - Suggestions: {suggestions_count}")
                
                # Générer un rapport détaillé
                if resultats.get("corrections_appliquees"):
                    rapport_file = self.project_path / "auto_correction_report.json"
                    try:
                        import json
                        with open(rapport_file, "w", encoding="utf-8") as f:
                            json.dump(resultats, f, indent=2, ensure_ascii=False)
                        logger.info(f"📄 Rapport d'auto-correction généré: {rapport_file}")
                    except Exception as e:
                        logger.warning(f"Impossible de générer le rapport: {e}")
            else:
                logger.info("⚠️ Module d'auto-correction avancée non disponible")
                self.workflow_results["steps_completed"].append("advanced_auto_correction_skipped")

        except Exception as e:
            self.workflow_results["warnings"].append(f"Erreur auto-correction avancée: {e}")
            logger.warning(f"⚠️ Erreur auto-correction avancée: {e}")

    def _validate_code(self, code: str) -> bool:
        """Valide la syntaxe du code Python"""
        try:
            compile(code, "<string>", "exec")
            return True
        except SyntaxError:
            return False

    def _step_security_audit(self):
        """Étape 4: Audit de sécurité"""
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
        """Étape 5: Linting du code"""
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
        """Étape 7: Optimisation des corrections"""
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
        """Étape 8: Tests automatiques"""
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
        """Étape 9: Documentation automatique"""
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
        """Étape 10: Nettoyage automatique"""
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
        """Étape 11: CI/CD automatique"""
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

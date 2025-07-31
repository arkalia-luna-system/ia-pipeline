#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Athalia Unified - Pipeline d'industrialisation IA complet
Interface unifiée pour tous les modules Athalia
"""

import argparse
import logging
import os
import sys


# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    """Fonction principale du CLI unifié"""
    parser = argparse.ArgumentParser(
        description="""
🚀 ATHALIA UNIFIED - Pipeline d'industrialisation IA complet

EXEMPLES D'UTILISATION:
  python athalia_unified.py /chemin/vers/projet --action complete
  python athalia_unified.py /chemin/vers/repertoire --scan

MODULES INTÉGRÉS:
  🔍 Audit intelligent     - Analyse complète avec score et recommandations
  🧹 Nettoyage automatique - Suppression des fichiers parasites
  📚 Documentation auto    - Génération de README, API docs
  🧪 Tests automatiques    - Création de tests unitaires
  🚀 CI/CD automatique     - Configuration GitHub Actions
  🔧 Auto-correction       - Correction syntaxique et optimisation
  👤 Profils utilisateur   - Gestion des préférences et historique
  📊 Dashboard unifié      - Visualisations et rapports
        """
    )

    parser.add_argument(
        "project_path", help="Chemin du projet à industrialiser ou répertoire à scanner"
    )

    parser.add_argument(
        "--action",
        choices=["complete", "audit", "fix", "dashboard"],
        default="complete",
        help="Action spécifique à exécuter",
    )

    parser.add_argument(
        "--scan",
        action="store_true",
        help="Scanner les projets au lieu d'industrialiser",
    )

    parser.add_argument(
        "--no-audit", action="store_true", help="Passer l'étape d'audit intelligent"
    )

    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Passer l'étape de nettoyage automatique",
    )

    parser.add_argument(
        "--no-doc",
        action="store_true",
        help="Passer l'étape de génération de documentation",
    )

    parser.add_argument(
        "--no-test", action="store_true", help="Passer l'étape de génération de tests"
    )

    parser.add_argument(
        "--no-cicd", action="store_true", help="Passer l'étape de configuration CI/CD"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mode simulation - aucun fichier ne sera modifié",
    )

    parser.add_argument(
        "--auto-fix", action="store_true", help="Corriger automatiquement le code"
    )

    parser.add_argument(
        "--utilisateur",
        "-u",
        default="default",
        help="Nom de l'utilisateur pour les profils",
    )

    parser.add_argument(
        "--verbose", action="store_true", help="Mode verbeux avec plus de détails"
    )

    parser.add_argument(
        "--lang",
        default="fr",
        choices=["fr", "en"],
        help="Langue pour la documentation et les messages",
    )

    args = parser.parse_args()

    # Vérification du chemin
    if not os.path.exists(args.project_path):
        logger.info(f"❌ Le chemin {args.project_path} n'existe pas")
        sys.exit(1)

    # Affichage du header
    logger.info("🚀" + "=" * 60 + "🚀")
    logger.info("🌟 ATHALIA UNIFIED - Industrialisation IA complète")
    logger.info("🌟 Tous les modules intégrés dans un pipeline unifié")
    logger.info("🚀" + "=" * 60 + "🚀")

    logger.info(f"📁 Projet: {args.project_path}")
    logger.info(f"👤 Utilisateur: {args.utilisateur}")
    logger.info(f"🔧 Action: {args.action}")
    logger.info("")

    try:
        if args.action == "complete" and not args.scan:
            # Mode industrialisation complète
            logger.info("🚀 Lancement de l'industrialisation complète...")

            # Import de l'orchestrateur principal
            try:
                from athalia_core.athalia_orchestrator import AthaliaOrchestrator
            except ImportError:
                logger.info(
                    "⚠️ Module athalia_orchestrator non disponible, "
                    "utilisation de la version simplifiée"
                )
                # Version simplifiée pour les tests

                class AthaliaOrchestrator:
                    def industrialize_project(self, project_path, config=None):
                        return {
                            "status": (
                                "Industrialisation simulée - Modules non disponibles"
                            )
                        }

                    def audit_project(self, project_path):
                        return {"score": 75, "issues": 15}

                    def scan_projects(self, project_path):
                        return [
                            {"name": "test", "type": "python", "path": project_path}
                        ]

            config = {
                "audit": not args.no_audit,
                "clean": not args.no_clean,
                "doc": not args.no_doc,
                "test": not args.no_test,
                "cicd": not args.no_cicd,
                "dry_run": args.dry_run,
                "auto_fix": args.auto_fix,
                "lang": args.lang,
            }

            orchestrator = AthaliaOrchestrator()
            results = orchestrator.industrialize_project(args.project_path, config)

            if "status" in results:
                logger.info("✅ Industrialisation terminée avec succès!")
                logger.info(f"📊 Rapport: {results['status']}")
            else:
                logger.info("✅ Industrialisation terminée!")

        elif args.action == "audit":
            logger.info("🔍 Lancement de l'audit intelligent...")
            try:
                from athalia_core.audit import audit_project_intelligent

                audit_result = audit_project_intelligent(args.project_path)
                logger.info(f"📊 Score: {audit_result.get('score', 'N/A')}/100")
                logger.info(f"🚨 Problèmes: {len(audit_result.get('issues', []))}")
                logger.info(
                    f"💡 Suggestions: {len(audit_result.get('suggestions', []))}"
                )
            except Exception as e:
                logger.error(f"❌ Erreur lors de l'audit: {e}")

        elif args.action == "fix":
            logger.info("🔧 Lancement de l'auto-correction...")
            try:
                from modules.auto_correction_avancee import AutoCorrectionAvancee

                corrector = AutoCorrectionAvancee(args.project_path)
                result = corrector.analyser_et_corriger(dry_run=args.dry_run)
                logger.info(f"✅ Correction terminée: {result}")
            except Exception as e:
                logger.error(f"❌ Erreur lors de la correction: {e}")

        elif args.action == "dashboard":
            logger.info("📊 Lancement du dashboard...")
            try:
                from modules.dashboard_unifie_simple import DashboardUnifieSimple

                dashboard = DashboardUnifieSimple()
                print(dashboard.generer_rapport_consolide())
            except Exception as e:
                logger.error(f"❌ Erreur lors du dashboard: {e}")

        elif args.scan:
            logger.info("🔍 Scanner les projets...")
            try:
                from modules.orchestrateur_principal import AthaliaOrchestrator

                orchestrator = AthaliaOrchestrator()
                projects = orchestrator.scan_projects(args.project_path)
                logger.info(f"📁 Projets trouvés: {len(projects)}")
                for project in projects:
                    logger.info(
                        f"  - {project.get('name', 'N/A')} "
                        f"({project.get('type', 'N/A')})"
                    )
            except Exception as e:
                logger.error(f"❌ Erreur lors du scan: {e}")

    except Exception as e:
        logger.error(f"❌ Erreur générale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

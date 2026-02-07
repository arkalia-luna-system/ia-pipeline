#!/usr/bin/env python3
"""
Athalia Unified - Pipeline d'industrialisation IA complet
Interface unifiée pour tous les modules Athalia
"""

import argparse
import logging
import os
import sys
from pathlib import Path

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
        choices=[
            "complete",
            "audit",
            "fix",
            "dashboard",
            "api",
            "benchmark",
            "security-dashboard",
            "tutorials",
        ],
        default="complete",
        help="Action à exécuter (complete, audit, fix, dashboard, api, benchmark, security-dashboard, tutorials)",
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
            # Mode industrialisation complète avec l'orchestrateur unifié réel
            logger.info("🚀 Lancement de l'industrialisation complète...")

            try:
                from athalia_core.core.unified_orchestrator import UnifiedOrchestrator

                orchestrator = UnifiedOrchestrator(project_path=args.project_path)
                orchestrator.initialize_modules()
                # Blueprint minimal pour un projet existant (scan du répertoire)
                blueprint = {
                    "name": "project",
                    "description": "Industrialisation complète",
                    "path": args.project_path,
                    "config": {
                        "audit": not args.no_audit,
                        "clean": not args.no_clean,
                        "doc": not args.no_doc,
                        "test": not args.no_test,
                        "cicd": not args.no_cicd,
                        "dry_run": args.dry_run,
                        "auto_fix": args.auto_fix,
                        "lang": args.lang,
                    },
                }
                results = orchestrator.run_full_workflow(blueprint)
                status = results.get("status", "completed")
                logger.info("✅ Industrialisation terminée avec succès!")
                logger.info(f"📊 Statut: {status}")
                if results.get("errors"):
                    for err in results["errors"]:
                        logger.warning(f"⚠️ {err}")
            except Exception as e:
                logger.error(f"❌ Erreur lors de l'industrialisation: {e}")
                raise

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
                from athalia_core.advanced_modules.auto_correction_advanced import (
                    AutoCorrectionAvancee,
                )

                corrector = AutoCorrectionAvancee(args.project_path)
                result = corrector.analyser_et_corriger(dry_run=args.dry_run)
                logger.info(f"✅ Correction terminée: {result}")
            except Exception as e:
                logger.error(f"❌ Erreur lors de la correction: {e}")

        elif args.action == "dashboard":
            logger.info("📊 Lancement du dashboard...")
            try:
                from athalia_core.advanced_modules.dashboard_unified import (
                    DashboardUnifieSimple,
                )

                dashboard = DashboardUnifieSimple()
                print(dashboard.generer_rapport_consolide())
            except Exception as e:
                logger.error(f"❌ Erreur lors du dashboard: {e}")

        elif args.scan:
            logger.info("🔍 Scanner les projets...")
            try:
                root = Path(args.project_path)
                if not root.is_dir():
                    logger.info(f"  - {root.name} (fichier)")
                else:
                    projects = []
                    for p in root.iterdir():
                        if p.name.startswith(".") or p.name in (
                            "__pycache__",
                            "node_modules",
                        ):
                            continue
                        proj_type = "directory"
                        if p.is_file():
                            proj_type = "file"
                        elif (p / "pyproject.toml").exists() or (
                            p / "setup.py"
                        ).exists():
                            proj_type = "python"
                        projects.append(
                            {"name": p.name, "type": proj_type, "path": str(p)}
                        )
                    if not projects:
                        projects = [
                            {"name": root.name, "type": "project", "path": str(root)}
                        ]
                    logger.info(f"📁 Projets / éléments trouvés: {len(projects)}")
                    for project in projects:
                        logger.info(
                            f"  - {project.get('name', 'N/A')} "
                            f"({project.get('type', 'N/A')})"
                        )
            except Exception as e:
                logger.error(f"❌ Erreur lors du scan: {e}")

        elif args.action == "api":
            logger.info("🌐 Lancement du serveur API REST (uvicorn)...")
            try:
                import subprocess

                subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "uvicorn",
                        "athalia_core.api.main_api_server:app",
                        "--host",
                        "0.0.0.0",
                        "--port",
                        "8000",
                    ],
                    check=False,
                )
            except FileNotFoundError:
                logger.info(
                    "💡 Installez uvicorn (pip install uvicorn) puis exécutez :"
                )
                logger.info(
                    "   uvicorn athalia_core.api.main_api_server:app --reload --port 8000"
                )
            except Exception as e:
                logger.error(f"❌ Erreur API: {e}")

        elif args.action == "benchmark":
            logger.info("📊 Lancement du système de benchmarks...")
            try:
                old_argv = sys.argv
                sys.argv = [
                    "benchmark",
                    "--project-path",
                    args.project_path,
                    "--run-all",
                ]
                from athalia_core.benchmarks.advanced_benchmark_system import (
                    main as benchmark_main,
                )

                benchmark_main()
                sys.argv = old_argv
            except Exception as e:
                logger.error(f"❌ Erreur benchmarks: {e}")

        elif args.action == "security-dashboard":
            logger.info("🛡️ Lancement du dashboard de sécurité...")
            try:
                old_argv = sys.argv
                sys.argv = [
                    "security_dashboard",
                    "--project-path",
                    args.project_path,
                    "--open",
                ]
                from athalia_core.security.security_dashboard import (
                    main as security_main,
                )

                security_main()
                sys.argv = old_argv
            except Exception as e:
                logger.error(f"❌ Erreur security dashboard: {e}")

        elif args.action == "tutorials":
            logger.info("🎓 Lancement des tutoriels interactifs...")
            try:
                old_argv = sys.argv
                sys.argv = ["tutorials", args.project_path]
                from athalia_core.tutorials.interactive_tutorial_system import (
                    main as tutorials_main,
                )

                tutorials_main()
                sys.argv = old_argv
            except Exception as e:
                logger.error(f"❌ Erreur tutoriels: {e}")

    except Exception as e:
        logger.error(f"❌ Erreur générale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

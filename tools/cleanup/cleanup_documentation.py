#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de nettoyage et organisation de la documentation
"""

import logging
import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/athalia.log", mode="a", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class DocumentationCleaner:
    """Classe pour nettoyer et organiser la documentation"""

    def __init__(self, docs_dir="docs"):
        self.docs_dir = Path(docs_dir)
        self.archive_dir = (
            self.docs_dir / "archive" / datetime.now().strftime("%Y%m%d")
        )
        self.archive_dir.mkdir(parents=True, exist_ok=True)

        # Documents à conserver (actuels)
        self.current_docs = {
            # Principaux
            "README.md",
            "INDEX_PRINCIPAL.md",
            "INSTALLATION.md",
            "USAGE.md",
            "API.md",
            # Plans d'action
            "PHASE_1_URGENT_TERMINEE.md",
            "PLAN_ACTION_IMPORTANT.md",
            "PLAN_ACTION_AMELIORATION.md",
            "PLAN_ACTION_URGENT.md",
            "CAHIER_CHARGES_COMPLET.md",
            # Guides techniques
            "MODULES.md",
            "TESTS_GUIDE.md",
            "PLUGINS_GUIDE.md",
            "DEPLOYMENT.md",
            "DEVELOPER_GUIDE.md",
            "CONTRIBUTING.md",
            "GIT_WORKFLOW.md",
            "BEST_PRACTICES.md",
            # Robotics et IA
            "ROBOTICS_GUIDE.md",
            "REACHY_SETUP_GUIDE.md",
            "RESUME_TEST_PROMPTS.md",
            "UNIFIED_ORCHESTRATOR.md",
            "ALIAS_UNIFIED.md",
            # Analyses et rapports
            "RAPPORT_FINAL.md",
            "AUDIT_COMPLET_PROJET.md",
            "INVENTAIRE_COMPLET.md",
            "ANALYSE_PLAN_OPTIMISATION_AVANCE.md",
            "OPTIMISATION_PERFORMANCES.md",
            "ORGANISATION_WORKSPACE.md",
            # Support
            "FAQ.md",
            "TROUBLESHOOTING.md",
        }

        # Documents obsolètes à archiver
        self.obsolete_docs = [
            "INDEX.md",  # Remplacé par INDEX_PRINCIPAL.md
            "dashboard.md",  # Remplacé par dashboard optimisé
            "ROADMAP.md",  # Contenu obsolète
            "GENESIS.md",  # Historique
            "FINAL_SUMMARY.md",  # Remplacé par PHASE_1_URGENT_TERMINEE.md
            "FINAL_SYSTEM_STATUS.md",  # Remplacé par RAPPORT_FINAL.md
            "USER_GUIDE.md",  # Remplacé par USAGE.md
            "ALIAS.md",  # Remplacé par ALIAS_UNIFIED.md
            "INSTALL.md",  # Remplacé par INSTALLATION.md
            "API_REFERENCE.md",  # Remplacé par API.md
            "CLEANUP_REPORT.md",  # Historique
            "CI_PROBLEMS_ANALYSIS.md",  # Historique
            "NETTOYAGE_FINAL.md",  # Historique
            "CORRECTIONS_EFFECTUEES.md",  # Historique
            "PROCHAINES_ETAPES.md",  # Remplacé par PLAN_ACTION_*.md
            "STATUT_ACTUEL.md",  # Remplacé par PHASE_1_URGENT_TERMINEE.md
            "INVENTAIRE_COMPLET_SYSTEME.md",  # Remplacé par INVENTAIRE_COMPLET.md
            "ORGANISATION_PROJET.md",  # Remplacé par ORGANISATION_WORKSPACE.md
            "GUIDE_TEST_PLUGIN_VSCODE.md",  # Spécifique, à archiver
            "GUIDE_VALIDATION.md",  # Remplacé par TESTS_GUIDE.md
            "GUIDE_VALIDATION_TEMPS_REEL.md",  # Historique
            "GUIDE_PROMPTS_TEST.md",  # Remplacé par RESUME_TEST_PROMPTS.md
            "INTELLIGENT_MODULES.md",  # Remplacé par MODULES.md
            "ORCHESTRATION_CLARIFICATION.md",  # Historique
            "RAPPORT_AUDIT_FINAL.md",  # Remplacé par AUDIT_COMPLET_PROJET.md
            "RAPPORT_COHERENCE_DOCUMENTATION.md",  # Historique
            "RAPPORT_NETTOYAGE_COMPLET.md",  # Historique
            "RAPPORT_RANGEMENT_RACINE.md",  # Historique
            "RAPPORT_OPTIMISATION_FINALE.md",  # Historique
            "RAPPORT_OPTIMISATION_FINALE_V2.md",  # Historique
            "RAPPORT_FINAL_COMPLET.md",  # Remplacé par RAPPORT_FINAL.md
            "PROCHAINES_ETAPES_FINALES.md",  # Remplacé par PLAN_ACTION_*.md
            "RAPPORT_CORRECTIONS_AUTO_TESTER.md",  # Historique
            "RAPPORT_FINAL_VALIDATION_PROFESSIONNELLE.md",  # Historique
            "RAPPORT_PROGRESSION_VALIDATION.md",  # Historique
            "RAPPORT_FINAL_CORRECTIONS.md",  # Historique
            "RAPPORT_FINAL_OPTIMISATION.md",  # Historique
            "RAPPORT_FINAL_CORRECTIONS.md",  # Historique
        ]

    def scan_documentation(self):
        """Scanne la documentation et catégorise les fichiers"""
        all_files = list(self.docs_dir.glob("*.md"))

        categories = {"current": [], "obsolete": [], "unknown": []}

        for file_path in all_files:
            file_name = file_path.name

            # Ignorer les fichiers système macOS
            if file_name.startswith("._"):
                continue

            if file_name in self.current_docs:
                categories["current"].append(file_path)
            elif file_name in self.obsolete_docs:
                categories["obsolete"].append(file_path)
            else:
                categories["unknown"].append(file_path)

        return categories

    def archive_obsolete_docs(self, obsolete_files):
        """Archive les documents obsolètes"""
        archived_count = 0

        for file_path in obsolete_files:
            try:
                # Créer le nom d'archive
                archive_name = f"obsolete_{file_path.name}"
                archive_path = self.archive_dir / archive_name

                # Déplacer vers l'archive
                shutil.move(str(file_path), str(archive_path))
                logger.info(f"📦 Archivé: {file_path.name} -> {archive_path}")
                archived_count += 1

            except Exception as e:
                logger.error(f"❌ Erreur archivage {file_path.name}: {e}")

        return archived_count

    def create_documentation_report(self, categories, archived_count):
        """Crée un rapport de nettoyage de la documentation"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_files": sum(
                    len(files) for files in categories.values()
                ),
                "current_files": len(categories["current"]),
                "obsolete_files": len(categories["obsolete"]),
                "unknown_files": len(categories["unknown"]),
                "archived": archived_count,
            },
            "categories": {
                "current": [f.name for f in categories["current"]],
                "obsolete": [f.name for f in categories["obsolete"]],
                "unknown": [f.name for f in categories["unknown"]],
            },
        }

        return report

    def cleanup(self, dry_run=False):
        """Exécute le nettoyage complet de la documentation"""
        logger.info("📚 DÉBUT DU NETTOYAGE DE LA DOCUMENTATION")
        logger.info(f"📁 Dossier de documentation: {self.docs_dir}")
        logger.info(f"📦 Dossier d'archive: {self.archive_dir}")

        if dry_run:
            logger.info("🔍 MODE DRY-RUN - Aucun fichier ne sera déplacé")

        # Scanner la documentation
        categories = self.scan_documentation()

        # Afficher les statistiques
        logger.info(f"📊 Statistiques:")
        logger.info(f"  - Documents actuels: {len(categories['current'])}")
        logger.info(f"  - Documents obsolètes: {len(categories['obsolete'])}")
        logger.info(f"  - Documents inconnus: {len(categories['unknown'])}")

        # Afficher les documents inconnus
        if categories["unknown"]:
            logger.info(f"📋 Documents inconnus (à examiner):")
            for file_path in categories["unknown"]:
                logger.info(f"    - {file_path.name}")

        # Actions de nettoyage
        archived_count = 0

        if not dry_run:
            # Archiver les documents obsolètes
            archived_count = self.archive_obsolete_docs(categories["obsolete"])

        # Générer le rapport
        report = self.create_documentation_report(categories, archived_count)

        # Sauvegarder le rapport
        report_file = (
            self.docs_dir
            / f"documentation_cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        import json

        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Afficher le résumé
        logger.info("✅ NETTOYAGE DE LA DOCUMENTATION TERMINÉ")
        logger.info(f"📦 Documents archivés: {archived_count}")
        logger.info(f"📄 Rapport sauvegardé: {report_file}")

        return report


def main():
    """Fonction principale"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Nettoyage et organisation de la documentation"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Mode simulation"
    )
    parser.add_argument(
        "--docs-dir", default="docs", help="Dossier de documentation"
    )

    args = parser.parse_args()

    # Créer le nettoyeur
    cleaner = DocumentationCleaner(args.docs_dir)

    # Exécuter le nettoyage
    report = cleaner.cleanup(dry_run=args.dry_run)

    # Afficher l'espace libéré
    if not args.dry_run:
        logger.info("💾 Espace disque après nettoyage:")
        os.system(f"du -sh {args.docs_dir}")


if __name__ == "__main__":
    main()

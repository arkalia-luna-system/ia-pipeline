#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de nettoyage et d'organisation de la documentation
"""

import json
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DocumentationCleaner:
    """Classe pour nettoyer et organiser la documentation"""

    def __init__(self, docs_dir="docs"):
        self.docs_dir = Path(docs_dir)
        self.archive_dir = self.docs_dir / "archive" / datetime.now().strftime("%Y%m%d")
        self.archive_dir.mkdir(parents=True, exist_ok=True)

        # Documents à conserver (actuels)
        self.current_docs = {
            # Principaux
            'README.md', 'INDEX_PRINCIPAL.md', 'INSTALLATION.md', 'USAGE.md', 'API.md',
            # Plans d'action
            'PHASE_1_URGENT_TERMINEE.md', 'PLAN_ACTION_IMPORTANT.md',
            'PLAN_ACTION_AMELIORATION.md', 'PLAN_ACTION_URGENT.md', 'CAHIER_CHARGES_COMPLET.md',
            # Guides techniques
            'MODULES.md', 'TESTS_GUIDE.md', 'PLUGINS_GUIDE.md', 'DEPLOYMENT.md',
            'DEVELOPER_GUIDE.md', 'CONTRIBUTING.md', 'GIT_WORKFLOW.md', 'BEST_PRACTICES.md',
            # Robotics et IA
            'ROBOTICS_GUIDE.md', 'REACHY_SETUP_GUIDE.md', 'RESUME_TEST_PROMPTS.md',
            'UNIFIED_ORCHESTRATOR.md', 'ALIAS_UNIFIED.md',
            # Analyses et rapports
            'RAPPORT_FINAL.md', 'AUDIT_COMPLET_PROJET.md', 'INVENTAIRE_COMPLET.md',
            'ANALYSE_PLAN_OPTIMISATION_AVANCE.md', 'OPTIMISATION_PERFORMANCES.md',
            'ORGANISATION_WORKSPACE.md',
            # Support
            'FAQ.md', 'TROUBLESHOOTING.md'
        }

        # Documents obsolètes à archiver
        self.obsolete_docs = [
            'INDEX.md',  # Remplacé par INDEX_PRINCIPAL.md
            'dashboard.md',  # Remplacé par dashboard optimisé
            'ROADMAP.md',  # Contenu obsolète
            'GENESIS.md',  # Historique
            'FINAL_SUMMARY.md',  # Remplacé par PHASE_1_URGENT_TERMINEE.md
            'FINAL_SYSTEM_STATUS.md',  # Remplacé par RAPPORT_FINAL.md
            'USER_GUIDE.md',  # Remplacé par USAGE.md
            'ALIAS.md',  # Remplacé par ALIAS_UNIFIED.md
            'INSTALL.md',  # Remplacé par INSTALLATION.md
            'API_REFERENCE.md',  # Remplacé par API.md
            'CLEANUP_REPORT.md',  # Historique
            'CI_PROBLEMS_ANALYSIS.md',  # Historique
            'NETTOYAGE_FINAL.md',  # Historique
            'CORRECTIONS_EFFECTUEES.md',  # Historique
            'PROCHAINES_ETAPES.md',  # Remplacé par PLAN_ACTION_*.md
            'STATUT_ACTUEL.md',  # Remplacé par PHASE_1_URGENT_TERMINEE.md
            'INVENTAIRE_COMPLET_SYSTEME.md',  # Remplacé par INVENTAIRE_COMPLET.md
            'ORGANISATION_PROJET.md',  # Remplacé par ORGANISATION_WORKSPACE.md
            'GUIDE_TEST_PLUGIN_VSCODE.md',  # Spécifique, à archiver
            'GUIDE_VALIDATION.md',  # Remplacé par TESTS_GUIDE.md
            'GUIDE_VALIDATION_TEMPS_REEL.md',  # Historique
            'GUIDE_PROMPTS_TEST.md',  # Remplacé par RESUME_TEST_PROMPTS.md
            'INTELLIGENT_MODULES.md',  # Remplacé par MODULES.md
            'ORCHESTRATION_CLARIFICATION.md',  # Historique
            'RAPPORT_AUDIT_FINAL.md',  # Remplacé par AUDIT_COMPLET_PROJET.md
            'RAPPORT_COHERENCE_DOCUMENTATION.md',  # Historique
            'RAPPORT_NETTOYAGE_COMPLET.md',  # Historique
            'RAPPORT_RANGEMENT_RACINE.md',  # Historique
            'RAPPORT_OPTIMISATION_FINALE.md',  # Historique
            'RAPPORT_OPTIMISATION_FINALE_V2.md',  # Historique
            'RAPPORT_FINAL_COMPLET.md',  # Remplacé par RAPPORT_FINAL.md
            'PROCHAINES_ETAPES_FINALES.md',  # Remplacé par PLAN_ACTION_*.md
            'RAPPORT_CORRECTIONS_AUTO_TESTER.md',  # Historique
            'RAPPORT_FINAL_VALIDATION_PROFESSIONNELLE.md',  # Historique
            'RAPPORT_PROGRESSION_VALIDATION.md',  # Historique
            'RAPPORT_FINAL_CORRECTIONS.md',  # Historique
            'RAPPORT_FINAL_OPTIMISATION.md',  # Historique
            'RAPPORT_FINAL_CORRECTIONS.md',  # Historique
        ]

    def scan_documentation(self):
        """Scanne la documentation et catégorise les fichiers"""
        all_files = list(self.docs_dir.glob("*.md"))

        categories = {
            'current': [],
            'obsolete': [],
            'unknown': []
        }

        for file_path in all_files:
            file_name = file_path.name

            # Ignorer les fichiers système macOS
            if file_name.startswith('._'):
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
                # Copier vers l'archive
                archive_path = self.archive_dir / file_path.name
                with open(file_path, "r", encoding="utf-8") as src:
                    with open(archive_path, "w", encoding="utf-8") as dst:
                        dst.write(src.read())

                # Supprimer l'original
                file_path.unlink()
                archived_count += 1
                logger.info(f"📦 Archivé: {file_path.name}")

            except Exception as e:
                logger.error(f"❌ Erreur lors de l'archivage de {file_path.name}: {e}")

        return archived_count

    def create_documentation_report(self, categories, archived_count):
        """Crée un rapport de nettoyage de la documentation"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'current_docs': len(categories['current']),
                'obsolete_docs': len(categories['obsolete']),
                'unknown_docs': len(categories['unknown']),
                'archived_count': archived_count
            },
            'categories': {
                'current': [str(f) for f in categories['current']],
                'obsolete': [str(f) for f in categories['obsolete']],
                'unknown': [str(f) for f in categories['unknown']]
            }
        }

        return report

    def cleanup(self, dry_run=False):
        """Exécute le nettoyage complet de la documentation"""
        logger.info("🧹 DÉBUT DU NETTOYAGE DE LA DOCUMENTATION")
        logger.info(f"📁 Dossier de documentation: {self.docs_dir}")

        if dry_run:
            logger.info("🔍 MODE DRY-RUN - Aucun fichier ne sera modifié")

        # Scanner la documentation
        categories = self.scan_documentation()

        # Afficher les statistiques
        logger.info("📊 Statistiques:")
        logger.info(f"  - Documents actuels: {len(categories['current'])}")
        logger.info(f"  - Documents obsolètes: {len(categories['obsolete'])}")
        logger.info(f"  - Documents inconnus: {len(categories['unknown'])}")

        # Actions de nettoyage
        archived_count = 0

        if not dry_run:
            # Archiver les documents obsolètes
            archived_count = self.archive_obsolete_docs(categories['obsolete'])

        # Générer le rapport
        report = self.create_documentation_report(categories, archived_count)

        # Sauvegarder le rapport
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = self.docs_dir / f"cleanup_report_{timestamp}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Afficher le résumé
        logger.info("✅ NETTOYAGE TERMINÉ")
        logger.info(f"📦 Documents archivés: {archived_count}")
        logger.info(f"📄 Rapport sauvegardé: {report_file}")

        return report


def main():
    """Fonction principale"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Nettoyage intelligent de la documentation"
    )
    parser.add_argument("--dry-run", action="store_true", help="Mode simulation")
    parser.add_argument("--docs-dir", default="docs", help="Dossier de documentation")

    args = parser.parse_args()

    # Créer le nettoyeur
    cleaner = DocumentationCleaner(args.docs_dir)

    # Exécuter le nettoyage
    cleaner.cleanup(dry_run=args.dry_run)


if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Script de nettoyage des rapports Athalia
Supprime les rapports anciens (>90 jours) pour économiser l'espace disque
"""
import argparse
import logging
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ReportCleaner:
    """Nettoyeur de rapports avec rétention configurable"""

    def __init__(self, project_root: Path, retention_days: int = 90):
        self.project_root = project_root
        self.retention_days = retention_days
        self.cutoff_date = datetime.now() - timedelta(days=retention_days)

        # Dossiers de rapports à nettoyer
        self.report_dirs = [
            "data/reports/security",
            "data/reports/quality",
            "data/reports/testing",
            "data/reports/performance",
            "data/reports/coverage",
            "test-results",
            "coverage",
            "htmlcov",
            ".pytest_cache",
            "__pycache__",
        ]

        # Extensions de fichiers à nettoyer
        self.report_extensions = {
            ".json",
            ".xml",
            ".html",
            ".csv",
            ".log",
            ".txt",
            ".md",
            ".pdf",
            ".png",
            ".jpg",
        }

    def is_old_file(self, file_path: Path) -> bool:
        """Vérifie si un fichier est plus ancien que la rétention"""
        try:
            file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            return file_mtime < self.cutoff_date
        except (OSError, ValueError):
            return False

    def should_clean_file(self, file_path: Path) -> bool:
        """Détermine si un fichier doit être nettoyé"""
        # Vérifier l'extension
        if file_path.suffix.lower() not in self.report_extensions:
            return False

        # Vérifier l'âge
        if not self.is_old_file(file_path):
            return False

        # Exclure les fichiers importants
        important_files = {
            "README.md",
            "index.md",
            "requirements.txt",
            "pyproject.toml",
            "setup.py",
        }

        if file_path.name in important_files:
            return False

        return True

    def clean_directory(self, dir_path: Path) -> dict:
        """Nettoie un répertoire et retourne les statistiques"""
        stats = {
            "files_checked": 0,
            "files_deleted": 0,
            "dirs_deleted": 0,
            "space_freed": 0,
            "errors": 0,
        }

        if not dir_path.exists():
            logger.warning(f"Répertoire inexistant: {dir_path}")
            return stats

        try:
            # Nettoyer les fichiers
            for file_path in dir_path.rglob("*"):
                if file_path.is_file():
                    stats["files_checked"] += 1

                    if self.should_clean_file(file_path):
                        try:
                            file_size = file_path.stat().st_size
                            file_path.unlink()
                            stats["files_deleted"] += 1
                            stats["space_freed"] += file_size
                            logger.debug(f"Supprimé: {file_path}")
                        except OSError as e:
                            stats["errors"] += 1
                            logger.error(f"Erreur suppression {file_path}: {e}")

            # Nettoyer les répertoires vides
            for subdir in sorted(
                dir_path.rglob("*"), key=lambda p: len(p.parts), reverse=True
            ):
                if subdir.is_dir() and subdir != self.project_root:
                    try:
                        if not any(subdir.iterdir()):  # Répertoire vide
                            subdir.rmdir()
                            stats["dirs_deleted"] += 1
                            logger.debug(f"Répertoire supprimé: {subdir}")
                    except OSError:
                        pass  # Ignorer les erreurs de suppression de répertoires

        except Exception as e:
            logger.error(f"Erreur lors du nettoyage de {dir_path}: {e}")
            stats["errors"] += 1

        return stats

    def clean_all_reports(self, dry_run: bool = False) -> dict:
        """Nettoie tous les rapports"""
        total_stats = {
            "files_checked": 0,
            "files_deleted": 0,
            "dirs_deleted": 0,
            "space_freed": 0,
            "errors": 0,
        }

        logger.info(
            f"🧹 Nettoyage des rapports (rétention: {self.retention_days} jours)"
        )
        logger.info(
            f"📅 Date de coupure: {self.cutoff_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        if dry_run:
            logger.info("🔍 Mode simulation (dry-run) - aucun fichier ne sera supprimé")

        for report_dir in self.report_dirs:
            dir_path = self.project_root / report_dir
            logger.info(f"📁 Nettoyage de: {dir_path}")

            if dry_run:
                # Mode simulation - compter seulement
                stats = self._simulate_clean_directory(dir_path)
            else:
                stats = self.clean_directory(dir_path)

            # Accumuler les statistiques
            for key in total_stats:
                total_stats[key] += stats[key]

            if stats["files_deleted"] > 0 or stats["dirs_deleted"] > 0:
                logger.info(
                    f"  ✅ {stats['files_deleted']} fichiers, {stats['dirs_deleted']} dossiers"
                )
            else:
                logger.info("  ℹ️  Aucun élément à nettoyer")

        return total_stats

    def _simulate_clean_directory(self, dir_path: Path) -> dict:
        """Simule le nettoyage sans supprimer"""
        stats = {
            "files_checked": 0,
            "files_deleted": 0,
            "dirs_deleted": 0,
            "space_freed": 0,
            "errors": 0,
        }

        if not dir_path.exists():
            return stats

        try:
            for file_path in dir_path.rglob("*"):
                if file_path.is_file():
                    stats["files_checked"] += 1
                    if self.should_clean_file(file_path):
                        file_size = file_path.stat().st_size
                        stats["files_deleted"] += 1
                        stats["space_freed"] += file_size
                        logger.debug(f"[SIMULATION] Supprimerait: {file_path}")
        except Exception as e:
            logger.error(f"Erreur simulation {dir_path}: {e}")
            stats["errors"] += 1

        return stats

    def format_size(self, size_bytes: int) -> str:
        """Formate la taille en unités lisibles"""
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Nettoyage des rapports Athalia")
    parser.add_argument(
        "--retention-days",
        type=int,
        default=90,
        help="Nombre de jours de rétention (défaut: 90)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Mode simulation (ne supprime rien)"
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Racine du projet (défaut: répertoire courant)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Mode verbeux")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Vérifier que nous sommes dans le bon répertoire
    if not (args.project_root / "pyproject.toml").exists():
        logger.error("❌ pyproject.toml non trouvé - mauvais répertoire de projet")
        sys.exit(1)

    # Créer le nettoyeur
    cleaner = ReportCleaner(args.project_root, args.retention_days)

    # Exécuter le nettoyage
    try:
        stats = cleaner.clean_all_reports(dry_run=args.dry_run)

        # Afficher le résumé
        logger.info("=" * 50)
        logger.info("📊 RÉSUMÉ DU NETTOYAGE")
        logger.info("=" * 50)
        logger.info(f"📁 Fichiers vérifiés: {stats['files_checked']}")
        logger.info(f"🗑️  Fichiers supprimés: {stats['files_deleted']}")
        logger.info(f"📂 Dossiers supprimés: {stats['dirs_deleted']}")
        logger.info(f"💾 Espace libéré: {cleaner.format_size(stats['space_freed'])}")
        logger.info(f"❌ Erreurs: {stats['errors']}")

        if args.dry_run:
            logger.info("🔍 Mode simulation - aucun fichier supprimé")
        else:
            logger.info("✅ Nettoyage terminé")

    except KeyboardInterrupt:
        logger.info("⏹️  Nettoyage interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Erreur fatale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

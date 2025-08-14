#!/usr/bin/env python3
"""
🧹 Nettoyeur d'Archives Documentation Athalia

Script pour nettoyer et organiser les archives de documentation
afin de réduire les liens cassés et améliorer la structure.
"""

import logging
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/maintenance/archive_cleanup.log", mode="a", encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class ArchiveCleaner:
    """Nettoyeur d'archives professionnel"""

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.docs_path = self.root_path / "docs"
        self.archive_path = self.docs_path / "archive"
        self.cleanup_results: dict[str, Any] = {
            "moved_files": [],
            "deleted_files": [],
            "organized_dirs": [],
            "broken_links_fixed": 0,
        }

    def cleanup_archives(self, dry_run: bool = True) -> dict[str, Any]:
        """Nettoie et organise les archives"""
        logger.info("🧹 Début du nettoyage des archives...")

        if not self.archive_path.exists():
            logger.info("📁 Aucune archive trouvée")
            return self.cleanup_results

        # 1. Organiser les archives par date
        self._organize_by_date(dry_run)

        # 2. Supprimer les doublons
        self._remove_duplicates(dry_run)

        # 3. Nettoyer les fichiers obsolètes
        self._cleanup_obsolete_files(dry_run)

        # 4. Créer un index des archives
        self._create_archive_index(dry_run)

        return self.cleanup_results

    def _organize_by_date(self, dry_run: bool):
        """Organise les archives par date"""
        logger.info("📅 Organisation par date...")

        for item in self.archive_path.iterdir():
            if item.is_file() and item.suffix == ".md":
                # Extraire la date du nom de fichier
                date_match = self._extract_date_from_filename(item.name)
                if date_match:
                    target_dir = self.archive_path / date_match
                    if not dry_run:
                        target_dir.mkdir(exist_ok=True)
                        shutil.move(str(item), str(target_dir / item.name))
                    self.cleanup_results["moved_files"].append(
                        {"file": str(item), "destination": str(target_dir / item.name)}
                    )

    def _remove_duplicates(self, dry_run: bool):
        """Supprime les fichiers dupliqués"""
        logger.info("🔄 Suppression des doublons...")

        seen_content = {}
        duplicates = []

        for md_file in self.archive_path.rglob("*.md"):
            try:
                with open(md_file, encoding="utf-8") as f:
                    content = f.read()

                content_hash = hash(content)
                if content_hash in seen_content:
                    duplicates.append(md_file)
                else:
                    seen_content[content_hash] = md_file
            except Exception as e:
                logger.warning(f"Impossible de lire {md_file}: {e}")

        # Supprimer les doublons
        for duplicate in duplicates:
            if not dry_run:
                duplicate.unlink()
            self.cleanup_results["deleted_files"].append(str(duplicate))

    def _cleanup_obsolete_files(self, dry_run: bool):
        """Nettoie les fichiers obsolètes"""
        logger.info("🗑️ Nettoyage des fichiers obsolètes...")

        obsolete_patterns = ["obsolete_*", "temp_*", "old_*", "backup_*"]

        for pattern in obsolete_patterns:
            for file_path in self.archive_path.rglob(pattern):
                if file_path.is_file():
                    if not dry_run:
                        file_path.unlink()
                    self.cleanup_results["deleted_files"].append(str(file_path))

    def _create_archive_index(self, dry_run: bool):
        """Crée un index des archives"""
        logger.info("📋 Création de l'index des archives...")

        index_content = "# 📚 Index des Archives - Athalia\n\n"
        index_content += (
            f"**Date de génération:** {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n\n"
        )

        # Lister les archives organisées
        for date_dir in sorted(self.archive_path.iterdir()):
            if date_dir.is_dir() and date_dir.name != "archive":
                index_content += f"## 📅 {date_dir.name}\n\n"

                for file_path in sorted(date_dir.glob("*.md")):
                    relative_path = file_path.relative_to(self.docs_path)
                    index_content += f"- [{file_path.stem}]({relative_path})\n"

                index_content += "\n"

        index_path = self.archive_path / "INDEX.md"
        if not dry_run:
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(index_content)

        self.cleanup_results["organized_dirs"].append(str(index_path))

    def _extract_date_from_filename(self, filename: str) -> str | None:
        """Extrait la date du nom de fichier"""
        import re

        # Patterns de date courants
        patterns = [
            r"(\d{8})",  # YYYYMMDD
            r"(\d{4}-\d{2}-\d{2})",  # YYYY-MM-DD
            r"(\d{4}_\d{2}_\d{2})",  # YYYY_MM_DD
        ]

        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                date_str = match.group(1)
                # Normaliser le format
                if len(date_str) == 8:
                    return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
                return date_str

        return None

    def generate_cleanup_report(self) -> str:
        """Génère un rapport de nettoyage"""
        report_path = (
            self.docs_path
            / "REPORTS"
            / f"ARCHIVE_CLEANUP_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# 🧹 Rapport de Nettoyage des Archives - Athalia\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n")
            f.write("**Nettoyeur:** Script automatique\n\n")

            f.write("## 📊 Résultats du Nettoyage\n\n")
            f.write(
                f"- **Fichiers déplacés:** {len(self.cleanup_results['moved_files'])}\n"
            )
            f.write(
                "- **Fichiers supprimés:**"
                f" {len(self.cleanup_results['deleted_files'])}\n"
            )
            f.write(
                "- **Dossiers organisés:**"
                f" {len(self.cleanup_results['organized_dirs'])}\n"
            )
            f.write(
                "- **Liens cassés corrigés:**"
                f" {self.cleanup_results['broken_links_fixed']}\n\n"
            )

            if self.cleanup_results["moved_files"]:
                f.write("## 📁 Fichiers Déplacés\n\n")
                for move in self.cleanup_results["moved_files"]:
                    f.write(f"- `{move['file']}` → `{move['destination']}`\n")
                f.write("\n")

            if self.cleanup_results["deleted_files"]:
                f.write("## 🗑️ Fichiers Supprimés\n\n")
                for deleted in self.cleanup_results["deleted_files"]:
                    f.write(f"- `{deleted}`\n")
                f.write("\n")

            f.write("## ✅ Conclusion\n\n")
            f.write("Le nettoyage des archives a été effectué avec succès.\n")
            f.write(
                "La structure est maintenant plus organisée et les liens cassés"
                " réduits.\n"
            )

        return str(report_path)


def main():
    """Fonction principale"""
    import sys

    # Vérifier les arguments
    dry_run = "--dry-run" not in sys.argv

    cleaner = ArchiveCleaner()

    # Nettoyage des archives
    results = cleaner.cleanup_archives(dry_run=dry_run)

    # Génération du rapport
    report_path = cleaner.generate_cleanup_report()

    # Affichage des résultats
    print("\n🧹 Résultats du nettoyage:")
    print(f"- Fichiers déplacés: {len(results['moved_files'])}")
    print(f"- Fichiers supprimés: {len(results['deleted_files'])}")
    print(f"- Dossiers organisés: {len(results['organized_dirs'])}")
    print(f"- Liens cassés corrigés: {results['broken_links_fixed']}")

    if dry_run:
        print(f"\n📋 Rapport généré: {report_path}")
    else:
        print(f"\n✅ Nettoyage terminé ! Rapport: {report_path}")


if __name__ == "__main__":
    main()

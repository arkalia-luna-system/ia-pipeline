#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛠️ Organisateur de Workspace Athalia

Script de maintenance pour maintenir l'organisation professionnelle
du workspace Athalia selon les standards définis.
"""

import logging
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/workspace_organizer.log", mode="a", encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class WorkspaceOrganizer:
    """Organisateur de workspace professionnel"""

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.organization_rules = self._load_organization_rules()

    def _load_organization_rules(self) -> Dict[str, List[str]]:
        """Charge les règles d'organisation"""
        return {
            # Fichiers à conserver en racine
            "root_files": [
                "README.md",
                "LICENSE",
                "CHANGELOG.md",
                "requirements.txt",
                "pytest.ini",
                "activate_venv.sh",
                "athalia_unified.py",
                "athalia.f(f",
                ".gitignore",
                ".coverage",
                ".pytestignore",
            ],
            # Scripts de démonstration et validation
            "scripts": ["demo_*.py", "validation_*.py", "test_logging_*.py"],
            # Outils de nettoyage
            "tools_cleanup": ["cleanup_*.py"],
            # Scripts système
            "bin": ["*.sh", "ark-*.sh"],
            # Rapports de validation
            "data_reports": ["rapport_validation_*.md"],
            # Dashboards
            "dashboard": ["*.html"],
            # Documentation
            "docs": ["*.md", "audit_*.md", "dashboard.md"],
        }

    def scan_workspace(self) -> Dict[str, List[Path]]:
        """Scanne le workspace et catégorise les fichiers"""
        logger.info("🔍 Scan du workspace en cours...")

        files_by_category = {
            "root_files": [],
            "scripts": [],
            "tools_cleanup": [],
            "bin": [],
            "data_reports": [],
            "dashboard": [],
            "docs": [],
            "unclassified": [],
        }

        # Scanner tous les fichiers en racine
        for file_path in self.root_path.iterdir():
            if file_path.is_file():
                categorized = False

                # Vérifier chaque catégorie
                for category, patterns in self.organization_rules.items():
                    if category == "root_files":
                        if file_path.name in patterns:
                            files_by_category[category].append(file_path)
                            categorized = True
                            break
                    else:
                        for pattern in patterns:
                            if self._matches_pattern(file_path.name, pattern):
                                files_by_category[category].append(file_path)
                                categorized = True
                                break
                        if categorized:
                            break

                if not categorized:
                    files_by_category["unclassified"].append(file_path)

        return files_by_category

    def _matches_pattern(self, filename: str, pattern: str) -> bool:
        """Vérifie si un nom de fichier correspond à un pattern"""
        import fnmatch

        return fnmatch.fnmatch(filename, pattern)

    def organize_files(self, dry_run: bool = True) -> Dict[str, Any]:
        """Organise les fichiers selon les règles"""
        logger.info("📁 Organisation des fichiers...")

        files_by_category = self.scan_workspace()
        moved_files = []

        # Créer les dossiers nécessaires
        directories = {
            "scripts": self.root_path / "scripts",
            "tools_cleanup": self.root_path / "tools" / "cleanup",
            "bin": self.root_path / "bin",
            "data_reports": self.root_path / "data" / "reports",
            "dashboard": self.root_path / "dashboard",
            "docs": self.root_path / "docs",
        }

        if not dry_run:
            for dir_path in directories.values():
                dir_path.mkdir(parents=True, exist_ok=True)

        # Déplacer les fichiers
        for category, files in files_by_category.items():
            if category in directories and files:
                target_dir = directories[category]

                for file_path in files:
                    target_path = target_dir / file_path.name

                    if dry_run:
                        logger.info(
                            f"📋 [DRY RUN] {file_path} → {target_path}"
                        )
                        moved_files.append((file_path, target_path))
                    else:
                        try:
                            shutil.move(str(file_path), str(target_path))
                            logger.info(f"✅ {file_path} → {target_path}")
                            moved_files.append((file_path, target_path))
                        except Exception as e:
                            logger.error(
                                f"❌ Erreur lors du déplacement de {file_path}: {e}"
                            )

        return {
            "moved_files": moved_files,
            "files_by_category": files_by_category,
        }

    def generate_organization_report(
        self, files_by_category: Dict[str, List[Path]]
    ) -> str:
        """Génère un rapport d'organisation"""
        report = []
        report.append("# 📊 Rapport d'Organisation du Workspace")
        report.append(
            f"**Date :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report.append("")

        total_files = sum(len(files) for files in files_by_category.values())
        report.append(f"**Total de fichiers analysés :** {total_files}")
        report.append("")

        for category, files in files_by_category.items():
            if files:
                report.append(f"## 📂 {category.upper()}")
                report.append(f"**Nombre de fichiers :** {len(files)}")
                report.append("")

                for file_path in files:
                    report.append(f"- `{file_path.name}`")
                report.append("")

        return "\n".join(report)

    def cleanup_temp_files(self, dry_run: bool = True) -> List[Path]:
        """Nettoie les fichiers temporaires"""
        logger.info("🧹 Nettoyage des fichiers temporaires...")

        temp_patterns = [
            "*.tmp",
            "*.temp",
            "*.bak",
            "*.backup",
            "*.log",
            "._*",
            ".DS_Store",
            "Thumbs.db",
        ]

        temp_files = []

        for pattern in temp_patterns:
            for file_path in self.root_path.rglob(pattern):
                if file_path.is_file():
                    temp_files.append(file_path)

                    if dry_run:
                        logger.info(f"📋 [DRY RUN] Suppression : {file_path}")
                    else:
                        try:
                            file_path.unlink()
                            logger.info(f"🗑️ Supprimé : {file_path}")
                        except Exception as e:
                            logger.error(
                                f"❌ Erreur lors de la suppression de {file_path}: {e}"
                            )

        return temp_files

    def validate_organization(self) -> Dict[str, bool]:
        """Valide l'organisation actuelle"""
        logger.info("✅ Validation de l'organisation...")

        validation_results = {}

        # Vérifier que les dossiers essentiels existent
        essential_dirs = [
            "scripts",
            "tools",
            "bin",
            "data",
            "dashboard",
            "docs",
            "tests",
        ]

        for dir_name in essential_dirs:
            dir_path = self.root_path / dir_name
            validation_results[f"directory_{dir_name}"] = dir_path.exists()

        # Vérifier que les fichiers essentiels sont en racine
        essential_files = [
            "README.md",
            "LICENSE",
            "requirements.txt",
            "athalia_unified.py",
        ]

        for file_name in essential_files:
            file_path = self.root_path / file_name
            validation_results[f"file_{file_name}"] = file_path.exists()

        return validation_results


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Organisateur de Workspace Athalia"
    )
    parser.add_argument(
        "--root", default=".", help="Chemin racine du workspace"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Mode simulation"
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Nettoyer les fichiers temporaires",
    )
    parser.add_argument(
        "--validate", action="store_true", help="Valider l'organisation"
    )
    parser.add_argument(
        "--report", action="store_true", help="Générer un rapport"
    )

    args = parser.parse_args()

    organizer = WorkspaceOrganizer(args.root)

    if args.dry_run:
        logger.info("🔍 Mode simulation activé")

    # Scan et organisation
    files_by_category = organizer.scan_workspace()
    organization_result = organizer.organize_files(dry_run=args.dry_run)

    # Nettoyage des fichiers temporaires
    if args.cleanup:
        temp_files = organizer.cleanup_temp_files(dry_run=args.dry_run)
        logger.info(f"📋 {len(temp_files)} fichiers temporaires identifiés")

    # Validation
    if args.validate:
        validation_results = organizer.validate_organization()
        logger.info("📊 Résultats de validation :")
        for check, result in validation_results.items():
            status = "✅" if result else "❌"
            logger.info(f"  {status} {check}")

    # Rapport
    if args.report:
        report = organizer.generate_organization_report(files_by_category)
        report_path = (
            Path("logs")
            / f"workspace_organization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )
        report_path.parent.mkdir(exist_ok=True)

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        logger.info(f"📄 Rapport généré : {report_path}")

    logger.info("🎯 Organisation du workspace terminée !")


if __name__ == "__main__":
    main()

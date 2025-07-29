#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de sauvegarde pour Athalia
"""

import json
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BackupManager:
    """Gestionnaire de sauvegardes pour Athalia"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.backup_dir = self.project_root / "backups" / "daily"
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_backup(self, backup_name: Optional[str] = None) -> str:
        """Crée une nouvelle sauvegarde"""
        if not backup_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"backup_{timestamp}"

        backup_path = self.backup_dir / backup_name
        backup_path.mkdir(exist_ok=True)

        # Patterns d'exclusion
        exclude_patterns = [
            "__pycache__",
            "*.pyc",
            ".git",
            "venv",
            "node_modules",
            "*.log",
            ".DS_Store",
            "backups",
            "archive",
        ]

        logger.info(f"Création de la sauvegarde: {backup_name}")

        # Copie des fichiers
        for item in self.project_root.iterdir():
            if item.name == backup_name:
                continue

            if item.is_file():
                self._copy_file(item, backup_path, exclude_patterns)
            elif item.is_dir():
                self._copy_directory(item, backup_path, exclude_patterns)

        # Métadonnées de sauvegarde
        metadata = {
            "backup_name": backup_name,
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "files_count": len(list(backup_path.rglob("*"))),
        }

        metadata_file = backup_path / "backup_metadata.json"
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)

        logger.info(f"Sauvegarde terminée: {backup_path}")
        return str(backup_path)

    def _copy_file(self, src: Path, dst_dir: Path, exclude_patterns: List[str]) -> None:
        """Copie un fichier en respectant les exclusions"""
        if self._should_exclude(src, exclude_patterns):
            return

        dst_file = dst_dir / src.relative_to(self.project_root)
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst_file)

    def _copy_directory(
        self, src: Path, dst_dir: Path, exclude_patterns: List[str]
    ) -> None:
        """Copie un répertoire en respectant les exclusions"""
        if self._should_exclude(src, exclude_patterns):
            return

        dst_path = dst_dir / src.relative_to(self.project_root)
        if not dst_path.exists():
            shutil.copytree(
                src, dst_path, ignore=shutil.ignore_patterns(*exclude_patterns)
            )

    def _should_exclude(self, path: Path, exclude_patterns: List[str]) -> bool:
        """Vérifie si un chemin doit être exclu"""
        path_str = str(path)
        return any(pattern.replace("*", "") in path_str for pattern in exclude_patterns)

    def list_backups(self) -> List[Dict]:
        """Liste toutes les sauvegardes disponibles"""
        backups = []
        for backup_dir in self.backup_dir.iterdir():
            if backup_dir.is_dir():
                metadata_file = backup_dir / "backup_metadata.json"
                if metadata_file.exists():
                    with open(metadata_file) as f:
                        metadata = json.load(f)
                        backups.append(metadata)
        return sorted(backups, key=lambda x: x["timestamp"], reverse=True)

    def restore_backup(
        self, backup_name: str, target_dir: Optional[str] = None
    ) -> bool:
        """Restaure une sauvegarde"""
        backup_path = self.backup_dir / backup_name
        if not backup_path.exists():
            logger.error(f"Sauvegarde non trouvée: {backup_name}")
            return False

        target_path = Path(target_dir) if target_dir else self.project_root

        logger.info(f"Restauration de {backup_name} vers {target_path}")

        try:
            # Copie des fichiers de sauvegarde
            for item in backup_path.iterdir():
                if item.name == "backup_metadata.json":
                    continue

                if item.is_file():
                    shutil.copy2(item, target_path / item.name)
                elif item.is_dir():
                    if (target_path / item.name).exists():
                        shutil.rmtree(target_path / item.name)
                    shutil.copytree(item, target_path / item.name)

            logger.info("Restauration terminée avec succès")
            return True

        except Exception as e:
            logger.error(f"Erreur lors de la restauration: {e}")
            return False


def main():
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="Script de sauvegarde Athalia")
    parser.add_argument(
        "action", choices=["create", "list", "restore"], help="Action à effectuer"
    )
    parser.add_argument("--name", help="Nom de la sauvegarde")
    parser.add_argument("--target", help="Répertoire cible pour la restauration")
    parser.add_argument("--project-root", default=".", help="Racine du projet")

    args = parser.parse_args()

    backup_manager = BackupManager(args.project_root)

    if args.action == "create":
        backup_path = backup_manager.create_backup(args.name)
        print(f"Sauvegarde créée: {backup_path}")

    elif args.action == "list":
        backups = backup_manager.list_backups()
        print("Sauvegardes disponibles:")
        for backup in backups:
            print(f"  - {backup['backup_name']} ({backup['timestamp']})")

    elif args.action == "restore":
        if not args.name:
            print("Erreur: nom de sauvegarde requis pour la restauration")
            sys.exit(1)

        success = backup_manager.restore_backup(args.name, args.target)
        if not success:
            sys.exit(1)


if __name__ == "__main__":
    main()

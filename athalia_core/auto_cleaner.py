#!/usr/bin/env python3
from pathlib import Path
from typing import Dict, List, Any, Set
import json
import os
import re
import hashlib
import argparse
from datetime import datetime, timedelta
import shutil
import logging

logger = logging.getLogger(__name__)

"""
Module de nettoyage automatique pour Athalia
Suppression intelligente des fichiers parasites et optimisation
"""


class AutoCleaner:
    """Nettoyeur automatique pour Athalia"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.dry_run = False
        self.cleaned_files: List[Dict[str, Any]] = []
        self.cleaned_dirs: List[Dict[str, Any]] = []
        self.errors: List[str] = []
        self.stats: Dict[str, Any] = {
            "files_removed": 0,
            "dirs_removed": 0,
            "space_freed_mb": 0.0,
            "errors": 0
        }

    def clean_project(self, dry_run: bool = False) -> Dict[str, Any]:
        """Nettoyage complet d'un projet"""
        self.dry_run = dry_run
        project_path_obj = self.project_path

        logger.info(
            f"🧹 Nettoyage automatique en cours pour : {project_path_obj.name}")
        if dry_run:
            logger.info("🔍 Mode simulation - aucun fichier ne sera supprimé")

        # Nettoyages en séquence
        self._clean_system_files(project_path_obj)
        self._clean_cache_files(project_path_obj)
        self._clean_backup_files(project_path_obj)
        self._clean_temp_files(project_path_obj)
        self._clean_duplicate_files(project_path_obj)
        self._clean_empty_directories(project_path_obj)
        self._clean_old_files(project_path_obj)
        self._clean_large_files(project_path_obj)

        return self._generate_cleanup_report()

    def run(self) -> Dict[str, Any]:
        """Méthode run() pour l'orchestrateur - exécute le nettoyage"""
        return self.clean_project(dry_run=False)

    def _clean_system_files(self, project_path: Path):
        """Nettoyage des fichiers système"""
        system_patterns = [
            ".DS_Store",  # macOS
            "Thumbs.db",  # Windows
            ".Spotlight-V100",  # macOS
            ".Trashes",  # macOS
            "ehthumbs.db",  # Windows
            "Desktop.ini",  # Windows
            "._*",  # macOS metadata
            ".!*",
            # Fichiers temporaires macOS spécifiques (comme .!44956!*.clean)
            "*.clean",  # Fichiers de nettoyage temporaires
            "*.apdisk",  # Apple Partition Map
            ".fseventsd",  # File System Events
            ".TemporaryItems",  # Items temporaires
            "._.DS_Store",  # AppleDouble DS_Store
            ".AppleDouble",  # Dossier AppleDouble
            ".LSOverride",  # Launch Services Override
        ]

        for pattern in system_patterns:
            for file_path in project_path.rglob(pattern):
                self._safe_remove_file(
                    file_path, f"Fichier système: {pattern}")

        # Nettoyage spécifique des dossiers macOS
        macos_dirs = [
            ".Spotlight-V100",
            ".Trashes",
            ".fseventsd",
            ".TemporaryItems",
            ".AppleDouble",
            ".LSOverride"
        ]

        for dir_name in macos_dirs:
            for dir_path in project_path.rglob(dir_name):
                if dir_path.is_dir():
                    self._safe_remove_dir(
                        dir_path, f"Dossier système macOS: {dir_name}")

    def _clean_cache_files(self, project_path: Path):
        """Nettoyage des fichiers de cache"""
        cache_patterns = [
            "__pycache__",
            "*.pyc",
            "*.pyo",
            ".mypy_cache",
            ".pytest_cache",
            ".cache",
            ".ipynb_checkpoints",
            ".vscode",
            ".idea",
            ".eggs",
            "*.egg-info",
            ".tox",
            ".coverage",
            ".hypothesis",
            ".nox",
            ".env",
            ".venv",
            "*.log",
            "*.tmp",
            "*.temp",
            "*.bak",
        ]

        for pattern in cache_patterns:
            for file_path in project_path.rglob(pattern):
                if file_path.is_dir():
                    self._safe_remove_dir(file_path, f"Cache: {pattern}")
                else:
                    self._safe_remove_file(file_path, f"Cache: {pattern}")

    def _clean_backup_files(self, project_path: Path):
        """Nettoyage des fichiers de sauvegarde"""
        backup_patterns = [
            "*~",  # Vim
            "*.bak",
            "*.old",
            "*.orig",
            "*.swp",
            "*_backup*",
            "*_old*",
            "backup*",
            ".swo",  # Vim swap
            ".swp",  # Vim swap
        ]

        for pattern in backup_patterns:
            for file_path in project_path.rglob(pattern):
                self._safe_remove_file(file_path, f"Backup: {pattern}")

    def _clean_temp_files(self, project_path: Path):
        """Nettoyage des fichiers temporaires"""
        temp_patterns = [
            "*.tmp",
            "*.temp",
            "temp*",
            "tmp*",
            ".tmp*",
            ".temp*",
        ]

        for pattern in temp_patterns:
            for file_path in project_path.rglob(pattern):
                self._safe_remove_file(file_path, f"Temporaire: {pattern}")

    def _clean_duplicate_files(self, project_path: Path):
        """Nettoyage des fichiers dupliqués"""
        file_hashes: Dict[str, Path] = {}
        duplicates = []

        # Calcul des hashes pour les fichiers de code
        for file_path in project_path.rglob("*"):
            if file_path.is_file() and self._is_code_file(file_path):
                try:
                    file_hash = self._calculate_file_hash(file_path)
                    if file_hash in file_hashes:
                        duplicates.append((file_hashes[file_hash], file_path))
                    else:
                        file_hashes[file_hash] = file_path
                except Exception:
                    pass

        # Suppression des doublons (garder le plus ancien)
        for original, duplicate in duplicates:
            if original.stat().st_mtime < duplicate.stat().st_mtime:
                self._safe_remove_file(duplicate, "Fichier dupliqué")
            else:
                self._safe_remove_file(original, "Fichier dupliqué")

    def _clean_empty_directories(self, project_path: Path):
        """Nettoyage des répertoires vides"""
        # Parcours en profondeur pour traiter les sous-dossiers d'abord
        for root, dirs, files in os.walk(project_path, topdown=False):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                if self._is_empty_directory(dir_path):
                    self._safe_remove_dir(dir_path, "Répertoire vide")

    def _clean_old_files(self, project_path: Path):
        """Nettoyage des fichiers anciens"""
        cutoff_date = datetime.now() - timedelta(days=365)  # 1 an

        for file_path in project_path.rglob("*"):
            if file_path.is_file():
                try:
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime < cutoff_date and not self._is_important_file(
                            file_path):
                        self._safe_remove_file(
                            file_path, "Fichier ancien (>1 an)")
                except Exception:
                    pass

    def _clean_large_files(self, project_path: Path):
        """Nettoyage des fichiers volumineux"""
        max_size_mb = 50  # 50MB

        for file_path in project_path.rglob("*"):
            if file_path.is_file():
                try:
                    size_mb = file_path.stat().st_size / (1024 * 1024)
                    if size_mb > max_size_mb and not self._is_important_file(
                            file_path):
                        self._safe_remove_file(
                            file_path, f"Fichier volumineux ({size_mb:.1f}MB)")
                except Exception:
                    pass

    def _safe_remove_file(self, file_path: Path, reason: str):
        """Suppression sécurisée d'un fichier"""
        try:
            if not self.dry_run:
                file_size = file_path.stat().st_size / (1024 * 1024)  # MB
                file_path.unlink()
                self.cleaned_files.append({
                    "path": str(file_path),
                    "reason": reason,
                    "size_mb": file_size
                })
                self.stats["files_removed"] += 1
                self.stats["space_freed_mb"] += file_size
            else:
                logger.info(
                    f"🔍 Simulation: Suppression de {file_path} ({reason})")

        except Exception as e:
            self.errors.append(f"Erreur suppression {file_path}: {e}")
            self.stats["errors"] += 1

    def _safe_remove_dir(self, dir_path: Path, reason: str):
        """Suppression sécurisée d'un répertoire"""
        try:
            if not self.dry_run:
                shutil.rmtree(dir_path)
                self.stats["dirs_removed"] += 1

            self.cleaned_dirs.append({
                "path": str(dir_path),
                "reason": reason
            })

        except Exception as e:
            self.errors.append(f"Erreur suppression {dir_path}: {e}")
            self.stats["errors"] += 1

    def _is_code_file(self, file_path: Path) -> bool:
        """Détermine si un fichier est un fichier de code"""
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.scala', '.cs',
            '.html', '.css', '.scss', '.sass', '.xml', '.json', '.yaml', '.yml'
        }
        return file_path.suffix.lower() in code_extensions

    def _is_important_file(self, file_path: Path) -> bool:
        """Détermine si un fichier est important (ex: config, requirements, etc.)"""
        important_patterns = [
            "README", "LICENSE", "requirements.txt", "package.json",
            "Makefile", "docker-compose.yml", ".env",
            "setup.py", "pyproject.toml", "Cargo.toml", "go.mod"
        ]

        file_name = file_path.name.lower()
        return any(
            pattern.lower() in file_name for pattern in important_patterns)

    def _is_empty_directory(self, dir_path: Path) -> bool:
        """Vérifie si un répertoire est vide"""
        try:
            return not any(dir_path.iterdir())
        except Exception:
            return False

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calcule le hash d'un fichier"""
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as file_handle:
                for chunk in iter(lambda: file_handle.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception:
            return ""

    def _generate_cleanup_report(self) -> Dict[str, Any]:
        """Génère le rapport de nettoyage"""
        reasons: Dict[str, List[Dict[str, Any]]] = {}
        for file_info in self.cleaned_files:
            reason = file_info["reason"]
            if reason not in reasons:
                reasons[reason] = []
            reasons[reason].append(file_info)

        return {
            "stats": self.stats,
            "files": self.cleaned_files,
            "dirs": self.cleaned_dirs,
            "errors": self.errors,
            "summary": self._generate_summary()
        }

    def _generate_summary(self) -> str:
        """Génère un résumé du nettoyage"""
        reasons: Dict[str, List[Dict[str, Any]]] = {}
        for file_info in self.cleaned_files:
            reason = file_info["reason"]
            if reason not in reasons:
                reasons[reason] = []
            reasons[reason].append(file_info)

        summary = f"""
{'='*60}
🧹 RAPPORT DE NETTOYAGE AUTOMATIQUE
{'='*60}

📊 STATISTIQUES:
• Fichiers supprimés: {self.stats['files_removed']}
• Répertoires supprimés: {self.stats['dirs_removed']}
• Espace libéré: {self.stats['space_freed_mb']:.1f} MB
• Erreurs: {self.stats['errors']}

📁 FICHIERS SUPPRIMÉS PAR CATÉGORIE:
"""
        for reason, files in reasons.items():
            summary += f"\n   {reason} ({len(files)} fichiers):"
            for file_info in files[:5]:  # Limiter à 5 exemples
                summary += f"\n     • {file_info['path']}"
            if len(files) > 5:
                summary += f"\n     • ... et {len(files)-5} autres"

        if self.cleaned_dirs:
            summary += f"\n📂 RÉPERTOIRES SUPPRIMÉS ({len(self.cleaned_dirs)}):"
            for dir_info in self.cleaned_dirs:
                summary += f"\n   • {dir_info['path']} ({dir_info['reason']})"

        if self.errors:
            summary += f"\n❌ ERREURS ({len(self.errors)}):"
            for error in self.errors[:5]:
                summary += f"\n   • {error}"

        summary += f"\n{'='*60}\n"
        return summary

    def optimize_project_structure(self, project_path: str) -> Dict[str, Any]:
        """Optimise la structure du projet"""
        project_path_obj = Path(project_path)
        optimizations = []

        logger.info(
            f"⚡ Optimisation de la structure pour : {project_path_obj.name}")

        # Création de répertoires standards
        standard_dirs = ["src", "tests", "docs", "data", "scripts", "assets"]
        for dir_name in standard_dirs:
            dir_path = project_path_obj / dir_name
            if not dir_path.exists():
                if not self.dry_run:
                    dir_path.mkdir(exist_ok=True)
                optimizations.append(f"Créé: {dir_name}/")

        # Déplacement des fichiers dans les bons répertoires
        self._organize_files(project_path_obj, optimizations)

        return {
            "optimizations": optimizations,
            "dry_run": self.dry_run
        }

    def _organize_files(self, project_path: Path, optimizations: List[str]):
        """Organise les fichiers dans la structure du projet"""
        # Déplacer les fichiers de test
        for file_path in project_path.rglob("*test*.py"):
            if file_path.parent != project_path / "tests":
                new_path = project_path / "tests" / file_path.name
                if not self.dry_run and not new_path.exists():
                    file_path.rename(new_path)
                    optimizations.append(f"Déplacé: {file_path.name} → tests/")

        # Déplacer les scripts
        for file_path in project_path.rglob("*.sh"):
            if file_path.parent != project_path / "scripts":
                new_path = project_path / "scripts" / file_path.name
                if not self.dry_run and not new_path.exists():
                    file_path.rename(new_path)
                    optimizations.append(
                        f"Déplacé: {file_path.name} → scripts/")

        # Déplacer les assets
        for ext in ["png", "jpg", "jpeg", "gif", "svg", "ico"]:
            for file_path in project_path.rglob(f"*.{ext}"):
                if file_path.parent != project_path / "assets":
                    new_path = project_path / "assets" / file_path.name
                if not self.dry_run and not new_path.exists():
                    file_path.rename(new_path)
                    optimizations.append(
                        f"Déplacé: {file_path.name} → assets/")


def main():
    """Point d'entrée du module AutoCleaner"""

    parser = argparse.ArgumentParser(description="Nettoyage automatique de f")
    parser.add_argument(
        "project_path",
        help="Chemin vers le projet à nettoyer")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mode simulation - aucun fichier ne sera supprimé")
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Optimiser la structure du projet")

    args = parser.parse_args()

    if not os.path.exists(args.project_path):
        logger.info(f"❌ Le chemin {args.project_path} n'existe pas")
        return

    # Configuration du logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s-%(message)s)')

    # Nettoyage
    cleaner = AutoCleaner(args.project_path)
    cleanup_report = cleaner.clean_project(dry_run=args.dry_run)

    # Affichage du rapport
    logger.info(cleanup_report["summary"])

    # Optimisation de structure si demandée
    if args.optimize:
        structure_report = cleaner.optimize_project_structure(
            args.project_path)
        logger.info("\n⚡ OPTIMISATIONS DE STRUCTURE:")
        for opt in structure_report["optimizations"]:
            logger.info(f"   • {opt}")

    # Sauvegarde du rapport
    report_file = f"cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(cleanup_report, f, indent=2, ensure_ascii=False)

    logger.info(f"\n📄 Rapport sauvegardé: {report_file}")


if __name__ == "__main__":
    main()

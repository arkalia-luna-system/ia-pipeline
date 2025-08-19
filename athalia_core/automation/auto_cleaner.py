#!/usr/bin/env python3
"""
Module auto_cleaner pour Athalia
Nettoyage automatique des projets
"""

import hashlib
import json
import logging
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

import yaml

from athalia_core.core.performance_optimizer import (
    PerformanceOptimizer,
    SecurityValidator,
    memory_efficient,
    performance_monitor,
)

logger = logging.getLogger(__name__)


class AutoCleaner:
    """Nettoyeur automatique de projets"""

    def __init__(self, project_path: str = "."):
        """Initialise le nettoyeur automatique"""
        self.project_path = Path(project_path)
        self.cleanup_config = self._load_cleanup_config()

        # Initialiser les listes avec des types appropriés
        self.cleanup_history: list[dict[str, Any]] = []
        self.cleaned_files: list[str] = []
        self.cleaned_dirs: list[str] = []
        self.errors: list[str] = []
        self.dry_run = False
        self.stats = {
            "files_removed": 0,
            "dirs_removed": 0,
            "space_freed_mb": 0,
            "errors": 0,
        }

        # Optimisations de performance et sécurité
        self.optimizer = PerformanceOptimizer()
        self.security_validator = SecurityValidator()

    def load_cleanup_config(self, config_path: str | None = None) -> dict[str, Any]:
        """Charge la configuration de nettoyage (méthode publique)"""
        return self._load_cleanup_config(config_path)

    def _load_cleanup_config(self, config_path: str | None = None) -> dict[str, Any]:
        """Charge la configuration de nettoyage (méthode privée)"""
        default_config = {
            "patterns_to_remove": [
                "*.pyc",
                "__pycache__",
                "*.log",
                "*.tmp",
                "*.swp",
                "*.swo",
                ".DS_Store",
                "Thumbs.db",
                "*.cache",
                "*.bak",
            ],
            "max_file_size_mb": 10,
            "keep_recent_days": 30,
            "exclude_patterns": [
                "*.git*",
                "*.svn*",
                "*.hg*",
                "node_modules",
                "venv",
                ".venv",
                "animation",
                "audio",
                "visualization",
                "artistic_templates",
            ],
            "cleanup_directories": [
                "__pycache__",
                ".cache",
                ".pytest_cache",
                "build",
                "dist",
                "*.egg-info",
                "target",
                "bin",
                "obj",
                "htmlcov",
            ],
        }

        if config_path:
            try:
                with open(config_path, encoding="utf-8") as f:
                    user_config = yaml.safe_load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(
                    f"Impossible de charger la configuration {config_path}: {e}"
                )

        return default_config

    def save_cleanup_history(self, output_path: str | None = None) -> str:
        """Sauvegarde l'historique de nettoyage"""
        if output_path is None:
            output_path = str(self.project_path / "cleanup_history.json")

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(self.cleanup_history, f, indent=2, default=str)
            return output_path
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde de l'historique: {e}")
            return ""

    @performance_monitor
    @memory_efficient
    def scan_for_cleanup_candidates(self) -> dict[str, list[Path]]:
        """Scanne le projet pour identifier les candidats au nettoyage"""
        candidates: dict[str, list[Path]] = {
            "pyc_files": [],
            "cache_dirs": [],
            "log_files": [],
            "temp_files": [],
            "build_artifacts": [],
            "test_artifacts": [],
            "duplicate_files": [],
            "large_files": [],
            "old_files": [],
            "files_to_remove": [],
            "directories_to_remove": [],
        }

        try:
            # Scanner les fichiers selon les patterns
            for pattern in self.cleanup_config["patterns_to_remove"]:
                if "*" in pattern:
                    # Pattern avec wildcard
                    for file_path in self.project_path.rglob(pattern):
                        if file_path.is_file() and not self._is_excluded(file_path):
                            candidates["files_to_remove"].append(file_path)
                else:
                    # Pattern exact
                    exact_path = self.project_path / pattern
                    if exact_path.exists() and not self._is_excluded(exact_path):
                        if exact_path.is_file():
                            candidates["files_to_remove"].append(exact_path)
                        elif exact_path.is_dir():
                            candidates["directories_to_remove"].append(exact_path)

            # Scanner les répertoires de nettoyage
            for dir_pattern in self.cleanup_config["cleanup_directories"]:
                if "*" in dir_pattern:
                    for dir_path in self.project_path.rglob(dir_pattern):
                        if dir_path.is_dir() and not self._is_excluded(dir_path):
                            candidates["directories_to_remove"].append(dir_path)
                else:
                    exact_dir = self.project_path / dir_pattern
                    if (
                        exact_dir.exists()
                        and exact_dir.is_dir()
                        and not self._is_excluded(exact_dir)
                    ):
                        candidates["directories_to_remove"].append(exact_dir)

            # Scanner les gros fichiers
            max_size = self.cleanup_config["max_file_size_mb"] * 1024 * 1024
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._is_excluded(file_path):
                    if file_path.stat().st_size > max_size:
                        candidates["large_files"].append(file_path)

            # Scanner les anciens fichiers
            cutoff_date = datetime.now() - timedelta(
                days=self.cleanup_config["keep_recent_days"]
            )
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._is_excluded(file_path):
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime < cutoff_date:
                        candidates["old_files"].append(file_path)

        except Exception as e:
            logger.error(f"Erreur scan candidats: {e}")

        return candidates

    def _is_excluded(self, path: Path) -> bool:
        """Vérifie si un chemin est exclu du nettoyage"""
        # Validation de sécurité
        if not self.security_validator.validate_file_path(path):
            return True

        path_str = str(path)
        for exclude_pattern in self.cleanup_config["exclude_patterns"]:
            if exclude_pattern in path_str:
                return True
        return False

    def cleanup_pyc_files(self) -> dict[str, Any]:
        """Nettoie les fichiers .pyc"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for pyc_file in self.scan_for_cleanup_candidates()["pyc_files"]:
            try:
                size = pyc_file.stat().st_size
                pyc_file.unlink()
                result["removed_files"].append(str(pyc_file))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(f"Erreur suppression {pyc_file}: {e}")

        return result

    def cleanup_cache_directories(self) -> dict[str, Any]:
        """Nettoie les répertoires de cache"""
        result: dict[str, Any] = {
            "removed_directories": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for cache_dir in self.scan_for_cleanup_candidates()["cache_dirs"]:
            try:
                size = self._get_directory_size(cache_dir)
                shutil.rmtree(cache_dir)
                result["removed_directories"].append(str(cache_dir))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(
                    f"Erreur suppression répertoire {cache_dir}: {e}"
                )

        return result

    def _get_directory_size(self, directory: Path) -> int:
        """Calcule la taille d'un répertoire"""
        total_size = 0
        try:
            for file_path in directory.rglob("*"):
                if file_path.is_file():
                    total_size += file_path.stat().st_size
        except Exception as e:
            logger.warning(f"Erreur calcul taille {directory}: {e}")
        return total_size

    def cleanup_log_files(self) -> dict[str, Any]:
        """Nettoie les fichiers de log"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for log_file in self.scan_for_cleanup_candidates()["log_files"]:
            try:
                size = log_file.stat().st_size
                log_file.unlink()
                result["removed_files"].append(str(log_file))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(f"Erreur suppression {log_file}: {e}")

        return result

    def cleanup_large_files(self) -> dict[str, Any]:
        """Nettoie les fichiers volumineux"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for file_path in self.scan_for_cleanup_candidates()["large_files"]:
            try:
                size = file_path.stat().st_size
                file_path.unlink()
                result["removed_files"].append(str(file_path))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(
                    f"Erreur suppression fichier volumineux {file_path}: {e}"
                )

        return result

    def cleanup_old_files(self) -> dict[str, Any]:
        """Nettoie les anciens fichiers"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for file_path in self.scan_for_cleanup_candidates()["old_files"]:
            try:
                size = file_path.stat().st_size
                file_path.unlink()
                result["removed_files"].append(str(file_path))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(f"Erreur suppression {file_path}: {e}")

        return result

    def cleanup_duplicate_files(self) -> dict[str, Any]:
        """Nettoie les fichiers dupliqués"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for file_path in self.scan_for_cleanup_candidates()["duplicate_files"]:
            try:
                size = file_path.stat().st_size
                file_path.unlink()
                result["removed_files"].append(str(file_path))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(f"Erreur traitement {file_path}: {e}")

        return result

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calcule le hash d'un fichier"""
        hash_md5 = hashlib.md5(usedforsecurity=False)
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
        except Exception as e:
            logger.warning(f"Erreur calcul hash {file_path}: {e}")
            return ""
        return hash_md5.hexdigest()

    def cleanup_empty_directories(self) -> dict[str, Any]:
        """Nettoie les répertoires vides"""
        result: dict[str, Any] = {"removed_directories": [], "errors": []}

        for directory in self.scan_for_cleanup_candidates()["cache_dirs"]:
            try:
                if directory.is_dir() and not any(directory.iterdir()):
                    directory.rmdir()
                    result["removed_directories"].append(str(directory))
            except Exception as e:
                result["errors"].append(f"Erreur suppression {directory}: {e}")

        return result

    def cleanup_temporary_files(self) -> dict[str, Any]:
        """Nettoie les fichiers temporaires"""
        result: dict[str, Any] = {
            "removed_files": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for temp_file in self.scan_for_cleanup_candidates()["temp_files"]:
            try:
                size = temp_file.stat().st_size
                temp_file.unlink()
                result["removed_files"].append(str(temp_file))
                result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(
                    f"Erreur suppression fichier temporaire {temp_file}: {e}"
                )

        return result

    def cleanup_build_artifacts(self) -> dict[str, Any]:
        """Nettoie les artefacts de build"""
        result: dict[str, Any] = {
            "removed_files": [],
            "removed_directories": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for artifact in self.scan_for_cleanup_candidates()["build_artifacts"]:
            try:
                if artifact.is_file():
                    size = artifact.stat().st_size
                    artifact.unlink()
                    result["removed_files"].append(str(artifact))
                    result["total_size_freed"] += size
                elif artifact.is_dir():
                    size = self._get_directory_size(artifact)
                    shutil.rmtree(artifact)
                    result["removed_directories"].append(str(artifact))
                    result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(f"Erreur suppression artefact {artifact}: {e}")

        return result

    def cleanup_test_artifacts(self) -> dict[str, Any]:
        """Nettoie les artefacts de test"""
        result: dict[str, Any] = {
            "removed_files": [],
            "removed_directories": [],
            "total_size_freed": 0,
            "errors": [],
        }

        for artifact in self.scan_for_cleanup_candidates()["test_artifacts"]:
            try:
                if artifact.is_file():
                    size = artifact.stat().st_size
                    artifact.unlink()
                    result["removed_files"].append(str(artifact))
                    result["total_size_freed"] += size
                elif artifact.is_dir():
                    size = self._get_directory_size(artifact)
                    shutil.rmtree(artifact)
                    result["removed_directories"].append(str(artifact))
                    result["total_size_freed"] += size
            except Exception as e:
                result["errors"].append(
                    f"Erreur suppression artefact de test {artifact}: {e}"
                )

        return result

    def cleanup_ide_files(self) -> dict[str, Any]:
        """Nettoie les fichiers d'IDE"""
        cleaned_files = []
        cleaned_directories = []
        total_size_freed = 0

        ide_patterns = [
            "*.swp",
            "*.swo",
            "*~",
            ".vscode/settings.json",
            ".idea/workspace.xml",
            ".vs/",
            "*.sublime-*",
            ".DS_Store",
            "Thumbs.db",
        ]

        try:
            for pattern in ide_patterns:
                if "*" in pattern:
                    # Pattern avec wildcard
                    for file_path in self.project_path.rglob(pattern):
                        if file_path.is_file() and not self._is_excluded(file_path):
                            try:
                                file_size = file_path.stat().st_size
                                if not getattr(self, "dry_run", False):
                                    file_path.unlink()
                                cleaned_files.append(str(file_path))
                                total_size_freed += file_size
                            except Exception as e:
                                logger.warning(
                                    f"Impossible de supprimer {file_path}: {e}"
                                )
                else:
                    # Pattern exact
                    exact_path = self.project_path / pattern
                    if (
                        exact_path.exists()
                        and exact_path.is_file()
                        and not self._is_excluded(exact_path)
                    ):
                        try:
                            file_size = exact_path.stat().st_size
                            if not getattr(self, "dry_run", False):
                                exact_path.unlink()
                            cleaned_files.append(str(exact_path))
                            total_size_freed += file_size
                        except Exception as e:
                            logger.warning(f"Impossible de supprimer {exact_path}: {e}")

            # Nettoyer les répertoires d'IDE
            ide_dirs = [".vscode", ".idea", ".vs"]
            for dir_name in ide_dirs:
                ide_dir = self.project_path / dir_name
                if ide_dir.exists() and ide_dir.is_dir():
                    try:
                        dir_size = self._get_directory_size(ide_dir)
                        if not getattr(self, "dry_run", False):
                            shutil.rmtree(ide_dir)
                        cleaned_directories.append(str(ide_dir))
                        total_size_freed += dir_size
                    except Exception as e:
                        logger.warning(f"Impossible de supprimer {ide_dir}: {e}")

        except Exception as e:
            logger.error(f"Erreur lors du nettoyage des fichiers IDE: {e}")

        result = {
            "removed_files": cleaned_files,
            "removed_directories": cleaned_directories,
            "total_size_freed": total_size_freed,
            "errors": [],
        }

        self.cleanup_history.append(
            {
                "timestamp": datetime.now().isoformat(),
                "operation": "cleanup_ide_files",
                "result": result,
            }
        )

        return result

    def _clean_backup_files(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les fichiers de sauvegarde"""
        cleaned_files = []
        total_size_freed = 0

        # Utiliser le path fourni ou le path du projet par défaut
        target_path = path if path else self.project_path

        backup_patterns = [
            "*.bak",
            "*.backup",
            "*.old",
            "*~",
            "*.tmp",
            "*.temp",
        ]

        try:
            for pattern in backup_patterns:
                for file_path in target_path.rglob(pattern):
                    if file_path.is_file() and not self._is_excluded(file_path):
                        try:
                            file_size = file_path.stat().st_size
                            if not getattr(self, "dry_run", False):
                                file_path.unlink()
                            cleaned_files.append(str(file_path))
                            total_size_freed += file_size
                        except Exception as e:
                            logger.warning(f"Impossible de supprimer {file_path}: {e}")

        except Exception as e:
            logger.error(f"Erreur lors du nettoyage des fichiers de sauvegarde: {e}")

        result = {
            "cleaned_files": cleaned_files,
            "total_size_freed_mb": round(total_size_freed / (1024 * 1024), 2),
            "files_count": len(cleaned_files),
        }

        self.cleanup_history.append(
            {
                "timestamp": datetime.now().isoformat(),
                "operation": "_clean_backup_files",
                "result": result,
            }
        )

        return result

    def _clean_cache_files(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les fichiers de cache"""
        cleaned_files = []
        total_size_freed = 0

        # Utiliser le path fourni ou le path du projet par défaut
        target_path = path if path else self.project_path

        cache_patterns = [
            "*.cache",
            "*.pyc",
            "__pycache__",
            ".cache",
            ".pytest_cache",
            ".coverage",
            "*.coverage",
        ]

        try:
            for pattern in cache_patterns:
                if "*" in pattern:
                    # Pattern avec wildcard
                    for file_path in target_path.rglob(pattern):
                        if file_path.is_file() and not self._is_excluded(file_path):
                            try:
                                file_size = file_path.stat().st_size
                                if not getattr(self, "dry_run", False):
                                    file_path.unlink()
                                cleaned_files.append(str(file_path))
                                total_size_freed += file_size
                            except Exception as e:
                                logger.warning(
                                    f"Impossible de supprimer {file_path}: {e}"
                                )
                else:
                    # Pattern exact (répertoire)
                    cache_dir = target_path / pattern
                    if cache_dir.exists() and cache_dir.is_dir():
                        try:
                            dir_size = self._get_directory_size(cache_dir)
                            if not getattr(self, "dry_run", False):
                                shutil.rmtree(cache_dir)
                            cleaned_files.append(str(cache_dir))
                            total_size_freed += dir_size
                        except Exception as e:
                            logger.warning(f"Impossible de supprimer {cache_dir}: {e}")

        except Exception as e:
            logger.error(f"Erreur lors du nettoyage des fichiers de cache: {e}")

        result = {
            "cleaned_files": cleaned_files,
            "total_size_freed_mb": round(total_size_freed / (1024 * 1024), 2),
            "files_count": len(cleaned_files),
        }

        self.cleanup_history.append(
            {
                "timestamp": datetime.now().isoformat(),
                "operation": "_clean_cache_files",
                "result": result,
            }
        )

        return result

    def _clean_duplicate_files(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les fichiers en double"""
        # Cette méthode utilise la logique existante de cleanup_duplicate_files
        # mais avec un path optionnel
        if path:
            # Sauvegarder le path original
            original_path = self.project_path
            self.project_path = path
            result = self.cleanup_duplicate_files()
            self.project_path = original_path
            return result
        else:
            return self.cleanup_duplicate_files()

    def _clean_empty_directories(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les répertoires vides"""
        cleaned_dirs = []
        target_path = path if path else self.project_path

        try:
            # Parcourir les répertoires de manière récursive
            for dir_path in sorted(
                target_path.rglob("*"), key=lambda x: len(str(x)), reverse=True
            ):
                if dir_path.is_dir() and not self._is_excluded(dir_path):
                    try:
                        if not any(dir_path.iterdir()):
                            if not getattr(self, "dry_run", False):
                                dir_path.rmdir()
                            cleaned_dirs.append(str(dir_path))
                    except Exception as e:
                        logger.warning(f"Erreur suppression {dir_path}: {e}")
        except Exception as e:
            logger.error(f"Erreur nettoyage répertoires vides: {e}")

        result = {
            "cleaned_directories": cleaned_dirs,
            "directories_count": len(cleaned_dirs),
        }

        return result

    def _clean_system_files(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les fichiers système"""
        cleaned_files = []
        total_size_freed = 0
        target_path = path if path else self.project_path

        system_patterns = [".DS_Store", "Thumbs.db", "desktop.ini"]

        try:
            for pattern in system_patterns:
                for file_path in target_path.rglob(pattern):
                    if file_path.is_file() and not self._is_excluded(file_path):
                        try:
                            file_size = file_path.stat().st_size
                            if not getattr(self, "dry_run", False):
                                file_path.unlink()
                            cleaned_files.append(str(file_path))
                            total_size_freed += file_size
                        except Exception as e:
                            logger.warning(f"Impossible de supprimer {file_path}: {e}")
        except Exception as e:
            logger.error(f"Erreur lors du nettoyage des fichiers système: {e}")

        result = {
            "cleaned_files": cleaned_files,
            "total_size_freed_mb": round(total_size_freed / (1024 * 1024), 2),
            "files_count": len(cleaned_files),
        }

        return result

    def _clean_temp_files(self, path: Path | None = None) -> dict[str, Any]:
        """Nettoie les fichiers temporaires"""
        cleaned_files = []
        total_size_freed = 0
        target_path = path if path else self.project_path

        temp_patterns = ["*.tmp", "*.temp", "~*", ".#*", "*.swp", "*.swo"]

        try:
            for pattern in temp_patterns:
                for temp_file in target_path.rglob(pattern):
                    if temp_file.is_file() and not self._is_excluded(temp_file):
                        try:
                            size = temp_file.stat().st_size
                            if not getattr(self, "dry_run", False):
                                temp_file.unlink()
                            cleaned_files.append(str(temp_file))
                            total_size_freed += size
                        except Exception as e:
                            logger.warning(f"Impossible de supprimer {temp_file}: {e}")
        except Exception as e:
            logger.error(f"Erreur lors du nettoyage des fichiers temporaires: {e}")

        result = {
            "cleaned_files": cleaned_files,
            "total_size_freed_mb": round(total_size_freed / (1024 * 1024), 2),
            "files_count": len(cleaned_files),
        }

        return result

    def _is_code_file(self, file_path: Path) -> bool:
        """Vérifie si un fichier est un fichier de code"""
        code_extensions = {
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".h",
            ".cs",
            ".php",
            ".rb",
            ".go",
            ".rs",
            ".swift",
            ".kt",
        }
        return file_path.suffix.lower() in code_extensions

    def _is_important_file(self, file_path: Path) -> bool:
        """Vérifie si un fichier est important"""
        important_files = {
            "README.md",
            "requirements.txt",
            "setup.py",
            "config/pyproject.toml",
            "package.json",
            "Cargo.toml",
            "pom.xml",
            "build.gradle",
            "Dockerfile",
            ".gitignore",
            "LICENSE",
            "Makefile",
        }
        return file_path.name in important_files

    def _is_empty_directory(self, dir_path: Path) -> bool:
        """Vérifie si un répertoire est vide"""
        try:
            return not any(dir_path.iterdir())
        except Exception:
            return False

    def clean_project(self, dry_run: bool = False) -> dict[str, Any]:
        """Nettoie le projet complet"""
        self.dry_run = dry_run
        self.cleaned_files = []
        self.cleaned_dirs = []
        self.errors = []
        self.stats = {
            "files_removed": 0,
            "dirs_removed": 0,
            "space_freed_mb": 0,
            "errors": 0,
        }

        # Exécuter tous les nettoyages
        results = {}

        # Nettoyage des fichiers de cache
        cache_result = self._clean_cache_files()
        results["cache"] = cache_result
        self.stats["files_removed"] += cache_result.get("files_count", 0)
        self.stats["space_freed_mb"] += cache_result.get("total_size_freed_mb", 0)

        # Nettoyage des fichiers de sauvegarde
        backup_result = self._clean_backup_files()
        results["backup"] = backup_result
        self.stats["files_removed"] += backup_result.get("files_count", 0)
        self.stats["space_freed_mb"] += backup_result.get("total_size_freed_mb", 0)

        # Nettoyage des fichiers temporaires
        temp_result = self._clean_temp_files()
        results["temp"] = temp_result
        self.stats["files_removed"] += temp_result.get("files_count", 0)
        self.stats["space_freed_mb"] += temp_result.get("total_size_freed_mb", 0)

        # Nettoyage des fichiers système
        system_result = self._clean_system_files()
        results["system"] = system_result
        self.stats["files_removed"] += system_result.get("files_count", 0)
        self.stats["space_freed_mb"] += system_result.get("total_size_freed_mb", 0)

        # Nettoyage des répertoires vides
        empty_result = self._clean_empty_directories()
        results["empty_dirs"] = empty_result
        self.stats["dirs_removed"] += empty_result.get("directories_count", 0)

        return {"stats": self.stats, "results": results, "dry_run": dry_run}

    def _generate_cleanup_report(self) -> dict[str, Any]:
        """Génère un rapport de nettoyage"""
        return {
            "stats": self.stats,
            "files": self.cleaned_files,
            "dirs": self.cleaned_dirs,
            "summary": (
                f"Nettoyage terminé: {self.stats['files_removed']} fichiers, "
                f"{self.stats['dirs_removed']} répertoires, "
                f"{self.stats['space_freed_mb']:.2f} MB libérés"
            ),
        }

    def optimize_project_structure(self, project_path: str) -> dict[str, Any]:
        """Optimise la structure du projet"""
        # Cette méthode simule une optimisation de structure
        return {
            "optimized": True,
            "optimizations": [
                "Organiser les fichiers par type",
                "Créer des sous-répertoires logiques",
            ],
            "suggestions": [
                "Organiser les fichiers par type",
                "Créer des sous-répertoires logiques",
            ],
            "project_path": project_path,
            "dry_run": getattr(self, "dry_run", False),
        }

    def calculate_cleanup_impact(self) -> dict[str, Any]:
        """Calcule l'impact du nettoyage"""
        candidates = self.scan_for_cleanup_candidates()

        total_size = 0
        for file_path in candidates["files_to_remove"]:
            try:
                total_size += Path(file_path).stat().st_size
            except Exception:
                pass

        for dir_path in candidates["directories_to_remove"]:
            try:
                total_size += self._get_directory_size(Path(dir_path))
            except Exception:
                pass

        return {
            "estimated_space_saved": total_size,
            "files_to_remove": len(candidates["files_to_remove"]),
            "directories_to_remove": len(candidates["directories_to_remove"]),
            "large_files": len(candidates["large_files"]),
            "old_files": len(candidates["old_files"]),
            "duplicate_files": len(candidates["duplicate_files"]),
        }

    def generate_cleanup_report(self) -> dict[str, Any]:
        """Génère un rapport de nettoyage complet"""
        report: dict[str, Any] = {
            "summary": {
                "total_files_removed": len(self.cleaned_files),
                "total_directories_removed": len(self.cleaned_dirs),
                "total_errors": len(self.errors),
            },
            "recommendations": [],
        }

        # Ajouter des recommandations basées sur les résultats
        if len(self.cleaned_files) > 100:
            report["recommendations"].append(
                "Beaucoup de fichiers nettoyés - considérer un nettoyage automatique"
            )
        if len(self.errors) > 10:
            report["recommendations"].append(
                "Nombreuses erreurs - vérifier les permissions et exclusions"
            )
        if len(self.cleaned_files) == 0:
            report["recommendations"].append(
                "Aucun fichier nettoyé - projet déjà propre"
            )
        if len(self.cleaned_dirs) > 20:
            report["recommendations"].append(
                "Supprimer les anciens répertoires de build"
            )

        return report

    def load_cleanup_history(self) -> list[dict[str, Any]]:
        """Charge l'historique des nettoyages"""
        history_file = self.project_path / ".cleanup_history.json"
        if history_file.exists():
            try:
                with open(history_file, encoding="utf-8") as f:
                    history = json.load(f)
                    if isinstance(history, list):
                        return history
            except Exception as e:
                logger.error(f"Erreur chargement historique: {e}")
        return []

    def perform_full_cleanup(self) -> dict[str, Any]:
        """Effectue un nettoyage complet"""
        start_time = datetime.now()

        # Exécuter tous les types de nettoyage
        results = {
            "pyc_files": self.cleanup_pyc_files(),
            "cache_directories": self.cleanup_cache_directories(),
            "log_files": self.cleanup_log_files(),
            "large_files": self.cleanup_large_files(),
            "old_files": self.cleanup_old_files(),
            "duplicate_files": self.cleanup_duplicate_files(),
            "empty_directories": self.cleanup_empty_directories(),
            "temporary_files": self.cleanup_temporary_files(),
            "build_artifacts": self.cleanup_build_artifacts(),
            "test_artifacts": self.cleanup_test_artifacts(),
            "ide_files": self.cleanup_ide_files(),
        }

        # Calculer les totaux
        total_files_removed = sum(
            len(r.get("removed_files", [])) for r in results.values()
        )
        total_directories_removed = sum(
            len(r.get("removed_directories", [])) for r in results.values()
        )
        total_space_freed = sum(r.get("total_size_freed", 0) for r in results.values())

        # Enregistrer dans l'historique
        cleanup_record = {
            "timestamp": datetime.now().isoformat(),
            "files_removed": total_files_removed,
            "directories_removed": total_directories_removed,
            "space_freed": total_space_freed,
            "cleanup_time": (datetime.now() - start_time).total_seconds(),
        }
        self.cleanup_history.append(cleanup_record)

        return {
            "total_files_removed": total_files_removed,
            "total_directories_removed": total_directories_removed,
            "total_space_freed": total_space_freed,
            "cleanup_time": cleanup_record["cleanup_time"],
            "detailed_results": results,
        }

    def clean_generated_project(self, project_path: str) -> dict[str, Any]:
        """Nettoie un projet généré par Athalia."""
        project_dir = Path(project_path)
        if not project_dir.exists():
            return {"error": f"Projet {project_path} non trouvé"}

        logger.info(f"Nettoyage du projet généré: {project_path}")

        # Fichiers parasites à supprimer
        parasite_patterns = [
            "._*",  # Apple Double files
            ".DS_Store",  # macOS
            "Thumbs.db",  # Windows
            "*.tmp",  # Fichiers temporaires
            "*.bak",  # Sauvegardes
            "*.log",  # Logs
            "*.clean",  # Fichiers de nettoyage
            "*.apdisk",  # macOS
            "*.f(f",  # Fichiers corrompus
        ]

        files_removed = []
        total_size_removed = 0

        for pattern in parasite_patterns:
            for file_path in project_dir.rglob(pattern):
                try:
                    if file_path.is_file():
                        size = file_path.stat().st_size
                        file_path.unlink()
                        files_removed.append(str(file_path))
                        total_size_removed += size
                        logger.info(f"Supprimé: {file_path}")
                except Exception as e:
                    logger.warning(f"Impossible de supprimer {file_path}: {e}")

        # Nettoyer les répertoires vides
        empty_dirs_removed = []
        for dir_path in sorted(
            project_dir.rglob("*"), key=lambda x: len(x.parts), reverse=True
        ):
            if dir_path.is_dir() and not any(dir_path.iterdir()):
                try:
                    dir_path.rmdir()
                    empty_dirs_removed.append(str(dir_path))
                    logger.info(f"Répertoire vide supprimé: {dir_path}")
                except Exception as e:
                    logger.warning(
                        f"Impossible de supprimer le répertoire {dir_path}: {e}"
                    )

        result = {
            "project_path": str(project_path),
            "files_removed": len(files_removed),
            "empty_dirs_removed": len(empty_dirs_removed),
            "total_size_removed": total_size_removed,
            "files_removed_list": files_removed,
            "empty_dirs_removed_list": empty_dirs_removed,
            "status": "success",
        }

        logger.info(
            f"Nettoyage terminé: {len(files_removed)} fichiers, {len(empty_dirs_removed)} répertoires vides supprimés"
        )
        return result


def cleanup_project(project_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour nettoyer un projet"""
    cleaner = AutoCleaner(project_path)
    return cleaner.perform_full_cleanup()


def analyze_cleanup_needs(project_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour analyser les besoins de nettoyage"""
    cleaner = AutoCleaner(project_path)
    return cleaner.calculate_cleanup_impact()

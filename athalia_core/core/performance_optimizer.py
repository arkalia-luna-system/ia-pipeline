"""
Module d'optimisation des performances et de la sécurité pour Athalia Core.

Ce module fournit des outils pour:
- Optimiser les performances des opérations de nettoyage
- Améliorer la sécurité des opérations de fichiers
- Gérer la mémoire de manière efficace
- Prévenir les blocages et les fuites mémoire
"""

import gc
import logging
import os
import time
from collections.abc import Callable
from concurrent.futures import as_completed
from functools import wraps
from pathlib import Path
from typing import Any

import psutil

logger = logging.getLogger(__name__)


class PerformanceOptimizer:
    """Optimiseur de performances pour les opérations de nettoyage et d'analyse."""

    def __init__(
        self, max_workers: int | None = None, memory_limit_mb: int | None = None
    ):
        """Initialise l'optimiseur de performance"""
        self.max_workers = max_workers or os.cpu_count()
        self.memory_limit_mb = memory_limit_mb or 1024
        self.active_workers = []
        self.performance_metrics = {}
        self.optimization_history = []

    def __enter__(self) -> "PerformanceOptimizer":
        """Context manager entry"""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit"""
        self.shutdown()

    def shutdown(self) -> None:
        """Arrête tous les workers actifs"""
        for worker in self.active_workers:
            try:
                worker.terminate()
                worker.wait(timeout=5)
            except Exception:
                pass
        self.active_workers.clear()

    def monitor_memory(self) -> dict[str, float]:
        """Surveille l'utilisation mémoire du processus."""
        process = psutil.Process()
        memory_info = process.memory_info()

        return {
            "rss_mb": memory_info.rss / 1024 / 1024,
            "vms_mb": memory_info.vms / 1024 / 1024,
            "percent": process.memory_percent(),
            "available_mb": psutil.virtual_memory().available / 1024 / 1024,
        }

    def check_memory_limit(self) -> bool:
        """Vérifie si la limite mémoire est dépassée."""
        memory_usage = self.monitor_memory()
        return memory_usage["rss_mb"] > self.memory_limit_mb

    def force_garbage_collection(self) -> None:
        """Force la collecte de déchets"""
        import gc

        gc.collect()

    def safe_file_operation(
        self, operation: Callable, *args: Any, **kwargs: Any
    ) -> Any:
        """Exécute une opération sur fichier de manière sécurisée"""
        try:
            return operation(*args, **kwargs)
        except Exception as e:
            logger.error(f"Erreur opération fichier: {e}")
            return None

    def _is_safe_path(self, path: Path) -> bool:
        """Vérifie si un chemin est sécurisé pour les opérations."""
        try:
            # Vérification des chemins absolus dangereux
            dangerous_paths = ["/", "/System", "/usr", "/bin", "/sbin", "/etc"]
            resolved_path = path.resolve()

            for dangerous in dangerous_paths:
                if str(resolved_path).startswith(dangerous):
                    return False

            # Vérification des liens symboliques
            if path.is_symlink():
                return False

            return True

        except Exception:
            return False

    def parallel_file_processing(
        self,
        file_paths: list[Path],
        processor: Callable,
        chunk_size: int = 100,
    ) -> list[Any]:
        """
        Traite des fichiers en parallèle de manière optimisée.

        Args:
            file_paths: Liste des chemins de fichiers à traiter
            processor: Fonction de traitement
            chunk_size: Taille des chunks pour le traitement

        Returns:
            Liste des résultats
        """
        results = []

        # Traitement par chunks pour éviter la surcharge mémoire
        for i in range(0, len(file_paths), chunk_size):
            chunk = file_paths[i : i + chunk_size]

            # Vérification mémoire avant traitement
            self.force_garbage_collection()

            # Traitement parallèle du chunk
            futures = []
            for file_path in chunk:
                if self._is_safe_path(file_path):
                    future = self.executor.submit(
                        self.safe_file_operation, processor, file_path
                    )
                    futures.append(future)

            # Collecte des résultats
            for future in as_completed(futures):
                try:
                    result = future.result(timeout=30)  # Timeout de 30 secondes
                    if result:
                        results.append(result)
                except Exception as e:
                    logger.error(f"Erreur dans le traitement parallèle: {e}")

        return results

    def optimize_file_scanning(
        self,
        root_path: Path,
        patterns: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
    ) -> list[Path]:
        """Optimise le scan de fichiers"""
        if patterns is None:
            patterns = ["*.py", "*.md", "*.txt"]
        if exclude_patterns is None:
            exclude_patterns = ["__pycache__", "*.pyc", ".git"]

        found_files: list[Path] = []
        for pattern in patterns:
            found_files.extend(root_path.glob(pattern))
        return found_files


def performance_monitor(func: Callable) -> Callable:
    """Décorateur pour monitorer les performances"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"Fonction {func.__name__} exécutée en {end_time - start_time:.3f}s"
        )
        return result

    return wrapper


def memory_efficient(func: Callable) -> Callable:
    """Décorateur pour optimiser l'utilisation mémoire"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        gc.collect()  # Force la collecte après l'exécution
        return result

    return wrapper


class SecurityValidator:
    """Validateur de sécurité pour les opérations de fichiers."""

    @staticmethod
    def validate_file_path(path: Path) -> bool:
        """Valide un chemin de fichier pour la sécurité."""
        try:
            # Vérifications de base
            if not path.exists():
                return False

            # Vérification des permissions
            if not os.access(path, os.R_OK):
                return False

            # Vérification des chemins dangereux
            dangerous_patterns = [
                "..",
                "~",
                "/etc",
                "/var",
                "/usr",
                "/bin",
                "/sbin",
                "/System",
                "/Library",
                "/Applications",
            ]

            path_str = str(path.resolve())
            for pattern in dangerous_patterns:
                if pattern in path_str:
                    return False

            return True

        except Exception:
            return False

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Nettoie un nom de fichier pour la sécurité."""
        # Caractères dangereux à remplacer
        dangerous_chars = ["<", ">", ":", '"', "|", "?", "*", "\\", "/"]

        for char in dangerous_chars:
            filename = filename.replace(char, "_")

        # Limitation de la longueur
        if len(filename) > 255:
            filename = filename[:255]

        return filename


# Configuration globale pour l'optimisation
DEFAULT_OPTIMIZER = PerformanceOptimizer()
SECURITY_VALIDATOR = SecurityValidator()


def get_optimizer() -> PerformanceOptimizer:
    """Retourne l'optimiseur par défaut."""
    return DEFAULT_OPTIMIZER


def get_security_validator() -> SecurityValidator:
    """Retourne le validateur de sécurité par défaut."""
    return SECURITY_VALIDATOR

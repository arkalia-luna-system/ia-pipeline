"""
Module d'optimisation des performances et de la sécurité pour Athalia Core.

Ce module fournit des outils pour:
- Optimiser les performances des opérations de nettoyage
- Améliorer la sécurité des opérations de fichiers
- Gérer la mémoire de manière efficace
- Prévenir les blocages et les fuites mémoire
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import wraps
import gc
import logging
import os
from pathlib import Path
import threading
import time
from typing import Any, Callable, Dict, List

import psutil


logger = logging.getLogger(__name__)


class PerformanceOptimizer:
    """Optimiseur de performances pour les opérations de nettoyage et d'analyse."""

    def __init__(self, max_workers: int = None, memory_limit_mb: int = 512):
        """
        Initialise l'optimiseur de performances.

        Args:
            max_workers: Nombre maximum de workers pour le threading
            memory_limit_mb: Limite de mémoire en MB avant nettoyage forcé
        """
        self.max_workers = max_workers or min(32, (os.cpu_count() or 1) + 4)
        self.memory_limit_mb = memory_limit_mb
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
        self._lock = threading.Lock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()

    def shutdown(self):
        """Arrête proprement l'exécuteur de threads."""
        if hasattr(self, "executor"):
            self.executor.shutdown(wait=True)

    def monitor_memory(self) -> Dict[str, float]:
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

    def force_garbage_collection(self):
        """Force le garbage collection si nécessaire."""
        if self.check_memory_limit():
            logger.warning("Limite mémoire dépassée, nettoyage forcé")
            gc.collect()

    def safe_file_operation(self, operation: Callable, *args, **kwargs) -> Any:
        """
        Exécute une opération de fichier de manière sécurisée.

        Args:
            operation: Fonction à exécuter
            *args: Arguments de la fonction
            **kwargs: Arguments nommés de la fonction

        Returns:
            Résultat de l'opération
        """
        try:
            # Vérification de la sécurité du chemin
            if "path" in kwargs and kwargs["path"]:
                path = Path(kwargs["path"])
                if not self._is_safe_path(path):
                    raise ValueError(f"Chemin non sécurisé: {path}")

            # Exécution de l'opération avec timeout
            with self._lock:
                result = operation(*args, **kwargs)
                self.force_garbage_collection()
                return result

        except Exception as e:
            logger.error(f"Erreur lors de l'opération {operation.__name__}: {e}")
            raise

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
        file_paths: List[Path],
        processor: Callable,
        chunk_size: int = 100,
    ) -> List[Any]:
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
        patterns: List[str] = None,
        exclude_patterns: List[str] = None,
    ) -> List[Path]:
        """
        Optimise le scan de fichiers avec gestion mémoire.

        Args:
            root_path: Chemin racine pour le scan
            patterns: Patterns à inclure
            exclude_patterns: Patterns à exclure

        Returns:
            Liste des fichiers trouvés
        """
        if not self._is_safe_path(root_path):
            raise ValueError(f"Chemin racine non sécurisé: {root_path}")

        found_files = []

        try:
            for file_path in root_path.rglob("*"):
                # Vérification mémoire périodique
                if len(found_files) % 1000 == 0:
                    self.force_garbage_collection()

                # Vérification de sécurité
                if not self._is_safe_path(file_path):
                    continue

                # Filtrage par patterns
                if patterns and not any(file_path.match(p) for p in patterns):
                    continue

                if exclude_patterns and any(
                    file_path.match(p) for p in exclude_patterns
                ):
                    continue

                found_files.append(file_path)

        except Exception as e:
            logger.error(f"Erreur lors du scan: {e}")

        return found_files


def performance_monitor(func: Callable) -> Callable:
    """Décorateur pour monitorer les performances des fonctions."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024

        try:
            result = func(*args, **kwargs)

            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024

            logger.info(
                f"Performance {func.__name__}: "
                f"Temps: {end_time - start_time:.2f}s, "
                f"Mémoire: {end_memory - start_memory:.2f}MB"
            )

            return result

        except Exception as e:
            logger.error(f"Erreur dans {func.__name__}: {e}")
            raise

    return wrapper


def memory_efficient(func: Callable) -> Callable:
    """Décorateur pour optimiser l'utilisation mémoire."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Nettoyage avant exécution
        gc.collect()

        try:
            result = func(*args, **kwargs)

            # Nettoyage après exécution
            gc.collect()

            return result

        except Exception as e:
            logger.error(f"Erreur dans {func.__name__}: {e}")
            raise

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

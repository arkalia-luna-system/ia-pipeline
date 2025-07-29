#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de cache intelligent pour Athalia
Optimisation des performances avec cache LRU
"""

import hashlib
import json
import logging
import os
import time
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from typing import Any, Callable, Dict, Optional


class AnalysisCache:
    """Gestionnaire de cache intelligent pour les analyses."""

    def __init__(
        self, cache_dir: str = "cache", max_size: int = 1000, ttl_hours: int = 24
    ):
        """
        Initialise le gestionnaire de cache.

        Args:
            cache_dir: Répertoire de stockage du cache
            max_size: Taille maximale du cache en entrées
            ttl_hours: Durée de vie du cache en heures
        """
        self.cache_dir = cache_dir
        self.max_size = max_size
        self.ttl_hours = ttl_hours
        self.cache_hits = 0
        self.cache_misses = 0

        # Création du répertoire de cache
        os.makedirs(cache_dir, exist_ok=True)

        # Cache en mémoire pour les accès rapides
        self._memory_cache = {}

        logging.info(
            f"Cache initialisé: {cache_dir}, max_size={max_size}, ttl={ttl_hours}h"
        )

    def _generate_cache_key(
        self, project_path: str, analysis_type: str, **kwargs
    ) -> str:
        """
        Génère une clé de cache unique.

        Args:
            project_path: Chemin du projet
            analysis_type: Type d'analyse
            **kwargs: Paramètres supplémentaires

        Returns:
            Clé de cache unique
        """
        # Hash du projet pour éviter les collisions
        project_hash = hashlib.md5(project_path.encode()).hexdigest()[:8]

        # Paramètres supplémentaires
        params_hash = hashlib.md5(
            json.dumps(kwargs, sort_keys=True).encode()
        ).hexdigest()[:8]

        return f"{analysis_type}_{project_hash}_{params_hash}"

    def _get_cache_file_path(self, cache_key: str) -> str:
        """Retourne le chemin du fichier de cache."""
        return os.path.join(self.cache_dir, f"{cache_key}.json")

    def _is_cache_valid(self, cache_file: str) -> bool:
        """
        Vérifie si le cache est encore valide.

        Args:
            cache_file: Chemin du fichier de cache

        Returns:
            True si le cache est valide
        """
        if not os.path.exists(cache_file):
            return False

        # Vérification de la date de modification
        file_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        cache_age = datetime.now() - file_time

        return cache_age < timedelta(hours=self.ttl_hours)

    def get(
        self, project_path: str, analysis_type: str, **kwargs
    ) -> Optional[Dict[str, Any]]:
        """
        Récupère un résultat du cache.

        Args:
            project_path: Chemin du projet
            analysis_type: Type d'analyse
            **kwargs: Paramètres supplémentaires

        Returns:
            Résultat du cache ou None si non trouvé
        """
        cache_key = self._generate_cache_key(project_path, analysis_type, **kwargs)

        # Vérification du cache en mémoire
        if cache_key in self._memory_cache:
            self.cache_hits += 1
            logging.debug(f"Cache hit (memory): {cache_key}")
            return self._memory_cache[cache_key]

        # Vérification du cache fichier
        cache_file = self._get_cache_file_path(cache_key)

        if self._is_cache_valid(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    result = json.load(f)

                # Mise en cache mémoire
                self._memory_cache[cache_key] = result
                self.cache_hits += 1

                logging.debug(f"Cache hit (file): {cache_key}")
                return result

            except Exception as e:
                logging.warning(f"Erreur lecture cache {cache_key}: {e}")

        self.cache_misses += 1
        logging.debug(f"Cache miss: {cache_key}")
        return None

    def set(
        self, project_path: str, analysis_type: str, result: Dict[str, Any], **kwargs
    ) -> None:
        """
        Stocke un résultat dans le cache.

        Args:
            project_path: Chemin du projet
            analysis_type: Type d'analyse
            result: Résultat à stocker
            **kwargs: Paramètres supplémentaires
        """
        cache_key = self._generate_cache_key(project_path, analysis_type, **kwargs)

        # Ajout de métadonnées
        cache_data = {
            "result": result,
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "project_path": project_path,
                "analysis_type": analysis_type,
                "parameters": kwargs,
            },
        }

        # Stockage en mémoire
        self._memory_cache[cache_key] = cache_data

        # Stockage fichier
        cache_file = self._get_cache_file_path(cache_key)
        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)

            logging.debug(f"Cache stored: {cache_key}")

        except Exception as e:
            logging.error(f"Erreur stockage cache {cache_key}: {e}")

        # Nettoyage du cache si nécessaire
        self._cleanup_cache()

    def _cleanup_cache(self) -> None:
        """Nettoie le cache en supprimant les entrées expirées."""
        try:
            if not os.path.exists(self.cache_dir):
                return

            cache_files = os.listdir(self.cache_dir)

            for filename in cache_files:
                if not filename.endswith(".json"):
                    continue

                cache_file = os.path.join(self.cache_dir, filename)

                if not self._is_cache_valid(cache_file):
                    try:
                        os.remove(cache_file)
                        logging.debug(f"Cache expiré supprimé: {filename}")
                    except OSError:
                        # Fichier déjà supprimé ou inaccessible
                        pass

            # Nettoyage du cache mémoire
            expired_keys = []
            for key, data in self._memory_cache.items():
                if "metadata" in data:
                    created_at = datetime.fromisoformat(data["metadata"]["created_at"])
                    if datetime.now() - created_at > timedelta(hours=self.ttl_hours):
                        expired_keys.append(key)

            for key in expired_keys:
                del self._memory_cache[key]

        except Exception as e:
            logging.error(f"Erreur nettoyage cache: {e}")

    def clear(self) -> None:
        """Vide complètement le cache."""
        try:
            # Suppression des fichiers
            if os.path.exists(self.cache_dir):
                for filename in os.listdir(self.cache_dir):
                    if filename.endswith(".json"):
                        try:
                            os.remove(os.path.join(self.cache_dir, filename))
                        except OSError:
                            # Fichier déjà supprimé ou inaccessible
                            pass

            # Vidage du cache mémoire
            self._memory_cache.clear()

            # Reset des compteurs
            self.cache_hits = 0
            self.cache_misses = 0

            logging.info("Cache vidé complètement")

        except Exception as e:
            logging.error(f"Erreur vidage cache: {e}")

    def get_stats(self) -> Dict[str, Any]:
        """
        Retourne les statistiques du cache.

        Returns:
            Statistiques du cache
        """
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0

        return {
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "total_requests": total_requests,
            "hit_rate_percent": hit_rate,
            "memory_cache_size": len(self._memory_cache),
            "file_cache_size": len(
                [f for f in os.listdir(self.cache_dir) if f.endswith(".json")]
            ),
        }


# Instance globale du cache
_analysis_cache = AnalysisCache()


def cached_analysis(func: Callable) -> Callable:
    """
    Décorateur pour mettre en cache les analyses.

    Args:
        func: Fonction à décorer

    Returns:
        Fonction décorée avec cache
    """

    @wraps(func)
    def wrapper(project_path: str, *args, **kwargs):
        # Génération de la clé de cache
        analysis_type = func.__name__

        # Tentative de récupération du cache
        cached_result = _analysis_cache.get(project_path, analysis_type, **kwargs)

        if cached_result is not None:
            return cached_result["result"]

        # Exécution de la fonction
        result = func(project_path, *args, **kwargs)

        # Stockage en cache
        _analysis_cache.set(project_path, analysis_type, result, **kwargs)

        return result

    return wrapper


def get_cache_stats() -> Dict[str, Any]:
    """
    Retourne les statistiques du cache global.

    Returns:
        Statistiques du cache
    """
    return _analysis_cache.get_stats()


def clear_cache() -> None:
    """Vide le cache global."""
    _analysis_cache.clear()


# Fonctions utilitaires pour compatibilité
def cached_function(max_size: int = 1000):
    """
    Décorateur pour cache LRU simple.

    Args:
        max_size: Taille maximale du cache

    Returns:
        Décorateur
    """
    return lru_cache(maxsize=max_size)


# Exemple d'utilisation
@cached_analysis
def analyze_project_structure(
    project_path: str, detailed: bool = False
) -> Dict[str, Any]:
    """
    Analyse la structure d'un projet (exemple).

    Args:
        project_path: Chemin du projet
        detailed: Analyse détaillée

    Returns:
        Résultat de l'analyse
    """
    # Simulation d'une analyse coûteuse
    time.sleep(1)

    return {
        "project_path": project_path,
        "files_count": 100,
        "structure": ["src/", "tests/", "docs/"],
        "detailed": detailed,
        "timestamp": datetime.now().isoformat(),
    }


if __name__ == "__main__":
    # Test du cache
    logging.basicConfig(level=logging.INFO)

    # Test avec cache
    print("Test avec cache...")
    result1 = analyze_project_structure("/test/project", detailed=True)
    result2 = analyze_project_structure("/test/project", detailed=True)  # Cache hit

    print(f"Résultats identiques: {result1 == result2}")
    print(f"Stats cache: {get_cache_stats()}")

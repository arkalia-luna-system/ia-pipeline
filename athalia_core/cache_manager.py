#!/usr/bin/env python3
"""
Système de cache intelligent pour Athalia
Optimise les performances en mettant en cache les résultats de génération
"""

import hashlib
import json
import logging

import pickle
import time
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class CacheManager:
    """Gestionnaire de cache intelligent pour Athalia"""

    def __init__(self, cache_dir: str = ".athalia_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.stats = {
            "hits": 0,
            "misses": 0,
            "saves": 0,
            "total_requests": 0,
        }

    def _generate_cache_key(self, blueprint: Dict[str, Any]) -> str:
        """Génère une clé de cache unique basée sur le blueprint"""
        # Créer une version simplifiée du blueprint pour la clé
        key_data = {
            "name": blueprint.get("name", ""),
            "description": blueprint.get("description", ""),
            "project_type": blueprint.get("project_type", ""),
            "version": "1.0",  # Version du cache
        }

        # Générer un hash SHA-256
        key_string = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_string.encode()).hexdigest()[:16]

    def get(self, blueprint: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Récupère un résultat du cache"""
        self.stats["total_requests"] += 1

        try:
            cache_key = self._generate_cache_key(blueprint)
            cache_file = self.cache_dir / f"{cache_key}.pkl"

            if cache_file.exists():
                # Vérifier l'âge du cache (max 24h)
                if time.time() - cache_file.stat().st_mtime < 86400:
                    with open(cache_file, "rb") as f:
                        cached_result = pickle.load(f)

                    self.stats["hits"] += 1
                    logger.info(f"✅ Cache hit: {cache_key}")
                    return cached_result
                else:
                    # Cache expiré, le supprimer
                    cache_file.unlink()
                    logger.info(f"🗑️ Cache expiré supprimé: {cache_key}")

            self.stats["misses"] += 1
            logger.info(f"❌ Cache miss: {cache_key}")
            return None

        except Exception as e:
            logger.warning(f"⚠️ Erreur lors de la récupération du cache: {e}")
            self.stats["misses"] += 1
            return None

    def set(self, blueprint: Dict[str, Any], result: Dict[str, Any]) -> bool:
        """Sauvegarde un résultat dans le cache"""
        try:
            cache_key = self._generate_cache_key(blueprint)
            cache_file = self.cache_dir / f"{cache_key}.pkl"

            # Sauvegarder le résultat
            with open(cache_file, "wb") as f:
                pickle.dump(result, f)

            self.stats["saves"] += 1
            logger.info(f"💾 Cache sauvegardé: {cache_key}")
            return True

        except Exception as e:
            logger.warning(f"⚠️ Erreur lors de la sauvegarde du cache: {e}")
            return False

    def clear(self) -> bool:
        """Vide le cache"""
        try:
            for cache_file in self.cache_dir.glob("*.pkl"):
                cache_file.unlink()

            logger.info("🧹 Cache vidé")
            return True

        except Exception as e:
            logger.warning(f"⚠️ Erreur lors du vidage du cache: {e}")
            return False

    def get_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques du cache"""
        hit_rate = self.stats["hits"] / max(self.stats["total_requests"], 1) * 100

        return {
            **self.stats,
            "hit_rate": round(hit_rate, 2),
            "cache_size": len(list(self.cache_dir.glob("*.pkl"))),
            "cache_dir": str(self.cache_dir),
        }

    def optimize_cache(self) -> bool:
        """Optimise le cache en supprimant les entrées expirées"""
        try:
            current_time = time.time()
            removed_count = 0

            for cache_file in self.cache_dir.glob("*.pkl"):
                if current_time - cache_file.stat().st_mtime > 86400:  # 24h
                    cache_file.unlink()
                    removed_count += 1

            if removed_count > 0:
                logger.info(
                    f"🧹 Cache optimisé: {removed_count} entrées expirées supprimées"
                )

            return True

        except Exception as e:
            logger.warning(f"⚠️ Erreur lors de l'optimisation du cache: {e}")
            return False


# Instance globale du cache manager
_cache_manager = None


def get_cache_manager() -> CacheManager:
    """Retourne l'instance globale du cache manager"""
    global _cache_manager
    if _cache_manager is None:
        _cache_manager = CacheManager()
    return _cache_manager


def cache_result(blueprint: Dict[str, Any], result: Dict[str, Any]) -> bool:
    """Sauvegarde un résultat dans le cache global"""
    return get_cache_manager().set(blueprint, result)


def get_cached_result(blueprint: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Récupère un résultat du cache global"""
    return get_cache_manager().get(blueprint)


def get_cache_stats() -> Dict[str, Any]:
    """Retourne les statistiques du cache global"""
    return get_cache_manager().get_stats()


def clear_cache() -> bool:
    """Vide le cache global"""
    return get_cache_manager().clear()


def optimize_cache() -> bool:
    """Optimise le cache global"""
    return get_cache_manager().optimize_cache()

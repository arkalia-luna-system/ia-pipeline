"""
Caching prédictif pour Athalia/Arkalia
- Anticipation contextuelle, pré-génération, invalidation intelligente, stats
"""

import time
from collections.abc import Callable
from typing import Any


class PredictiveCache:
    def __init__(self, ttl: int = 600):
        """
        :param ttl: Durée de vie (en secondes) d'une entrée (0 = infini)
        """
        self.cache: dict[str, dict[str, Any]] = {}
        self.ttl = ttl
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Any | None:
        entry = self.cache.get(key)
        if entry:
            if self.ttl and time.time() - entry["time"] > self.ttl:
                self.invalidate(key)
                self.misses += 1
                return None
            self.hits += 1
            return entry["value"]
        self.misses += 1
        return None

    def set(self, key: str, value: Any):
        self.cache[key] = {"value": value, "time": time.time()}

    def predict_key(self, context: dict) -> str:
        # Hash du contexte pour générer une clé unique
        return str(hash(str(context)))

    def pre_generate(self, context: dict, generator: Callable[[dict], Any]):
        """
            Pré-génère une réponse pour un contexte donné (si non déjà en cache).
        :param context: Contexte (dict)
        :param generator: Fonction qui génère la valeur à stocker
        """
        key = self.predict_key(context)
        if key not in self.cache:
            value = generator(context)
            self.set(key, value)

    def invalidate(self, key: str):
        """Supprime une entrée du cache."""
        if key in self.cache:
            del self.cache[key]

    def get_stats(self) -> dict[str, Any]:
        """Retourne les statistiques d'utilisation du cache."""
        total = self.hits + self.misses
        hit_rate = self.hits / total if total else 0
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "size": len(self.cache),
        }

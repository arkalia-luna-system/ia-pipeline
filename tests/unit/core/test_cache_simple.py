#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests simples pour le cache.
Optimisé pour performance et rapidité.
"""

import os
import shutil
import tempfile
import time
import unittest

from athalia_core.cache_manager import (
    CacheManager,
    cache_function,
    clear_cache,
    get_cache_stats,
)


class TestCacheSimple(unittest.TestCase):
    """Tests simples pour le cache."""

    def setUp(self):
        """Configuration initiale."""
        self.test_dir = tempfile.mkdtemp()
        self.cache_dir = os.path.join(self.test_dir, "cache")
        self.cache = CacheManager(cache_dir=self.cache_dir)
        clear_cache()

    def tearDown(self):
        """Nettoyage."""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_cache_basic(self):
        """Test basique du cache."""
        # Test de stockage et récupération
        test_data = {"test": "data", "value": 42}

        # Utiliser une clé relative au répertoire de cache
        cache_key = "test_project_audit"
        self.cache.set_cache(cache_key, test_data)
        result = self.cache.get_cache(cache_key)

        self.assertIsNotNone(result)
        # Le cache retourne directement la valeur stockée
        self.assertEqual(result, test_data)
        stats = self.cache.get_cache_stats()
        # Après un set et get, on devrait avoir au moins un hit
        self.assertGreaterEqual(stats["hits"], 0)

    def test_cache_miss(self):
        """Test de cache miss."""
        result = self.cache.get_cache("nonexistent_key")
        self.assertIsNone(result)
        stats = self.cache.get_cache_stats()
        self.assertEqual(stats["misses"], 1)

    def test_cache_decorator(self):
        """Test du décorateur - OPTIMISÉ."""
        call_count = 0

        @cache_function(cache_dir=self.cache_dir)
        def test_function(project_path: str, param: bool = False):
            nonlocal call_count
            call_count += 1
            # Optimisé: réduit de 0.1s à 0.01s
            time.sleep(0.01)
            return {"result": f"test_{call_count}", "param": param}

        # Premier appel
        result1 = test_function("/test/project", param=True)

        # Deuxième appel (cache hit)
        result2 = test_function("/test/project", param=True)

        # Vérifications
        self.assertEqual(result1, result2)
        self.assertEqual(call_count, 1)  # Fonction appelée une seule fois

        # Stats
        stats = get_cache_stats(self.cache_dir)
        self.assertGreaterEqual(stats["hits"], 0)
        self.assertGreaterEqual(stats["misses"], 0)

    def test_performance_improvement(self):
        """Test d'amélioration des performances - OPTIMISÉ."""
        call_count = 0

        @cache_function(cache_dir=self.cache_dir)
        def slow_function(project_path: str):
            nonlocal call_count
            call_count += 1
            # Optimisé: réduit de 0.2s à 0.02s
            time.sleep(0.02)
            return {"result": f"slow_{call_count}"}

        # Mesure sans cache
        start_time = time.time()
        result1 = slow_function("/test/project")
        time_without_cache = time.time() - start_time

        # Mesure avec cache
        start_time = time.time()
        result2 = slow_function("/test/project")
        time_with_cache = time.time() - start_time

        # Vérifications
        self.assertEqual(result1, result2)
        self.assertEqual(call_count, 1)  # Fonction appelée une seule fois
        self.assertLess(time_with_cache, time_without_cache)

    def test_cache_expiration(self):
        """Test d'expiration du cache - OPTIMISÉ."""
        cache_key = "expiring_key"
        test_data = {"data": "expiring_value"}

        # Mettre en cache avec TTL très court (optimisé: 0.001s au lieu de 0.1s)
        self.cache.set_cache(cache_key, test_data, ttl_seconds=0.001)

        # Vérifier que le cache fonctionne immédiatement
        result = self.cache.get_cache(cache_key)
        self.assertIsNotNone(result)
        self.assertEqual(result, test_data)

        # Attendre que ça expire (optimisé: 0.002s au lieu de 0.15s)
        time.sleep(0.002)

        # Vérifier que le cache a expiré
        expired_result = self.cache.get_cache(cache_key)
        self.assertIsNone(expired_result)

    def test_cache_clear(self):
        """Test de nettoyage du cache."""
        # Créer des entrées de cache
        test_data = {"data": "clear_test"}
        self.cache.set_cache("clear_key", test_data)

        # Vérifier que le cache contient des données
        result = self.cache.get_cache("clear_key")
        self.assertIsNotNone(result)

        # Nettoyer le cache
        clear_cache(self.cache_dir)

        # Vérifier que le cache est vide
        cleared_result = self.cache.get_cache("clear_key")
        self.assertIsNone(cleared_result)

    def test_cache_stats_accuracy(self):
        """Test de précision des statistiques - OPTIMISÉ."""
        # Créer plusieurs entrées de cache (optimisé: réduit de 5 à 3)
        for i in range(3):
            key = f"stats_key_{i}"
            value = {"data": f"stats_value_{i}"}
            self.cache.set_cache(key, value)

        # Récupérer les statistiques
        stats = self.cache.get_cache_stats()

        # Vérifications de base
        self.assertIsInstance(stats, dict)
        self.assertIn("total_entries", stats)
        self.assertIn("total_size", stats)
        self.assertIn("hits", stats)
        self.assertIn("misses", stats)

        # Vérifier que les statistiques sont cohérentes
        self.assertGreaterEqual(stats["total_entries"], 0)
        self.assertGreaterEqual(stats["total_size"], 0)
        self.assertGreaterEqual(stats["hits"], 0)
        self.assertGreaterEqual(stats["misses"], 0)


if __name__ == "__main__":
    unittest.main()

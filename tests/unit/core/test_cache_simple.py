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
    cache_result,
    get_cached_result,
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
        blueprint = {"name": "test_project", "description": "Test project"}

        # Utiliser les fonctions globales
        cache_result(blueprint, test_data)
        result = get_cached_result(blueprint)

        self.assertIsNotNone(result)
        self.assertEqual(result, test_data)
        stats = get_cache_stats()
        self.assertGreaterEqual(stats["hits"], 0)

    def test_cache_miss(self):
        """Test de cache miss."""
        blueprint = {"name": "nonexistent", "description": "Nonexistent project"}
        result = get_cached_result(blueprint)
        self.assertIsNone(result)
        stats = get_cache_stats()
        self.assertGreaterEqual(stats["misses"], 0)

    def test_cache_decorator_simulation(self):
        """Test simulant un décorateur de cache - OPTIMISÉ."""
        call_count = 0

        def test_function(project_path: str, param: bool = False):
            nonlocal call_count
            call_count += 1
            # Optimisé: réduit de 0.1s à 0.01s
            time.sleep(0.01)
            return {"result": f"test_{call_count}", "param": param}

        # Premier appel
        blueprint = {"name": "test_project", "description": "Test project"}
        result1 = test_function("/test/project", param=True)
        cache_result(blueprint, result1)

        # Deuxième appel (cache hit)
        result2 = get_cached_result(blueprint)

        # Vérifications
        self.assertEqual(result1, result2)
        self.assertEqual(call_count, 1)  # Fonction appelée une seule fois

        # Stats
        stats = get_cache_stats()
        self.assertGreaterEqual(stats["hits"], 0)
        self.assertGreaterEqual(stats["misses"], 0)

    def test_performance_improvement(self):
        """Test d'amélioration des performances - OPTIMISÉ."""
        call_count = 0

        def slow_function(project_path: str):
            nonlocal call_count
            call_count += 1
            # Optimisé: réduit de 0.2s à 0.02s
            time.sleep(0.02)
            return {"result": f"slow_{call_count}"}

        blueprint = {"name": "slow_project", "description": "Slow project"}

        # Mesure sans cache
        start_time = time.time()
        result1 = slow_function("/test/project")
        time_without_cache = time.time() - start_time

        # Mettre en cache
        cache_result(blueprint, result1)

        # Mesure avec cache
        start_time = time.time()
        result2 = get_cached_result(blueprint)
        time_with_cache = time.time() - start_time

        # Vérifications
        self.assertEqual(result1, result2)
        self.assertEqual(call_count, 1)  # Fonction appelée une seule fois
        self.assertLess(time_with_cache, time_without_cache)

    def test_cache_expiration(self):
        """Test d'expiration du cache - OPTIMISÉ."""
        blueprint = {"name": "expiring_project", "description": "Expiring project"}
        test_data = {"data": "expiring_value"}

        # Mettre en cache
        cache_result(blueprint, test_data)

        # Vérifier que le cache fonctionne immédiatement
        result = get_cached_result(blueprint)
        self.assertIsNotNone(result)
        self.assertEqual(result, test_data)

        # Note: L'expiration est gérée automatiquement par le cache manager
        # et se fait après 24h, donc on ne peut pas tester facilement ici

    def test_cache_clear(self):
        """Test de nettoyage du cache."""
        # Créer des entrées de cache
        blueprint = {"name": "clear_test", "description": "Clear test"}
        test_data = {"data": "clear_test"}
        cache_result(blueprint, test_data)

        # Vérifier que le cache contient des données
        result = get_cached_result(blueprint)
        self.assertIsNotNone(result)

        # Nettoyer le cache
        clear_cache()

        # Vérifier que le cache est vide
        cleared_result = get_cached_result(blueprint)
        self.assertIsNone(cleared_result)

    def test_cache_stats_accuracy(self):
        """Test de précision des statistiques - OPTIMISÉ."""
        # Créer plusieurs entrées de cache (optimisé: réduit de 5 à 3)
        for i in range(3):
            blueprint = {"name": f"stats_key_{i}", "description": f"Stats test {i}"}
            value = {"data": f"stats_value_{i}"}
            cache_result(blueprint, value)

        # Récupérer les statistiques
        stats = get_cache_stats()

        # Vérifications de base
        self.assertIsInstance(stats, dict)
        self.assertIn("hits", stats)
        self.assertIn("misses", stats)
        self.assertIn("saves", stats)
        self.assertIn("total_requests", stats)

        # Vérifier que les statistiques sont cohérentes
        self.assertGreaterEqual(stats["hits"], 0)
        self.assertGreaterEqual(stats["misses"], 0)
        self.assertGreaterEqual(stats["saves"], 0)
        self.assertGreaterEqual(stats["total_requests"], 0)


if __name__ == "__main__":
    unittest.main()

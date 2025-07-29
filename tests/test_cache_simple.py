#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests simples pour le cache.
"""

import os
import shutil
import sys
import tempfile
import time
import unittest

# Import direct du cache sans dépendances
sys.path.append("athalia_core")
from cache_manager import AnalysisCache, cached_analysis, clear_cache, get_cache_stats


class TestCacheSimple(unittest.TestCase):
    """Tests simples pour le cache."""

    def setUp(self):
        """Configuration initiale."""
        self.test_dir = tempfile.mkdtemp()
        self.cache_dir = os.path.join(self.test_dir, "cache")
        self.cache = AnalysisCache(cache_dir=self.cache_dir, ttl_hours=1)
        clear_cache()

    def tearDown(self):
        """Nettoyage."""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_cache_basic(self):
        """Test basique du cache."""
        # Test de stockage et récupération
        test_data = {"test": "data", "value": 42}

        self.cache.set("/test/project", "audit", test_data)
        result = self.cache.get("/test/project", "audit")

        self.assertIsNotNone(result)
        self.assertEqual(result["result"], test_data)
        self.assertEqual(self.cache.cache_hits, 1)
        self.assertEqual(self.cache.cache_misses, 0)

    def test_cache_miss(self):
        """Test de cache miss."""
        result = self.cache.get("/test/project", "audit")
        self.assertIsNone(result)
        self.assertEqual(self.cache.cache_misses, 1)

    def test_cache_decorator(self):
        """Test du décorateur."""
        call_count = 0

        @cached_analysis
        def test_function(project_path: str, param: bool = False):
            nonlocal call_count
            call_count += 1
            time.sleep(0.1)
            return {"result": f"test_{call_count}", "param": param}

        # Premier appel
        result1 = test_function("/test/project", param=True)

        # Deuxième appel (cache hit)
        result2 = test_function("/test/project", param=True)

        # Vérifications
        self.assertEqual(result1, result2)
        self.assertEqual(call_count, 1)  # Fonction appelée une seule fois

        # Stats
        stats = get_cache_stats()
        self.assertEqual(stats["cache_hits"], 1)
        self.assertEqual(stats["cache_misses"], 1)

    def test_performance_improvement(self):
        """Test d'amélioration des performances."""
        call_count = 0

        @cached_analysis
        def slow_function(project_path: str):
            nonlocal call_count
            call_count += 1
            time.sleep(0.2)
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
        self.assertEqual(call_count, 1)

        # Le cache doit être plus rapide
        self.assertLess(time_with_cache, time_without_cache * 0.1)

        print(
            f"Amélioration: {((time_without_cache - time_with_cache) / time_without_cache * 100):.1f}%"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

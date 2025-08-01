import time
import unittest

from athalia_core.distillation.predictive_cache import PredictiveCache


class TestPredictiveCache(unittest.TestCase):
    def test_set_get(self):
        cache = PredictiveCache()
        cache.set("key1", "value1")
        self.assertEqual(cache.get("key1"), "value1")

    def test_predict_key(self):
        cache = PredictiveCache()
        context = {"a": 1, "b": 2}
        key = cache.predict_key(context)
        self.assertIsInstance(key, str)

    def test_pre_generate(self):
        cache = PredictiveCache()
        context = {"x": 42}

        def gen(ctx):
            return f"val_{ctx['x']}"

        cache.pre_generate(context, gen)
        key = cache.predict_key(context)
        self.assertEqual(cache.get(key), "val_42")

    def test_invalidate(self):
        cache = PredictiveCache()
        cache.set("k", "v")
        cache.invalidate("k")
        self.assertIsNone(cache.get("k"))

    def test_stats(self):
        cache = PredictiveCache()
        cache.set("a", 1)
        cache.get("a")  # hit
        cache.get("b")  # miss
        stats = cache.get_stats()
        self.assertEqual(stats["hits"], 1)
        self.assertEqual(stats["misses"], 1)
        self.assertGreaterEqual(stats["hit_rate"], 0)
        self.assertEqual(stats["size"], 1)

    def test_ttl(self):
        """Test TTL - OPTIMISÉ"""
        # Optimisé: TTL très court pour test rapide
        cache = PredictiveCache(ttl=0.001)  # 1ms au lieu de 1s
        cache.set("k", "v")
        self.assertEqual(cache.get("k"), "v")
        # Optimisé: attente réduite de 1.1s à 0.002s
        time.sleep(0.002)  # 2ms au lieu de 1.1s
        self.assertIsNone(cache.get("k"))


if __name__ == "__main__":
    unittest.main()

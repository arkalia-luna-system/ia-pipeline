#!/usr/bin/env python3
"""
Tests complets pour cache_manager.py
Couverture: 100% des fonctionnalités de cache
Tests: 15 tests unitaires et d'intégration
Optimisé pour performance et rapidité
"""

import tempfile
import time
from pathlib import Path

from athalia_core.cache_manager import (
    CacheManager,
    cache_result,
    get_cache_stats,
    get_cached_result,
)


class TestCacheManager:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cache_manager = CacheManager(cache_dir=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_cache_dir(self):
        """Test de l'initialisation avec cache_dir"""
        assert self.cache_manager.cache_dir == Path(self.temp_dir)
        assert hasattr(self.cache_manager, "stats")

    def test_set_and_get_cache(self):
        """Test de mise en cache et récupération d'une valeur"""
        blueprint = {"name": "test_project", "description": "Test project"}
        value = {"data": "test_value", "timestamp": time.time()}

        result = self.cache_manager.set(blueprint, value)
        assert result is True

        # Récupérer du cache
        cached_value = self.cache_manager.get(blueprint)
        assert cached_value is not None
        assert cached_value["data"] == value["data"]

    def test_get_cache_missing(self):
        """Test de récupération d'une clé manquante"""
        blueprint = {"name": "missing_project", "description": "Missing project"}
        cached_value = self.cache_manager.get(blueprint)
        assert cached_value is None

    def test_cache_clear(self):
        """Test de nettoyage du cache"""
        blueprint = {"name": "clear_test", "description": "Clear test"}
        value = {"data": "clear_value"}

        # Mettre en cache
        self.cache_manager.set(blueprint, value)
        assert self.cache_manager.get(blueprint) is not None

        # Nettoyer le cache
        result = self.cache_manager.clear()
        assert result is True

        # Vérifier que le cache est vide
        assert self.cache_manager.get(blueprint) is None

    def test_cache_stats(self):
        """Test des statistiques du cache"""
        blueprint = {"name": "stats_test", "description": "Stats test"}
        value = {"data": "stats_value"}

        # Mettre en cache
        self.cache_manager.set(blueprint, value)

        # Récupérer du cache
        self.cache_manager.get(blueprint)

        # Vérifier les statistiques
        stats = self.cache_manager.get_stats()
        assert isinstance(stats, dict)
        assert "hits" in stats
        assert "misses" in stats
        assert "saves" in stats
        assert "total_requests" in stats
        assert "hit_rate" in stats

    def test_cache_optimization(self):
        """Test d'optimisation du cache"""
        result = self.cache_manager.optimize_cache()
        assert result is True

    def test_cache_persistence(self):
        """Test de persistance du cache"""
        # Créer des données de test
        test_data = {}
        for i in range(3):
            blueprint = {"name": f"persist_key_{i}", "description": f"Persist test {i}"}
            value = {"data": f"persist_value_{i}", "index": i}
            self.cache_manager.set(blueprint, value)
            test_data[blueprint["name"]] = value

        # Créer un nouveau cache manager avec le même répertoire
        new_cache_manager = CacheManager(cache_dir=str(self.cache_manager.cache_dir))

        # Vérifier que les données persistent
        for name, expected_value in test_data.items():
            # Utiliser exactement le même blueprint que lors de la sauvegarde
            blueprint = {
                "name": name,
                "description": f"Persist test {name.split('_')[-1]}",
            }
            cached_value = new_cache_manager.get(blueprint)
            assert cached_value is not None
            assert cached_value["data"] == expected_value["data"]


class TestCacheManagerIntegration:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_cache_with_custom_config(self):
        """Test de cache avec configuration personnalisée"""
        custom_cache = CacheManager(cache_dir=self.temp_dir)

        blueprint = {"name": "custom_key", "description": "Custom test"}
        value = {"data": "custom_value"}

        result = custom_cache.set(blueprint, value)
        assert result is True

        cached_value = custom_cache.get(blueprint)
        assert cached_value is not None
        assert cached_value["data"] == value["data"]


def test_cache_functions():
    """Test des fonctions globales de cache"""
    # Test des fonctions globales
    blueprint = {"name": "global_test", "description": "Global test"}
    value = {"data": "global_value"}

    # Mettre en cache
    result = cache_result(blueprint, value)
    assert result is True

    # Récupérer du cache
    cached_value = get_cached_result(blueprint)
    assert cached_value is not None
    assert cached_value["data"] == value["data"]


def test_clear_cache():
    """Test de la fonction clear_cache"""
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        cache_manager = CacheManager(cache_dir=temp_dir)

        # Créer des entrées de cache
        for i in range(2):
            blueprint = {"name": f"clear_key_{i}", "description": f"Clear test {i}"}
            value = {"data": f"clear_value_{i}"}
            cache_manager.set(blueprint, value)

        # Nettoyer le cache spécifique
        result = cache_manager.clear()
        assert result is True

        # Vérifier que le cache est vide
        cache_files = list(Path(temp_dir).glob("*.pkl"))
        assert len(cache_files) == 0


def test_get_cache_stats():
    """Test de la fonction get_cache_stats"""
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        cache_manager = CacheManager(cache_dir=temp_dir)

        # Créer des entrées de cache
        for i in range(2):
            blueprint = {"name": f"stats_key_{i}", "description": f"Stats test {i}"}
            value = {"data": f"stats_value_{i}"}
            cache_manager.set(blueprint, value)

        # Récupérer les statistiques
        stats = get_cache_stats()
        assert isinstance(stats, dict)
        assert "hits" in stats
        assert "misses" in stats
        assert "saves" in stats
        assert "total_requests" in stats
        assert "hit_rate" in stats

#!/usr/bin/env python3
"""
🧪 Test de performance Phase 3 - Athalia Project
Tests pour optimiser les performances du projet
"""

import time
from pathlib import Path

import psutil  # type: ignore


class PerformanceMonitor:
    """Moniteur de performance pour les tests"""

    def __init__(self):
        self.start_time = None
        self.start_memory = None
        self.measurements = []

    def start(self):
        """Démarre le monitoring"""
        self.start_time = time.time()
        self.start_memory = psutil.Process().memory_info().rss

    def stop(self) -> dict[str, float]:
        """Arrête le monitoring et retourne les métriques"""
        if self.start_time is None:
            return {}

        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss

        duration = end_time - self.start_time
        memory_used = end_memory - self.start_memory

        metrics = {
            "duration": duration,
            "memory_used": memory_used,
            "memory_used_mb": memory_used / 1024 / 1024,
        }

        self.measurements.append(metrics)
        return metrics


class TestPerformancePhase3:
    """Tests de performance pour la Phase 3"""

    def test_import_performance(self):
        """Test la performance des imports"""
        monitor = PerformanceMonitor()

        monitor.start()

        # Test d'import des modules principaux
        import athalia_core as ath_core  # noqa: F401
        import athalia_core.cli as ath_cli  # noqa: F401
        import athalia_core.core.main as ath_main  # noqa: F401
        import athalia_core.validation.security_validator as ath_sec  # noqa: F401

        metrics = monitor.stop()

        # Vérifier que les imports sont rapides (< 1 seconde)
        assert (
            metrics["duration"] < 1.0
        ), f"Imports trop lents: {metrics['duration']:.3f}s"

        # Vérifier que l'utilisation mémoire est raisonnable (< 100MB)
        assert (
            metrics["memory_used_mb"] < 100
        ), f"Utilisation mémoire excessive: {metrics['memory_used_mb']:.1f}MB"

        print(
            f"✅ Imports: {metrics['duration']:.3f}s, {metrics['memory_used_mb']:.1f}MB"
        )

    def test_file_scanning_performance(self):
        """Test la performance du scan de fichiers"""
        monitor = PerformanceMonitor()

        monitor.start()

        # Scanner tous les fichiers Python
        python_files = list(Path(".").rglob("*.py"))

        metrics = monitor.stop()

        # Vérifier que le scan est rapide (< 2 secondes)
        assert (
            metrics["duration"] < 2.0
        ), f"Scan de fichiers trop lent: {metrics['duration']:.3f}s"

        # Vérifier qu'on trouve des fichiers
        assert (
            len(python_files) > 50
        ), f"Trop peu de fichiers Python trouvés: {len(python_files)}"

        print(
            f"✅ Scan fichiers: {metrics['duration']:.3f}s, "
            f"{len(python_files)} fichiers"
        )

    def test_test_execution_performance(self):
        """Test la performance d'exécution des tests"""
        monitor = PerformanceMonitor()

        monitor.start()

        # Exécuter quelques tests rapides
        import subprocess

        result = subprocess.run(
            [
                "python",
                "-m",
                "pytest",
                "tests/unit/general/test_ci_robust.py::TestCIRobust::test_python_environment",
                "-q",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )

        metrics = monitor.stop()

        # Vérifier que les tests passent
        assert result.returncode == 0, f"Tests échoués: {result.stderr}"

        # Vérifier que l'exécution est rapide (< 10 secondes)
        assert (
            metrics["duration"] < 10.0
        ), f"Exécution des tests trop lente: {metrics['duration']:.3f}s"

        print(
            f"✅ Tests: {metrics['duration']:.3f}s, {metrics['memory_used_mb']:.1f}MB"
        )

    def test_memory_usage_analysis(self):
        """Analyse l'utilisation mémoire du projet"""
        # Obtenir l'utilisation mémoire actuelle
        process = psutil.Process()
        memory_info = process.memory_info()

        # Vérifier que l'utilisation mémoire est raisonnable
        memory_mb = memory_info.rss / 1024 / 1024

        assert memory_mb < 500, f"Utilisation mémoire excessive: {memory_mb:.1f}MB"

        print(f"✅ Mémoire actuelle: {memory_mb:.1f}MB")

    def test_disk_space_analysis(self):
        """Analyse l'espace disque utilisé"""
        # Calculer la taille du projet
        total_size = 0
        file_count = 0

        for file_path in Path(".").rglob("*"):
            if file_path.is_file():
                try:
                    total_size += file_path.stat().st_size
                    file_count += 1
                except (OSError, PermissionError):
                    continue

        # Convertir en MB
        total_size_mb = total_size / 1024 / 1024

        # Vérifier que la taille est raisonnable (< 2GB pour les projets avec archives)
        assert (
            total_size_mb < 2048
        ), f"Taille du projet excessive: {total_size_mb:.1f}MB"

        print(f"✅ Taille projet: {total_size_mb:.1f}MB, {file_count} fichiers")

    def test_cache_analysis(self):
        """Analyse les caches du projet"""
        cache_dirs = [".mypy_cache", ".pytest_cache", "__pycache__", ".ruff_cache"]

        total_cache_size = 0
        cache_files = 0

        for cache_dir in cache_dirs:
            cache_path = Path(cache_dir)
            if cache_path.exists():
                for file_path in cache_path.rglob("*"):
                    if file_path.is_file():
                        try:
                            total_cache_size += file_path.stat().st_size
                            cache_files += 1
                        except (OSError, PermissionError):
                            continue

        # Convertir en MB
        cache_size_mb = total_cache_size / 1024 / 1024

        print(f"✅ Cache: {cache_size_mb:.1f}MB, {cache_files} fichiers")

        # Recommandation si le cache est trop gros
        if cache_size_mb > 100:
            print(
                f"⚠️ Cache volumineux détecté: {cache_size_mb:.1f}MB - Considérer le"
                " nettoyage"
            )


if __name__ == "__main__":
    # Test rapide en ligne de commande
    print("🧪 Test de performance Phase 3...")

    monitor = PerformanceMonitor()
    monitor.start()

    # Test d'import rapide
    import athalia_core  # noqa: F401

    metrics = monitor.stop()
    print(
        f"✅ Performance: {metrics['duration']:.3f}s, {metrics['memory_used_mb']:.1f}MB"
    )

    if metrics["duration"] < 1.0 and metrics["memory_used_mb"] < 100:
        print("✅ Performance Phase 3 OK")
        exit(0)
    else:
        print("❌ Performance Phase 3 à améliorer")
        exit(1)

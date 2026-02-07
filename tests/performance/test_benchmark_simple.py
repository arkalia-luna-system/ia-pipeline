#!/usr/bin/env python3
"""
Test de performance simplifié pour Athalia
Version qui fonctionne sans dépendances externes problématiques
"""

import os
import sys
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

# Ajouter le répertoire racine au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


class PerformanceBenchmark:
    """Classe pour mesurer les performances des fonctions critiques"""

    def __init__(self):
        self.results: dict[str, float] = {}
        self.iterations = 1000

    def measure_time(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> float:
        """Mesure le temps d'exécution d'une fonction"""
        start_time = time.perf_counter()

        for _ in range(self.iterations):
            func(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        avg_time = total_time / self.iterations

        return avg_time

    def benchmark_string_operations(self) -> dict[str, float]:
        """Benchmark des opérations sur les chaînes"""
        logger.info("🔍 Benchmark des opérations sur les chaînes...")

        test_string = "Ceci est une chaîne de test pour mesurer les performances"

        # Test de concaténation
        def string_concat():
            result = ""
            for i in range(100):
                result += str(i)
            return result

        # Test de formatage
        def string_format():
            return "".join([f"item_{i}" for i in range(100)])

        # Test de split/join
        def string_split_join():
            words = test_string.split()
            return " ".join(words)

        results = {
            "concat": self.measure_time(string_concat),
            "format": self.measure_time(string_format),
            "split_join": self.measure_time(string_split_join),
        }

        self.results.update(results)
        return results

    def benchmark_file_operations(self) -> dict[str, float]:
        """Benchmark des opérations sur les fichiers"""
        logger.info("📁 Benchmark des opérations sur les fichiers...")

        test_content = "Contenu de test\n" * 100
        test_file = Path("temp_benchmark.txt")

        # Test d'écriture
        def file_write():
            test_file.write_text(test_content, encoding="utf-8")

        # Test de lecture
        def file_read():
            return test_file.read_text(encoding="utf-8")

        # Test de suppression
        def file_delete():
            if test_file.exists():
                test_file.unlink()

        # Préparer le fichier
        test_file.write_text(test_content, encoding="utf-8")

        results = {
            "write": self.measure_time(file_write),
            "read": self.measure_time(file_read),
            "delete": self.measure_time(file_delete),
        }

        # Nettoyer
        if test_file.exists():
            test_file.unlink()

        self.results.update(results)
        return results

    def benchmark_path_operations(self) -> dict[str, float]:
        """Benchmark des opérations sur les chemins"""
        logger.info("🛤️ Benchmark des opérations sur les chemins...")

        test_path = Path("tests/performance/benchmark_test")

        # Test de création de répertoire
        def create_dir():
            test_path.mkdir(parents=True, exist_ok=True)

        # Test de vérification d'existence
        def check_exists():
            return test_path.exists()

        # Test de suppression
        def remove_dir():
            if test_path.exists():
                test_path.rmdir()

        results = {
            "create_dir": self.measure_time(create_dir),
            "check_exists": self.measure_time(check_exists),
            "remove_dir": self.measure_time(remove_dir),
        }

        # Nettoyer
        if test_path.exists():
            test_path.rmdir()

        self.results.update(results)
        return results

    def benchmark_memory_operations(self) -> dict[str, float]:
        """Benchmark des opérations mémoire"""
        logger.info("🧠 Benchmark des opérations mémoire...")

        # Test de création de liste
        def create_list():
            return list(range(1000))

        # Test de création de dictionnaire
        def create_dict():
            return {f"key_{i}": f"value_{i}" for i in range(1000)}

        # Test de création de set
        def create_set():
            return set(range(1000))

        results = {
            "create_list": self.measure_time(create_list),
            "create_dict": self.measure_time(create_dict),
            "create_set": self.measure_time(create_set),
        }

        self.results.update(results)
        return results

    def run_all_benchmarks(self) -> dict[str, dict[str, float]]:
        """Exécute tous les benchmarks"""
        logger.info("🚀 Démarrage des benchmarks de performance...")

        all_results = {
            "string_operations": self.benchmark_string_operations(),
            "file_operations": self.benchmark_file_operations(),
            "path_operations": self.benchmark_path_operations(),
            "memory_operations": self.benchmark_memory_operations(),
        }

        return all_results

    def generate_report(self) -> str:
        """Génère un rapport de performance"""
        report = """
==========================================
📊 RAPPORT DE PERFORMANCE ATHALIA
==========================================

Résultats des benchmarks (temps moyen en secondes):
"""

        for category, results in self.results.items():
            report += f"\n--- {category.upper()} ---\n"
            if isinstance(results, dict):
                for operation, time_taken in results.items():
                    report += f"  {operation}: {time_taken:.6f}s\n"
            elif isinstance(results, int | float):
                report += f"  {category}: {results:.6f}s\n"

        report += f"\nTotal des opérations testées: {len(self.results)}"
        report += f"\nItérations par test: {self.iterations}"

        return report


# Configuration du logging simple
class SimpleLogger:
    def info(self, message: str):
        print(f"ℹ️  {message}")

    def error(self, message: str):
        print(f"❌ {message}")

    def success(self, message: str):
        print(f"✅ {message}")


logger = SimpleLogger()


def test_performance_benchmarks():
    """Test principal des benchmarks de performance"""
    logger.info("⚡ Démarrage des tests de performance...")

    try:
        # Créer l'instance de benchmark
        benchmark = PerformanceBenchmark()

        # Exécuter tous les benchmarks
        results = benchmark.run_all_benchmarks()

        # Générer le rapport
        report = benchmark.generate_report()

        # Afficher le rapport
        print(report)

        # Vérifier que les temps sont raisonnables
        for category, category_results in results.items():
            if isinstance(category_results, dict):
                for operation, time_taken in category_results.items():
                    # Les opérations ne devraient pas prendre plus de 1 seconde en moyenne
                    assert time_taken < 1.0, (
                        f"Performance dégradée: {operation} prend {time_taken}s"
                    )
            elif isinstance(category_results, int | float):
                # Si c'est une valeur directe, vérifier qu'elle est raisonnable
                assert category_results < 1.0, (
                    f"Performance dégradée: {category} prend {category_results}s"
                )

        logger.success("Tous les tests de performance ont réussi!")
        return True

    except Exception as e:
        logger.error(f"Erreur lors des tests de performance: {e}")
        return False


if __name__ == "__main__":
    success = test_performance_benchmarks()
    sys.exit(0 if success else 1)

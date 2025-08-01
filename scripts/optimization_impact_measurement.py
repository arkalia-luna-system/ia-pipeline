#!/usr/bin/env python3
"""
Script de mesure d'impact des optimisations de tests.
Mesure les performances avant et après les optimisations.
"""

import time
import subprocess
import psutil
import os
from pathlib import Path
from typing import Dict, List, Tuple


class OptimizationImpactMeasurer:
    """Mesureur d'impact des optimisations de tests."""

    def __init__(self):
        self.results = {}
        self.test_files = [
            "tests/performance/test_performance_optimization.py::TestPerformanceOptimization::test_memory_leak_detection",
            "tests/integration/test_yaml_validity.py::TestYAMLValidity::test_yaml_performance",
            "tests/unit/ai/test_ai_robust_integration.py::test_ai_robust_memory_usage",
        ]

    def measure_test_performance(self, test_path: str) -> Dict[str, float]:
        """Mesure les performances d'un test spécifique."""
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        initial_cpu = process.cpu_percent()

        start_time = time.time()

        try:
            # Exécuter le test
            result = subprocess.run(
                ["python", "-m", "pytest", test_path, "-v", "--tb=short", "--no-cov"],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=Path(__file__).parent.parent,
            )

            end_time = time.time()
            execution_time = end_time - start_time

            # Mesurer l'utilisation finale
            final_memory = process.memory_info().rss / 1024 / 1024  # MB
            final_cpu = process.cpu_percent()

            memory_used = final_memory - initial_memory
            cpu_used = final_cpu - initial_cpu

            return {
                "execution_time": execution_time,
                "memory_used_mb": memory_used,
                "cpu_used_percent": cpu_used,
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
            }

        except subprocess.TimeoutExpired:
            return {
                "execution_time": 60.0,
                "memory_used_mb": 0,
                "cpu_used_percent": 0,
                "success": False,
                "output": "",
                "error": "Timeout",
            }
        except Exception as e:
            return {
                "execution_time": 0,
                "memory_used_mb": 0,
                "cpu_used_percent": 0,
                "success": False,
                "output": "",
                "error": str(e),
            }

    def run_measurements(self) -> Dict[str, Dict[str, float]]:
        """Exécute les mesures pour tous les tests."""
        print("🔍 Mesure de l'impact des optimisations...")
        print("=" * 60)

        for test_file in self.test_files:
            print(f"\n📊 Test: {test_file}")
            print("-" * 40)

            result = self.measure_test_performance(test_file)
            self.results[test_file] = result

            if result["success"]:
                print(f"✅ Succès")
                print(f"⏱️  Temps d'exécution: {result['execution_time']:.2f}s")
                print(f"💾 Mémoire utilisée: {result['memory_used_mb']:.1f}MB")
                print(f"🖥️  CPU utilisé: {result['cpu_used_percent']:.1f}%")
            else:
                print(f"❌ Échec: {result['error']}")

        return self.results

    def generate_report(self) -> str:
        """Génère un rapport d'impact des optimisations."""
        report = []
        report.append("# Rapport d'Impact des Optimisations de Tests")
        report.append("")
        report.append("## Résumé des Performances")
        report.append("")

        total_time = 0
        total_memory = 0
        successful_tests = 0

        for test_file, result in self.results.items():
            if result["success"]:
                successful_tests += 1
                total_time += result["execution_time"]
                total_memory += result["memory_used_mb"]

                report.append(f"### {test_file}")
                report.append(
                    f"- **Temps d'exécution**: {result['execution_time']:.2f}s"
                )
                report.append(
                    f"- **Mémoire utilisée**: {result['memory_used_mb']:.1f}MB"
                )
                report.append(f"- **CPU utilisé**: {result['cpu_used_percent']:.1f}%")
                report.append("")

        report.append("## Statistiques Globales")
        report.append("")
        report.append(f"- **Tests réussis**: {successful_tests}/{len(self.test_files)}")
        report.append(f"- **Temps total**: {total_time:.2f}s")
        report.append(f"- **Mémoire totale**: {total_memory:.1f}MB")
        report.append(
            f"- **Temps moyen par test**: {total_time/successful_tests:.2f}s"
            if successful_tests > 0
            else "- **Temps moyen par test**: N/A"
        )
        report.append(
            f"- **Mémoire moyenne par test**: {total_memory/successful_tests:.1f}MB"
            if successful_tests > 0
            else "- **Mémoire moyenne par test**: N/A"
        )

        return "\n".join(report)

    def save_report(self, filename: str = "optimization_impact_report.md"):
        """Sauvegarde le rapport dans un fichier."""
        report = self.generate_report()
        report_path = Path(__file__).parent / filename

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"\n📄 Rapport sauvegardé: {report_path}")
        return report_path


def main():
    """Fonction principale."""
    print("🚀 Démarrage de la mesure d'impact des optimisations")
    print("=" * 60)

    # Vérifier que nous sommes dans l'environnement virtuel
    if not os.path.exists(".venv"):
        print("❌ Erreur: Environnement virtuel non trouvé")
        print("   Veuillez activer l'environnement virtuel: source .venv/bin/activate")
        return 1

    measurer = OptimizationImpactMeasurer()

    try:
        # Exécuter les mesures
        results = measurer.run_measurements()

        # Générer et sauvegarder le rapport
        report_path = measurer.save_report()

        print("\n" + "=" * 60)
        print("✅ Mesure d'impact terminée avec succès!")
        print(f"📊 Rapport disponible: {report_path}")

        # Afficher un résumé
        successful_tests = sum(1 for r in results.values() if r["success"])
        total_time = sum(r["execution_time"] for r in results.values() if r["success"])
        total_memory = sum(
            r["memory_used_mb"] for r in results.values() if r["success"]
        )

        print(f"\n📈 Résumé:")
        print(f"   Tests réussis: {successful_tests}/{len(results)}")
        print(f"   Temps total: {total_time:.2f}s")
        print(f"   Mémoire totale: {total_memory:.1f}MB")

        return 0

    except KeyboardInterrupt:
        print("\n⚠️  Mesure interrompue par l'utilisateur")
        return 1
    except Exception as e:
        print(f"\n❌ Erreur lors de la mesure: {e}")
        return 1


if __name__ == "__main__":
    exit(main())

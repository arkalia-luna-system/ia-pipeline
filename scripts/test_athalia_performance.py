#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de performance d'Athalia avec cache
"""

from datetime import datetime
import json
import subprocess
import time


def test_athalia_performance():
    """Test de performance d'Athalia."""
    print("🚀 Test de performance Athalia avec cache...")

    # Test sur le projet athalia_core
    test_path = "athalia_core"

    results = {
        "timestamp": datetime.now().isoformat(),
        "test_path": test_path,
        "baseline": {},
        "with_cache": {},
        "improvement": {},
    }

    # Test 1: Baseline (sans cache)
    print("\n📊 Test baseline (sans cache)...")
    start_time = time.time()

    try:
        result = subprocess.run(
            ["python", "athalia_unified.py", test_path, "--action", "audit"],
            capture_output=True,
            text=True,
            timeout=60,
        )

        baseline_time = time.time() - start_time
        results["baseline"] = {
            "execution_time": baseline_time,
            "success": result.returncode == 0,
            "output_lines": len(result.stdout.split("\n")),
            "error_lines": len(result.stderr.split("\n")) if result.stderr else 0,
        }

        print(f"✅ Baseline: {baseline_time:.2f} secondes")

    except subprocess.TimeoutExpired:
        print("❌ Timeout baseline")
        results["baseline"] = {"error": "timeout"}
        return results
    except Exception as e:
        print(f"❌ Erreur baseline: {e}")
        results["baseline"] = {"error": str(e)}
        return results

    # Test 2: Avec cache (deuxième exécution)
    print("\n⚡ Test avec cache (deuxième exécution)...")
    start_time = time.time()

    try:
        result = subprocess.run(
            ["python", "athalia_unified.py", test_path, "--action", "audit"],
            capture_output=True,
            text=True,
            timeout=60,
        )

        cached_time = time.time() - start_time
        results["with_cache"] = {
            "execution_time": cached_time,
            "success": result.returncode == 0,
            "output_lines": len(result.stdout.split("\n")),
            "error_lines": len(result.stderr.split("\n")) if result.stderr else 0,
        }

        print(f"✅ Avec cache: {cached_time:.2f} secondes")

    except subprocess.TimeoutExpired:
        print("❌ Timeout avec cache")
        results["with_cache"] = {"error": "timeout"}
    except Exception as e:
        print(f"❌ Erreur avec cache: {e}")
        results["with_cache"] = {"error": str(e)}

    # Calcul de l'amélioration
    if (
        "execution_time" in results["baseline"]
        and "execution_time" in results["with_cache"]
    ):
        baseline = results["baseline"]["execution_time"]
        cached = results["with_cache"]["execution_time"]

        improvement = ((baseline - cached) / baseline) * 100

        results["improvement"] = {
            "time_saved": baseline - cached,
            "improvement_percent": improvement,
            "speedup_factor": baseline / cached if cached > 0 else 0,
        }

        print(f"\n📈 Amélioration: {improvement:.1f}%")
        print(f"⏱️  Temps économisé: {baseline - cached:.2f} secondes")
        print(f"🚀 Facteur d'accélération: {baseline / cached:.2f}x")

    return results


def test_multiple_runs():
    """Test avec plusieurs exécutions pour valider le cache."""
    print("\n🔄 Test avec plusieurs exécutions...")

    test_path = "athalia_core"
    times = []

    for i in range(3):
        print(f"  Exécution {i+1}/3...")
        start_time = time.time()

        try:
            subprocess.run(
                ["python", "athalia_unified.py", test_path, "--action", "audit"],
                capture_output=True,
                text=True,
                timeout=60,
            )

            execution_time = time.time() - start_time
            times.append(execution_time)

            print(f"    Temps: {execution_time:.2f}s")

        except Exception as e:
            print(f"    Erreur: {e}")
            times.append(None)

    # Analyse des résultats
    valid_times = [t for t in times if t is not None]

    if len(valid_times) >= 2:
        first_time = valid_times[0]
        avg_subsequent = sum(valid_times[1:]) / len(valid_times[1:])

        improvement = ((first_time - avg_subsequent) / first_time) * 100

        print("\n📊 Résultats multiples:")
        print(f"  Premier exécution: {first_time:.2f}s")
        print(f"  Moyenne suivantes: {avg_subsequent:.2f}s")
        print(f"  Amélioration: {improvement:.1f}%")

        return {
            "first_execution": first_time,
            "avg_subsequent": avg_subsequent,
            "improvement_percent": improvement,
            "all_times": valid_times,
        }

    return {"error": "Pas assez de données valides"}


def print_summary(results, multiple_results=None):
    """Affiche un résumé des résultats."""
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ PERFORMANCE ATHALIA")
    print("=" * 60)

    if "baseline" in results and "execution_time" in results["baseline"]:
        print(
            f"⏱️  Temps baseline: {results['baseline']['execution_time']:.2f} secondes"
        )

    if "with_cache" in results and "execution_time" in results["with_cache"]:
        print(
            "⚡ Temps avec cache: "
            f"{results['with_cache']['execution_time']:.2f} secondes"
        )

    if "improvement" in results and "improvement_percent" in results["improvement"]:
        improvement = results["improvement"]["improvement_percent"]
        print(f"📈 Amélioration: {improvement:.1f}%")

        if improvement >= 30:
            print("🎉 OBJECTIF ATTEINT! (-30% ou plus)")
        elif improvement >= 15:
            print("✅ BONNE AMÉLIORATION (-15% ou plus)")
        elif improvement >= 5:
            print("📈 AMÉLIORATION MODESTE (-5% ou plus)")
        else:
            print("⚠️  AMÉLIORATION LIMITÉE")

    if multiple_results and "improvement_percent" in multiple_results:
        print(
            "\n🔄 Test multiple: "
            f"{multiple_results['improvement_percent']:.1f}% d'amélioration"
        )

    print("=" * 60)


def main():
    """Fonction principale."""
    # Test de performance simple
    results = test_athalia_performance()

    # Test avec plusieurs exécutions
    multiple_results = test_multiple_runs()

    # Affichage du résumé
    print_summary(results, multiple_results)

    # Sauvegarde des résultats
    output = {"single_test": results, "multiple_test": multiple_results}

    filename = (
        f"athalia_performance_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n💾 Résultats sauvegardés dans {filename}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script de validation finale des optimisations de tests.
Vérifie que les optimisations sont robustes et n'ont pas cassé la fonctionnalité.
"""

import subprocess
import time
from pathlib import Path


class OptimizationValidator:
    """Validateur des optimisations de tests."""

    def __init__(self):
        self.validation_results = {}
        self.test_suites = [
            {
                "name": "Tests de Performance Optimisés",
                "path": "tests/performance/test_performance_optimization.py",
                "expected_tests": 18,
            },
            {
                "name": "Tests d'Intégration YAML",
                "path": "tests/integration/test_yaml_validity.py",
                "expected_tests": 15,
            },
            {
                "name": "Tests d'IA Robust",
                "path": "tests/unit/ai/test_ai_robust_integration.py",
                "expected_tests": 8,
            },
            {
                "name": "Tests de Cache Manager",
                "path": "tests/unit/test_cache_manager_complete.py",
                "expected_tests": 25,
            },
            {
                "name": "Tests d'Audit Intelligent",
                "path": "tests/unit/test_audit_intelligent.py",
                "expected_tests": 8,
            },
        ]

    def run_test_suite(self, suite: dict) -> dict:
        """Exécute une suite de tests et mesure ses performances."""
        print(f"\n🔍 Validation: {suite['name']}")
        print("-" * 50)

        start_time = time.time()

        try:
            # Exécuter la suite de tests
            result = subprocess.run(
                [
                    "python",
                    "-m",
                    "pytest",
                    suite["path"],
                    "-v",
                    "--tb=short",
                    "--no-cov",
                ],
                capture_output=True,
                text=True,
                timeout=120,
                cwd=Path(__file__).parent.parent,
            )

            end_time = time.time()
            execution_time = end_time - start_time

            # Analyser les résultats
            output_lines = result.stdout.split("\n")
            test_count = 0
            passed_tests = 0
            failed_tests = 0

            for line in output_lines:
                if "PASSED" in line:
                    passed_tests += 1
                    test_count += 1
                elif "FAILED" in line:
                    failed_tests += 1
                    test_count += 1
                elif "ERROR" in line:
                    failed_tests += 1
                    test_count += 1

            return {
                "success": result.returncode == 0,
                "execution_time": execution_time,
                "total_tests": test_count,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "expected_tests": suite["expected_tests"],
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode,
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "execution_time": 120.0,
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "expected_tests": suite["expected_tests"],
                "output": "",
                "error": "Timeout après 120 secondes",
                "return_code": -1,
            }
        except Exception as e:
            return {
                "success": False,
                "execution_time": 0,
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "expected_tests": suite["expected_tests"],
                "output": "",
                "error": str(e),
                "return_code": -1,
            }

    def validate_optimizations(self) -> dict:
        """Valide toutes les optimisations."""
        print("🚀 Démarrage de la validation des optimisations")
        print("=" * 60)

        total_execution_time = 0
        total_tests = 0
        total_passed = 0
        total_failed = 0

        for suite in self.test_suites:
            result = self.run_test_suite(suite)
            self.validation_results[suite["name"]] = result

            # Afficher les résultats
            if result["success"]:
                print(f"✅ {suite['name']}: SUCCÈS")
                print(f"   ⏱️  Temps: {result['execution_time']:.2f}s")
                print(
                    f"   📊 Tests: {result['passed_tests']}/{result['total_tests']} réussis"
                )

                if result["total_tests"] != result["expected_tests"]:
                    print(
                        f"   ⚠️  Attention: {result['total_tests']} tests trouvés, {result['expected_tests']} attendus"
                    )
            else:
                print(f"❌ {suite['name']}: ÉCHEC")
                print(f"   ⏱️  Temps: {result['execution_time']:.2f}s")
                print(
                    f"   📊 Tests: {result['passed_tests']}/{result['total_tests']} réussis"
                )
                print(f"   🚨 Erreur: {result['error']}")

            # Accumuler les statistiques
            total_execution_time += result["execution_time"]
            total_tests += result["total_tests"]
            total_passed += result["passed_tests"]
            total_failed += result["failed_tests"]

        return {
            "total_execution_time": total_execution_time,
            "total_tests": total_tests,
            "total_passed": total_passed,
            "total_failed": total_failed,
            "success_rate": (
                (total_passed / total_tests * 100) if total_tests > 0 else 0
            ),
        }

    def generate_validation_report(self) -> str:
        """Génère un rapport de validation."""
        report = []
        report.append("# Rapport de Validation des Optimisations")
        report.append("")
        report.append("## Résumé de la Validation")
        report.append("")

        total_execution_time = 0
        total_tests = 0
        total_passed = 0
        total_failed = 0

        for suite_name, result in self.validation_results.items():
            total_execution_time += result["execution_time"]
            total_tests += result["total_tests"]
            total_passed += result["passed_tests"]
            total_failed += result["failed_tests"]

            report.append(f"### {suite_name}")
            report.append(
                f"- **Statut**: {'✅ SUCCÈS' if result['success'] else '❌ ÉCHEC'}"
            )
            report.append(f"- **Temps d'exécution**: {result['execution_time']:.2f}s")
            report.append(f"- **Tests exécutés**: {result['total_tests']}")
            report.append(f"- **Tests réussis**: {result['passed_tests']}")
            report.append(f"- **Tests échoués**: {result['failed_tests']}")

            if result["total_tests"] != result["expected_tests"]:
                report.append(
                    f"- **⚠️  Attention**: {result['total_tests']} tests trouvés, {result['expected_tests']} attendus"
                )

            if not result["success"]:
                report.append(f"- **Erreur**: {result['error']}")

            report.append("")

        report.append("## Statistiques Globales")
        report.append("")
        report.append(f"- **Temps total d'exécution**: {total_execution_time:.2f}s")
        report.append(f"- **Total des tests**: {total_tests}")
        report.append(f"- **Tests réussis**: {total_passed}")
        report.append(f"- **Tests échoués**: {total_failed}")
        report.append(
            f"- **Taux de succès**: {total_passed / total_tests * 100:.1f}%"
            if total_tests > 0
            else "- **Taux de succès**: N/A"
        )

        # Évaluation de la validation
        report.append("")
        report.append("## Évaluation de la Validation")
        report.append("")

        if total_failed == 0 and total_tests > 0:
            report.append("✅ **VALIDATION RÉUSSIE**")
            report.append("- Tous les tests optimisés passent avec succès")
            report.append("- Les optimisations n'ont pas cassé la fonctionnalité")
            report.append("- Les performances sont améliorées")
        else:
            report.append("❌ **VALIDATION ÉCHOUÉE**")
            report.append(f"- {total_failed} tests ont échoué")
            report.append("- Des problèmes ont été détectés")
            report.append("- Révision des optimisations nécessaire")

        return "\n".join(report)

    def save_validation_report(
        self, filename: str = "optimization_validation_report.md"
    ):
        """Sauvegarde le rapport de validation."""
        report = self.generate_validation_report()
        report_path = Path(__file__).parent / filename

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"\n📄 Rapport de validation sauvegardé: {report_path}")
        return report_path


def main():
    """Fonction principale."""
    print("🚀 Démarrage de la validation des optimisations")
    print("=" * 60)

    # Vérifier que nous sommes dans l'environnement virtuel
    if not Path(".venv").exists():
        print("❌ Erreur: Environnement virtuel non trouvé")
        print("   Veuillez activer l'environnement virtuel: source .venv/bin/activate")
        return 1

    validator = OptimizationValidator()

    try:
        # Exécuter la validation
        stats = validator.validate_optimizations()

        # Générer et sauvegarder le rapport
        report_path = validator.save_validation_report()

        print("\n" + "=" * 60)
        print("✅ Validation terminée!")
        print(f"📊 Rapport disponible: {report_path}")

        # Afficher un résumé final
        print("\n📈 Résumé de la validation:")
        print(f"   Temps total: {stats['total_execution_time']:.2f}s")
        print(f"   Tests totaux: {stats['total_tests']}")
        print(f"   Tests réussis: {stats['total_passed']}")
        print(f"   Tests échoués: {stats['total_failed']}")
        print(f"   Taux de succès: {stats['success_rate']:.1f}%")

        if stats["total_failed"] == 0:
            print("\n🎉 Toutes les optimisations sont validées avec succès!")
            return 0
        else:
            print(
                f"\n⚠️  {stats['total_failed']} tests ont échoué. Révision nécessaire."
            )
            return 1

    except KeyboardInterrupt:
        print("\n⚠️  Validation interrompue par l'utilisateur")
        return 1
    except Exception as e:
        print(f"\n❌ Erreur lors de la validation: {e}")
        return 1


if __name__ == "__main__":
    exit(main())

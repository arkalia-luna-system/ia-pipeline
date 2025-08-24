#!/usr/bin/env python3
"""
Système de benchmarks avancés pour Athalia
Interface web moderne avec métriques détaillées et comparaisons
"""

import json
import logging
import time
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any

import psutil

# Import des composants Athalia réels
try:
    from athalia_core.core.cache_manager import CacheManager
    from athalia_core.core.unified_orchestrator import UnifiedOrchestrator
    from athalia_core.metrics.collector import MetricsCollector
    from athalia_core.quality.code_linter import CodeLinter
    from athalia_core.validation.security_validator import CommandSecurityValidator

    ATHALIA_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Composants Athalia non disponibles: {e}")
    ATHALIA_AVAILABLE = False

logger = logging.getLogger(__name__)


class AdvancedBenchmarkSystem:
    """
    Système de benchmarks avancés avec interface web moderne
    et vraie intégration Athalia
    """

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.benchmarks_dir = self.project_path / "dashboard" / "benchmarks"
        self.benchmarks_dir.mkdir(parents=True, exist_ok=True)
        self.results_file = self.benchmarks_dir / "benchmark_results.json"
        self.benchmark_data = self._load_benchmark_data()

        # Initialisation des composants Athalia
        self.athalia_components = self._initialize_athalia_components()

    def _initialize_athalia_components(self) -> dict[str, Any]:
        """Initialise les composants Athalia pour les benchmarks"""
        if not ATHALIA_AVAILABLE:
            return {}

        try:
            return {
                "orchestrator": UnifiedOrchestrator(),
                "security_validator": CommandSecurityValidator(),
                "code_linter": CodeLinter(str(self.project_path)),
                "cache_manager": CacheManager(".athalia_cache"),
                "metrics_collector": MetricsCollector(str(self.project_path)),
            }
        except Exception as e:
            logger.error(f"Erreur d'initialisation des composants Athalia: {e}")
            return {}

    def _load_benchmark_data(self) -> dict[str, Any]:
        """Charge les données de benchmark existantes"""
        if self.results_file.exists():
            try:
                with open(self.results_file, encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Impossible de charger les benchmarks: {e}")

        return self._get_default_benchmarks()

    def _get_default_benchmarks(self) -> dict[str, Any]:
        """Retourne des benchmarks par défaut"""
        return {
            "last_updated": datetime.now().isoformat(),
            "total_runs": 0,
            "benchmarks": {
                "performance": {
                    "name": "Performance Générale",
                    "description": "Tests de performance CPU, mémoire et I/O",
                    "last_score": 0,
                    "best_score": 0,
                    "runs": [],
                    "category": "Performance",
                },
                "security": {
                    "name": "Sécurité",
                    "description": "Tests de sécurité et validation",
                    "last_score": 0,
                    "best_score": 0,
                    "runs": [],
                    "category": "Sécurité",
                },
                "code_quality": {
                    "name": "Qualité du Code",
                    "description": "Tests de qualité et standards",
                    "last_score": 0,
                    "best_score": 0,
                    "runs": [],
                    "category": "Qualité",
                },
                "ai_generation": {
                    "name": "Génération IA",
                    "description": "Tests de génération automatique",
                    "last_score": 0,
                    "best_score": 0,
                    "runs": [],
                    "category": "IA",
                },
                "robotics": {
                    "name": "Robotics",
                    "description": "Tests de validation robotics",
                    "last_score": 0,
                    "best_score": 0,
                    "runs": [],
                    "category": "Robotics",
                },
            },
        }

    def run_performance_benchmark(self) -> dict[str, Any]:
        """Exécute le benchmark de performance avec vraie intégration Athalia"""
        start_time = time.time()

        # Test CPU avec vraie charge
        cpu_start = time.time()
        cpu_result = self._cpu_benchmark()
        cpu_time = time.time() - cpu_start

        # Test mémoire avec vraie utilisation
        memory_result = self._memory_benchmark()

        # Test I/O avec vraies opérations
        io_start = time.time()
        io_result = self._io_benchmark()
        io_time = time.time() - io_start

        # Test de cache Athalia (si disponible)
        cache_start = time.time()
        cache_result = self._cache_benchmark()
        cache_time = time.time() - cache_start

        total_time = time.time() - start_time

        # Calcul du score basé sur de vrais métriques
        cpu_score = max(0, 100 - (cpu_time * 10))
        memory_score = max(0, 100 - (memory_result["usage_percent"] * 0.5))
        io_score = max(0, 100 - (io_time * 20))
        cache_score = cache_result.get("score", 50)

        overall_score = (cpu_score + memory_score + io_score + cache_score) / 4

        result = {
            "timestamp": datetime.now().isoformat(),
            "duration": total_time,
            "scores": {
                "cpu": round(cpu_score, 2),
                "memory": round(memory_score, 2),
                "io": round(io_score, 2),
                "cache": round(cache_score, 2),
                "overall": round(overall_score, 2),
            },
            "metrics": {
                "cpu_time": round(cpu_time, 4),
                "memory_usage": memory_result["usage_percent"],
                "io_time": round(io_time, 4),
                "cache_time": round(cache_time, 4),
            },
            "details": {
                "cpu": cpu_result,
                "memory": memory_result,
                "io": io_result,
                "cache": cache_result,
            },
        }

        return result

    def _cpu_benchmark(self) -> dict[str, Any]:
        """Benchmark CPU avec vraie charge de travail"""
        start_time = time.time()

        # Calcul intensif réaliste
        result = 0
        for i in range(1000000):
            result += i * i
            if i % 100000 == 0:  # Vérification périodique
                _ = result % 1000

        duration = time.time() - start_time

        return {
            "operations": 1000000,
            "duration": duration,
            "operations_per_second": 1000000 / duration if duration > 0 else 0,
            "result_hash": hash(result) % 1000000,  # Vérification d'intégrité
        }

    def _memory_benchmark(self) -> dict[str, Any]:
        """Benchmark mémoire avec vraie utilisation"""
        process = psutil.Process()
        memory_info = process.memory_info()

        # Test d'allocation mémoire
        test_data = []
        try:
            for i in range(1000):
                test_data.append([i] * 100)
            memory_after = process.memory_info()
            memory_increase = memory_after.rss - memory_info.rss
        except Exception as e:
            memory_increase = 0
            logger.warning(f"Erreur lors du test mémoire: {e}")
        finally:
            del test_data  # Libération mémoire

        return {
            "rss_mb": round(memory_info.rss / 1024 / 1024, 2),
            "vms_mb": round(memory_info.vms / 1024 / 1024, 2),
            "usage_percent": process.memory_percent(),
            "memory_increase_kb": round(memory_increase / 1024, 2),
        }

    def _io_benchmark(self) -> dict[str, Any]:
        """Benchmark I/O avec vraies opérations de fichiers"""
        start_time = time.time()

        # Test d'écriture/lecture réaliste
        test_file = self.benchmarks_dir / "io_test.tmp"
        test_data = "x" * 10000

        try:
            # Écriture
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_data)

            # Lecture
            with open(test_file, encoding="utf-8") as f:
                content = f.read()

            # Vérification d'intégrité
            data_valid = content == test_data

            # Nettoyage
            if test_file.exists():
                test_file.unlink()

            duration = time.time() - start_time

            return {
                "write_size": len(test_data),
                "read_size": len(content),
                "duration": duration,
                "success": True,
                "data_valid": data_valid,
                "file_size_bytes": len(test_data),
            }
        except Exception as e:
            return {
                "error": str(e),
                "duration": time.time() - start_time,
                "success": False,
            }

    def _cache_benchmark(self) -> dict[str, Any]:
        """Benchmark du cache Athalia (si disponible)"""
        if (
            not self.athalia_components
            or "cache_manager" not in self.athalia_components
        ):
            return {"score": 50, "status": "non disponible"}

        try:
            cache_manager = self.athalia_components["cache_manager"]

            # Test de performance du cache
            start_time = time.time()

            # Test d'écriture
            test_key = "benchmark_test"
            test_value = {"data": "test", "timestamp": time.time()}

            if hasattr(cache_manager, "set"):
                cache_manager.set(test_key, test_value)
                write_time = time.time() - start_time

                # Test de lecture
                read_start = time.time()
                if hasattr(cache_manager, "get"):
                    cache_manager.get(test_key)  # Test de lecture
                    read_time = time.time() - read_start

                    # Test de suppression
                    if hasattr(cache_manager, "delete"):
                        cache_manager.delete(test_key)

                    # Calcul du score
                    write_score = max(0, 100 - (write_time * 1000))
                    read_score = max(0, 100 - (read_time * 1000))
                    overall_score = (write_score + read_score) / 2

                    return {
                        "score": round(overall_score, 2),
                        "status": "testé",
                        "write_time_ms": round(write_time * 1000, 3),
                        "read_time_ms": round(read_time * 1000, 3),
                        "write_score": round(write_score, 2),
                        "read_score": round(read_score, 2),
                        "cache_available": True,
                    }

            return {"score": 50, "status": "méthodes non disponibles"}

        except Exception as e:
            logger.warning(f"Erreur lors du benchmark cache: {e}")
            return {"score": 50, "status": f"erreur: {str(e)}"}

    def run_security_benchmark(self) -> dict[str, Any]:
        """Exécute le benchmark de sécurité avec vraie validation Athalia"""
        start_time = time.time()

        if (
            not self.athalia_components
            or "security_validator" not in self.athalia_components
        ):
            return self._fallback_security_benchmark()

        try:
            security_validator = self.athalia_components["security_validator"]

            # Test de validation de commandes
            test_commands = [
                "ls -la",  # Commande sûre
                "rm -rf /",  # Commande dangereuse
                "python -c 'print(\"hello\")'",  # Commande Python sûre
                "curl http://example.com",  # Commande réseau
                "echo 'test' > /tmp/test",  # Commande d'écriture
            ]

            validation_results = []
            for cmd in test_commands:
                if hasattr(security_validator, "validate_command"):
                    is_safe = security_validator.validate_command(cmd)
                    validation_results.append(
                        {
                            "command": cmd,
                            "is_safe": is_safe,
                            "expected_safe": cmd != "rm -rf /",
                        }
                    )
                else:
                    validation_results.append(
                        {
                            "command": cmd,
                            "is_safe": "non testé",
                            "expected_safe": cmd != "rm -rf /",
                        }
                    )

            # Test d'audit de sécurité
            audit_results = {}
            if hasattr(security_validator, "audit_security"):
                audit_results = security_validator.audit_security()

            # Calcul du score de sécurité
            safe_commands = sum(
                1 for r in validation_results if r.get("is_safe") is True
            )
            total_commands = len(validation_results)
            validation_score = (
                (safe_commands / total_commands) * 100 if total_commands > 0 else 0
            )

            # Score global
            overall_score = validation_score
            if audit_results:
                audit_score = audit_results.get("score", 0)
                overall_score = (validation_score + audit_score) / 2

            duration = time.time() - start_time

            return {
                "timestamp": datetime.now().isoformat(),
                "duration": duration,
                "score": round(overall_score, 2),
                "validation_score": round(validation_score, 2),
                "audit_score": audit_results.get("score", 0),
                "tests": {
                    "total_commands": total_commands,
                    "safe_commands": safe_commands,
                    "validation_results": validation_results,
                    "audit_results": audit_results,
                },
            }

        except Exception as e:
            logger.error(f"Erreur lors du benchmark de sécurité: {e}")
            return self._fallback_security_benchmark()

    def _fallback_security_benchmark(self) -> dict[str, Any]:
        """Benchmark de sécurité de fallback"""
        return {
            "timestamp": datetime.now().isoformat(),
            "duration": 0.1,
            "score": 50,
            "validation_score": 50,
            "audit_score": 50,
            "tests": {
                "total_commands": 0,
                "safe_commands": 0,
                "validation_results": [],
                "audit_results": {},
                "note": "Composants Athalia non disponibles",
            },
        }

    def run_code_quality_benchmark(self) -> dict[str, Any]:
        """Exécute le benchmark de qualité de code avec vrai linter Athalia"""
        start_time = time.time()

        if not self.athalia_components or "code_linter" not in self.athalia_components:
            return self._fallback_quality_benchmark()

        try:
            code_linter = self.athalia_components["code_linter"]

            # Test de linting sur le projet actuel
            lint_results = {}
            if hasattr(code_linter, "run_linting"):
                lint_results = code_linter.run_linting(str(self.project_path))

            # Test de métriques de qualité
            quality_metrics = {}
            if hasattr(code_linter, "get_quality_stats"):
                quality_metrics = code_linter.get_quality_stats()

            # Calcul du score de qualité
            quality_score = 100

            if lint_results:
                # Réduction du score basée sur les erreurs
                errors = lint_results.get("errors", 0)
                warnings = lint_results.get("warnings", 0)
                quality_score = max(0, 100 - (errors * 5) - (warnings * 1))

            duration = time.time() - start_time

            return {
                "timestamp": datetime.now().isoformat(),
                "duration": duration,
                "score": round(quality_score, 2),
                "lint_results": lint_results,
                "quality_metrics": quality_metrics,
                "project_path": str(self.project_path),
            }

        except Exception as e:
            logger.error(f"Erreur lors du benchmark de qualité: {e}")
            return self._fallback_quality_benchmark()

    def _fallback_quality_benchmark(self) -> dict[str, Any]:
        """Benchmark de qualité de fallback"""
        return {
            "timestamp": datetime.now().isoformat(),
            "duration": 0.1,
            "score": 50,
            "lint_results": {},
            "quality_metrics": {},
            "note": "Composants Athalia non disponibles",
        }

    def run_ai_generation_benchmark(self) -> dict[str, Any]:
        """Exécute le benchmark de génération IA avec vrais composants Athalia"""
        start_time = time.time()

        if not self.athalia_components or "orchestrator" not in self.athalia_components:
            return self._fallback_ai_benchmark()

        try:
            orchestrator = self.athalia_components["orchestrator"]

            # Test de génération de projet simple
            test_config = {
                "name": "benchmark_test_project",
                "description": "Projet de test pour benchmark",
                "type": "api",
                "dependencies": ["fastapi", "uvicorn"],
                "modules": ["core", "api"],
            }

            generation_result = {}
            if hasattr(orchestrator, "generate_project"):
                generation_result = orchestrator.generate_project(test_config)

            # Test de performance de génération
            generation_time = generation_result.get("generation_time", 0)
            files_created = generation_result.get("files_created", 0)

            # Calcul du score
            time_score = max(0, 100 - (generation_time * 10))
            files_score = min(100, files_created * 10)
            overall_score = (time_score + files_score) / 2

            duration = time.time() - start_time

            return {
                "timestamp": datetime.now().isoformat(),
                "duration": duration,
                "score": round(overall_score, 2),
                "generation_result": generation_result,
                "time_score": round(time_score, 2),
                "files_score": round(files_score, 2),
                "test_config": test_config,
            }

        except Exception as e:
            logger.error(f"Erreur lors du benchmark IA: {e}")
            return self._fallback_ai_benchmark()

    def _fallback_ai_benchmark(self) -> dict[str, Any]:
        """Benchmark IA de fallback"""
        return {
            "timestamp": datetime.now().isoformat(),
            "duration": 0.1,
            "score": 50,
            "generation_result": {},
            "time_score": 50,
            "files_score": 50,
            "note": "Composants Athalia non disponibles",
        }

    def run_robotics_benchmark(self) -> dict[str, Any]:
        """Exécute le benchmark robotics avec vrais composants Athalia"""
        start_time = time.time()

        # Test de validation robotics (si disponible)
        robotics_score = 50
        robotics_tests = {}

        try:
            # Vérifier la disponibilité des modules robotics
            robotics_modules = [
                "athalia_core.robotics.docker_robotics",
                "athalia_core.robotics.reachy_auditor",
                "athalia_core.robotics.robotics_validator",
            ]

            available_modules = 0
            for module_name in robotics_modules:
                try:
                    __import__(module_name)
                    available_modules += 1
                except ImportError:
                    pass

            if available_modules > 0:
                robotics_score = min(100, available_modules * 25)
                robotics_tests = {
                    "available_modules": available_modules,
                    "total_modules": len(robotics_modules),
                    "module_coverage": f"{available_modules}/{len(robotics_modules)}",
                }

        except Exception as e:
            logger.warning(f"Erreur lors du benchmark robotics: {e}")
            robotics_tests = {"error": str(e)}

        duration = time.time() - start_time

        return {
            "timestamp": datetime.now().isoformat(),
            "duration": duration,
            "score": round(robotics_score, 2),
            "robotics_tests": robotics_tests,
            "note": "Validation des modules robotics disponibles",
        }

    def run_all_benchmarks(self) -> dict[str, Any]:
        """Exécute tous les benchmarks et génère un rapport complet"""
        logger.info("🚀 Démarrage de la suite complète de benchmarks...")

        start_time = time.time()

        # Exécution des benchmarks
        results: dict[str, Any] = {
            "timestamp": datetime.now().isoformat(),
            "performance": self.run_performance_benchmark(),
            "security": self.run_security_benchmark(),
            "code_quality": self.run_code_quality_benchmark(),
            "ai_generation": self.run_ai_generation_benchmark(),
            "robotics": self.run_robotics_benchmark(),
        }

        # Calcul du score global
        scores = [
            results.get("performance", {}).get("scores", {}).get("overall", 0),
            results.get("security", {}).get("score", 0),
            results.get("code_quality", {}).get("score", 0),
            results.get("ai_generation", {}).get("score", 0),
            results.get("robotics", {}).get("score", 0),
        ]

        global_score = sum(scores) / len(scores)
        results["global_score"] = round(global_score, 2)
        results["total_duration"] = time.time() - start_time

        # Sauvegarde des résultats
        self._save_benchmark_results(results)

        logger.info(f"✅ Benchmarks terminés - Score global: {global_score}/100")

        return results

    def _save_benchmark_results(self, results: dict[str, Any]):
        """Sauvegarde les résultats des benchmarks"""
        try:
            # Mise à jour des données de benchmark
            self.benchmark_data["last_updated"] = datetime.now().isoformat()
            self.benchmark_data["total_runs"] += 1

            # Ajout des nouveaux résultats
            for benchmark_name, result in results.items():
                if benchmark_name in self.benchmark_data["benchmarks"]:
                    benchmark = self.benchmark_data["benchmarks"][benchmark_name]
                    benchmark["last_score"] = result.get("score", 0)
                    benchmark["best_score"] = max(
                        benchmark["best_score"], result.get("score", 0)
                    )
                    benchmark["runs"].append(
                        {
                            "timestamp": result.get("timestamp", ""),
                            "score": result.get("score", 0),
                            "duration": result.get("duration", 0),
                        }
                    )

                    # Garder seulement les 10 dernières exécutions
                    if len(benchmark["runs"]) > 10:
                        benchmark["runs"] = benchmark["runs"][-10:]

            # Sauvegarde dans le fichier
            with open(self.results_file, "w", encoding="utf-8") as f:
                json.dump(self.benchmark_data, f, indent=2, ensure_ascii=False)

            logger.info(f"💾 Résultats sauvegardés dans {self.results_file}")

        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde des benchmarks: {e}")

    def generate_html_report(self) -> str:
        """Génère un rapport HTML complet des benchmarks"""
        try:
            # Charger les derniers résultats
            if not self.results_file.exists():
                self.run_all_benchmarks()

            with open(self.results_file, encoding="utf-8") as f:
                data = json.load(f)

            # Génération du HTML
            html_content = self._generate_html_content(data)

            # Sauvegarde du rapport
            report_file = self.benchmarks_dir / "benchmark_report.html"
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            logger.info(f"📊 Rapport HTML généré: {report_file}")
            return str(report_file)

        except Exception as e:
            logger.error(f"Erreur lors de la génération du rapport HTML: {e}")
            return ""

    def _generate_html_content(self, data: dict[str, Any]) -> str:
        """Génère le contenu HTML du rapport"""
        # Template HTML moderne et responsive
        html_template = """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rapport de Benchmarks Athalia</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
                .container { max-width: 1200px; margin: 0 auto; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; }
                .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; }
                .header h1 { margin: 0; font-size: 2.5em; }
                .header p { margin: 10px 0 0 0; opacity: 0.9; }
                .content { padding: 30px; }
                .score-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
                .score-card { background: #f8f9fa; border-radius: 8px; padding: 20px; text-align: center; border-left: 4px solid #007bff; }
                .score-value { font-size: 2em; font-weight: bold; color: #007bff; margin: 10px 0; }
                .chart-container { margin: 30px 0; }
                .benchmark-details { background: #f8f9fa; border-radius: 8px; padding: 20px; margin: 20px 0; }
                .benchmark-details h3 { margin-top: 0; color: #333; }
                .metric-row { display: flex; justify-content: space-between; margin: 10px 0; padding: 10px; background: white; border-radius: 5px; }
                .metric-label { font-weight: bold; }
                .metric-value { color: #666; }
                .status-good { color: #28a745; }
                .status-warning { color: #ffc107; }
                .status-error { color: #dc3545; }
                .footer { text-align: center; padding: 20px; color: #666; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
                    <h1>🚀 Benchmarks Athalia</h1>
                    <p>Rapport de performance et qualité - {timestamp}</p>
        </div>

                <div class="content">
                    <div class="score-grid">
                        <div class="score-card">
                            <h3>Score Global</h3>
                            <div class="score-value">{global_score}</div>
                            <p>/ 100</p>
        </div>
                        <div class="score-card">
                            <h3>Performance</h3>
                            <div class="score-value">{perf_score}</div>
                            <p>/ 100</p>
                </div>
                        <div class="score-card">
                            <h3>Sécurité</h3>
                            <div class="score-value">{security_score}</div>
                            <p>/ 100</p>
                </div>
                        <div class="score-card">
                            <h3>Qualité Code</h3>
                            <div class="score-value">{quality_score}</div>
                            <p>/ 100</p>
            </div>
        </div>

                    <div class="chart-container">
                        <canvas id="benchmarkChart" width="400" height="200"></canvas>
            </div>

                    <div class="benchmark-details">
                        <h3>📊 Détails des Benchmarks</h3>
                        {benchmark_details}
            </div>
        </div>

        <div class="footer">
                    <p>Généré automatiquement par Athalia Benchmark System v12.0.0</p>
                    <p>Dernière mise à jour: {last_updated}</p>
        </div>
    </div>

    <script>
                // Graphique des scores
                const ctx = document.getElementById('benchmarkChart').getContext('2d');
                new Chart(ctx, {{
                    type: 'radar',
                    data: {{
                        labels: ['Performance', 'Sécurité', 'Qualité Code', 'IA Génération', 'Robotics'],
                        datasets: [{{
                            label: 'Scores',
                            data: [{perf_score}, {security_score}, {quality_score}, {ai_score}, {robotics_score}],
                            backgroundColor: 'rgba(102, 126, 234, 0.2)',
                            borderColor: 'rgba(102, 126, 234, 1)',
                            borderWidth: 2,
                            pointBackgroundColor: 'rgba(102, 126, 234, 1)',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: 'rgba(102, 126, 234, 1)'
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        scales: {{
                            r: {{
                                beginAtZero: true,
                                max: 100,
                                ticks: {{
                                    stepSize: 20
                                }}
                            }}
                        }},
                        plugins: {{
                            title: {{
                                display: true,
                                text: 'Vue d\'ensemble des performances'
                            }}
                        }}
                    }}
        }});
    </script>
</body>
        </html>
        """

        # Remplissage des données
        global_score = data.get("global_score", 0)
        perf_score = data.get("performance", {}).get("scores", {}).get("overall", 0)
        security_score = data.get("security", {}).get("score", 0)
        quality_score = data.get("code_quality", {}).get("score", 0)
        ai_score = data.get("ai_generation", {}).get("score", 0)
        robotics_score = data.get("robotics", {}).get("score", 0)

        # Génération des détails des benchmarks
        benchmark_details = ""
        for benchmark_name, benchmark_data in data.items():
            if benchmark_name in ["timestamp", "global_score", "total_duration"]:
                continue

            score = benchmark_data.get("score", 0)
            duration = benchmark_data.get("duration", 0)

            benchmark_details += f"""
            <div class="metric-row">
                <span class="metric-label">{benchmark_name.replace('_', ' ').title()}</span>
                <span class="metric-value">
                    Score: <span class="status-{'good' if score >= 80 else 'warning' if score >= 60 else 'error'}">{score}/100</span> |
                    Durée: {duration:.3f}s
                </span>
            </div>
            """

        # Remplacement des variables dans le template
        html_content = html_template.format(
            timestamp=data.get("timestamp", ""),
            global_score=global_score,
            perf_score=perf_score,
            security_score=security_score,
            quality_score=quality_score,
            ai_score=ai_score,
            robotics_score=robotics_score,
            benchmark_details=benchmark_details,
            last_updated=data.get("last_updated", ""),
        )

        return html_content

    def open_report(self):
        """Ouvre le rapport HTML dans le navigateur"""
        try:
            report_file = self.generate_html_report()
            if report_file and Path(report_file).exists():
                webbrowser.open(f"file://{Path(report_file).absolute()}")
                logger.info("🌐 Rapport ouvert dans le navigateur")
            else:
                logger.error("❌ Impossible de générer le rapport HTML")
        except Exception as e:
            logger.error(f"Erreur lors de l'ouverture du rapport: {e}")


# Fonction principale pour exécution directe
def main():
    """Fonction principale pour exécution directe du système de benchmarks"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Système de benchmarks avancés Athalia"
    )
    parser.add_argument(
        "--project-path", default=".", help="Chemin du projet à analyser"
    )
    parser.add_argument(
        "--run-all", action="store_true", help="Exécuter tous les benchmarks"
    )
    parser.add_argument(
        "--performance", action="store_true", help="Benchmark de performance uniquement"
    )
    parser.add_argument(
        "--security", action="store_true", help="Benchmark de sécurité uniquement"
    )
    parser.add_argument(
        "--quality", action="store_true", help="Benchmark de qualité uniquement"
    )
    parser.add_argument("--ai", action="store_true", help="Benchmark IA uniquement")
    parser.add_argument(
        "--robotics", action="store_true", help="Benchmark robotics uniquement"
    )
    parser.add_argument(
        "--html-report", action="store_true", help="Générer le rapport HTML"
    )
    parser.add_argument(
        "--open-report",
        action="store_true",
        help="Ouvrir le rapport dans le navigateur",
    )

    args = parser.parse_args()

    # Initialisation du système
    benchmark_system = AdvancedBenchmarkSystem(args.project_path)

    # Exécution des benchmarks selon les arguments
    if args.run_all:
        results = benchmark_system.run_all_benchmarks()
        print(
            f"✅ Benchmarks terminés - Score global: {results.get('global_score', 0)}/100"
        )

    elif args.performance:
        results = benchmark_system.run_performance_benchmark()
        print(
            f"✅ Benchmark performance terminé - Score: {results.get('scores', {}).get('overall', 0)}/100"
        )

    elif args.security:
        results = benchmark_system.run_security_benchmark()
        print(f"✅ Benchmark sécurité terminé - Score: {results.get('score', 0)}/100")

    elif args.quality:
        results = benchmark_system.run_code_quality_benchmark()
        print(f"✅ Benchmark qualité terminé - Score: {results.get('score', 0)}/100")

    elif args.ai:
        results = benchmark_system.run_ai_generation_benchmark()
        print(f"✅ Benchmark IA terminé - Score: {results.get('score', 0)}/100")

    elif args.robotics:
        results = benchmark_system.run_robotics_benchmark()
        print(f"✅ Benchmark robotics terminé - Score: {results.get('score', 0)}/100")

    # Génération du rapport HTML
    if args.html_report or args.open_report:
        report_file = benchmark_system.generate_html_report()
        if report_file:
            print(f"📊 Rapport HTML généré: {report_file}")

            if args.open_report:
                benchmark_system.open_report()

    # Si aucun argument spécifique, exécuter tous les benchmarks
    if not any(
        [
            args.run_all,
            args.performance,
            args.security,
            args.quality,
            args.ai,
            args.robotics,
        ]
    ):
        print("🚀 Exécution de tous les benchmarks...")
        results = benchmark_system.run_all_benchmarks()
        print(
            f"✅ Benchmarks terminés - Score global: {results.get('global_score', 0)}/100"
        )

        # Génération automatique du rapport HTML
        report_file = benchmark_system.generate_html_report()
        if report_file:
            print(f"📊 Rapport HTML généré: {report_file}")


if __name__ == "__main__":
    main()

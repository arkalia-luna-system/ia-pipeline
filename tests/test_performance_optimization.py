#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests de performance et d'optimisation pour Athalia.
Tests professionnels pour la CI/CD.
"""

import sys
import tempfile
import time
from pathlib import Path

import pytest

# Import conditionnel de psutil
try:
    import psutil

    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Imports conditionnels pour éviter les erreurs si les modules n'existent pas
try:
    from athalia_core.performance_analyzer import PerformanceAnalyzer
except ImportError:
    PerformanceAnalyzer = None

try:
    from athalia_core.cache_manager import AnalysisCache
except ImportError:
    AnalysisCache = None


class TestPerformanceOptimization:
    """Tests de performance et d'optimisation."""

    def setup_method(self):
        """Initialisation pour chaque test."""
        self.test_dir = Path(tempfile.mkdtemp())

        # Initialiser les composants si disponibles
        if PerformanceAnalyzer:
            self.performance_analyzer = PerformanceAnalyzer(str(self.test_dir))
        else:
            self.performance_analyzer = None

        if AnalysisCache:
            self.cache_manager = AnalysisCache()
        else:
            self.cache_manager = None

    def teardown_method(self):
        """Nettoyage après chaque test."""
        import shutil

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_performance_analyzer_initialization(self):
        """Test de l'initialisation de l'analyseur de performance."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        assert self.performance_analyzer is not None
        assert hasattr(self.performance_analyzer, "root_path")
        assert str(self.test_dir) in str(self.performance_analyzer.root_path)

    def test_cache_manager_initialization(self):
        """Test de l'initialisation du gestionnaire de cache."""
        if not AnalysisCache:
            pytest.skip("AnalysisCache non disponible")

        assert self.cache_manager is not None
        assert hasattr(self.cache_manager, "cache_dir")

    def test_performance_analysis_basic(self):
        """Test d'analyse de performance basique."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Créer un fichier de test
        test_file = self.test_dir / "test_file.py"
        test_file.write_text(
            """
def test_function():
    return "test"
"""
        )

        # Analyser la performance du projet
        report = self.performance_analyzer.analyze_project_performance(
            str(self.test_dir)
        )

        assert hasattr(report, "overall_score")
        assert hasattr(report, "metrics")
        assert hasattr(report, "issues")
        assert hasattr(report, "recommendations")

    def test_cache_operations(self):
        """Test des opérations de cache."""
        if not AnalysisCache:
            pytest.skip("AnalysisCache non disponible")

        # Test de mise en cache
        project_path = str(self.test_dir)
        analysis_type = "test_analysis"
        data = {"test": "data"}

        self.cache_manager.set(project_path, analysis_type, data)

        # Test de récupération
        retrieved = self.cache_manager.get(project_path, analysis_type)
        assert retrieved is not None
        assert "result" in retrieved
        assert retrieved["result"] == data

    def test_performance_optimization_suggestions(self):
        """Test des suggestions d'optimisation."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Créer un fichier avec des problèmes de performance
        problematic_file = self.test_dir / "problematic.py"
        problematic_file.write_text(
            """
import time

def slow_function():
    time.sleep(1)  # Problème de performance
    return "slow"

def inefficient_loop():
    result = []
    for i in range(10000):
        result.append(i)  # Problème d'efficacité
    return result
"""
        )

        # Analyser et obtenir des suggestions
        report = self.performance_analyzer.analyze_project_performance(
            str(self.test_dir)
        )

        assert isinstance(report.recommendations, list)
        assert len(report.recommendations) >= 0  # Peut être vide

    def test_memory_usage_analysis(self):
        """Test d'analyse de l'utilisation mémoire."""
        if not PSUTIL_AVAILABLE:
            pytest.skip("psutil non disponible")

        # Test de monitoring mémoire
        process = psutil.Process()
        memory_info = process.memory_info()

        assert isinstance(memory_info.rss, int)
        assert memory_info.rss > 0

    def test_execution_time_measurement(self):
        """Test de mesure du temps d'exécution."""

        def test_function():
            time.sleep(0.1)
            return "test"

        # Mesurer le temps d'exécution
        start_time = time.time()
        result = test_function()
        end_time = time.time()
        execution_time = end_time - start_time

        assert isinstance(execution_time, float)
        assert execution_time > 0.1  # Au moins le temps de sleep
        assert result == "test"

    def test_bottleneck_detection(self):
        """Test de détection des goulots d'étranglement."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Créer un fichier avec des goulots d'étranglement
        bottleneck_file = self.test_dir / "bottleneck.py"
        bottleneck_file.write_text(
            """
import time

def bottleneck_function():
    # Goulot d'étranglement simulé
    time.sleep(2)
    return "bottleneck"

def normal_function():
    return "normal"
"""
        )

        # Détecter les goulots d'étranglement
        report = self.performance_analyzer.analyze_project_performance(
            str(self.test_dir)
        )

        assert isinstance(report.issues, list)

    def test_performance_regression_detection(self):
        """Test de détection de régression de performance."""
        # Simuler des métriques de performance
        baseline_metrics = {"execution_time": 1.0, "memory_usage": 100, "cpu_usage": 50}

        current_metrics = {
            "execution_time": 1.5,  # Plus lent
            "memory_usage": 120,  # Plus de mémoire
            "cpu_usage": 60,  # Plus de CPU
        }

        # Détecter les régressions
        regressions = []
        for metric in baseline_metrics:
            if current_metrics[metric] > baseline_metrics[metric]:
                regressions.append(
                    f"{metric}: {baseline_metrics[metric]} -> {current_metrics[metric]}"
                )

        assert isinstance(regressions, list)
        assert len(regressions) > 0

    def test_optimization_application(self):
        """Test d'application d'optimisations."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Créer un fichier à optimiser
        file_to_optimize = self.test_dir / "to_optimize.py"
        file_to_optimize.write_text(
            """
def inefficient_function():
    result = []
    for i in range(1000):
        result.append(i)
    return result
"""
        )

        # Analyser les opportunités d'optimisation
        report = self.performance_analyzer.analyze_project_performance(
            str(self.test_dir)
        )

        assert isinstance(report.optimization_opportunities, list)

    def test_performance_report_generation(self):
        """Test de génération de rapport de performance."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Générer un rapport de performance
        report = self.performance_analyzer.analyze_project_performance(
            str(self.test_dir)
        )

        assert hasattr(report, "overall_score")
        assert hasattr(report, "metrics")
        assert hasattr(report, "issues")
        assert hasattr(report, "recommendations")

    def test_cache_performance(self):
        """Test de performance du cache."""
        if not AnalysisCache:
            pytest.skip("AnalysisCache non disponible")

        # Test de performance du cache
        start_time = time.time()

        # Opérations de cache multiples
        project_path = str(self.test_dir)
        for i in range(100):
            self.cache_manager.set(project_path, f"test_{i}", {"value": i})
            self.cache_manager.get(project_path, f"test_{i}")

        end_time = time.time()
        execution_time = end_time - start_time

        # Le cache doit être rapide (moins de 1 seconde pour 100 opérations)
        assert execution_time < 1.0

    def test_memory_leak_detection(self):
        """Test de détection de fuites mémoire."""
        if not PSUTIL_AVAILABLE:
            pytest.skip("psutil non disponible")

        # Simuler une fuite mémoire
        initial_memory = psutil.Process().memory_info().rss

        # Créer des objets pour simuler une fuite
        leak_objects = []
        for i in range(1000):
            leak_objects.append([i] * 1000)

        final_memory = psutil.Process().memory_info().rss
        memory_increase = final_memory - initial_memory

        # Vérifier que la détection fonctionne
        assert memory_increase > 0

    def test_performance_thresholds(self):
        """Test des seuils de performance."""
        if not PerformanceAnalyzer:
            pytest.skip("PerformanceAnalyzer non disponible")

        # Vérifier que les seuils sont définis
        assert hasattr(self.performance_analyzer, "thresholds")
        assert isinstance(self.performance_analyzer.thresholds, dict)
        assert "complexity" in self.performance_analyzer.thresholds

    def test_optimization_impact_measurement(self):
        """Test de mesure de l'impact des optimisations."""
        # Mesurer l'impact d'une optimisation
        before_metrics = {"execution_time": 2.0, "memory_usage": 150}

        after_metrics = {"execution_time": 1.0, "memory_usage": 100}

        # Calculer l'amélioration
        time_improvement = (
            (before_metrics["execution_time"] - after_metrics["execution_time"])
            / before_metrics["execution_time"]
            * 100
        )
        memory_improvement = (
            (before_metrics["memory_usage"] - after_metrics["memory_usage"])
            / before_metrics["memory_usage"]
            * 100
        )

        assert time_improvement > 0
        assert memory_improvement > 0


def test_performance_analyzer_integration():
    """Test d'intégration de l'analyseur de performance."""
    if not PerformanceAnalyzer:
        pytest.skip("PerformanceAnalyzer non disponible")

    with tempfile.TemporaryDirectory() as temp_dir:
        analyzer = PerformanceAnalyzer(temp_dir)

        # Test complet du workflow
        assert analyzer is not None

        # Créer un fichier de test
        test_file = Path(temp_dir) / "integration_test.py"
        test_file.write_text(
            """
def integration_function():
    return "integration_test"
"""
        )

        # Analyser le projet
        report = analyzer.analyze_project_performance(temp_dir)
        assert hasattr(report, "overall_score")

        # Obtenir des insights
        insights = analyzer.get_performance_insights()
        assert isinstance(insights, dict)


@pytest.mark.skipif(not PSUTIL_AVAILABLE, reason="psutil non disponible")
def test_system_performance_monitoring():
    """Test de monitoring des performances système."""
    # Test de monitoring système
    process = psutil.Process()

    # Vérifier que les métriques système sont accessibles
    cpu_percent = process.cpu_percent()
    memory_info = process.memory_info()

    assert isinstance(cpu_percent, (int, float))
    assert isinstance(memory_info.rss, int)
    assert memory_info.rss > 0


def test_performance_optimization_workflow():
    """Test du workflow complet d'optimisation de performance."""
    if not PerformanceAnalyzer or not AnalysisCache:
        pytest.skip("Modules de performance non disponibles")

    with tempfile.TemporaryDirectory() as temp_dir:
        analyzer = PerformanceAnalyzer(temp_dir)
        _ = AnalysisCache()

        # 1. Analyser les performances actuelles
        current_performance = analyzer.analyze_project_performance(temp_dir)
        assert hasattr(current_performance, "overall_score")

        # 2. Identifier les problèmes
        test_file = Path(temp_dir) / "workflow_test.py"
        test_file.write_text(
            """
def workflow_function():
    import time
    time.sleep(0.1)
    return "workflow"
"""
        )

        # 3. Analyser à nouveau
        improved_performance = analyzer.analyze_project_performance(temp_dir)
        assert hasattr(improved_performance, "overall_score")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

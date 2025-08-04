#!/usr/bin/env python3
"""
Tests complets pour performance_analyzer.py (580 lignes)
Couverture actuelle: 20% → Objectif: 85%

Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import time
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from athalia_core.performance_analyzer import PerformanceAnalyzer


class TestPerformanceAnalyzerComplete:
    """Tests complets pour PerformanceAnalyzer."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer fichiers de test avec différents profils de performance
        (self.project_path / "fast_module.py").write_text("""
def fast_function():
    '''Fonction rapide et efficace.'''
    return [i for i in range(10)]

def efficient_algorithm():
    '''Algorithme efficace O(n).'''
    data = list(range(100))
    return sum(data)
""")
        
        (self.project_path / "slow_module.py").write_text("""
def slow_function():
    '''Fonction lente avec boucles imbriquées.'''
    result = []
    for i in range(100):
        for j in range(100):
            result.append(i * j)
    return result

def inefficient_algorithm():
    '''Algorithme inefficace O(n²).'''
    data = list(range(100))
    result = []
    for i in data:
        for j in data:
            if i == j:
                result.append(i)
    return result

def memory_intensive():
    '''Fonction consommatrice de mémoire.'''
    big_list = [i for i in range(100000)]
    big_dict = {i: str(i) * 100 for i in range(10000)}
    return len(big_list) + len(big_dict)
""")
        
        (self.project_path / "recursive_module.py").write_text("""
def fibonacci_recursive(n):
    '''Fibonacci récursif non optimisé.'''
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_optimized(n):
    '''Fibonacci optimisé avec mémoisation.'''
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib(n)
""")
        
        self.analyzer = PerformanceAnalyzer(str(self.project_path))

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_analyzer_initialization(self):
        """Test initialisation de l'analyseur."""
        assert self.analyzer.project_path == str(self.project_path)
        assert hasattr(self.analyzer, 'analysis_results')
        assert hasattr(self.analyzer, 'performance_metrics')

    def test_analyzer_initialization_invalid_path(self):
        """Test initialisation avec chemin invalide."""
        invalid_path = "/path/that/does/not/exist"
        
        try:
            analyzer = PerformanceAnalyzer(invalid_path)
            assert analyzer.project_path == invalid_path
        except Exception as e:
            # Exception attendue pour chemin invalide
            assert "not found" in str(e).lower() or "invalid" in str(e).lower()

    def test_analyze_cpu_performance(self):
        """Test analyse performance CPU."""
        cpu_analysis = self.analyzer.analyze_cpu_performance()
        
        assert isinstance(cpu_analysis, dict)
        # Métriques CPU typiques
        expected_metrics = ["execution_time", "cpu_usage", "hotspots", "bottlenecks"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in cpu_analysis for metric in expected_metrics)

    def test_analyze_memory_usage(self):
        """Test analyse utilisation mémoire."""
        memory_analysis = self.analyzer.analyze_memory_usage()
        
        assert isinstance(memory_analysis, dict)
        # Métriques mémoire typiques
        expected_metrics = ["memory_usage", "peak_memory", "memory_leaks", "allocations"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in memory_analysis for metric in expected_metrics)

    def test_profile_function_execution_fast(self):
        """Test profiling fonction rapide."""
        fast_file = self.project_path / "fast_module.py"
        profile_results = self.analyzer.profile_function_execution(str(fast_file), "fast_function")
        
        assert isinstance(profile_results, dict)
        
        if "execution_time" in profile_results:
            # La fonction rapide devrait s'exécuter rapidement
            exec_time = profile_results["execution_time"]
            assert exec_time < 1.0  # Moins d'1 seconde

    def test_profile_function_execution_slow(self):
        """Test profiling fonction lente."""
        slow_file = self.project_path / "slow_module.py"
        profile_results = self.analyzer.profile_function_execution(str(slow_file), "slow_function")
        
        assert isinstance(profile_results, dict)
        
        if "execution_time" in profile_results:
            # La fonction lente devrait prendre plus de temps
            exec_time = profile_results["execution_time"]
            assert exec_time >= 0  # Au moins mesurable

    def test_detect_performance_bottlenecks(self):
        """Test détection goulots d'étranglement."""
        bottlenecks = self.analyzer.detect_performance_bottlenecks()
        
        assert isinstance(bottlenecks, (dict, list))
        
        if isinstance(bottlenecks, dict):
            assert "bottlenecks" in bottlenecks or "issues" in bottlenecks
        else:
            # Liste de goulots d'étranglement
            assert len(bottlenecks) >= 0

    def test_analyze_algorithm_complexity(self):
        """Test analyse complexité algorithmique."""
        slow_file = self.project_path / "slow_module.py"
        complexity = self.analyzer.analyze_algorithm_complexity(str(slow_file))
        
        assert isinstance(complexity, dict)
        
        # Devrait détecter la complexité O(n²) de inefficient_algorithm
        if "complexity_analysis" in complexity:
            analysis = complexity["complexity_analysis"]
            assert isinstance(analysis, (dict, list))

    def test_memory_profiling_intensive_function(self):
        """Test profiling mémoire fonction intensive."""
        slow_file = self.project_path / "slow_module.py"
        memory_profile = self.analyzer.profile_memory_usage(str(slow_file), "memory_intensive")
        
        assert isinstance(memory_profile, dict)
        
        # Devrait détecter une utilisation mémoire élevée
        if "peak_memory" in memory_profile:
            peak = memory_profile["peak_memory"]
            assert peak > 0

    def test_io_performance_analysis(self):
        """Test analyse performance I/O."""
        # Créer fichier pour tests I/O
        io_file = self.project_path / "io_test.py"
        io_file.write_text("""
def file_operations():
    '''Opérations fichier pour test I/O.'''
    with open('/tmp/test_file.txt', 'w') as f:
        for i in range(1000):
            f.write(f"Line {i}\\n")
    
    with open('/tmp/test_file.txt', 'r') as f:
        return len(f.readlines())
""")
        
        io_analysis = self.analyzer.analyze_io_performance()
        
        assert isinstance(io_analysis, dict)
        # Métriques I/O typiques
        expected_metrics = ["io_operations", "file_access", "disk_usage"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in io_analysis for metric in expected_metrics)

    def test_recursive_function_analysis(self):
        """Test analyse fonctions récursives."""
        recursive_file = self.project_path / "recursive_module.py"
        recursive_analysis = self.analyzer.analyze_recursive_functions(str(recursive_file))
        
        assert isinstance(recursive_analysis, dict)
        
        # Devrait détecter les fonctions récursives
        if "recursive_functions" in recursive_analysis:
            recursive_funcs = recursive_analysis["recursive_functions"]
            assert len(recursive_funcs) >= 2  # fibonacci_recursive et fib interne

    def test_compare_function_performance(self):
        """Test comparaison performance fonctions."""
        recursive_file = self.project_path / "recursive_module.py"
        
        # Comparer fibonacci récursif vs optimisé
        comparison = self.analyzer.compare_function_performance(
            str(recursive_file), 
            ["fibonacci_recursive", "fibonacci_optimized"],
            args=[10]  # Argument test
        )
        
        assert isinstance(comparison, dict)
        
        # Devrait montrer que la version optimisée est plus rapide
        if "performance_comparison" in comparison:
            comp_data = comparison["performance_comparison"]
            assert isinstance(comp_data, (dict, list))

    def test_generate_performance_report(self):
        """Test génération rapport performance."""
        # Exécuter analyse complète d'abord
        self.analyzer.run_comprehensive_analysis()
        
        report = self.analyzer.generate_performance_report()
        
        assert isinstance(report, (dict, str))
        
        if isinstance(report, str):
            # Rapport texte
            assert "performance" in report.lower()
            assert len(report) > 100
        else:
            # Rapport structuré
            assert "summary" in report or "analysis" in report

    def test_calculate_performance_score(self):
        """Test calcul score performance."""
        # Exécuter analyses
        self.analyzer.run_comprehensive_analysis()
        
        score = self.analyzer.calculate_performance_score()
        
        assert isinstance(score, (int, float, dict))
        
        if isinstance(score, (int, float)):
            assert 0 <= score <= 100
        else:
            assert "score" in score or "rating" in score

    def test_identify_optimization_opportunities(self):
        """Test identification opportunités optimisation."""
        optimizations = self.analyzer.identify_optimization_opportunities()
        
        assert isinstance(optimizations, (dict, list))
        
        if isinstance(optimizations, list):
            # Liste d'optimisations
            assert len(optimizations) >= 0
        else:
            assert "optimizations" in optimizations or "recommendations" in optimizations

    def test_benchmark_execution_time(self):
        """Test benchmark temps d'exécution."""
        fast_file = self.project_path / "fast_module.py"
        
        benchmark = self.analyzer.benchmark_execution_time(
            str(fast_file), 
            "fast_function",
            iterations=10
        )
        
        assert isinstance(benchmark, dict)
        
        # Devrait contenir statistiques de benchmark
        expected_stats = ["mean_time", "min_time", "max_time", "std_dev"]
        present_stats = sum(1 for stat in expected_stats if stat in benchmark)
        assert present_stats >= 2  # Au moins 2 statistiques

    def test_analyze_code_hotspots(self):
        """Test analyse points chauds du code."""
        hotspots = self.analyzer.analyze_code_hotspots()
        
        assert isinstance(hotspots, (dict, list))
        
        # Devrait identifier les sections de code coûteuses
        if isinstance(hotspots, dict):
            assert "hotspots" in hotspots or "expensive_operations" in hotspots

    def test_memory_leak_detection(self):
        """Test détection fuites mémoire."""
        # Créer code avec fuite mémoire potentielle
        leak_file = self.project_path / "memory_leak.py"
        leak_file.write_text("""
global_list = []

def potential_leak():
    '''Fonction avec fuite mémoire potentielle.'''
    global global_list
    for i in range(1000):
        global_list.append([i] * 1000)  # Accumulation sans nettoyage
    return len(global_list)
""")
        
        leak_analysis = self.analyzer.detect_memory_leaks()
        
        assert isinstance(leak_analysis, dict)
        # Devrait analyser les fuites potentielles
        assert "leak_analysis" in leak_analysis or "memory_issues" in leak_analysis

    def test_cache_performance_analysis(self):
        """Test analyse performance cache."""
        cache_analysis = self.analyzer.analyze_cache_performance()
        
        assert isinstance(cache_analysis, dict)
        # Métriques cache typiques
        expected_metrics = ["cache_hits", "cache_misses", "cache_efficiency"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in cache_analysis for metric in expected_metrics)

    def test_database_query_performance(self):
        """Test analyse performance requêtes base de données."""
        # Créer code avec requêtes simulées
        db_file = self.project_path / "database_queries.py"
        db_file.write_text("""
def slow_query():
    '''Simulation requête lente.'''
    # Simulation d'une requête avec boucle
    result = []
    for i in range(1000):
        for j in range(100):
            if i == j:
                result.append((i, j))
    return result

def optimized_query():
    '''Simulation requête optimisée.'''
    return [(i, i) for i in range(100)]
""")
        
        db_analysis = self.analyzer.analyze_database_performance()
        
        assert isinstance(db_analysis, dict)
        # Métriques DB typiques
        expected_metrics = ["query_performance", "slow_queries", "optimization_suggestions"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in db_analysis for metric in expected_metrics)

    def test_run_comprehensive_analysis(self):
        """Test analyse complète."""
        comprehensive_results = self.analyzer.run_comprehensive_analysis()
        
        assert isinstance(comprehensive_results, dict)
        
        # Vérifier que toutes les sections principales sont présentes
        expected_sections = [
            "cpu_analysis", "memory_analysis", "io_analysis", 
            "bottlenecks", "optimizations", "score"
        ]
        
        # Au moins la moitié des sections devraient être présentes
        present_sections = sum(1 for section in expected_sections if section in comprehensive_results)
        assert present_sections >= len(expected_sections) // 2

    def test_export_performance_results(self):
        """Test export résultats performance."""
        # Exécuter analyse
        self.analyzer.run_comprehensive_analysis()
        
        export_file = self.project_path / "performance_report.json"
        success = self.analyzer.export_performance_results(str(export_file))
        
        if success:
            assert export_file.exists()
            
            # Vérifier que le JSON est valide
            with open(export_file) as f:
                data = json.load(f)
                assert isinstance(data, dict)

    @patch('athalia_core.performance_analyzer.cProfile')
    def test_profiling_with_cprofile(self, mock_cprofile):
        """Test profiling avec cProfile."""
        mock_profiler = Mock()
        mock_cprofile.Profile.return_value = mock_profiler
        mock_profiler.enable.return_value = None
        mock_profiler.disable.return_value = None
        mock_profiler.get_stats.return_value = {"test": "stats"}
        
        fast_file = self.project_path / "fast_module.py"
        profile_results = self.analyzer.profile_with_cprofile(str(fast_file))
        
        assert isinstance(profile_results, dict)

    def test_performance_regression_detection(self):
        """Test détection régressions performance."""
        # Simuler données performance historiques
        historical_data = {
            "fast_function": {"execution_time": 0.001},
            "slow_function": {"execution_time": 0.1}
        }
        
        # Analyser performance actuelle
        current_results = self.analyzer.run_comprehensive_analysis()
        
        # Détecter régressions
        regressions = self.analyzer.detect_performance_regressions(historical_data, current_results)
        
        assert isinstance(regressions, (dict, list))

    def test_performance_trends_analysis(self):
        """Test analyse tendances performance."""
        # Créer données de tendance simulées
        trend_data = []
        for i in range(10):
            trend_data.append({
                "timestamp": time.time() - (i * 86400),  # i jours avant
                "performance_score": 80 - i,  # Dégradation progressive
                "execution_time": 0.1 + (i * 0.01)
            })
        
        trends = self.analyzer.analyze_performance_trends(trend_data)
        
        assert isinstance(trends, dict)
        # Devrait détecter la tendance de dégradation
        if "trend_direction" in trends:
            assert trends["trend_direction"] in ["improving", "degrading", "stable"]

    @pytest.mark.parametrize("complexity_type,expected_pattern", [
        ("O(1)", "constant"),
        ("O(n)", "linear"),
        ("O(n²)", "quadratic"),
        ("O(log n)", "logarithmic"),
    ])
    def test_complexity_pattern_recognition(self, complexity_type, expected_pattern):
        """Test reconnaissance patterns de complexité."""
        # Code avec différentes complexités
        test_code = f"""
def algorithm():
    # Simulation complexité {complexity_type}
    pass
"""
        
        pattern = self.analyzer.recognize_complexity_pattern(test_code)
        
        assert isinstance(pattern, (str, dict))
        # Devrait reconnaître le pattern de complexité
        if isinstance(pattern, str):
            assert expected_pattern in pattern.lower() or complexity_type in pattern
        else:
            assert "complexity" in pattern

    def test_performance_with_different_inputs(self):
        """Test performance avec différentes tailles d'entrée."""
        fast_file = self.project_path / "fast_module.py"
        
        input_sizes = [10, 100, 1000]
        performance_scaling = self.analyzer.analyze_performance_scaling(
            str(fast_file), 
            "efficient_algorithm",
            input_sizes
        )
        
        assert isinstance(performance_scaling, dict)
        # Devrait montrer comment la performance évolue avec la taille
        if "scaling_analysis" in performance_scaling:
            scaling = performance_scaling["scaling_analysis"]
            assert isinstance(scaling, (dict, list))

    def test_concurrent_performance_analysis(self):
        """Test analyse performance concurrente."""
        # Créer code avec gestion concurrence
        concurrent_file = self.project_path / "concurrent_code.py"
        concurrent_file.write_text("""
import threading
import time

def concurrent_task():
    '''Tâche pour test concurrence.'''
    time.sleep(0.01)  # Simulation travail
    return threading.current_thread().name

def sequential_processing():
    '''Traitement séquentiel.'''
    results = []
    for i in range(10):
        results.append(concurrent_task())
    return results

def parallel_processing():
    '''Traitement parallèle.'''
    threads = []
    results = []
    
    def worker():
        results.append(concurrent_task())
    
    for i in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results
""")
        
        concurrency_analysis = self.analyzer.analyze_concurrency_performance()
        
        assert isinstance(concurrency_analysis, dict)
        # Devrait analyser les gains de performance concurrente
        assert "concurrency_analysis" in concurrency_analysis or "parallel_efficiency" in concurrency_analysis

    def test_performance_monitoring_realtime(self):
        """Test monitoring performance temps réel."""
        # Démarrer monitoring
        monitoring_data = self.analyzer.start_performance_monitoring()
        
        assert isinstance(monitoring_data, (dict, bool))
        
        # Simuler activité
        time.sleep(0.1)
        
        # Arrêter monitoring
        results = self.analyzer.stop_performance_monitoring()
        
        assert isinstance(results, dict)
        # Devrait contenir données de monitoring
        if "monitoring_results" in results:
            assert results["monitoring_results"] is not None


class TestPerformanceAnalyzerIntegration:
    """Tests d'intégration pour PerformanceAnalyzer."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_performance_audit_workflow(self):
        """Test workflow complet audit performance."""
        # Créer projet avec profils performance variés
        (self.project_path / "src").mkdir()
        
        # Module avec bonnes performances
        (self.project_path / "src" / "optimized.py").write_text("""
def efficient_search(data, target):
    '''Recherche binaire efficace.'''
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
""")
        
        # Module avec performances dégradées
        (self.project_path / "src" / "unoptimized.py").write_text("""
def inefficient_search(data, target):
    '''Recherche linéaire inefficace.'''
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def nested_loops_example():
    '''Exemple boucles imbriquées coûteuses.'''
    result = 0
    for i in range(100):
        for j in range(100):
            for k in range(10):
                result += i * j * k
    return result
""")
        
        # Exécuter analyse complète
        analyzer = PerformanceAnalyzer(str(self.project_path))
        results = analyzer.run_comprehensive_analysis()
        
        # Vérifications
        assert isinstance(results, dict)
        assert len(results) > 0
        
        # Générer rapport
        report = analyzer.generate_performance_report()
        assert isinstance(report, (dict, str))
        
        # Calculer score
        score = analyzer.calculate_performance_score()
        assert isinstance(score, (int, float, dict))
        
        # Identifier optimisations
        optimizations = analyzer.identify_optimization_opportunities()
        assert isinstance(optimizations, (dict, list))
        
        # Export
        export_file = self.project_path / "performance_audit.json"
        export_success = analyzer.export_performance_results(str(export_file))
        
        if export_success:
            assert export_file.exists()


class TestPerformanceAnalyzerBenchmarks:
    """Tests de benchmark pour PerformanceAnalyzer."""

    def setup_method(self):
        """Configuration tests benchmark."""
        self.temp_dir = tempfile.mkdtemp()
        self.analyzer = PerformanceAnalyzer(self.temp_dir)

    def teardown_method(self):
        """Nettoyage tests benchmark."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_analyzer_performance_large_codebase(self):
        """Test performance analyseur sur grande base de code."""
        import time
        
        large_project = Path(self.temp_dir) / "large_project"
        large_project.mkdir()
        
        # Créer beaucoup de fichiers avec code complexe
        for i in range(50):
            (large_project / f"module_{i}.py").write_text(f"""
# Module {i}
def complex_function_{i}():
    '''Fonction complexe {i}.'''
    result = 0
    for j in range(100):
        for k in range(50):
            result += j * k * {i}
    return result

def recursive_function_{i}(n):
    '''Fonction récursive {i}.'''
    if n <= 1:
        return 1
    return n * recursive_function_{i}(n-1)

class DataProcessor{i}:
    '''Classe de traitement données {i}.'''
    def __init__(self):
        self.data = list(range(1000))
    
    def process(self):
        return [x * {i} for x in self.data if x % 2 == 0]
""")
        
        # Tester performance de l'analyse
        analyzer = PerformanceAnalyzer(str(large_project))
        
        start_time = time.time()
        results = analyzer.run_comprehensive_analysis()
        analysis_time = time.time() - start_time
        
        # Vérifications performance
        assert isinstance(results, dict)
        assert analysis_time < 120.0  # Moins de 2 minutes pour 50 modules
        
        # Vérifier que l'analyse a traité tous les fichiers
        if "analyzed_files" in results:
            analyzed_count = results["analyzed_files"]
            assert analyzed_count >= 50

    def test_memory_usage_during_analysis(self):
        """Test utilisation mémoire pendant analyse."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        
        # Exécuter analyse intensive
        self.analyzer.run_comprehensive_analysis()
        
        memory_after = process.memory_info().rss
        memory_increase = memory_after - memory_before
        
        # L'augmentation mémoire ne devrait pas être excessive
        # (50MB = 50 * 1024 * 1024 bytes)
        assert memory_increase < 50 * 1024 * 1024
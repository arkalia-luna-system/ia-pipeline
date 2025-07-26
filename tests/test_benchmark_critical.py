import importlib
import os
import sys

import pytest

# Import conditionnel de pytest-benchmark
try:
    import pytest_benchmark
    BENCHMARK_AVAILABLE = True
except ImportError:
    BENCHMARK_AVAILABLE = False

# Liste des modules/fonctions critiques à tester (corrigée)
CRITICAL_FUNCTIONS = [
    ("athalia_core.advanced_analytics", "AdvancedAnalytics", True),  # True = nécessite un argument
    ("athalia_core.unified_orchestrator", "UnifiedOrchestrator", False),
    ("athalia_core.auto_tester", "AutoTester", False),
]

def import_critical_function(module_name, func_name):
    try:
        module = importlib.import_module(module_name)
        return getattr(module, func_name, None)
    except ImportError:
        return None

@pytest.mark.skipif(not BENCHMARK_AVAILABLE, reason="pytest-benchmark non disponible")
@pytest.mark.benchmark(group="critical_functions")
@pytest.mark.parametrize("module_name,func_name,needs_path", CRITICAL_FUNCTIONS)
def test_critical_function_benchmark(benchmark, module_name, func_name, needs_path):
    func = import_critical_function(module_name, func_name)
    if func is None:
        pytest.skip(f"{module_name}.{func_name} non disponible")
    
    # Instanciation adaptée
    if needs_path:
        # Utilise le dossier courant comme chemin de projet
        result = benchmark(lambda: func(os.getcwd()))
    else:
        result = benchmark(lambda: func())
    assert result is not None


@pytest.mark.skip(reason="Test désactivé - cause une récursivité infinie avec coverage")
def test_global_coverage_threshold():
    """Ce test échoue si la couverture descend sous 80%."""
    # Empêcher la récursion infinie en détectant l'environnement
    if os.environ.get("ATHALIA_COVERAGE_SUBPROCESS") == "1":
        pytest.skip("Test de couverture lancé en sous-processus, skip pour éviter la récursion.")
    import subprocess
    env = os.environ.copy()
    env["ATHALIA_COVERAGE_SUBPROCESS"] = "1"
    result = subprocess.run([
        sys.executable, "-m", "pytest", "--cov=athalia_core", "--cov-report=term", "--cov-fail-under=80", "-q"
    ], capture_output=True, text=True, env=env)
    print(result.stdout)
    assert result.returncode == 0, "La couverture de code est insuffisante (<80%) !" 
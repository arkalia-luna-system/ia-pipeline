import pytest
import importlib
import os
import sys

# Liste des modules/fonctions critiques à tester (corrigée)
CRITICAL_FUNCTIONS = [
    ("athalia_core.advanced_analytics", "AdvancedAnalytics", True),  # True = nécessite un argument
    ("athalia_core.athalia_orchestrator", "AthaliaOrchestrator", False),
    ("athalia_core.auto_tester", "AutoTester", False),
]

def import_critical_function(module_name, func_name):
    module = importlib.import_module(module_name)
    return getattr(module, func_name, None)

@pytest.mark.benchmark(group="critical_functions")
@pytest.mark.parametrize("module_name,func_name,needs_path", CRITICAL_FUNCTIONS)
def test_critical_function_benchmark(benchmark, module_name, func_name, needs_path):
    func = import_critical_function(module_name, func_name)
    assert func is not None, f"{module_name}.{func_name} introuvable"
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
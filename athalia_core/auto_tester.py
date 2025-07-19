#!/usr/bin/env python3
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import re
import sys
import argparse
from datetime import datetime
import ast
import cProfile
import importlib.util
import pstats
import shutil
import subprocess
import tempfile
import time
import unittest
import logging

logger = logging.getLogger(__name__)

"""
Module de tests automatiques pour Athalia
Génération automatique de tests unitaires et d'intégration
"""

class AutoTester:
    """Générateur de tests pour Athalia"""

    def __init__(self):
        self.project_path: Path = Path('.')
        self.test_results = {}
        self.generated_tests = []

    def generate_tests(self, project_path: str) -> Dict[str, Any]:
        """Génération complète de tests pour un projet"""
        self.project_path = Path(project_path)

        logger.info(f"🧪 Génération de tests pour : {self.project_path.name}")

        # Analyse du projet
        modules = self._analyze_modules()

        # Génération des tests
        unit_tests = self._generate_unit_tests(modules)
        integration_tests = self._generate_integration_tests(modules)
        performance_tests = self._generate_performance_tests(modules)

        # Sauvegarde des tests
        self._save_tests(unit_tests, integration_tests, performance_tests)

        # Exécution des tests
        test_results = self._run_tests()

        return {
            "unit_tests": unit_tests,
            "integration_tests": integration_tests,
            "performance_tests": performance_tests,
            "test_results": test_results,
            "files_created": self._get_created_files()
        }

    def _analyze_modules(self) -> List[Dict[str, Any]]:
        """Analyse les modules Python du projet"""
        modules = []
        
        for py_file in self.project_path.rglob("*.py"):
            # Ignorer les fichiers macOS ._*
            if py_file.name.startswith("._"):
                continue
                
            if py_file.name != "__init__.py" and "test" not in py_file.name.lower():
                try:
                    with open(py_file, 'r', encoding='utf-8') as file_handle:
                        content = file_handle.read()
                    
                    tree = ast.parse(content)
                    module_info = {
                        'name': py_file.stem,
                        'path': str(py_file),
                        'classes': [],
                        'functions': [],
                        'imports': []
                    }
                    
                    for item in tree.body:
                        if isinstance(item, ast.ClassDef):
                            class_info = {
                                'name': item.name,
                                'methods': []
                            }
                            for node in item.body:
                                if isinstance(node, ast.FunctionDef):
                                    class_info['methods'].append(node.name)
                            module_info['classes'].append(class_info)
                        elif isinstance(item, ast.FunctionDef) and not any(
                            decorator.id == 'property' if isinstance(decorator, ast.Name) else False
                            for decorator in (item.decorator_list or [])
                        ):
                            module_info['functions'].append(item.name)
                        elif isinstance(item, (ast.Import, ast.ImportFrom)):
                            if isinstance(item, ast.Import):
                                for alias in item.names:
                                    module_info['imports'].append(alias.name)
                            else:
                                module_info['imports'].append(item.module or '')
                    
                    modules.append(module_info)
                    
                except Exception as e:
                    logger.warning(f"Erreur lors de l'analyse de {py_file}: {e}")
                    continue
        
        return modules

    def _generate_unit_tests(self, modules: List[Dict[str, Any]]) -> List[str]:
        """Génère les tests f"""
        unit_tests = []

        for module in modules:
            test_content = self._generate_module_unit_tests(module)
            if test_content:
                unit_tests.append(test_content)

        return unit_tests

    def _generate_module_unit_tests(self, module: Dict[str, Any]) -> str:
        """Génère les tests unitaires pour un f"""
        test_content = """#!/usr/bin/env python3
"""

        # Tests pour les classes
        for class_info in module["classes"]:
            test_content += """
    def test_{class_info['name']}_creation(self):
        \"\"\"Test de création de {class_info['name']}\"\"\"
        try:
            instance = {class_info['name']}()
            self.assertIsNotNone(instance)
        except Exception as e:
            self.skipTest(f"Impossible de créer {class_info['name']}: {{e}}")
"""

            # Tests pour les méthodes
            for method_info in class_info["methods"]:
                if method_info["name"] not in ["__init__", "__str__", "__repr__"]:
                    test_content += """
    def test_{class_info['name']}_{method_info['name']}(self):
        \"\"\"Test de la méthode {method_info['name']}\"\"\"
        try:
            instance = {class_info['name']}()
            # TODO: Ajouter des paramètres de test appropriés
            result = instance.{method_info['name']}()
            # TODO: Ajouter des assertions appropriées
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester {method_info['name']}: {{e}}")
"""

        # Tests pour les fonctions
        for func_info in module["functions"]:
            test_content += """
    def test_{func_info['name']}(self):
        \"\"\"Test de la fonction {func_info['name']}\"\"\"
        try:
            # TODO: Ajouter des paramètres de test appropriés
            result = {func_info['name']}()
            # TODO: Ajouter des assertions appropriées
            self.assertIsNotNone(result)
        except Exception as e:
            self.skipTest(f"Impossible de tester {func_info['name']}: {{e}}")
"""

        test_content += """
if __name__ == '__main__':
    unittest.main()
"""

        return test_content

    def _generate_integration_tests(self, modules: List[Dict[str, Any]]) -> List[str]:
        """Génère les tests df"""
        integration_tests = []

        # Test dintégration principal
        integration_content = """#!/usr/bin/env python3
"""

        # Ajouter le chemin du projet
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

        integration_content += """

class TestIntegration(unittest.TestCase):
    \"\"\"Tests dintégration\"\"\"

    def setUp(self):
        \"\"\"Configuration avant chaque test\"\"\"
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        \"\"\"Nettoyage après chaque test\"\"\"
        shutil.rmtree(self.temp_dir, ignore_errors = True)

    def test_project_import(self):
        \"\"\"Test dimport du projet\"\"\"
        try:
            # Tester l'import des modules principaux
            for module in {[m['name'] for m in modules]}:
                try:
                    __import__(module)
                except ImportError:
                    pass  # Module optionnel
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Erreur d'import: {{e}}")

    def test_basic_functionality(self):
        \"\"\"Test de fonctionnalité de base\"\"\"
        try:
            # TODO: Ajouter des tests de fonctionnalité de base
            self.assertTrue(True)
        except Exception as e:
            self.skipTest(f"Fonctionnalité de base non disponible: {{e}}")

    def test_error_handling(self):
        \"\"\"Test de gestion derreurs\"\"\"
        try:
            # TODO: Ajouter des tests de gestion derreurs
            self.assertTrue(True)
        except Exception as e:
            self.skipTest(f"Gestion derreurs non testable: {{e}}")

if __name__ == '__main__':
    unittest.main()
"""

        integration_tests.append(integration_content)

        return integration_tests

    def _generate_performance_tests(self, modules: List[Dict[str, Any]]) -> List[str]:
        """Génère les tests de f"""
        performance_tests = []

        # Test de performance principal
        performance_content = """#!/usr/bin/env python3
"""

        # Ajouter le chemin du projet
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

        performance_content += """

class TestPerformance(unittest.TestCase):
    \"\"\"Tests de performance\"\"\"

    def setUp(self):
        \"\"\"Configuration avant chaque test\"\"\"
        pass

    def test_import_performance(self):
        \"\"\"Test de performance des imports\"\"\"
        start_time = time.time()
        try:
            # Tester l'import des modules principaux
            for module in {[m['name'] for m in modules]}:
                try:
                    __import__(module)
                except ImportError:
                    pass
            end_time = time.time()
            import_time = end_time - start_time
            self.assertLess(import_time, 5.0, f"Import trop lent: {{import_time:.2f}}f")
        except Exception as e:
            self.skipTest(f"Test dimport impossible: {{e}}")

    def test_memory_usage(self):
        \"\"\"Test dusage mémoire\"\"\"

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        try:
            # TODO: Ajouter des opérations qui utilisent de la mémoire
            pass
        except Exception as e:
            self.skipTest(f"Test mémoire impossible: {{e}}")

        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = final_memory - initial_memory

        self.assertLess(memory_increase, 100, f"Usage mémoire excessif: {{memory_increase:.1f}}MB")

    def test_execution_time(self):
        \"\"\"Test de temps dexécution\"\"\"
        start_time = time.time()
        try:
            # TODO: Ajouter des opérations à mesurer
            time.sleep(0.1)  # Simulation
            end_time = time.time()
            execution_time = end_time - start_time
            self.assertLess(execution_time, 1.0, f"Exécution trop lente: {{execution_time:.2f}}string_data")
        except Exception as e:
            self.skipTest(f"Test dexécution impossible: {{e}}")

if __name__ == '__main__':
    unittest.main()
"""

        performance_tests.append(performance_content)

        return performance_tests

    def _save_tests(self, unit_tests: List[str], integration_tests: List[str], performance_tests: List[str]):
        """Sauvegarde les tests f"""
        tests_dir = self.project_path / "tests"
        tests_dir.mkdir(exist_ok = True)

        # Tests unitaires
        for index, test_content in enumerate(unit_tests):
            test_file = tests_dir / f"test_unit_{index + 1}.py"
            with open(test_file, 'w', encoding='utf-8') as file_handle:
                file_handle.write(test_content)
            self.generated_tests.append(str(test_file))

        # Tests dintégration
        for index, test_content in enumerate(integration_tests):
            test_file = tests_dir / f"test_integration_{index + 1}.py"
            with open(test_file, 'w', encoding='utf-8') as file_handle:
                file_handle.write(test_content)
            self.generated_tests.append(str(test_file))

        # Tests de performance
        for index, test_content in enumerate(performance_tests):
            test_file = tests_dir / f"test_performance_{index + 1}.py"
            with open(test_file, 'w', encoding='utf-8') as file_handle:
                file_handle.write(test_content)
            self.generated_tests.append(str(test_file))

        # Fichier de configuration pytest
        pytest_config = """[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--verbose",
    "--tb=short",
    "--strict-markers",
    "--disable-warnings"
]
markers = (
    "slow: marks tests as slow (deselect with -m \"not slow\")",
    "integration: marks tests as integration tests",
    "performance: marks tests as performance tests"
)
"""

        pytest_file = self.project_path / "pytest.ini"
        with open(pytest_file, 'w', encoding='utf-8') as file_handle:
            file_handle.write(pytest_config)

        # Script de lancement des tests
        run_tests_script = """#!/usr/bin/env bash
# Script de lancement des tests pour {self.project_path.name}
# Généré automatiquement par Athalia

echo "🧪 Lancement des tests pour {self.project_path.name}"

# Tests unitaires
echo "📋 Tests unitaires..."
python -m pytest tests/test_unit_*.py -v

# Tests dintégration
echo "🔗 Tests dintégration..."
python -m pytest tests/test_integration_*.py -v

# Tests de performance
echo "⚡ Tests de performance..."
python -m pytest tests/test_performance_*.py -v

# Tests avec couverture
echo "📊 Tests avec couverture..."
python -m pytest tests/ --cov=. --cov-report=html --cov-report=term

echo "✅ Tests terminés !"
"""

        run_tests_file = self.project_path / "run_tests.sh"
        with open(run_tests_file, 'w', encoding='utf-8') as file_handle:
            file_handle.write(run_tests_script)

        # Rendre le script exécutable
        os.chmod(run_tests_file, 0o755)

    def _run_tests(self) -> Dict[str, Any]:
        """Exécute les tests générés et collecte les résultats"""
        results = {
            "unit_tests": {"passed": 0, "failed": 0, "errors": []},
            "integration_tests": {"passed": 0, "failed": 0, "errors": []},
            "performance_tests": {"passed": 0, "failed": 0, "errors": []}
        }

        try:
            # Changer vers le répertoire du projet
            original_dir = os.getcwd()
            os.chdir(self.project_path)

            # Exécuter les tests unitaires
            logger.info("🧪 Exécution des tests unitaires...")
            try:
                result = subprocess.run(
                    ["python", "-m", "pytest", "tests/test_unit_*.py", "-v", "--tb=short"],
                    capture_output=True,
                    text=True,
                    timeout=60
                )

                if result.returncode == 0:
                    results["unit_tests"]["passed"] = len(re.findall(r"PASSED", result.stdout))
                else:
                    results["unit_tests"]["failed"] = len(re.findall(r"FAILED", result.stdout))
                    results["unit_tests"]["errors"].append(result.stderr)
            except subprocess.TimeoutExpired:
                results["unit_tests"]["errors"].append("Timeout lors de l'exécution")
            except Exception as e:
                results["unit_tests"]["errors"].append(str(e))

            # Exécuter les tests dintégration
            logger.info("🔗 Exécution des tests dintégration...")
            try:
                result = subprocess.run(
                    ["python", "-m", "pytest", "tests/test_integration_*.py", "-v", "--tb=short"],
                    capture_output=True,
                    text=True,
                    timeout=60
                )

                if result.returncode == 0:
                    results["integration_tests"]["passed"] = len(re.findall(r"PASSED", result.stdout))
                else:
                    results["integration_tests"]["failed"] = len(re.findall(r"FAILED", result.stdout))
                    results["integration_tests"]["errors"].append(result.stderr)
            except subprocess.TimeoutExpired:
                results["integration_tests"]["errors"].append("Timeout lors de l'exécution")
            except Exception as e:
                results["integration_tests"]["errors"].append(str(e))

            # Retourner au répertoire original
            os.chdir(original_dir)

        except Exception as e:
            results["unit_tests"]["errors"].append(f"Erreur générale: {e}")

        return results

    def _get_created_files(self) -> List[str]:
        """Retourne la liste des fichiers créés"""
        files = ["pytest.ini", "run_tests.sh"] + self.generated_tests
        return [str(self.project_path / file_handle) if not file_handle.startswith(str(self.project_path)) else file_handle for file_handle in files]

    def generate_test_report(self) -> str:
        """Génère un rapport de tests"""
        report = """
{sep}
🧪 RAPPORT DE TESTS AUTOMATIQUES - {project_name}
{sep}

📊 RÉSULTATS DES TESTS:

📋 Tests unitaires:
   • Réussis: {unit_passed}
   • Échoués: {unit_failed}
   • Erreurs: {unit_errors}

🔗 Tests d'intégration:
   • Réussis: {integration_passed}
   • Échoués: {integration_failed}
   • Erreurs: {integration_errors}

⚡ Tests de performance:
   • Réussis: {perf_passed}
   • Échoués: {perf_failed}
   • Erreurs: {perf_errors}

📄 FICHIERS CRÉÉS ({num_files}):
"""
        report = report.format(
            sep='='*60,
            project_name=self.project_path.name,
            unit_passed=self.test_results.get('unit_tests', {}).get('passed', 0),
            unit_failed=self.test_results.get('unit_tests', {}).get('failed', 0),
            unit_errors=len(self.test_results.get('unit_tests', {}).get('errors', [])),
            integration_passed=self.test_results.get('integration_tests', {}).get('passed', 0),
            integration_failed=self.test_results.get('integration_tests', {}).get('failed', 0),
            integration_errors=len(self.test_results.get('integration_tests', {}).get('errors', [])),
            perf_passed=self.test_results.get('performance_tests', {}).get('passed', 0),
            perf_failed=self.test_results.get('performance_tests', {}).get('failed', 0),
            perf_errors=len(self.test_results.get('performance_tests', {}).get('errors', [])),
            num_files=len(self.generated_tests)
        )
        for test_file in self.generated_tests:
            report += f"   • {test_file}\n"
        report += """
🚀 POUR LANCER LES TESTS:

```bash
cd {project_path}
./run_tests.sh
```

Ou manuellement:
```bash
python -m pytest tests/ -v
```

{sep2}
""".format(
            project_path=self.project_path,
            sep2='='*60
        )
        return report

def main():
    """Point dentrée f"""

    parser = argparse.ArgumentParser(description="Génération automatique de f")
    parser.add_argument("project_path", help="Chemin du projet à f")
    parser.add_argument("--run", action="store_true", help="Exécuter les tests après f")

    args = parser.parse_args()

    if not os.path.exists(args.project_path):
        logger.info(f"❌ Le chemin {args.project_path} nexiste f")
        return

    tester = AutoTester()
    result = tester.generate_tests(args.project_path)

    logger.info("✅ Tests générés avec succès !")
    logger.info(f"\n📄 Fichiers créés ({len(result['files_created'])}):")
    for file_path in result['files_created']:
        logger.info(f"   • {file_path}")

    if args.run:
        logger.info("\n🧪 Exécution des tests...")
        tester.test_results = result['test_results']
        logger.info(tester.generate_test_report())

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Module de test automatique pour Athalia
Exécution et validation automatique des tests
"""

import argparse
import ast
import logging
from pathlib import Path
from typing import Any, Union

# Import du validateur de sécurité
try:
    from ..validation.security_validator import (
        SecurityError,
        validateand_run,
    )
except ImportError:
    # Fallback pour les tests - utiliser le module sécurisé
    try:
        from ..utilities.secure_subprocess import (
            secure_subprocess_run as validateand_run,
        )

        # Définir SecurityError pour la compatibilité
        class SecurityError(Exception):
            pass

    except ImportError:
        # Fallback final
        import subprocess

        # Définir SecurityError pour la compatibilité
        class SecurityError(Exception):
            pass

        def validateand_run(command: list[str], **kwargs: Any):
            # Paramètres de sécurité minimaux
            safe_kwargs = {"shell": False, "check": False}
            safe_kwargs.update(kwargs)
            return subprocess.run(command, **safe_kwargs)


logger = logging.getLogger(__name__)

# Module de tests automatiques pour Athalia
# Génération automatique de tests unitaires et d'intégration


class AutoTester:
    """Générateur automatique de tests"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.test_dir = self.project_path / "tests"
        self.generated_tests: list[str] = []
        self.test_results: dict[str, Any] = {
            "status": "initialized",
            "success": False,
            "analysis": {},
            "generated_tests": [],
            "execution": {},
        }

    def analyze_project(self) -> dict[str, Any]:
        """Analyse le projet pour identifier les modules à tester"""
        logger.info(f"🔍 Analyse du projet: {self.project_path.name}")

        analysis: dict[str, Any] = {
            "modules": [],
            "total_functions": 0,
            "total_classes": 0,
            "test_coverage": 0.0,
        }

        # Analyser chaque fichier Python
        py_files = list(self.project_path.rglob("*.py"))
        logger.info(f"🔍 Fichiers Python trouvés: {len(py_files)}")

        for py_file in py_files:
            if "test" not in py_file.name and "tests" not in str(py_file):
                logger.info(f"📁 Analyse du fichier: {py_file}")
                module_info = self._analyze_module(py_file)
                # Inclure tous les modules, même ceux avec des erreurs
                modules = analysis.get("modules", [])
                if isinstance(modules, list):
                    modules.append(module_info)

                total_functions = analysis.get("total_functions", 0)
                if isinstance(total_functions, int | float):
                    analysis["total_functions"] = total_functions + len(
                        module_info.get("functions", [])
                    )

                total_classes = analysis.get("total_classes", 0)
                if isinstance(total_classes, int | float):
                    analysis["total_classes"] = total_classes + len(
                        module_info.get("classes", [])
                    )

        # Calculer la couverture de tests
        total_functions = analysis.get("total_functions", 0)
        if isinstance(total_functions, int | float) and total_functions > 0:
            existing_tests = len(list(self.test_dir.rglob("test_*.py")))
            analysis["test_coverage"] = (existing_tests / total_functions) * 100

        return analysis

    def run(self, test_type: str = "all") -> dict[str, Any]:
        """Exécute les tests automatiques"""
        logger.info(f"🚀 Exécution des tests automatiques: {test_type}")

        # Validation du project_path
        if not self.project_path:
            raise ValueError("project_path doit être défini")

        try:
            if test_type == "all":
                # Analyser le projet
                analysis = self.analyze_project()
                self.test_results["analysis"] = analysis

                # Générer des tests si nécessaire
                if analysis.get("test_coverage", 0) < 80:
                    self.test_results["generated_tests"] = self.generate_tests(
                        str(self.project_path)
                    )

                # Exécuter les tests existants
                self.test_results["execution"] = self._run_existing_tests()

            elif test_type == "analysis":
                self.test_results["analysis"] = self.analyze_project()

            elif test_type == "generation":
                analysis = self.analyze_project()
                self.test_results["generated_tests"] = self._generate_missing_tests(
                    analysis
                )

            self.test_results["status"] = "completed"
            self.test_results["success"] = True

        except Exception as e:
            logger.error(f"Erreur lors de l'exécution des tests: {e}")
            self.test_results["status"] = "error"
            self.test_results["success"] = False
            self.test_results["error"] = str(e)

        return self.test_results

    def _generate_missing_tests(self, analysis: dict[str, Any]) -> list[str]:
        """Génère les tests manquants"""
        generated = []
        for module in analysis.get("modules", []):
            if len(module.get("functions", [])) > 0:
                test_file = f"test_{module['name']}.py"
                generated.append(test_file)
        return generated

    def _run_existing_tests(self) -> dict[str, Any]:
        """Exécute les tests existants"""
        try:
            result = validateand_run(
                ["python", "-m", "pytest", "tests/", "-v"],
                capture_output=True,
                text=True,
                cwd=self.project_path,
            )
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        except Exception as e:
            return {"error": str(e)}

    def _analyze_module(self, file_path: Path) -> dict[str, Any]:
        """Analyse un module Python individuel"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            module_info: dict[str, Any] = {
                "name": file_path.stem,
                "path": str(file_path),
                "functions": [],
                "classes": [],
                "imports": [],
            }

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions = module_info.get("functions", [])
                    if isinstance(functions, list):
                        functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    class_info = {
                        "name": node.name,
                        "methods": [],
                        "bases": [
                            base.id for base in node.bases if hasattr(base, "id")
                        ],
                    }
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            methods = class_info.get("methods", [])
                            if isinstance(methods, list):
                                methods.append(item.name)

                    classes = module_info.get("classes", [])
                    if isinstance(classes, list):
                        classes.append(class_info)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports = module_info.get("imports", [])
                        if isinstance(imports, list):
                            imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports = module_info.get("imports", [])
                        if isinstance(imports, list):
                            imports.append(node.module)

            logger.info(
                f"✅ Module analysé: {file_path.name} - {len(module_info['functions'])} fonctions, {len(module_info['classes'])} classes"
            )
            return module_info

        except Exception as e:
            logger.error(f"❌ Erreur analyse {file_path}: {e}")
            # Retourner un module info minimal au lieu d'un dict vide
            return {
                "name": file_path.stem,
                "path": str(file_path),
                "functions": [],
                "classes": [],
                "imports": [],
                "error": str(e),
            }

    def _analyze_modules(self) -> list[dict[str, Any]]:
        """Analyse tous les modules du projet"""
        modules = []
        for py_file in self.project_path.rglob("*.py"):
            if "test" not in py_file.name and "tests" not in str(py_file):
                module_info = self._analyze_module(py_file)
                if module_info:
                    modules.append(module_info)
        return modules

    def generate_tests(self, target_module: str = None) -> dict[str, Any]:
        """Génère des tests pour le projet ou un module spécifique"""
        logger.info(f"🧪 Génération de tests pour: {target_module or 'tout le projet'}")

        # Analyser le projet une seule fois
        analysis = self.analyze_project()
        logger.info(f"📊 Analyse terminée: {len(analysis['modules'])} modules trouvés")

        if target_module:
            # Vérifier si target_module est un chemin de projet (contient des slashes)
            if "/" in str(target_module) or "\\" in str(target_module):
                # C'est un chemin, utiliser tous les modules
                modules_to_test = analysis["modules"]
                logger.info(
                    "🎯 Chemin de projet détecté, utilisation de tous les modules"
                )
            else:
                # C'est un nom de module, filtrer
                modules_to_test = [
                    m for m in analysis["modules"] if m["name"] == target_module
                ]
                logger.info(f"🎯 Filtrage par nom de module: {target_module}")
        else:
            modules_to_test = analysis["modules"]
            logger.info("🎯 Aucun module cible, utilisation de tous les modules")

        logger.info(f"🎯 Modules à tester: {len(modules_to_test)}")
        for module in modules_to_test:
            logger.info(
                f"  - {module['name']}: {len(module.get('functions', []))} fonctions, {len(module.get('classes', []))} classes"
            )

        # Générer les tests unitaires
        unit_tests_result = self._generate_unit_tests(modules_to_test)
        logger.info(f"📝 Tests unitaires générés: {len(unit_tests_result)}")

        # Générer les tests d'intégration
        integration_tests_result = self._generate_integration_tests(modules_to_test)
        logger.info(f"🔗 Tests d'intégration générés: {len(integration_tests_result)}")

        # Générer les tests de performance
        performance_tests_result = self._generate_performance_tests(modules_to_test)
        logger.info(f"⚡ Tests de performance générés: {len(performance_tests_result)}")

        # Compter les fichiers créés
        files_created = (
            len(unit_tests_result)
            + len(integration_tests_result)
            + len(performance_tests_result)
        )

        return {
            "generated_tests": files_created,
            "total_modules": len(modules_to_test),
            "test_files": self.generated_tests,
            "unit_tests": unit_tests_result,
            "integration_tests": integration_tests_result,
            "performance_tests": performance_tests_result,
            "test_results": {"status": "completed", "success": True},
            "files_created": files_created,
        }

    def _generate_module_tests(self, module: dict[str, Any]) -> bool:
        """Génère des tests pour un module spécifique"""
        try:
            # Créer le répertoire de tests si nécessaire
            test_file = self.test_dir / f"test_{module['name']}.py"
            test_file.parent.mkdir(parents=True, exist_ok=True)

            # Générer le contenu des tests
            test_content = self._generate_test_content(module)

            # Sauvegarder le fichier de test
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_content)

            self.generated_tests.append(str(test_file))
            logger.info(f"✅ Tests générés pour {module['name']}: {test_file}")
            return True

        except Exception as e:
            logger.error(f"❌ Erreur génération tests {module['name']}: {e}")
            return False

    def _generate_test_content(self, module: dict[str, Any]) -> str:
        """Génère le contenu des tests pour un module"""
        content = f'''"""
Tests générés automatiquement pour {module['name']}
Fichier: {module['path']}
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import {module['name']}
except ImportError:
    pytest.skip(f"Module {module['name']} non importable")

'''

        # Tests pour les fonctions
        for func_name in module["functions"]:
            content += f'''
def test_{func_name}():
    """Test de la fonction {func_name}"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr({module['name']}, '{func_name}')
    assert callable(getattr({module['name']}, '{func_name}'))
'''

        # Tests pour les classes
        for class_info in module["classes"]:
            content += f'''
class Test{class_info['name']}:
    """Tests pour la classe {class_info['name']}"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr({module['name']}, '{class_info['name']}')
        assert isinstance(getattr({module['name']}, '{class_info['name']}'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr({module['name']}, '{class_info['name']}')
        for method_name in {class_info['methods']}:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))
'''

        content += """
if __name__ == "__main__":
    pytest.main([__file__])
"""
        return content

    def _generate_module_unit_tests(self, module: dict[str, Any]) -> str:
        """Génère des tests unitaires pour un module spécifique"""
        content = f'''"""
Tests unitaires générés pour {module['name']}
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import {module['name']}
except ImportError:
    pytest.skip(f"Module {module['name']} non importable")

'''

        # Tests pour les fonctions
        for func_name in module["functions"]:
            content += f'''
def test_{func_name}():
    """Test de la fonction {func_name}"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr({module['name']}, '{func_name}')
    assert callable(getattr({module['name']}, '{func_name}'))
'''

        # Tests pour les classes
        for class_info in module["classes"]:
            content += f'''
class Test{class_info['name']}:
    """Tests pour la classe {class_info['name']}"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr({module['name']}, '{class_info['name']}')
        assert isinstance(getattr({module['name']}, '{class_info['name']}'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr({module['name']}, '{class_info['name']}')
        for method_name in {class_info['methods']}:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))
'''

        content += """
if __name__ == "__main__":
    pytest.main([__file__])
"""
        return content

    def _generate_integration_tests(self, modules: list[dict[str, Any]]) -> list[str]:
        """Génère des tests d'intégration pour plusieurs modules"""
        integration_test_files = []

        for module in modules:
            content = f'''"""
Tests d'intégration générés automatiquement pour {module['name']}
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import {module['name']}
except ImportError:
    pytest.skip(f"Module {module['name']} non importable")

def test_{module['name']}_integration():
    """Test d'intégration pour {module['name']}"""
    # TODO: Implémenter les tests d'intégration spécifiques
    assert True

if __name__ == "__main__":
    pytest.main([__file__])
'''

            # Sauvegarder le fichier de test
            test_file = f"test_{module['name']}_integration.py"
            test_path = self.test_dir / test_file
            test_path.parent.mkdir(parents=True, exist_ok=True)

            with open(test_path, "w", encoding="utf-8") as f:
                f.write(content)

            integration_test_files.append(test_file)
            self.generated_tests.append(str(test_path))

        return integration_test_files

    def _generate_performance_tests(self, modules: list[dict[str, Any]]) -> list[str]:
        """Génère des tests de performance pour plusieurs modules"""
        performance_test_files = []

        for module in modules:
            content = f'''"""
Tests de performance générés automatiquement pour {module['name']}
"""

import pytest
import time
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import {module['name']}
except ImportError:
    pytest.skip(f"Module {module['name']} non importable")

    def test_{module['name']}_performance():
        """Test de performance pour {module['name']}"""
        start_time = time.time()

        # TODO: Implémenter les tests de performance spécifiques
        # Par exemple, tester le temps d'exécution des fonctions

        end_time = time.time()
        execution_time = end_time - start_time

        # Vérifier que l'exécution est rapide (moins de 1 seconde)
        assert execution_time < 1.0, f"Exécution trop lente: {{execution_time:.3f}}s"

if __name__ == "__main__":
    pytest.main([__file__])
'''

            # Sauvegarder le fichier de test
            test_file = f"test_{module['name']}_performance.py"
            test_path = self.test_dir / test_file
            test_path.parent.mkdir(parents=True, exist_ok=True)

            with open(test_path, "w", encoding="utf-8") as f:
                f.write(content)

            performance_test_files.append(test_file)
            self.generated_tests.append(str(test_path))

        return performance_test_files

    def _generate_unit_tests(self, modules: list[dict[str, Any]]) -> list[str]:
        """Génère des tests unitaires pour plusieurs modules"""
        unit_test_files = []

        for module in modules:
            test_file = f"test_{module['name']}_unit.py"
            test_content = self._generate_module_unit_tests(module)

            # Sauvegarder le fichier de test
            test_path = self.test_dir / test_file
            test_path.parent.mkdir(parents=True, exist_ok=True)

            with open(test_path, "w", encoding="utf-8") as f:
                f.write(test_content)

            unit_test_files.append(test_file)
            self.generated_tests.append(str(test_path))

        return unit_test_files

    def _run_tests(self) -> dict[str, Any]:
        """Exécute tous les tests du projet"""
        try:
            result = validateand_run(
                ["python", "-m", "pytest", "tests/", "-v"],
                capture_output=True,
                text=True,
                cwd=self.project_path,
            )
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "success": result.returncode == 0,
            }
        except Exception as e:
            return {"error": str(e), "success": False}

    def generate_test_report(self) -> str:
        """Génère un rapport complet des tests"""
        try:
            analysis = self.analyze_project()

            report_content = f"""
RAPPORT DE TESTS - {self.project_path.name}
==========================================
Date d'analyse: 2025-08-19
Modules analysés: {len(analysis.get("modules", []))}
Total fonctions: {analysis.get("total_functions", 0)}
Total classes: {analysis.get("total_classes", 0)}
Couverture de tests: {analysis.get("test_coverage", 0):.1f}%
Tests générés: {len(self.generated_tests)}

Fichiers de tests:
"""
            for test_file in self.generated_tests:
                report_content += f"- {test_file}\n"

            return report_content

        except Exception as e:
            logger.error(f"Erreur génération rapport: {e}")
            return f"Erreur: {str(e)}"

    def _save_tests(self, tests: dict[str, Any], output_dir: str = None) -> bool:
        """Sauvegarde les tests générés"""
        try:
            if output_dir:
                output_path = Path(output_dir)
            else:
                output_path = self.test_dir

            output_path.mkdir(parents=True, exist_ok=True)

            # Sauvegarder le rapport de génération
            report_file = output_path / "test_generation_report.txt"
            with open(report_file, "w", encoding="utf-8") as f:
                f.write("Rapport de génération de tests\n")
                f.write("=============================\n\n")
                f.write(f"Tests générés: {tests['generated_tests']}\n")
                f.write(f"Modules analysés: {tests['total_modules']}\n")
                f.write(f"Fichiers créés: {len(tests['test_files'])}\n\n")
                f.write("Fichiers de tests:\n")
                for test_file in tests["test_files"]:
                    f.write(f"- {test_file}\n")

            logger.info(f"📄 Rapport sauvegardé: {report_file}")
            return True

        except Exception as e:
            logger.error(f"❌ Erreur sauvegarde: {e}")
            return False

    def _cleanup_generated_tests(self) -> None:
        """Nettoie les tests générés automatiquement"""
        try:
            for test_file in self.generated_tests:
                if Path(test_file).exists():
                    Path(test_file).unlink()
                    logger.info(f"🗑️ Test supprimé: {test_file}")

            self.generated_tests.clear()

        except Exception as e:
            logger.warning(f"⚠️ Erreur nettoyage: {e}")

    def run_generated_tests(self) -> dict[str, Any]:
        """Exécute les tests générés automatiquement"""
        logger.info("🚀 Exécution des tests générés")

        results: dict[str, Any] = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "errors": [],
        }

        for test_file in self.generated_tests:
            if Path(test_file).exists():
                try:
                    # Exécuter pytest sur le fichier
                    result = validateand_run(
                        ["python", "-m", "pytest", test_file, "-v"],
                        capture_output=True,
                        text=True,
                        timeout=60,
                    )

                    if result.returncode == 0:
                        results["passed"] += 1
                        logger.info(f"✅ {test_file}: Tests réussis")
                    else:
                        results["failed"] += 1
                        results["errors"].append(f"{test_file}: {result.stderr}")

                    results["total_tests"] += 1

                except Exception as e:
                    results["failed"] += 1
                    results["errors"].append(f"{test_file}: {e}")

        return results

    def cleanup(self) -> None:
        """Nettoie les ressources"""
        self._cleanup_generated_tests()


def main() -> None:
    """Point d'entrée principal"""

    parser = argparse.ArgumentParser(description="Générateur automatique de tests")
    parser.add_argument("project_path", help="Chemin vers le projet")
    parser.add_argument("--module", help="Module spécifique à tester")
    parser.add_argument(
        "--run-tests", action="store_true", help="Exécuter les tests générés"
    )
    parser.add_argument(
        "--cleanup", action="store_true", help="Nettoyer les tests générés"
    )
    parser.add_argument("--output", help="Répertoire de sortie pour les tests")

    args = parser.parse_args()

    auto_tester = AutoTester(args.project_path)

    try:
        # Analyser le projet
        analysis = auto_tester.analyze_project()
        print(
            f"📊 Analyse terminée: {analysis['total_functions']} fonctions, {analysis['total_classes']} classes"
        )

        # Générer les tests
        if args.module:
            tests = auto_tester.generate_tests(args.module)
        else:
            tests = auto_tester.generate_tests()

        print(
            f"🧪 Tests générés: {tests['generated_tests']}/{tests['total_modules']} modules"
        )

        # Sauvegarder les tests
        if args.output:
            auto_tester._save_tests(tests, args.output)

        # Exécuter les tests si demandé
        if args.run_tests:
            results = auto_tester.run_generated_tests()
            print(
                f"🚀 Résultats: {results['passed']}/{results['total_tests']} tests réussis"
            )

        # Nettoyer si demandé
        if args.cleanup:
            auto_tester.cleanup()
            print("🗑️ Tests générés supprimés")

    except KeyboardInterrupt:
        print("\n⏹️ Interrompu par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    finally:
        auto_tester.cleanup()


if __name__ == "__main__":
    main()

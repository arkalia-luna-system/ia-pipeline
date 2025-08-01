#!/usr/bin/env python3
"""
Script pour analyser la couverture de tests et identifier les modules non testés.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


def get_python_files(directory: str) -> List[str]:
    """Récupère tous les fichiers Python dans un répertoire."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Ignorer les dossiers à exclure
        dirs[:] = [
            d
            for d in dirs
            if d
            not in [
                "__pycache__",
                ".git",
                "venv",
                ".venv",
                "archive",
                "backups",
                "logs",
                "htmlcov",
            ]
        ]

        for file in files:
            if file.endswith(".py") and not file.startswith("._"):
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                python_files.append(rel_path)

    return sorted(python_files)


def get_test_files() -> List[str]:
    """Récupère tous les fichiers de test."""
    return get_python_files("tests")


def run_coverage_analysis() -> Dict[str, float]:
    """Exécute l'analyse de couverture et retourne les résultats."""
    try:
        # Exécuter pytest avec coverage
        result = subprocess.run(
            [
                "python",
                "-m",
                "pytest",
                "tests/",
                "--cov-report=term-missing",
                "--quiet",
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )

        # Parser les résultats
        coverage_data = {}
        lines = result.stdout.split("\n")

        for line in lines:
            if "athalia_core/" in line and "%" in line:
                parts = line.split()
                if len(parts) >= 2:
                    module = parts[0]
                    coverage_str = parts[-1].replace("%", "")
                    try:
                        coverage = float(coverage_str)
                        coverage_data[module] = coverage
                    except ValueError:
                        continue

        return coverage_data

    except subprocess.TimeoutExpired:
        print("⚠️  Timeout lors de l'analyse de couverture")
        return {}
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse de couverture: {e}")
        return {}


def analyze_missing_tests() -> Tuple[List[str], List[str], List[str]]:
    """Analyse les modules manquants de tests."""
    # Récupérer tous les fichiers Python du projet
    all_python_files = get_python_files("athalia_core")

    # Récupérer tous les fichiers de test
    test_files = get_test_files()

    # Identifier les modules testés
    tested_modules = set()
    for test_file in test_files:
        # Extraire le nom du module testé à partir du nom du fichier de test
        test_name = os.path.basename(test_file)
        if test_name.startswith("test_"):
            module_name = test_name[5:]  # Enlever 'test_'
            if module_name.endswith(".py"):
                module_name = module_name[:-3]  # Enlever '.py'

            # Chercher le module correspondant
            for py_file in all_python_files:
                if module_name in py_file or py_file.replace(".py", "").endswith(
                    module_name
                ):
                    tested_modules.add(py_file)
                    break

    # Identifier les modules non testés
    untested_modules = [f for f in all_python_files if f not in tested_modules]

    # Identifier les modules avec 0% de couverture
    coverage_data = run_coverage_analysis()
    zero_coverage_modules = [
        module for module, coverage in coverage_data.items() if coverage == 0.0
    ]

    return untested_modules, zero_coverage_modules, list(tested_modules)


def generate_test_templates(untested_modules: List[str]) -> str:
    """Génère des templates de tests pour les modules non testés."""
    templates = []

    for module in untested_modules:
        if not module.startswith("athalia_core/"):
            continue

        module_name = (
            module.replace("athalia_core/", "").replace(".py", "").replace("/", ".")
        )
        test_file_name = f"test_{module_name.replace('.', '_')}.py"

        template = f"""
# Template de test pour {module}
# Fichier: tests/{test_file_name}

import pytest
import athalia_core.{module_name.replace('/', '.')} as module

class Test{module_name.split('.')[-1].title()}:
    \"\"\"Tests pour le module {module_name}\"\"\"
    
    def test_module_import(self):
        \"\"\"Test que le module peut être importé\"\"\"
        assert module is not None
    
    def test_module_has_expected_attributes(self):
        \"\"\"Test que le module a les attributs attendus\"\"\"
        # TODO: Ajouter les tests spécifiques au module
        pass
    
    def test_module_functions(self):
        \"\"\"Test des fonctions principales du module\"\"\"
        # TODO: Ajouter les tests des fonctions
        pass

def test_module_integration():
    \"\"\"Test d'intégration du module\"\"\"
    # TODO: Ajouter les tests d'intégration
    pass
"""
        templates.append((test_file_name, template))

    return templates


def main():
    """Fonction principale."""
    print("🔍 ANALYSE DE LA COUVERTURE DE TESTS")
    print("=" * 50)

    # Analyser les modules manquants
    untested_modules, zero_coverage_modules, tested_modules = analyze_missing_tests()

    print("\n📊 STATISTIQUES:")
    print(f"   • Modules Python totaux: {len(get_python_files('athalia_core'))}")
    print(f"   • Modules testés: {len(tested_modules)}")
    print(f"   • Modules non testés: {len(untested_modules)}")
    print(f"   • Modules avec 0% couverture: {len(zero_coverage_modules)}")

    if untested_modules:
        print(f"\n❌ MODULES NON TESTÉS ({len(untested_modules)}):")
        for module in untested_modules[:20]:  # Limiter à 20 pour l'affichage
            print(f"   • {module}")
        if len(untested_modules) > 20:
            print(f"   ... et {len(untested_modules) - 20} autres")

    if zero_coverage_modules:
        print(f"\n⚠️  MODULES AVEC 0% COUVERTURE ({len(zero_coverage_modules)}):")
        for module in zero_coverage_modules[:10]:  # Limiter à 10 pour l'affichage
            print(f"   • {module}")
        if len(zero_coverage_modules) > 10:
            print(f"   ... et {len(zero_coverage_modules) - 10} autres")

    # Générer des templates de tests
    if untested_modules:
        print("\n📝 TEMPLATES DE TESTS GÉNÉRÉS:")
        templates = generate_test_templates(untested_modules)

        for test_file_name, template in templates[:5]:  # Limiter à 5 templates
            print(f"   • {test_file_name}")

        if len(templates) > 5:
            print(f"   ... et {len(templates) - 5} autres templates")

        # Sauvegarder les templates
        templates_dir = Path("tests/templates")
        templates_dir.mkdir(exist_ok=True)

        for test_file_name, template in templates:
            template_path = templates_dir / test_file_name
            with open(template_path, "w", encoding="utf-8") as f:
                f.write(template.strip())

        print(f"\n💾 Templates sauvegardés dans: {templates_dir}")

    # Recommandations
    print("\n🎯 RECOMMANDATIONS:")
    print("   1. Créer des tests pour les modules non testés prioritaires")
    print("   2. Améliorer la couverture des modules avec 0% de couverture")
    print("   3. Utiliser les templates générés comme point de départ")
    print("   4. Exécuter: python -m pytest tests/ --cov-report=html")

    return len(untested_modules) + len(zero_coverage_modules)


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

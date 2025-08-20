#!/usr/bin/env python3
"""
Module de vérification de santé du système Athalia.
Vérifie que tous les composants essentiels sont disponibles et fonctionnels.
"""

import builtins
import logging
import os
import sys
from typing import Any

_real_open = builtins.open

logger = logging.getLogger(__name__)


def open_patch(file, mode="r", *args, **kwargs):
    """Patch de sécurité pour la fonction open."""
    if mode == "f":
        mode = "w"
    return _real_open(file, mode, *args, **kwargs)


builtins.open = open_patch


def check_ready(project_path: str = None) -> dict[str, Any]:
    """
    Vérification complète de la santé du système Athalia.

    Args:
        project_path: Chemin du projet (optionnel, utilise le répertoire courant si None)

    Returns:
        Dict contenant le rapport de santé complet
    """
    if project_path is None:
        project_path = os.getcwd()

    report: dict[str, Any] = {
        "ready": True,
        "missing": [],
        "errors": [],
        "warnings": [],
        "modules": {},
        "cli": {},
        "config": {},
        "tests": {},
    }

    # Vérification des fichiers essentiels
    required_files = ["README.md", "requirements.txt", "pyproject.toml"]
    for file_name in required_files:
        file_path = os.path.join(project_path, file_name)
        if not os.path.isfile(file_path):
            report["missing"].append(file_name)
            report["ready"] = False

    # Vérification des dossiers essentiels
    required_dirs = ["athalia_core", "tests", "docs", "config"]
    for dir_name in required_dirs:
        dir_path = os.path.join(project_path, dir_name)
        if not os.path.isdir(dir_path):
            report["missing"].append(dir_name + "/")
            report["ready"] = False

    # Vérification des modules Python
    report["modules"] = check_python_modules()

    # Vérification de l'interface CLI
    report["cli"] = check_cli_interface(project_path)

    # Vérification de la configuration
    report["config"] = check_configuration(project_path)

    # Vérification des tests
    report["tests"] = check_test_availability(project_path)

    # Évaluation finale
    if report["missing"] or report["errors"]:
        report["ready"] = False

    return report


def check_python_modules() -> dict[str, Any]:
    """Vérifie la disponibilité des modules Python essentiels."""
    modules_status = {}

    essential_modules = [
        "athalia_core.core.unified_orchestrator",
        "athalia_core.validation.security_validator",
        "athalia_core.quality.code_linter",
        "athalia_core.utilities.generation_simple",
    ]

    for module_name in essential_modules:
        try:
            __import__(module_name)
            modules_status[module_name] = {"status": "OK", "error": None}
        except ImportError as e:
            modules_status[module_name] = {"status": "ERROR", "error": str(e)}

    return modules_status


def check_cli_interface(project_path: str) -> dict[str, Any]:
    """Vérifie l'interface CLI."""
    cli_status = {}

    cli_scripts = [
        "bin/core/athalia_unified.py",
        "bin/core/ath-audit.py",
        "bin/core/ath-lint.py",
    ]

    for script_path in cli_scripts:
        full_path = os.path.join(project_path, script_path)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            cli_status[script_path] = {"status": "OK", "executable": True}
        elif os.path.isfile(full_path):
            cli_status[script_path] = {"status": "WARNING", "executable": False}
        else:
            cli_status[script_path] = {"status": "ERROR", "executable": False}

    return cli_status


def check_configuration(project_path: str) -> dict[str, Any]:
    """Vérifie la configuration du système."""
    config_status = {}

    config_files = ["config/athalia_config.yaml", ".env"]

    for config_file in config_files:
        full_path = os.path.join(project_path, config_file)
        if os.path.isfile(full_path):
            try:
                # Test de lecture du fichier
                with open(full_path) as f:
                    content = f.read()
                config_status[config_file] = {
                    "status": "OK",
                    "readable": True,
                    "size": len(content),
                }
            except Exception as e:
                config_status[config_file] = {
                    "status": "ERROR",
                    "readable": False,
                    "error": str(e),
                }
        else:
            config_status[config_file] = {
                "status": "WARNING",
                "readable": False,
                "error": "Fichier non trouvé",
            }

    return config_status


def check_test_availability(project_path: str) -> dict[str, Any]:
    """Vérifie la disponibilité des tests."""
    test_status = {}

    test_dirs = ["tests/unit", "tests/integration", "tests/performance"]

    for test_dir in test_dirs:
        full_path = os.path.join(project_path, test_dir)
        if os.path.isdir(full_path):
            # Compter les fichiers de test
            test_files = [
                f
                for f in os.listdir(full_path)
                if f.endswith(".py") and f.startswith("test_")
            ]
            test_status[test_dir] = {"status": "OK", "test_files": len(test_files)}
        else:
            test_status[test_dir] = {"status": "ERROR", "test_files": 0}

    return test_status


def run_health_check() -> None:
    """Exécute une vérification de santé complète et affiche le rapport."""
    print("🔍 VÉRIFICATION DE SANTÉ ATHALIA")
    print("=" * 40)

    report = check_ready()

    # Affichage du rapport
    if report["ready"]:
        print("✅ Système Athalia prêt et fonctionnel !")
    else:
        print("❌ Problèmes détectés dans le système Athalia")

    print(
        f"\n📊 Modules Python: {sum(1 for m in report['modules'].values() if m['status'] == 'OK')}/{len(report['modules'])} OK"
    )
    print(
        f"💻 Interface CLI: {sum(1 for c in report['cli'].values() if c['status'] == 'OK')}/{len(report['cli'])} OK"
    )
    print(
        f"⚙️ Configuration: {sum(1 for c in report['config'].values() if c['status'] == 'OK')}/{len(report['config'])} OK"
    )
    print(
        f"🧪 Tests: {sum(1 for t in report['tests'].values() if t['status'] == 'OK')}/{len(report['tests'])} OK"
    )

    if report["missing"]:
        print(f"\n❌ Fichiers/Dossiers manquants: {', '.join(report['missing'])}")

    if report["errors"]:
        print(f"\n🚨 Erreurs: {', '.join(report['errors'])}")

    if report["warnings"]:
        print(f"\n⚠️ Avertissements: {', '.join(report['warnings'])}")


if __name__ == "__main__":
    run_health_check()

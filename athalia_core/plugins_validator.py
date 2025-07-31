#!/usr/bin/env python3
"""
Module de validation de plugins pour Athalia
Validation et vérification des plugins tiers
"""

import ast
import json
import logging
from pathlib import Path
from typing import Any, Dict

import yaml


logger = logging.getLogger(__name__)


class PluginValidator:
    """Validateur de plugins pour Athalia"""

    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = Path(plugins_dir)
        self.validation_results = {
            "valid_plugins": [],
            "invalid_plugins": [],
            "warnings": [],
            "errors": [],
        }

    def validate_plugin(self, plugin_path: str) -> Dict[str, Any]:
        """Valide un plugin spécifique"""
        plugin_path_obj = Path(plugin_path)

        if not plugin_path_obj.exists():
            return {
                "valid": False,
                "errors": [f"Plugin {plugin_path} n'existe pas"],
            }

        results = {"valid": True, "errors": [], "warnings": [], "metadata": {}}

        # Vérifier la structure du plugin
        if not self._check_plugin_structure(plugin_path_obj, results):
            results["valid"] = False

        # Vérifier la syntaxe Python
        if not self._check_python_syntax(plugin_path_obj, results):
            results["valid"] = False

        # Vérifier les métadonnées
        self._check_metadata(plugin_path_obj, results)

        # Vérifier les dépendances
        self._check_dependencies(plugin_path_obj, results)

        return results

    def _check_plugin_structure(
        self, plugin_path: Path, results: Dict[str, Any]
    ) -> bool:
        """Vérifie la structure du plugin"""
        required_files = ["__init__.py"]

        for file in required_files:
            if not (plugin_path / file).exists():
                results["errors"].append(f"Fichier requis manquant: {file}")
                return False

        return True

    def _check_python_syntax(self, plugin_path: Path, results: Dict[str, Any]) -> bool:
        """Vérifie la syntaxe Python du plugin"""
        python_files = list(plugin_path.rglob("*.py"))

        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Vérifier la syntaxe avec ast
                ast.parse(content)

            except SyntaxError as e:
                results["errors"].append(f"Erreur de syntaxe dans {py_file}: {e}")
                return False
            except Exception as e:
                results["warnings"].append(f"Impossible de vérifier {py_file}: {e}")

        return True

    def _check_metadata(self, plugin_path: Path, results: Dict[str, Any]):
        """Vérifie les métadonnées du plugin"""
        metadata_files = ["plugin.yaml", "plugin.yml", "plugin.json"]

        for metadata_file in metadata_files:
            metadata_path = plugin_path / metadata_file
            if metadata_path.exists():
                try:
                    if metadata_file.endswith(".json"):
                        with open(metadata_path, "r") as f:
                            metadata = json.load(f)
                    else:
                        with open(metadata_path, "r") as f:
                            metadata = yaml.safe_load(f)

                    results["metadata"] = metadata

                    # Vérifier les champs requis
                    required_fields = ["name", "version", "description"]
                    for field in required_fields:
                        if field not in metadata:
                            results["warnings"].append(
                                f"Champ requis manquant: {field}"
                            )

                    break
                except Exception as e:
                    results["warnings"].append(
                        f"Impossible de lire {metadata_file}: {e}"
                    )

    def _check_dependencies(self, plugin_path: Path, results: Dict[str, Any]):
        """Vérifie les dépendances du plugin"""
        requirements_files = ["requirements.txt", "setup.py", "pyproject.toml"]

        for req_file in requirements_files:
            req_path = plugin_path / req_file
            if req_path.exists():
                try:
                    if req_file == "requirements.txt":
                        with open(req_path, "r") as f:
                            deps = [
                                line.strip()
                                for line in f
                                if line.strip() and not line.startswith("#")
                            ]
                        results["metadata"]["dependencies"] = deps
                    # Autres formats peuvent être ajoutés ici
                except Exception as e:
                    results["warnings"].append(f"Impossible de lire {req_file}: {e}")

    def validate_all_plugins(self) -> Dict[str, Any]:
        """Valide tous les plugins dans le répertoire"""
        if not self.plugins_dir.exists():
            return {
                "valid_plugins": [],
                "invalid_plugins": [],
                "warnings": ["Répertoire plugins n'existe pas"],
                "errors": [],
            }

        for plugin_dir in self.plugins_dir.iterdir():
            if plugin_dir.is_dir():
                result = self.validate_plugin(str(plugin_dir))

                if result["valid"]:
                    self.validation_results["valid_plugins"].append(
                        {
                            "path": str(plugin_dir),
                            "metadata": result.get("metadata", {}),
                        }
                    )
                else:
                    self.validation_results["invalid_plugins"].append(
                        {"path": str(plugin_dir), "errors": result["errors"]}
                    )

                self.validation_results["warnings"].extend(result["warnings"])
                self.validation_results["errors"].extend(result["errors"])

        return self.validation_results

    def generate_validation_report(self) -> str:
        """Génère un rapport de validation"""
        report = []
        report.append("# Rapport de Validation des Plugins")
        report.append("")

        report.append(
            f"## Plugins Valides ({len(self.validation_results['valid_plugins'])})"
        )
        for plugin in self.validation_results["valid_plugins"]:
            report.append(f"- {plugin['path']}")
            if plugin.get("metadata"):
                report.append(
                    f"  - Version: {plugin['metadata'].get('version', 'N/A')}"
                )
                report.append(
                    f"  - Description: {plugin['metadata'].get('description', 'N/A')}"
                )

        report.append("")
        report.append(
            f"## Plugins Invalides ({len(self.validation_results['invalid_plugins'])})"
        )
        for plugin in self.validation_results["invalid_plugins"]:
            report.append(f"- {plugin['path']}")
            for error in plugin["errors"]:
                report.append(f"  - ❌ {error}")

        if self.validation_results["warnings"]:
            report.append("")
            report.append("## Avertissements")
            for warning in self.validation_results["warnings"]:
                report.append(f"- ⚠️ {warning}")

        return "\n".join(report)


def validate_plugin(plugin_path: str) -> Dict[str, Any]:
    """Fonction utilitaire pour valider un plugin"""
    validator = PluginValidator()
    return validator.validate_plugin(plugin_path)


def validate_all_plugins(plugins_dir: str = "plugins") -> Dict[str, Any]:
    """Fonction utilitaire pour valider tous les plugins"""
    validator = PluginValidator(plugins_dir)
    return validator.validate_all_plugins()

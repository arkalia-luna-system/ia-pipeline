#!/usr/bin/env python3
"""
Module de validation ROS2 pour Athalia
Validation et vérification des packages ROS2
"""

import logging
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import validate_and_run, SecurityError
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


logger = logging.getLogger(__name__)


class ROS2Validator:
    """Validateur de packages ROS2"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.validation_results = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "metadata": {},
            "dependencies": [],
            "launch_files": [],
            "test_files": [],
        }

    def validate_package(self) -> Dict[str, Any]:
        """Valide un package ROS2 complet"""
        logger.info(f"🔍 Validation du package ROS2: {self.project_path.name}")

        # Vérifier la structure de base
        if not self._check_package_structure():
            self.validation_results["valid"] = False

        # Valider package.xml
        if not self._validate_package_xml():
            self.validation_results["valid"] = False

        # Valider setup.py
        if not self._validate_setup_py():
            self.validation_results["valid"] = False

        # Valider CMakeLists.txt
        if not self._validate_cmakelists():
            self.validation_results["valid"] = False

        # Vérifier les fichiers de lancement
        self._check_launch_files()

        # Vérifier les tests
        self._check_test_files()

        # Vérifier les dépendances
        self._check_dependencies()

        return self.validation_results

    def _check_package_structure(self) -> bool:
        """Vérifie la structure de base du package"""
        required_files = ["package.xml", "setup.py"]
        # optional_files = ["CMakeLists.txt", "launch/", "test/", "src/"]

        missing_required = []
        for file in required_files:
            if not (self.project_path / file).exists():
                missing_required.append(file)

        if missing_required:
            self.validation_results["errors"].append(
                f"Fichiers requis manquants: {missing_required}"
            )
            return False

        return True

    def _validate_package_xml(self) -> bool:
        """Valide le fichier package.xml"""
        package_xml_path = self.project_path / "package.xml"

        try:
            tree = ET.parse(package_xml_path)
            root = tree.getroot()

            # Vérifier les éléments requis
            required_elements = [
                "name",
                "version",
                "description",
                "maintainer",
                "license",
            ]
            missing_elements = []

            for element in required_elements:
                if root.find(element) is None:
                    missing_elements.append(element)

            if missing_elements:
                self.validation_results["errors"].append(
                    f"Éléments requis manquants dans package.xml: {missing_elements}"
                )
                return False

            # Extraire les métadonnées
            self.validation_results["metadata"] = {
                "name": root.find("name").text,
                "version": root.find("version").text,
                "description": root.find("description").text,
                "maintainer": root.find("maintainer").text,
                "license": root.find("license").text,
            }

            # Extraire les dépendances
            dependencies = []
            for dep in root.findall(".//depend"):
                dependencies.append(dep.text)
            for dep in root.findall(".//build_depend"):
                dependencies.append(dep.text)
            for dep in root.findall(".//exec_depend"):
                dependencies.append(dep.text)

            self.validation_results["dependencies"] = list(set(dependencies))

            return True

        except ET.ParseError as e:
            self.validation_results["errors"].append(f"Erreur parsing package.xml: {e}")
            return False
        except Exception as e:
            self.validation_results["errors"].append(
                f"Erreur validation package.xml: {e}"
            )
            return False

    def _validate_setup_py(self) -> bool:
        """Valide le fichier setup.py"""
        setup_py_path = self.project_path / "setup.py"

        if not setup_py_path.exists():
            self.validation_results["warnings"].append("setup.py manquant")
            return True

        try:
            with open(setup_py_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Vérifier les éléments requis
            required_patterns = [
                r"from\s+setuptools\s+import",
                r"package_name\s*=",
                r"setup\(",
            ]

            missing_patterns = []
            for pattern in required_patterns:
                if not re.search(pattern, content):
                    missing_patterns.append(pattern)

            if missing_patterns:
                self.validation_results["warnings"].append(
                    f"Patterns requis manquants dans setup.py: {missing_patterns}"
                )

            return True

        except Exception as e:
            self.validation_results["errors"].append(f"Erreur validation setup.py: {e}")
            return False

    def _validate_cmakelists(self) -> bool:
        """Valide le fichier CMakeLists.txt"""
        cmake_path = self.project_path / "CMakeLists.txt"

        if not cmake_path.exists():
            self.validation_results["warnings"].append("CMakeLists.txt manquant")
            return True

        try:
            with open(cmake_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Vérifier les éléments requis
            required_patterns = [
                r"cmake_minimum_required",
                r"project\(",
                r"find_package\(",
            ]

            missing_patterns = []
            for pattern in required_patterns:
                if not re.search(pattern, content):
                    missing_patterns.append(pattern)

            if missing_patterns:
                self.validation_results["warnings"].append(
                    f"Patterns requis manquants dans CMakeLists.txt: {missing_patterns}"
                )

            return True

        except Exception as e:
            self.validation_results["errors"].append(
                f"Erreur validation CMakeLists.txt: {e}"
            )
            return False

    def _check_launch_files(self):
        """Vérifie les fichiers de lancement"""
        launch_dir = self.project_path / "launch"

        if launch_dir.exists():
            launch_files = list(launch_dir.glob("*.launch.py")) + list(
                launch_dir.glob("*.launch")
            )

            for launch_file in launch_files:
                try:
                    with open(launch_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Vérifier la syntaxe de base
                    if "LaunchDescription" in content or "launch" in content:
                        self.validation_results["launch_files"].append(str(launch_file))
                    else:
                        self.validation_results["warnings"].append(
                            f"Fichier de lancement suspect: {launch_file}"
                        )

                except Exception as e:
                    self.validation_results["warnings"].append(
                        f"Impossible de lire {launch_file}: {e}"
                    )

    def _check_test_files(self):
        """Vérifie les fichiers de test"""
        test_dir = self.project_path / "test"

        if test_dir.exists():
            test_files = list(test_dir.rglob("*.py"))

            for test_file in test_files:
                try:
                    with open(test_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Vérifier si c'est un fichier de test
                    if (
                        "test" in test_file.name.lower()
                        or "unittest" in content
                        or "pytest" in content
                    ):
                        self.validation_results["test_files"].append(str(test_file))

                except Exception as e:
                    self.validation_results["warnings"].append(
                        f"Impossible de lire {test_file}: {e}"
                    )

    def _check_dependencies(self):
        """Vérifie les dépendances du package"""
        try:
            # Vérifier avec rosdep
            result = validate_and_run(
                [
                    "rosdep",
                    "check",
                    "--from-paths",
                    str(self.project_path),
                    "--ignore-src",
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode != 0:
                self.validation_results["warnings"].append(
                    f"Problèmes de dépendances détectés: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            self.validation_results["warnings"].append(
                "Timeout lors de la vérification des dépendances"
            )
        except Exception as e:
            self.validation_results["warnings"].append(
                f"Erreur vérification dépendances: {e}"
            )

    def generate_validation_report(self) -> str:
        """Génère un rapport de validation"""
        report = []
        report.append("# Rapport de Validation ROS2")
        report.append("")

        status = "✅ VALIDE" if self.validation_results["valid"] else "❌ INVALIDE"
        report.append(f"## Statut: {status}")
        report.append("")

        if self.validation_results["metadata"]:
            report.append("## Métadonnées")
            for key, value in self.validation_results["metadata"].items():
                report.append(f"- **{key}**: {value}")
            report.append("")

        if self.validation_results["dependencies"]:
            report.append("## Dépendances")
            for dep in self.validation_results["dependencies"]:
                report.append(f"- {dep}")
            report.append("")

        if self.validation_results["launch_files"]:
            report.append("## Fichiers de Lancement")
            for launch_file in self.validation_results["launch_files"]:
                report.append(f"- {launch_file}")
            report.append("")

        if self.validation_results["test_files"]:
            report.append("## Fichiers de Test")
            for test_file in self.validation_results["test_files"]:
                report.append(f"- {test_file}")
            report.append("")

        if self.validation_results["errors"]:
            report.append("## Erreurs")
            for error in self.validation_results["errors"]:
                report.append(f"- ❌ {error}")
            report.append("")

        if self.validation_results["warnings"]:
            report.append("## Avertissements")
            for warning in self.validation_results["warnings"]:
                report.append(f"- ⚠️ {warning}")
            report.append("")

        return "\n".join(report)


def validate_ros2_package(package_path: str = ".") -> Dict[str, Any]:
    """Fonction utilitaire pour valider un package ROS2"""
    validator = ROS2Validator(package_path)
    return validator.validate_package()

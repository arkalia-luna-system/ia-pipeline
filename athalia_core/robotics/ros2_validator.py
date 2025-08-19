#!/usr/bin/env python3
"""
Validateur ROS2 pour Athalia
Vérification de la configuration et de la structure des projets ROS2
"""

import logging
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from ..validation.security_validator import validateand_run

logger = logging.getLogger(__name__)


class ROS2Validator:
    """Validateur de packages ROS2"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.validation_results: dict[str, Any] = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "metadata": {},
            "dependencies": [],
            "launch_files": [],
            "test_files": [],
        }

    def validate_package(self) -> dict[str, Any]:
        """Valide un package ROS2 complet"""
        logger.info(f" Validation du package ROS2: {self.project_path.name}")

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
            errors = self.validation_results.get("errors", [])
            if isinstance(errors, list):
                errors.append(f"Fichiers requis manquants: {missing_required}")
            return False

        return True

    def _validate_package_xml(self) -> bool:
        """Valide le fichier package.xml"""
        package_xml_path = self.project_path / "package.xml"

        try:
            tree = ET.parse(package_xml_path)  # nosec B314
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
                errors = self.validation_results.get("errors", [])
                if isinstance(errors, list):
                    errors.append(
                        f"Éléments requis manquants dans package.xml: {missing_elements}"
                    )
                return False

            # Extraire les métadonnées
            name_elem = root.find("name")
            version_elem = root.find("version")
            description_elem = root.find("description")
            maintainer_elem = root.find("maintainer")
            license_elem = root.find("license")

            if all(
                [
                    name_elem,
                    version_elem,
                    description_elem,
                    maintainer_elem,
                    license_elem,
                ]
            ):
                self.validation_results["metadata"] = {
                    "name": (name_elem.text or "") if name_elem is not None else "",
                    "version": (
                        (version_elem.text or "") if version_elem is not None else ""
                    ),
                    "description": (
                        (description_elem.text or "")
                        if description_elem is not None
                        else ""
                    ),
                    "maintainer": (
                        (maintainer_elem.text or "")
                        if maintainer_elem is not None
                        else ""
                    ),
                    "license": (
                        (license_elem.text or "") if license_elem is not None else ""
                    ),
                }

            return True

        except ET.ParseError as e:
            errors = self.validation_results.get("errors", [])
            if isinstance(errors, list):
                errors.append(f"Erreur parsing package.xml: {e}")
            return False
        except Exception as e:
            errors = self.validation_results.get("errors", [])
            if isinstance(errors, list):
                errors.append(f"Erreur validation package.xml: {e}")
            return False

    def _validate_setup_py(self) -> bool:
        """Valide le fichier setup.py"""
        setup_path = self.project_path / "setup.py"

        if not setup_path.exists():
            self.validation_results["warnings"].append("setup.py manquant")
            return True

        try:
            with open(setup_path, encoding="utf-8") as f:
                content = f.read()

            # Vérifier les éléments requis
            required_patterns = [
                r"from setuptools import",
                r"setup\(",
                r"name=",
                r"version=",
            ]

            missing_patterns = []
            for pattern in required_patterns:
                if not re.search(pattern, content):
                    missing_patterns.append(pattern)  # type: ignore[unreachable]

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
            with open(cmake_path, encoding="utf-8") as f:
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
                    missing_patterns.append(pattern)  # type: ignore[unreachable]

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
                    with open(launch_file, encoding="utf-8") as f:
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
                    with open(test_file, encoding="utf-8") as f:
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
            result = subprocess.run(
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

        status = " VALIDE" if self.validation_results["valid"] else " INVALIDE"
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
                report.append(f"-  {error}")
            report.append("")

        if self.validation_results["warnings"]:
            report.append("## Avertissements")
            for warning in self.validation_results["warnings"]:
                report.append(f"-  {warning}")
            report.append("")

        return "\n".join(report)


def validate_ros2_package(package_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour valider un package ROS2"""
    validator = ROS2Validator(package_path)
    return validator.validate_package()

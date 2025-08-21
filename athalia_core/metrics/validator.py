#!/usr/bin/env python3
"""
Athalia Core Metrics Validator
==============================

Module de validation des métriques collectées.
Assure la cohérence et la fiabilité des données.
"""

from typing import Any, Optional


class MetricsValidator:
    """
    Validateur de métriques pour s'assurer de la cohérence des données.

    Vérifie que les métriques collectées sont logiques et cohérentes
    entre elles (ex: le nombre de tests ne peut pas être supérieur au
    nombre total de fichiers Python).
    """

    def __init__(self) -> None:
        """Initialise le validateur de métriques."""
        self.validation_errors: list[str] = []
        self.validation_warnings: list[str] = []

    def validate_metrics(
        self, metrics_data: dict[str, Any]
    ) -> tuple[bool, list[str], list[str]]:
        """
        Valide un ensemble complet de métriques.

        Args:
            metrics_data: Données des métriques à valider

        Returns:
            Tuple avec (is_valid, errors, warnings)
        """
        self.validation_errors.clear()
        self.validation_warnings.clear()

        # Vérifications de base
        self._validate_structure(metrics_data)
        self._validate_python_metrics(metrics_data)
        self._validate_test_metrics(metrics_data)
        self._validate_documentation_metrics(metrics_data)
        self._validate_cross_metrics(metrics_data)

        is_valid = len(self.validation_errors) == 0
        return is_valid, self.validation_errors.copy(), self.validation_warnings.copy()

    def _validate_structure(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide la structure de base des métriques.

        Args:
            metrics_data: Données à valider
        """
        required_sections = [
            "timestamp",
            "python_files",
            "tests",
            "documentation",
            "summary",
        ]

        for section in required_sections:
            if section not in metrics_data:
                self.validation_errors.append(f"Section manquante: {section}")

    def _validate_python_metrics(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide les métriques Python.

        Args:
            metrics_data: Données à valider
        """
        python_data = metrics_data.get("python_files", {})

        # Vérifier que les valeurs sont cohérentes
        total_count = python_data.get("count", 0)
        core_files = python_data.get("core_files", 0)
        test_files = python_data.get("test_files", 0)

        if core_files + test_files != total_count:
            self.validation_warnings.append(
                f"Incohérence: core_files ({core_files}) + test_files ({test_files}) "
                f"!= total_count ({total_count})"
            )

        # Vérifier les valeurs négatives
        for key, value in python_data.items():
            if isinstance(value, int) and value < 0:
                self.validation_errors.append(
                    f"Valeur négative pour python_files.{key}: {value}"
                )

        # Vérifier les lignes de code
        total_lines = python_data.get("total_lines", 0)
        if total_lines < total_count and total_count > 0:
            self.validation_warnings.append(
                f"Nombre de lignes ({total_lines}) suspicieusement bas "
                f"pour {total_count} fichiers Python"
            )

    def _validate_test_metrics(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide les métriques de tests.

        Args:
            metrics_data: Données à valider
        """
        test_data = metrics_data.get("tests", {})
        python_data = metrics_data.get("python_files", {})

        test_files_count = test_data.get("test_files_count", 0)
        collected_tests = test_data.get("collected_tests_count", 0)
        total_python_files = python_data.get("count", 0)

        # Vérifier que le nombre de fichiers de test ne dépasse pas le total
        if test_files_count > total_python_files:
            self.validation_errors.append(
                f"Nombre de fichiers de test ({test_files_count}) > "
                f"total de fichiers Python ({total_python_files})"
            )

        # Vérifier les valeurs négatives
        for key, value in test_data.items():
            if isinstance(value, int) and value < 0:
                self.validation_errors.append(
                    f"Valeur négative pour tests.{key}: {value}"
                )

        # Avertissement si pas de tests
        if test_files_count == 0:
            self.validation_warnings.append("Aucun fichier de test trouvé")

        # Avertissement si pytest n'a collecté aucun test mais il y a des fichiers
        if test_files_count > 0 and collected_tests == 0:
            self.validation_warnings.append(
                f"Fichiers de test trouvés ({test_files_count}) mais aucun test collecté par pytest"
            )

    def _validate_documentation_metrics(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide les métriques de documentation.

        Args:
            metrics_data: Données à valider
        """
        doc_data = metrics_data.get("documentation", {})

        total_files = doc_data.get("total_files", 0)
        by_format = doc_data.get("by_format", {})

        # Vérifier que la somme des formats correspond au total
        format_sum = sum(by_format.values())
        if format_sum != total_files:
            self.validation_warnings.append(
                f"Somme des formats ({format_sum}) != total documentation ({total_files})"
            )

        # Vérifier les valeurs négatives
        if total_files < 0:
            self.validation_errors.append(
                f"Valeur négative pour documentation.total_files: {total_files}"
            )

        for format_name, count in by_format.items():
            if count < 0:
                self.validation_errors.append(
                    f"Valeur négative pour documentation.by_format.{format_name}: {count}"
                )

    def _validate_cross_metrics(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide la cohérence entre différentes métriques.

        Args:
            metrics_data: Données à valider
        """
        python_data = metrics_data.get("python_files", {})
        summary = metrics_data.get("summary", {})

        # Vérifier la cohérence du résumé avec les données détaillées
        summary_python = summary.get("total_python_files", 0)
        detailed_python = python_data.get("count", 0)

        if summary_python != detailed_python:
            self.validation_errors.append(
                f"Incohérence summary.total_python_files ({summary_python}) != "
                f"python_files.count ({detailed_python})"
            )

        # Vérifier la cohérence des lignes de code
        summary_lines = summary.get("lines_of_code", 0)
        detailed_lines = python_data.get("total_lines", 0)

        if summary_lines != detailed_lines:
            self.validation_errors.append(
                f"Incohérence summary.lines_of_code ({summary_lines}) != "
                f"python_files.total_lines ({detailed_lines})"
            )

    def validate_timestamp(self, timestamp: str) -> bool:
        """
        Valide le format du timestamp.

        Args:
            timestamp: Timestamp à valider (format ISO)

        Returns:
            True si le timestamp est valide
        """
        try:
            from datetime import datetime

            datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            return True
        except (ValueError, AttributeError):
            self.validation_errors.append(f"Format de timestamp invalide: {timestamp}")
            return False

    def validate_ranges(self, metrics_data: dict[str, Any]) -> None:
        """
        Valide que les valeurs sont dans des plages raisonnables.

        Args:
            metrics_data: Données à valider
        """
        summary = metrics_data.get("summary", {})

        # Plages raisonnables pour un projet Python
        ranges = {
            "total_python_files": (1, 10000),
            "lines_of_code": (10, 1000000),
            "test_files": (0, 5000),
            "collected_tests": (0, 50000),
            "documentation_files": (1, 1000),
            "utility_scripts": (0, 200),
            "security_commands": (0, 500),
        }

        for metric, (min_val, max_val) in ranges.items():
            value = summary.get(metric, 0)
            if not (min_val <= value <= max_val):
                self.validation_warnings.append(
                    f"Valeur de {metric} ({value}) hors de la plage attendue "
                    f"[{min_val}, {max_val}]"
                )

    def get_validation_report(self) -> str:
        """
        Génère un rapport de validation lisible.

        Returns:
            Rapport de validation formaté
        """
        report = "# Rapport de Validation des Métriques\n\n"

        if not self.validation_errors and not self.validation_warnings:
            report += "✅ **Toutes les validations ont réussi !**\n\n"
            report += "Les métriques collectées sont cohérentes et fiables.\n"
            return report

        if self.validation_errors:
            report += "## ❌ Erreurs de Validation\n\n"
            for error in self.validation_errors:
                report += f"- ❌ {error}\n"
            report += "\n"

        if self.validation_warnings:
            report += "## ⚠️ Avertissements\n\n"
            for warning in self.validation_warnings:
                report += f"- ⚠️ {warning}\n"
            report += "\n"

        if self.validation_errors:
            report += "**Action requise :** Corriger les erreurs avant d'utiliser ces métriques.\n"
        else:
            report += "**Les métriques peuvent être utilisées avec prudence.**\n"

        return report

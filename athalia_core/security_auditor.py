#!/usr/bin/env python3
import json
import logging
from pathlib import Path
import re
import subprocess
from typing import Any, Dict

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback pour les tests
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityError(Exception):
        pass


logger = logging.getLogger(__name__)


"""
Module d'audit de sécurité pour Athalia
Détection automatique de vulnérabilités et bonnes pratiques
"""


class SecurityAuditor:
    """Auditeur de sécurité pour Athalia"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.report = {
            "score": 0,
            "vulnerabilities": [],
            "warnings": [],
            "recommendations": [],
        }

    def run(self) -> Dict[str, Any]:
        """Lance l'audit de sécurité renforcé"""
        logger.info(f"🔒 Audit de sécurité renforcé pour: {self.project_path.name}")

        # Vérifications en séquence
        self._check_dependencies()
        self._check_code_vulnerabilities()
        self._check_secrets()
        self._check_permissions()
        self._check_encryption()
        self._check_input_validation()
        self._check_authentication()
        self._check_data_protection()

        # Calcul du score
        self._calculate_score()

        # Générer un rapport détaillé
        self._generate_security_report()

        # Adapter le retour pour les tests
        return {
            "global_score": int(self.report.get("score", 0)),
            "summary": list(self.report.get("warnings", [])),
            "details": list(self.report.get("vulnerabilities", [])),
            "files": list(self.report.get("recommendations", [])),
            "security_level": self._get_security_level(),
            "compliance": self._check_compliance(),
        }

    def _check_dependencies(self):
        """Vérification des dépendances"""
        try:
            # Utiliser bandit pour lanalyse de sécurité
            result = validate_and_run(
                ["bandit", "-r", str(self.project_path), "-f", "json"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                self.report["vulnerabilities"].append(
                    "Aucune vulnérabilité détectée par Bandit"
                )
            else:
                self.report["vulnerabilities"].append(
                    f"Vulnérabilités Bandit détectées: {result.stdout}"
                )

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Bandit non exécuté: {e}")

        # Vérifier avec safety si disponible
        try:
            result = validate_and_run(
                ["safety", "check", "--json"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                vulns = json.loads(result.stdout)
                for vuln in vulns:
                    self.report["vulnerabilities"].append(
                        f"Vulnérabilité: {vuln['package']} {vuln['installed_version']}"
                    )

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Safety non exécuté: {e}")

    def _check_code_vulnerabilities(self):
        """Vérification des vulnérabilités dans le code"""
        dangerous_patterns = [
            r"eval\(",
            r"exec\(",
            r"subprocess\.call\(",
            r"os\.system\(",
            r"pickle\.loads\(",
            r"yaml\.load\(",
            r"input\(",
        ]

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in dangerous_patterns:
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        line_num = content[: match.start()].count("\n") + 1
                        self.report["vulnerabilities"].append(
                            f"Pattern dangereux {pattern} dans"
                            f" {py_file.name}:{line_num}"
                        )

            except (
                OSError,
                UnicodeDecodeError,
                PermissionError,
            ) as file_error:
                logger.debug(
                    f"Erreur lors de l'analyse du fichier {py_file}: {file_error}"
                )
                continue

    def _check_secrets(self):
        """Vérification des secrets"""
        secret_patterns = [
            r"password\s*=\s*\"[^\"]+\"",
            r"api_key\s*=\s*\"[^\"]+\"",
            r"secret\s*=\s*\"[^\"]+\"",
            r"token\s*=\s*\"[^\"]+\"",
        ]

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in secret_patterns:
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        line_num = content[: match.start()].count("\n") + 1
                        self.report["vulnerabilities"].append(
                            f"Secret potentiel dans {py_file.name}:{line_num}"
                        )

            except (
                OSError,
                UnicodeDecodeError,
                PermissionError,
            ) as file_error:
                logger.debug(
                    f"Erreur lors de l'analyse du fichier {py_file}: {file_error}"
                )
                continue

    def _check_permissions(self):
        """Vérification des permissions des fichiers"""
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                try:
                    stat = file_path.stat()
                    if stat.st_mode & 0o777 == 0o777:
                        self.report["warnings"].append(
                            f"Permissions trop ouvertes: {file_path}"
                        )
                except (OSError, PermissionError) as perm_error:
                    logger.debug(
                        f"Erreur lors de la vérification des permissions {file_path}:"
                        f" {perm_error}"
                    )
                    continue

    def _check_encryption(self):
        """Vérification de lutilisation du chiffrement"""
        encryption_patterns = [
            r"from cryptography",
            r"import hashlib",
            r"import secrets",
        ]

        has_encryption = False
        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in encryption_patterns:
                    if re.search(pattern, content):
                        has_encryption = True
                        break

            except (
                OSError,
                UnicodeDecodeError,
                PermissionError,
            ) as file_error:
                logger.debug(
                    f"Erreur lors de l'analyse du fichier {py_file}: {file_error}"
                )
                continue

        if not has_encryption:
            self.report["recommendations"].append(
                "Considérer lutilisation de modules de chiffrement pour les données"
                " sensibles."
            )

    def _calculate_score(self):
        """Calcul du score de sécurité"""
        base_score = 100
        # Pénalités
        base_score -= len(self.report["vulnerabilities"]) * 20
        base_score -= len(self.report["warnings"]) * 5
        self.report["score"] = max(0, base_score)

    def _check_input_validation(self):
        """Vérification de la validation des entrées"""
        validation_patterns = [
            r"\.validate\(",
            r"pydantic",
            r"re\.match\(",
            r"isinstance\(",
        ]

        has_validation = False
        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in validation_patterns:
                    if re.search(pattern, content):
                        has_validation = True
                        break

            except (OSError, UnicodeDecodeError, PermissionError):
                continue

        if not has_validation:
            self.report["warnings"].append(
                "Validation des entrées utilisateur recommandée"
            )

    def _check_authentication(self):
        """Vérification de l'authentification"""
        auth_patterns = [
            r"jwt",
            r"oauth",
            r"authentication",
            r"login",
            r"password",
        ]

        has_auth = False
        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in auth_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        has_auth = True
                        break

            except (OSError, UnicodeDecodeError, PermissionError):
                continue

        if not has_auth:
            self.report["recommendations"].append(
                "Considérer l'ajout d'un système d'authentification"
            )

    def _check_data_protection(self):
        """Vérification de la protection des données"""
        protection_patterns = [
            r"gdpr",
            r"privacy",
            r"data_protection",
            r"personal_data",
        ]

        has_protection = False
        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern in protection_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        has_protection = True
                        break

            except (OSError, UnicodeDecodeError, PermissionError):
                continue

        if not has_protection:
            self.report["recommendations"].append(
                "Considérer l'ajout de mesures de protection des données (GDPR)"
            )

    def _get_security_level(self) -> str:
        """Détermine le niveau de sécurité"""
        score = self.report.get("score", 0)
        if score >= 90:
            return "EXCELLENT"
        elif score >= 70:
            return "BON"
        elif score >= 50:
            return "MOYEN"
        else:
            return "CRITIQUE"

    def _check_compliance(self) -> Dict[str, bool]:
        """Vérifie la conformité aux standards"""
        return {
            "gdpr_ready": "gdpr" in str(self.report.get("recommendations", [])).lower(),
            "authentication_ready": (
                "authentication" in str(self.report.get("recommendations", [])).lower()
            ),
            "encryption_ready": (
                "chiffrement" in str(self.report.get("recommendations", [])).lower()
            ),
            "input_validation_ready": (
                "validation" in str(self.report.get("warnings", [])).lower()
            ),
        }

    def _generate_security_report(self):
        """Génère un rapport de sécurité détaillé"""
        try:
            report_file = self.project_path / "security_audit_report.json"
            report_data = {
                "timestamp": str(Path().cwd()),
                "project": str(self.project_path),
                "score": self.report.get("score", 0),
                "security_level": self._get_security_level(),
                "vulnerabilities": self.report.get("vulnerabilities", []),
                "warnings": self.report.get("warnings", []),
                "recommendations": self.report.get("recommendations", []),
                "compliance": self._check_compliance(),
            }

            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)

            logger.info(f"📄 Rapport de sécurité généré: {report_file}")

        except Exception as e:
            logger.warning(f"Impossible de générer le rapport de sécurité: {e}")

    def print_report(self):
        """Affichage du rapport de sécurité renforcé"""
        logger.info(
            f"🔒 Score sécurité: {self.report['score']}/100 ({self._get_security_level()})"
        )

        if self.report["vulnerabilities"]:
            logger.info("🔴 Vulnérabilités:")
            for v in self.report["vulnerabilities"]:
                logger.info(f" - {v}")

        if self.report["warnings"]:
            logger.info("🟡 Avertissements:")
            for w in self.report["warnings"]:
                logger.info(f" - {w}")

        if self.report["recommendations"]:
            logger.info("💡 Recommandations:")
            for r in self.report["recommendations"]:
                logger.info(f" - {r}")

        # Afficher la conformité
        compliance = self._check_compliance()
        logger.info("📋 Conformité:")
        for standard, ready in compliance.items():
            status = "✅" if ready else "❌"
            logger.info(f" - {standard}: {status}")

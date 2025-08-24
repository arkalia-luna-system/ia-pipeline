#!/usr/bin/env python3
"""
Auditeur de sécurité pour Athalia
Vérifications de sécurité automatisées
"""

import logging

# Import sécurisé pour subprocess
from pathlib import Path
from typing import Any

# Import du validateur de sécurité
try:
    from athalia_core.validation.security_validator import (
        SecurityError,
        validateand_run,
    )
except ImportError:
    # Fallback pour les tests
    class SecurityErrorFallback(Exception):
        pass

    def validateand_run(command: list[str], **kwargs: Any) -> Any:
        import subprocess

        return subprocess.run(command, **kwargs)


logger = logging.getLogger(__name__)


class SecurityAuditor:
    """Auditeur de sécurité pour projets Python"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.report: dict[str, Any] = {
            "score": 0,
            "warnings": [],
            "vulnerabilities": [],
            "recommendations": [],
        }

    def run(self) -> dict[str, Any]:
        """Lance l'audit de sécurité complet"""
        logger.info(f"🔒 Audit de sécurité pour: {self.project_path.name}")

        # Vérifications en séquence
        self._check_dependencies()
        self._check_code_vulnerabilities()
        self._check_secrets()
        self._check_permissions()
        self._check_encryption()
        self._check_input_validation()
        self._check_authentication()

        # Calcul du score et génération du rapport
        self._calculate_score()
        self._generate_security_report()

        return {
            "global_score": int(self.report.get("score", 0)),
            "summary": list(self.report.get("warnings", [])),
            "details": list(self.report.get("vulnerabilities", [])),
            "files": list(self.report.get("recommendations", [])),
        }

    def _check_dependencies(self) -> None:
        """Vérifie les dépendances pour les vulnérabilités connues"""
        try:
            # Vérifier avec bandit
            result = validateand_run(
                ["bandit", "-r", str(self.project_path), "-f", "json"],
                capture_output=True,
                text=True,
                timeout=120,
            )

            if result.returncode != 0:
                if isinstance(self.report["vulnerabilities"], list):
                    self.report["vulnerabilities"].append(
                        f"Bandit a détecté des problèmes: {result.stderr}"
                    )

        except Exception as e:
            if isinstance(self.report["warnings"], list):
                self.report["warnings"].append(f"Bandit non exécuté: {e}")

        try:
            # Vérifier avec safety
            result = validateand_run(
                ["safety", "check", "--json"],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode != 0:
                if isinstance(self.report["vulnerabilities"], list):
                    self.report["vulnerabilities"].append(
                        f"Safety a détecté des vulnérabilités: {result.stdout}"
                    )

        except Exception as e:
            if isinstance(self.report["warnings"], list):
                self.report["warnings"].append(f"Safety non exécuté: {e}")

    def _check_code_vulnerabilities(self) -> None:
        """Vérifie le code source pour les vulnérabilités"""
        try:
            # Rechercher des patterns dangereux
            dangerous_patterns = [
                "eval(",
                "exec(",
                "os.system(",
                "subprocess.call(",
                "pickle.loads(",
                "yaml.load(",
                "input(",
            ]

            for py_file in self.project_path.rglob("*.py"):
                try:
                    with open(py_file, encoding="utf-8") as f:
                        content = f.read()

                    for pattern in dangerous_patterns:
                        if pattern in content:
                            if isinstance(self.report["vulnerabilities"], list):
                                self.report["vulnerabilities"].append(
                                    f"Pattern dangereux '{pattern}' dans {py_file}"
                                )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification code: {e}")

    def _check_secrets(self) -> None:
        """Vérifie la présence de secrets exposés"""
        try:
            # Patterns de secrets
            secret_patterns = [
                r"password\s*=\s*['\"][^'\"]+['\"]",
                r"api_key\s*=\s*['\"][^'\"]+['\"]",
                r"secret\s*=\s*['\"][^'\"]+['\"]",
                r"token\s*=\s*['\"][^'\"]+['\"]",
            ]

            import re

            for py_file in self.project_path.rglob("*.py"):
                try:
                    with open(py_file, encoding="utf-8") as f:
                        content = f.read()

                    for pattern in secret_patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        if matches:
                            if isinstance(self.report["vulnerabilities"], list):
                                self.report["vulnerabilities"].append(
                                    f"Secret potentiel dans {py_file}: {matches[0]}"
                                )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification secrets: {e}")

    def _check_permissions(self) -> None:
        """Vérifie les permissions des fichiers"""
        try:
            for py_file in self.project_path.rglob("*.py"):
                try:
                    stat = py_file.stat()
                    if stat.st_mode & 0o777 != 0o644:
                        if isinstance(self.report["warnings"], list):
                            self.report["warnings"].append(
                                f"Permissions inhabituelles pour {py_file}: {oct(stat.st_mode)[-3:]}"
                            )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification permissions: {e}")

    def _check_encryption(self) -> None:
        """Vérifie l'utilisation de l'encryption"""
        try:
            # Rechercher des patterns d'encryption
            encryption_patterns = [
                "hashlib.md5(",
                "hashlib.sha1(",
                "base64.b64encode(",
                "base64.b64decode(",
            ]

            for py_file in self.project_path.rglob("*.py"):
                try:
                    with open(py_file, encoding="utf-8") as f:
                        content = f.read()

                    for pattern in encryption_patterns:
                        if pattern in content:
                            if isinstance(self.report["recommendations"], list):
                                self.report["recommendations"].append(
                                    f"Vérifier l'utilisation de '{pattern}' dans {py_file}"
                                )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification encryption: {e}")

    def _calculate_score(self) -> None:
        """Calcule le score de sécurité"""
        base_score = 100

        # Pénalités pour vulnérabilités
        if isinstance(self.report["vulnerabilities"], list):
            base_score -= len(self.report["vulnerabilities"]) * 20

        # Pénalités pour avertissements
        if isinstance(self.report["warnings"], list):
            base_score -= len(self.report["warnings"]) * 5

        self.report["score"] = max(0, base_score)

    def _check_input_validation(self) -> None:
        """Vérifie la validation des entrées"""
        try:
            # Rechercher des patterns de validation
            validation_patterns = [
                "input(",
                "raw_input(",
                "sys.argv[",
                "request.args[",
                "request.form[",
            ]

            for py_file in self.project_path.rglob("*.py"):
                try:
                    with open(py_file, encoding="utf-8") as f:
                        content = f.read()

                    for pattern in validation_patterns:
                        if pattern in content:
                            if isinstance(self.report["warnings"], list):
                                self.report["warnings"].append(
                                    f"Vérifier la validation des entrées '{pattern}' dans {py_file}"
                                )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification validation: {e}")

    def _check_authentication(self) -> None:
        """Vérifie l'authentification et l'autorisation"""
        try:
            # Rechercher des patterns d'authentification
            auth_patterns = [
                "login",
                "authenticate",
                "authorize",
                "session",
                "jwt",
                "oauth",
            ]

            for py_file in self.project_path.rglob("*.py"):
                try:
                    with open(py_file, encoding="utf-8") as f:
                        content = f.read()

                    for pattern in auth_patterns:
                        if pattern in content:
                            if isinstance(self.report["recommendations"], list):
                                self.report["recommendations"].append(
                                    f"Vérifier l'implémentation de '{pattern}' dans {py_file}"
                                )

                except Exception as e:

                    logger.debug(f"Erreur gérée: {e}")

                    continue

        except Exception as e:
            logger.warning(f"Erreur vérification authentification: {e}")

    def _get_security_level(self, score: int) -> str:
        """Détermine le niveau de sécurité"""
        if isinstance(score, int | float) and score >= 90:
            return "EXCELLENT"
        elif isinstance(score, int | float) and score >= 70:
            return "BON"
        elif isinstance(score, int | float) and score >= 50:
            return "MOYEN"
        else:
            return "FAIBLE"

    def _generate_security_report(self) -> None:
        """Génère un rapport de sécurité détaillé"""
        try:
            import json

            report_file = self.project_path / "security_report.json"
            report_data = {
                "timestamp": str(Path().cwd()),
                "project": str(self.project_path),
                "score": self.report.get("score", 0),
                "level": self._get_security_level(self.report.get("score", 0)),
                "vulnerabilities": self.report.get("vulnerabilities", []),
                "warnings": self.report.get("warnings", []),
                "recommendations": self.report.get("recommendations", []),
            }

            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)

            logger.info(f"📄 Rapport de sécurité généré: {report_file}")

        except Exception as e:
            logger.warning(f"Impossible de générer le rapport de sécurité: {e}")

    def print_report(self) -> None:
        """Affiche le rapport de sécurité"""
        score = self.report.get("score", 0)
        level = self._get_security_level(score)

        print(f"🔒 Rapport de sécurité - {self.project_path.name}")
        print(f"Score: {score}/100 ({level})")
        print()

        if (
            isinstance(self.report["vulnerabilities"], list)
            and self.report["vulnerabilities"]
        ):
            print("❌ Vulnérabilités détectées:")
            for v in self.report["vulnerabilities"]:
                print(f"  - {v}")
            print()

        if isinstance(self.report["warnings"], list) and self.report["warnings"]:
            print("⚠️ Avertissements:")
            for w in self.report["warnings"]:
                print(f"  - {w}")
            print()

        if (
            isinstance(self.report["recommendations"], list)
            and self.report["recommendations"]
        ):
            print("💡 Recommandations:")
            for r in self.report["recommendations"]:
                print(f"  - {r}")


def main() -> None:
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="Auditeur de sécurité")
    parser.add_argument("project_path", help="Chemin vers le projet")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")

    args = parser.parse_args()

    auditor = SecurityAuditor(args.project_path)
    results = auditor.run()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            import json

            json.dump(results, f, indent=2)
        print(f"📄 Rapport sauvegardé dans {args.output}")
    else:
        auditor.print_report()


if __name__ == "__main__":
    main()

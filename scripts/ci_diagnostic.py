#!/usr/bin/env python3
"""
Script de diagnostic CI/CD pour identifier les problèmes de performance
et de configuration dans les workflows GitHub Actions
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


class CIDiagnostic:
    """Diagnostic CI/CD pour Athalia"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "issues": [],
            "recommendations": [],
            "performance_metrics": {},
        }

    def print_header(self, title: str):
        """Affiche un en-tête"""
        print(f"\n{'=' * 60}")
        print(f"{title:^60}")
        print(f"{'=' * 60}")

    def print_success(self, message: str):
        """Affiche un message de succès"""
        print(f"✅ {message}")

    def print_warning(self, message: str):
        """Affiche un message d'avertissement"""
        print(f"⚠️  {message}")

    def print_error(self, message: str):
        """Affiche un message d'erreur"""
        print(f"❌ {message}")

    def check_workflow_files(self) -> Dict[str, Any]:
        """Vérifie les fichiers de workflow"""
        self.print_header("VÉRIFICATION DES WORKFLOWS")

        workflow_dir = self.project_root / ".github" / "workflows"
        if not workflow_dir.exists():
            self.print_error("Dossier .github/workflows/ manquant")
            return {"status": "ERROR", "files": []}

        workflow_files = list(workflow_dir.glob("*.yaml")) + list(
            workflow_dir.glob("*.yml")
        )
        workflow_files = [
            f
            for f in workflow_files
            if not f.name.startswith("._") and not f.name.startswith(".DS_Store")
        ]

        results = {"status": "OK", "files": [], "issues": []}

        for wf_file in workflow_files:
            try:
                with open(wf_file, "r") as f:
                    content = f.read()

                file_info = {
                    "name": wf_file.name,
                    "size": wf_file.stat().st_size,
                    "has_timeout": "timeout-minutes" in content,
                    "has_retry": "retries" in content or "continue-on-error" in content,
                }

                results["files"].append(file_info)

                if not file_info["has_timeout"]:
                    results["issues"].append(f"{wf_file.name}: Pas de timeout défini")

                if file_info["size"] > 10000:  # 10KB
                    results["issues"].append(
                        f"{wf_file.name}: Fichier volumineux "
                        f"({file_info['size']} bytes)"
                    )

            except Exception as e:
                self.print_error(f"Erreur lecture {wf_file.name}: {e}")
                results["issues"].append(f"Erreur lecture {wf_file.name}")

        return results

    def check_dependencies(self) -> Dict[str, Any]:
        """Vérifie les dépendances"""
        self.print_header("VÉRIFICATION DES DÉPENDANCES")

        results = {"status": "OK", "issues": []}

        # Vérifier requirements.txt
        req_file = self.project_root / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file, "r") as f:
                    lines = f.readlines()

                deps = [
                    line.strip()
                    for line in lines
                    if line.strip() and not line.startswith("#")
                ]
                results["total_deps"] = len(deps)

                if len(deps) > 50:
                    results["issues"].append(f"Trop de dépendances: {len(deps)}")
                    results["status"] = "WARNING"

            except Exception as e:
                self.print_error(f"Erreur lecture requirements.txt: {e}")
                results["issues"].append("Erreur lecture requirements.txt")
        else:
            results["issues"].append("requirements.txt manquant")
            results["status"] = "ERROR"

        return results

    def check_test_performance(self) -> Dict[str, Any]:
        """Vérifie la performance des tests"""
        self.print_header("VÉRIFICATION PERFORMANCE TESTS")

        results = {"status": "OK", "issues": []}

        test_dir = self.project_root / "tests"
        if not test_dir.exists():
            self.print_error("Dossier tests/ manquant")
            return {"status": "ERROR", "issues": ["Dossier tests/ manquant"]}

        # Compter les fichiers de test
        test_files = list(test_dir.rglob("test_*.py"))
        results["total_tests"] = len(test_files)

        if len(test_files) > 100:
            results["issues"].append(f"Trop de fichiers de test: {len(test_files)}")
            results["status"] = "WARNING"

        # Vérifier les tests lents
        slow_tests = []
        for test_file in test_files:
            try:
                with open(test_file, "r") as f:
                    content = f.read()

                if "@pytest.mark.slow" in content or "time.sleep" in content:
                    slow_tests.append(test_file.name)

            except Exception:
                pass

        if slow_tests:
            results["slow_tests"] = slow_tests
            results["issues"].append(f"Tests lents détectés: {len(slow_tests)}")
            results["status"] = "WARNING"

        return results

    def check_ci_configuration(self) -> Dict[str, Any]:
        """Vérifie la configuration CI"""
        self.print_header("VÉRIFICATION CONFIGURATION CI")

        results = {"status": "OK", "issues": [], "recommendations": []}

        # Vérifier le fichier principal CI
        ci_file = self.project_root / ".github" / "workflows" / "ci.yaml"
        if ci_file.exists():
            try:
                with open(ci_file, "r") as f:
                    content = f.read()

                # Vérifications importantes
                checks = {
                    "has_timeout": "timeout-minutes" in content,
                    "has_cache": "cache:" in content,
                    "has_continue_on_error": "continue-on-error:" in content,
                    "has_parallel": "needs:" in content,
                    "has_artifacts": "actions/upload-artifact" in content,
                }

                results["checks"] = checks

                if not checks["has_timeout"]:
                    results["issues"].append("Pas de timeout global défini")
                    results["recommendations"].append(
                        "Ajouter timeout-minutes au niveau job"
                    )

                if not checks["has_cache"]:
                    results["recommendations"].append(
                        "Activer le cache pip pour accélérer les builds"
                    )

                if not checks["has_parallel"]:
                    results["recommendations"].append(
                        "Considérer la parallélisation des jobs"
                    )

            except Exception as e:
                self.print_error(f"Erreur lecture ci.yaml: {e}")
                results["issues"].append("Erreur lecture ci.yaml")
        else:
            results["issues"].append("Fichier ci.yaml manquant")
            results["status"] = "ERROR"

        return results

    def generate_report(self) -> Dict[str, Any]:
        """Génère le rapport complet"""
        self.print_header("DIAGNOSTIC CI/CD ATHALIA")

        # Exécuter toutes les vérifications
        workflow_check = self.check_workflow_files()
        deps_check = self.check_dependencies()
        test_check = self.check_test_performance()
        ci_check = self.check_ci_configuration()

        # Compiler les résultats
        report = {
            "timestamp": datetime.now().isoformat(),
            "workflow_analysis": workflow_check,
            "dependencies_analysis": deps_check,
            "test_performance": test_check,
            "ci_configuration": ci_check,
            "summary": {
                "total_issues": (
                    len(workflow_check.get("issues", []))
                    + len(deps_check.get("issues", []))
                    + len(test_check.get("issues", []))
                    + len(ci_check.get("issues", []))
                ),
                "critical_issues": 0,
                "recommendations": [],
            },
        }

        # Compter les problèmes critiques
        for check in [workflow_check, deps_check, test_check, ci_check]:
            if check.get("status") == "ERROR":
                report["summary"]["critical_issues"] += 1

        # Compiler les recommandations
        all_recommendations = []
        for check in [workflow_check, deps_check, test_check, ci_check]:
            all_recommendations.extend(check.get("recommendations", []))

        report["summary"]["recommendations"] = list(set(all_recommendations))

        return report

    def print_summary(self, report: Dict[str, Any]):
        """Affiche le résumé"""
        self.print_header("RÉSUMÉ DU DIAGNOSTIC")

        summary = report["summary"]

        print(f"📊 Problèmes totaux: {summary['total_issues']}")
        print(f"🚨 Problèmes critiques: {summary['critical_issues']}")

        if summary["recommendations"]:
            print("\n💡 Recommandations prioritaires:")
            for i, rec in enumerate(summary["recommendations"][:5], 1):
                print(f"  {i}. {rec}")

        # Statut global
        if summary["critical_issues"] > 0:
            self.print_error("❌ Diagnostic révèle des problèmes critiques")
            return False
        elif summary["total_issues"] > 0:
            self.print_warning("⚠️ Diagnostic révèle des améliorations possibles")
            return True
        else:
            self.print_success("✅ Diagnostic excellent - configuration CI optimale")
            return True

    def save_report(self, report: Dict[str, Any], filename: str = None):
        """Sauvegarde le rapport"""
        if filename is None:
            filename = f"ci_diagnostic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w") as f:
            json.dump(report, f, indent=2)

        print(f"📄 Rapport sauvegardé: {filename}")


def main():
    """Fonction principale"""
    diagnostic = CIDiagnostic()

    try:
        # Générer le diagnostic
        report = diagnostic.generate_report()

        # Afficher le résumé
        success = diagnostic.print_summary(report)

        # Sauvegarder le rapport
        diagnostic.save_report(report)

        # Code de sortie
        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\n⚠️ Diagnostic interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors du diagnostic: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

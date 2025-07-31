#!/usr/bin/env python3
"""
Script d'analyse CI/CD Pro Athalia
Analyse automatique des corrections nécessaires par niveau
"""

import json
import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any


# Couleurs pour l'affichage
class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    NC = "\033[0m"


class CIProAnalyzer:
    """Analyseur CI/CD Pro pour Athalia"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.results = {}
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def print_header(self, title: str):
        """Affiche un en-tête coloré"""
        print(f"\n{Colors.PURPLE}{'='*60}{Colors.NC}")
        print(f"{Colors.PURPLE}{title:^60}{Colors.NC}")
        print(f"{Colors.PURPLE}{'='*60}{Colors.NC}")

    def print_section(self, title: str):
        """Affiche une section"""
        print(f"\n{Colors.BLUE}📋 {title}{Colors.NC}")

    def print_success(self, message: str):
        """Affiche un message de succès"""
        print(f"{Colors.GREEN}✅ {message}{Colors.NC}")

    def print_warning(self, message: str):
        """Affiche un message d'avertissement"""
        print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")

    def print_error(self, message: str):
        """Affiche un message d'erreur"""
        print(f"{Colors.RED}❌ {message}{Colors.NC}")

    def print_info(self, message: str):
        """Affiche un message d'information"""
        print(f"{Colors.CYAN}ℹ️  {message}{Colors.NC}")

    def run_command(
        self, command: str, capture_output: bool = True
    ) -> Tuple[int, str, str]:
        """Exécute une commande et retourne le résultat"""
        try:
            if capture_output:
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=300
                )
                return result.returncode, result.stdout, result.stderr
            else:
                result = subprocess.run(command, shell=True, timeout=300)
                return result.returncode, "", ""
        except subprocess.TimeoutExpired:
            return -1, "", "Timeout"
        except Exception as e:
            return -1, "", str(e)

    def analyze_level1_basic(self) -> Dict[str, Any]:
        """Analyse le niveau 1 - Tests de base"""
        self.print_section("Niveau 1 - Tests de Base")

        results = {"status": "FONCTIONNEL", "issues": [], "recommendations": []}

        # Test de linting
        returncode, stdout, stderr = self.run_command(
            "flake8 athalia_core/ --count --statistics"
        )
        if returncode == 0:
            self.print_success("Linting : Aucune erreur détectée")
        else:
            self.print_warning(f"Linting : {stdout.strip()} erreurs détectées")
            results["issues"].append(f"Erreurs de linting : {stdout.strip()}")

        # Test de syntaxe Python
        returncode, stdout, stderr = self.run_command(
            "python -m py_compile athalia_core/main.py"
        )
        if returncode == 0:
            self.print_success("Syntaxe Python : OK")
        else:
            self.print_error(f"Syntaxe Python : Erreur dans main.py")
            results["status"] = "DÉFAILLANT"
            results["issues"].append("Erreur de syntaxe Python")

        # Test des imports essentiels
        returncode, stdout, stderr = self.run_command(
            "python -c 'import athalia_core.audit; import athalia_core.cleanup; print(\"OK\")'"
        )
        if returncode == 0:
            self.print_success("Imports essentiels : OK")
        else:
            self.print_error("Imports essentiels : Erreur")
            results["status"] = "DÉFAILLANT"
            results["issues"].append("Erreur d'imports essentiels")

        # Recommandations
        results["recommendations"].extend(
            [
                "Ajouter mypy pour la vérification de types",
                "Ajouter pydocstyle pour la vérification des docstrings",
                "Optimiser les vérifications séquentielles",
            ]
        )

        return results

    def analyze_level2_security(self) -> Dict[str, Any]:
        """Analyse le niveau 2 - Tests de sécurité"""
        self.print_section("Niveau 2 - Tests de Sécurité")

        results = {
            "status": "PARTIEL",
            "vulnerabilities": {"high": 0, "medium": 0, "low": 0},
            "issues": [],
            "recommendations": [],
        }

        # Analyse Bandit
        returncode, stdout, stderr = self.run_command(
            "bandit -r athalia_core/ -f json -o /tmp/bandit_analysis.json"
        )
        if returncode == 0:
            try:
                with open("/tmp/bandit_analysis.json", "r") as f:
                    bandit_data = json.load(f)

                metrics = bandit_data.get("metrics", {}).get("_totals", {})
                results["vulnerabilities"]["high"] = metrics.get("SEVERITY.HIGH", 0)
                results["vulnerabilities"]["medium"] = metrics.get("SEVERITY.MEDIUM", 0)
                results["vulnerabilities"]["low"] = metrics.get("SEVERITY.LOW", 0)

                if (
                    results["vulnerabilities"]["high"] == 0
                    and results["vulnerabilities"]["medium"] == 0
                ):
                    self.print_success("Bandit : Aucune vulnérabilité critique")
                    results["status"] = "FONCTIONNEL"
                else:
                    self.print_warning(
                        f"Bandit : {results['vulnerabilities']['high']} HIGH, {results['vulnerabilities']['medium']} MEDIUM vulnérabilités"
                    )
                    results["issues"].append(
                        f"Vulnérabilités Bandit : {results['vulnerabilities']['high']} HIGH, {results['vulnerabilities']['medium']} MEDIUM"
                    )
            except Exception as e:
                self.print_error(f"Erreur lecture rapport Bandit : {e}")
        else:
            self.print_error("Erreur exécution Bandit")
            results["issues"].append("Erreur exécution Bandit")

        # Tests de sécurité spécifiques
        returncode, stdout, stderr = self.run_command(
            "python -m pytest tests/test_security_patterns.py -q"
        )
        if returncode == 0:
            self.print_success("Tests de sécurité : OK")
        else:
            self.print_warning("Tests de sécurité : Certains tests échouent")
            results["issues"].append("Tests de sécurité échoués")

        # Recommandations
        results["recommendations"].extend(
            [
                "Corriger les vulnérabilités HIGH et MEDIUM",
                "Marquer les faux positifs avec # nosec",
                "Ajouter Safety pour les dépendances",
                "Ajouter Semgrep pour patterns avancés",
            ]
        )

        return results

    def analyze_level3_performance(self) -> Dict[str, Any]:
        """Analyse le niveau 3 - Tests de performance"""
        self.print_section("Niveau 3 - Tests de Performance")

        results = {"status": "FONCTIONNEL", "issues": [], "recommendations": []}

        # Tests de performance
        returncode, stdout, stderr = self.run_command(
            "python -m pytest tests/test_performance_optimization.py -q"
        )
        if returncode == 0:
            self.print_success("Tests de performance : OK")
        else:
            self.print_error("Tests de performance : Échecs")
            results["status"] = "DÉFAILLANT"
            results["issues"].append("Tests de performance échoués")

        # Recommandations
        results["recommendations"].extend(
            [
                "Ajouter des benchmarks spécifiques",
                "Implémenter le profiling automatique",
                "Ajouter le monitoring en temps réel",
                "Optimiser les modules lents",
            ]
        )

        return results

    def analyze_level4_advanced(self) -> Dict[str, Any]:
        """Analyse le niveau 4 - Tests avancés"""
        self.print_section("Niveau 4 - Tests Avancés")

        results = {
            "status": "PARTIEL",
            "coverage": 0.0,
            "issues": [],
            "recommendations": [],
        }

        # Tests de couverture
        returncode, stdout, stderr = self.run_command(
            "python -m pytest tests/test_coverage_threshold.py -q"
        )
        if returncode == 0:
            self.print_success("Tests de couverture : OK")
        else:
            self.print_error("Tests de couverture : Échecs")
            results["issues"].append("Tests de couverture échoués")

        # Mesure de couverture réelle
        returncode, stdout, stderr = self.run_command(
            "python -m coverage run --source=athalia_core -m pytest tests/test_ai_robust_enhanced.py -q && python -m coverage report"
        )
        if returncode == 0:
            # Extraire le pourcentage de couverture
            for line in stdout.split("\n"):
                if "TOTAL" in line:
                    try:
                        coverage_str = line.split()[-1].replace("%", "")
                        results["coverage"] = float(coverage_str)
                        break
                    except:
                        pass

            if results["coverage"] >= 80:
                self.print_success(f"Couverture de code : {results['coverage']:.1f}%")
                results["status"] = "FONCTIONNEL"
            else:
                self.print_warning(
                    f"Couverture de code : {results['coverage']:.1f}% (objectif: 80%)"
                )
                results["issues"].append(
                    f"Couverture insuffisante : {results['coverage']:.1f}%"
                )
        else:
            self.print_error("Erreur mesure de couverture")
            results["issues"].append("Erreur mesure de couverture")

        # Recommandations
        results["recommendations"].extend(
            [
                f"Atteindre 80% de couverture (actuel: {results['coverage']:.1f}%)",
                "Créer des tests pour les modules sans couverture",
                "Prioriser les modules critiques",
                "Ajouter des tests paramétriques",
            ]
        )

        return results

    def analyze_level5_complete(self) -> Dict[str, Any]:
        """Analyse le niveau 5 - Tests complets"""
        self.print_section("Niveau 5 - Tests Complets")

        results = {"status": "DÉFAILLANT", "issues": [], "recommendations": []}

        # Vérifier l'existence des tests d'intégration
        integration_dir = self.project_root / "tests" / "integration"
        if integration_dir.exists():
            integration_files = list(integration_dir.glob("test_*.py"))
            if integration_files:
                self.print_success(
                    f"Tests d'intégration : {len(integration_files)} fichiers trouvés"
                )
                results["status"] = "PARTIEL"
            else:
                self.print_warning("Tests d'intégration : Dossier vide")
                results["issues"].append("Aucun test d'intégration")
        else:
            self.print_error("Tests d'intégration : Dossier manquant")
            results["issues"].append("Dossier tests/integration/ manquant")

        # Tests end-to-end existants
        e2e_tests = [
            "tests/integration/test_cli_robustesse.py",
            "tests/integration/test_end_to_end.py",
            "tests/integration/test_yaml_validity.py",
        ]

        existing_e2e = 0
        for test_file in e2e_tests:
            if Path(test_file).exists():
                existing_e2e += 1

        if existing_e2e > 0:
            self.print_info(f"Tests end-to-end : {existing_e2e} fichiers existants")
        else:
            self.print_warning("Tests end-to-end : Aucun fichier trouvé")
            results["issues"].append("Aucun test end-to-end")

        # Recommandations
        results["recommendations"].extend(
            [
                "Créer le dossier tests/integration/",
                "Implémenter les tests de workflow complet",
                "Créer les tests de scénarios réels",
                "Ajouter les tests de charge",
            ]
        )

        return results

    def generate_report(self) -> Dict[str, Any]:
        """Génère le rapport complet"""
        self.print_header("ANALYSE CI/CD PRO ATHALIA")

        report = {"timestamp": self.timestamp, "levels": {}}

        # Analyser chaque niveau
        report["levels"]["level1"] = self.analyze_level1_basic()
        report["levels"]["level2"] = self.analyze_level2_security()
        report["levels"]["level3"] = self.analyze_level3_performance()
        report["levels"]["level4"] = self.analyze_level4_advanced()
        report["levels"]["level5"] = self.analyze_level5_complete()

        return report

    def print_summary(self, report: Dict[str, Any]):
        """Affiche le résumé de l'analyse"""
        self.print_header("RÉSUMÉ DE L'ANALYSE")

        # Statut par niveau
        for level_name, level_data in report["levels"].items():
            status = level_data["status"]
            if status == "FONCTIONNEL":
                color = Colors.GREEN
                icon = "✅"
            elif status == "PARTIEL":
                color = Colors.YELLOW
                icon = "⚠️"
            else:
                color = Colors.RED
                icon = "❌"

            print(f"{color}{icon} {level_name.upper()} : {status}{Colors.NC}")

            # Afficher les problèmes principaux
            if level_data.get("issues"):
                for issue in level_data["issues"][:2]:  # Max 2 problèmes
                    print(f"   {Colors.RED}• {issue}{Colors.NC}")

        # Recommandations prioritaires
        self.print_section("Recommandations Prioritaires")

        priority_recommendations = []
        for level_name, level_data in report["levels"].items():
            if level_data["status"] != "FONCTIONNEL":
                priority_recommendations.extend(level_data["recommendations"][:2])

        for i, rec in enumerate(priority_recommendations[:5], 1):
            print(f"{Colors.CYAN}{i}. {rec}{Colors.NC}")

    def save_report(self, report: Dict[str, Any], filename: str = None):
        """Sauvegarde le rapport"""
        if filename is None:
            filename = (
                f"ci_pro_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )

        with open(filename, "w") as f:
            json.dump(report, f, indent=2)

        self.print_info(f"Rapport sauvegardé : {filename}")


def main():
    """Fonction principale"""
    analyzer = CIProAnalyzer()

    try:
        # Générer l'analyse
        report = analyzer.generate_report()

        # Afficher le résumé
        analyzer.print_summary(report)

        # Sauvegarder le rapport
        analyzer.save_report(report)

        # Code de sortie basé sur le statut global
        has_critical_issues = any(
            level["status"] == "DÉFAILLANT" for level in report["levels"].values()
        )

        if has_critical_issues:
            print(
                f"\n{Colors.RED}❌ Analyse terminée avec des problèmes critiques{Colors.NC}"
            )
            sys.exit(1)
        else:
            print(f"\n{Colors.GREEN}✅ Analyse terminée avec succès{Colors.NC}")
            sys.exit(0)

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Analyse interrompue par l'utilisateur{Colors.NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}❌ Erreur lors de l'analyse : {e}{Colors.NC}")
        sys.exit(1)


if __name__ == "__main__":
    main()

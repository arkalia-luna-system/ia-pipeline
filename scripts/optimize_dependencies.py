#!/usr/bin/env python3
"""
Script d'optimisation des dépendances Athalia
Analyse et optimise les dépendances du projet
"""
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DependencyOptimizer:
    """Optimiseur de dépendances"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.reports_dir = project_root / "data" / "reports" / "quality"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

        # Dépendances critiques à ne jamais supprimer
        self.critical_packages = {
            "pytest",
            "black",
            "ruff",
            "mypy",
            "bandit",
            "coverage",
            "fastapi",
            "uvicorn",
            "pydantic",
            "click",
            "typer",
            "streamlit",
            "pandas",
            "numpy",
            "requests",
            "pyyaml",
        }

    def run_command(self, cmd: list, timeout: int = 300) -> tuple:
        """Exécute une commande et retourne (returncode, stdout, stderr)"""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.project_root,
                timeout=timeout,
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            logger.error(f"Timeout pour la commande: {' '.join(cmd)}")
            return 1, "", "Timeout"
        except Exception as e:
            logger.error(f"Erreur commande {' '.join(cmd)}: {e}")
            return 1, "", str(e)

    def get_outdated_packages(self) -> dict:
        """Récupère les packages obsolètes"""
        logger.info("🔍 Analyse des packages obsolètes...")

        returncode, stdout, stderr = self.run_command(
            ["pip", "list", "--outdated", "--format=json"]
        )

        if returncode != 0:
            logger.error(f"Erreur pip list: {stderr}")
            return {}

        try:
            outdated = json.loads(stdout)
            logger.info(f"📦 {len(outdated)} packages obsolètes trouvés")
            return outdated
        except json.JSONDecodeError:
            logger.error("Erreur parsing JSON pip list")
            return {}

    def get_unused_packages(self) -> list:
        """Récupère les packages potentiellement inutilisés"""
        logger.info("🔍 Analyse des packages inutilisés...")

        # Utiliser pip-autoremove pour détecter les packages inutilisés
        returncode, stdout, stderr = self.run_command(["pip-autoremove", "--list"])

        if returncode != 0:
            logger.warning(f"pip-autoremove échoué: {stderr}")
            return []

        # Parser la sortie de pip-autoremove
        unused = []
        for line in stdout.strip().split("\n"):
            if line.strip() and not line.startswith("#"):
                package = line.strip()
                if package not in self.critical_packages:
                    unused.append(package)

        logger.info(f"📦 {len(unused)} packages potentiellement inutilisés")
        return unused

    def get_security_vulnerabilities(self) -> dict:
        """Récupère les vulnérabilités de sécurité"""
        logger.info("🔍 Analyse des vulnérabilités de sécurité...")

        returncode, stdout, stderr = self.run_command(["pip-audit", "--format=json"])

        if returncode != 0:
            logger.warning(f"pip-audit échoué: {stderr}")
            return {}

        try:
            vulns = json.loads(stdout)
            logger.info(f"🔒 {len(vulns.get('dependencies', []))} packages analysés")
            return vulns
        except json.JSONDecodeError:
            logger.error("Erreur parsing JSON pip-audit")
            return {}

    def analyze_dependencies(self) -> dict:
        """Analyse complète des dépendances"""
        logger.info("🚀 Analyse complète des dépendances...")

        analysis = {
            "timestamp": datetime.now().isoformat(),
            "outdated_packages": self.get_outdated_packages(),
            "unused_packages": self.get_unused_packages(),
            "security_vulnerabilities": self.get_security_vulnerabilities(),
            "recommendations": [],
        }

        # Générer des recommandations
        self._generate_recommendations(analysis)

        return analysis

    def _generate_recommendations(self, analysis: dict):
        """Génère des recommandations d'optimisation"""
        recommendations = []

        # Recommandations pour les packages obsolètes
        outdated = analysis["outdated_packages"]
        if outdated:
            recommendations.append(
                {
                    "type": "outdated",
                    "priority": "medium",
                    "message": f"Mettre à jour {len(outdated)} packages obsolètes",
                    "packages": [pkg["name"] for pkg in outdated[:5]],  # Top 5
                }
            )

        # Recommandations pour les packages inutilisés
        unused = analysis["unused_packages"]
        if unused:
            recommendations.append(
                {
                    "type": "unused",
                    "priority": "low",
                    "message": (
                        f"Considérer la suppression de {len(unused)} packages inutilisés"
                    ),
                    "packages": unused[:5],  # Top 5
                }
            )

        # Recommandations de sécurité
        vulns = analysis["security_vulnerabilities"]
        if vulns and "dependencies" in vulns:
            vulnerable_packages = [
                dep for dep in vulns["dependencies"] if dep.get("vulns", [])
            ]
            if vulnerable_packages:
                recommendations.append(
                    {
                        "type": "security",
                        "priority": "high",
                        "message": (
                            f"Corriger {len(vulnerable_packages)} vulnérabilités de sécurité"
                        ),
                        "packages": [pkg["name"] for pkg in vulnerable_packages],
                    }
                )

        analysis["recommendations"] = recommendations

    def save_analysis(self, analysis: dict):
        """Sauvegarde l'analyse dans des fichiers"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Sauvegarde JSON complète
        json_file = self.reports_dir / f"dependency-analysis-{timestamp}.json"
        with open(json_file, "w") as f:
            json.dump(analysis, f, indent=2)
        logger.info(f"📄 Analyse sauvegardée: {json_file}")

        # Sauvegarde rapport markdown
        md_file = self.reports_dir / f"dependency-report-{timestamp}.md"
        self._generate_markdown_report(analysis, md_file)
        logger.info(f"📄 Rapport sauvegardé: {md_file}")

    def _generate_markdown_report(self, analysis: dict, output_file: Path):
        """Génère un rapport markdown"""
        with open(output_file, "w") as f:
            f.write("# Rapport d'Analyse des Dépendances\n\n")
            f.write(f"**Date:** {analysis['timestamp']}\n\n")

            # Packages obsolètes
            f.write("## 📦 Packages Obsolètes\n\n")
            if analysis["outdated_packages"]:
                f.write("| Package | Version Actuelle | Version Latest | Type |\n")
                f.write("|---------|------------------|----------------|------|\n")
                for pkg in analysis["outdated_packages"][:10]:  # Top 10
                    f.write(
                        f"| {pkg['name']} | {pkg['version']} | {pkg['latest_version']} | {pkg.get('type', 'wheel')} |\n"
                    )
            else:
                f.write("✅ Aucun package obsolète détecté\n\n")

            # Packages inutilisés
            f.write("\n## 🗑️ Packages Potentiellement Inutilisés\n\n")
            if analysis["unused_packages"]:
                f.write("```\n")
                for pkg in analysis["unused_packages"]:
                    f.write(f"{pkg}\n")
                f.write("```\n")
            else:
                f.write("✅ Aucun package inutilisé détecté\n\n")

            # Vulnérabilités
            f.write("\n## 🔒 Vulnérabilités de Sécurité\n\n")
            vulns = analysis["security_vulnerabilities"]
            if vulns and "dependencies" in vulns:
                vulnerable = [
                    dep for dep in vulns["dependencies"] if dep.get("vulns", [])
                ]
                if vulnerable:
                    f.write(f"⚠️ {len(vulnerable)} packages avec des vulnérabilités\n\n")
                    for dep in vulnerable[:5]:  # Top 5
                        f.write(f"**{dep['name']}** ({dep['version']})\n")
                        for vuln in dep["vulns"][:2]:  # Top 2 vulns par package
                            f.write(
                                f"- {vuln.get('id', 'N/A')}: {vuln.get('description', 'N/A')[:100]}...\n"
                            )
                        f.write("\n")
                else:
                    f.write("✅ Aucune vulnérabilité détectée\n\n")
            else:
                f.write("✅ Aucune vulnérabilité détectée\n\n")

            # Recommandations
            f.write("\n## 💡 Recommandations\n\n")
            for rec in analysis["recommendations"]:
                priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(
                    rec["priority"], "⚪"
                )
                f.write(
                    f"{priority_emoji} **{rec['priority'].upper()}**: {rec['message']}\n"
                )
                if "packages" in rec:
                    f.write(f"   - Packages: {', '.join(rec['packages'])}\n")
                f.write("\n")

    def optimize(self, dry_run: bool = True):
        """Optimise les dépendances"""
        logger.info("🚀 Optimisation des dépendances...")

        # Analyser les dépendances
        analysis = self.analyze_dependencies()

        # Sauvegarder l'analyse
        self.save_analysis(analysis)

        # Afficher le résumé
        self._print_summary(analysis)

        if not dry_run:
            logger.info("⚠️  Mode exécution - les modifications seront appliquées")
            # Ici on pourrait implémenter les mises à jour automatiques
        else:
            logger.info("🔍 Mode simulation - aucune modification appliquée")

    def _print_summary(self, analysis: dict):
        """Affiche un résumé de l'analyse"""
        logger.info("=" * 60)
        logger.info("📊 RÉSUMÉ DE L'ANALYSE DES DÉPENDANCES")
        logger.info("=" * 60)

        outdated = len(analysis["outdated_packages"])
        unused = len(analysis["unused_packages"])
        vulns = len(
            [
                d
                for d in analysis["security_vulnerabilities"].get("dependencies", [])
                if d.get("vulns")
            ]
        )

        logger.info(f"📦 Packages obsolètes: {outdated}")
        logger.info(f"🗑️  Packages inutilisés: {unused}")
        logger.info(f"🔒 Packages vulnérables: {vulns}")
        logger.info(f"💡 Recommandations: {len(analysis['recommendations'])}")

        # Afficher les recommandations prioritaires
        high_priority = [
            r for r in analysis["recommendations"] if r["priority"] == "high"
        ]
        if high_priority:
            logger.info("\n🔴 RECOMMANDATIONS PRIORITAIRES:")
            for rec in high_priority:
                logger.info(f"  - {rec['message']}")


def main():
    """Fonction principale"""
    import argparse

    parser = argparse.ArgumentParser(description="Optimisation des dépendances Athalia")
    parser.add_argument(
        "--project-root", type=Path, default=Path.cwd(), help="Racine du projet"
    )
    parser.add_argument(
        "--dry-run", action="store_true", default=True, help="Mode simulation (défaut)"
    )
    parser.add_argument(
        "--execute", action="store_true", help="Exécuter les optimisations (dangereux)"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Mode verbeux")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Vérifier que nous sommes dans le bon répertoire
    if not (args.project_root / "pyproject.toml").exists():
        logger.error("❌ pyproject.toml non trouvé - mauvais répertoire de projet")
        sys.exit(1)

    # Créer l'optimiseur
    optimizer = DependencyOptimizer(args.project_root)

    # Exécuter l'optimisation
    try:
        optimizer.optimize(dry_run=not args.execute)
    except KeyboardInterrupt:
        logger.info("⏹️  Optimisation interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Erreur fatale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

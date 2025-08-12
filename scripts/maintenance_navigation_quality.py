#!/usr/bin/env python3
"""
🔗 Maintenance Automatique de la Qualité de Navigation - Documentation Athalia
Maintient automatiquement la qualité de navigation à 80+/100
"""

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import schedule


class NavigationQualityMaintainer:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.maintenance_log = self.workspace / "navigation_maintenance.log"
        self.quality_threshold = 80.0
        self.critical_links_threshold = 5

    def log_maintenance(self, message, level="INFO"):
        """Enregistre les actions de maintenance"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.maintenance_log, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f"[{level}] {message}")

    def run_navigation_test(self):
        """Exécute le test de navigation"""
        try:
            result = subprocess.run(
                ["python", "scripts/test_navigation_quality_smart.py"],
                capture_output=True,
                text=True,
                cwd=self.workspace,
            )

            if result.returncode == 0:
                return self.parse_navigation_results()
            else:
                self.log_maintenance(
                    f"Erreur lors du test de navigation: {result.stderr}", "ERROR"
                )
                return None

        except Exception as e:
            self.log_maintenance(f"Erreur lors de l'exécution du test: {e}", "ERROR")
            return None

    def parse_navigation_results(self):
        """Parse les résultats du test de navigation"""
        try:
            with open(self.workspace / "navigation_test_smart_results.json") as f:
                data = json.load(f)

            return {
                "score": data.get("navigation_score", 0),
                "critical_links": data.get("critical_broken_links", 0),
                "total_links": data.get("total_broken_links", 0),
                "files_tested": data.get("files_tested", 0),
                "success_rate": data.get("link_success_rate", 0),
            }
        except Exception as e:
            self.log_maintenance(f"Erreur lors du parsing des résultats: {e}", "ERROR")
            return None

    def check_quality_status(self, navigation_results):
        """Vérifie le statut de la qualité de navigation"""
        if not navigation_results:
            return "ERROR", "Impossible de récupérer les résultats"

        score = navigation_results["score"]
        critical_links = navigation_results["critical_links"]

        if (
            score >= self.quality_threshold
            and critical_links <= self.critical_links_threshold
        ):
            return (
                "GOOD",
                f"Qualité excellente: {score}/100, {critical_links} liens critiques",
            )
        elif score >= 75.0 and critical_links <= 10:
            return (
                "WARNING",
                f"Qualité acceptable: {score}/100, {critical_links} liens critiques",
            )
        else:
            return (
                "CRITICAL",
                f"Qualité dégradée: {score}/100, {critical_links} liens critiques",
            )

    def run_auto_cleanup(self):
        """Exécute le nettoyage automatique si nécessaire"""
        try:
            self.log_maintenance("Exécution du nettoyage automatique...")

            result = subprocess.run(
                ["python", "scripts/auto_cleanup_obsolete_files.py", "--dry-run"],
                capture_output=True,
                text=True,
                cwd=self.workspace,
            )

            if result.returncode == 0:
                self.log_maintenance("Nettoyage automatique terminé avec succès")
                return True
            else:
                self.log_maintenance(
                    f"Erreur lors du nettoyage: {result.stderr}", "ERROR"
                )
                return False

        except Exception as e:
            self.log_maintenance(f"Erreur lors du nettoyage automatique: {e}", "ERROR")
            return False

    def generate_maintenance_report(self, navigation_results, quality_status):
        """Génère un rapport de maintenance"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "navigation_quality": navigation_results,
            "quality_status": quality_status,
            "maintenance_actions": [],
            "recommendations": [],
        }

        # Recommandations basées sur la qualité
        if quality_status[0] == "CRITICAL":
            report["recommendations"].append(
                "Exécuter le nettoyage automatique immédiatement"
            )
            report["recommendations"].append("Vérifier manuellement les liens cassés")
            report["recommendations"].append("Supprimer les fichiers obsolètes")

        elif quality_status[0] == "WARNING":
            report["recommendations"].append("Planifier un nettoyage dans les 24h")
            report["recommendations"].append("Surveiller la tendance de dégradation")

        else:
            report["recommendations"].append("Maintenir la qualité actuelle")
            report["recommendations"].append("Surveillance hebdomadaire suffisante")

        return report

    def save_maintenance_report(self, report):
        """Sauvegarde le rapport de maintenance"""
        report_file = (
            self.workspace
            / f"maintenance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        self.log_maintenance(f"Rapport de maintenance sauvegardé: {report_file}")

    def display_maintenance_summary(self, navigation_results, quality_status, report):
        """Affiche un résumé de la maintenance"""
        print("\n" + "=" * 60)
        print("🔗 RÉSUMÉ DE LA MAINTENANCE AUTOMATIQUE")
        print("=" * 60)

        if navigation_results:
            print(f"🎯 Score de navigation : {navigation_results['score']}/100")
            print(f"🔗 Liens critiques cassés : {navigation_results['critical_links']}")
            print(f"📁 Fichiers testés : {navigation_results['files_tested']}")
            print(f"📈 Taux de succès : {navigation_results['success_rate']:.1f}%")

        print(f"\n📊 Statut de qualité : {quality_status[0]}")
        print(f"💡 Message : {quality_status[1]}")

        print("\n💡 Recommandations :")
        for rec in report["recommendations"]:
            print(f"  • {rec}")

        print("\n✅ Maintenance terminée !")

    def run_maintenance(self):
        """Exécute la maintenance complète"""
        self.log_maintenance(
            "🚀 Démarrage de la maintenance automatique de la qualité de navigation..."
        )

        # 1. Test de navigation
        navigation_results = self.run_navigation_test()

        # 2. Vérification de la qualité
        quality_status = self.check_quality_status(navigation_results)

        # 3. Actions de maintenance si nécessaire
        if quality_status[0] == "CRITICAL":
            self.log_maintenance(
                "🚨 Qualité critique détectée, exécution du nettoyage automatique..."
            )
            self.run_auto_cleanup()

        # 4. Génération du rapport
        report = self.generate_maintenance_report(navigation_results, quality_status)

        # 5. Sauvegarde du rapport
        self.save_maintenance_report(report)

        # 6. Affichage du résumé
        self.display_maintenance_summary(navigation_results, quality_status, report)

        return quality_status[0] != "ERROR"

    def schedule_maintenance(self):
        """Planifie la maintenance automatique"""
        # Maintenance quotidienne à 9h00
        schedule.every().day.at("09:00").do(self.run_maintenance)

        # Maintenance hebdomadaire le dimanche à 14h00
        schedule.every().sunday.at("14:00").do(self.run_maintenance)

        # Maintenance d'urgence si la qualité se dégrade
        schedule.every(6).hours.do(self.check_emergency_maintenance)

        self.log_maintenance(
            "📅 Maintenance planifiée : quotidienne à 9h00, hebdomadaire le dimanche à 14h00"
        )

    def check_emergency_maintenance(self):
        """Vérifie si une maintenance d'urgence est nécessaire"""
        navigation_results = self.run_navigation_test()
        if navigation_results:
            quality_status = self.check_quality_status(navigation_results)
            if quality_status[0] == "CRITICAL":
                self.log_maintenance(
                    "🚨 MAINTENANCE D'URGENCE DÉCLENCHÉE !", "CRITICAL"
                )
                self.run_maintenance()

    def run_scheduled_maintenance(self):
        """Exécute la maintenance planifiée"""
        self.log_maintenance("🔄 Démarrage de la maintenance planifiée...")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Vérifier toutes les minutes

        except KeyboardInterrupt:
            self.log_maintenance(
                "⚠️ Maintenance planifiée interrompue par l'utilisateur"
            )
        except Exception as e:
            self.log_maintenance(
                f"❌ Erreur lors de la maintenance planifiée: {e}", "ERROR"
            )


def main():
    """Fonction principale"""
    maintainer = NavigationQualityMaintainer()

    # Vérifier les arguments
    if "--schedule" in sys.argv or "-s" in sys.argv:
        # Mode planifié
        maintainer.schedule_maintenance()
        maintainer.run_scheduled_maintenance()
    else:
        # Mode exécution unique
        try:
            success = maintainer.run_maintenance()
            sys.exit(0 if success else 1)

        except KeyboardInterrupt:
            print("\n⚠️ Maintenance interrompue par l'utilisateur")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Erreur lors de la maintenance: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()

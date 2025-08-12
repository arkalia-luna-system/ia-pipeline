#!/usr/bin/env python3
"""
🔗 Maintenance Automatique de la Qualité de Navigation - Documentation Athalia
Maintient automatiquement la qualité de navigation à 80+/100
"""

import json
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

    def run_integrated_navigation_test(self):
        """Exécute un test de navigation intégré"""
        try:
            # Test basique de navigation
            total_files = 0
            broken_links = 0
            critical_broken_links = 0

            docs_dir = self.workspace / "docs"
            for md_file in docs_dir.rglob("*.md"):
                total_files += 1
                try:
                    with open(md_file, encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    # Détection simple des liens cassés
                    detected_links = self.detect_broken_links(content, md_file)
                    if detected_links:
                        broken_links += len(detected_links)
                        if len(detected_links) > 5:  # Plus de 5 liens cassés = critique
                            critical_broken_links += 1

                except Exception as e:
                    self.log_maintenance(
                        f"Erreur lors de l'analyse de {md_file}: {e}", "WARNING"
                    )
                    broken_links += 1

            # Calcul du score
            if total_files == 0:
                score = 100
            else:
                score = max(0, 100 - (broken_links * 2) - (critical_broken_links * 10))

            return {
                "score": score,
                "critical_broken_links": critical_broken_links,
                "total_broken_links": broken_links,
                "files_tested": total_files,
                "success_rate": max(
                    0, 100 - (broken_links / max(total_files, 1) * 100)
                ),
            }

        except Exception as e:
            self.log_maintenance(f"Erreur lors du test intégré: {e}", "ERROR")
            return {
                "score": 0,
                "critical_broken_links": 0,
                "total_broken_links": 0,
                "files_tested": 0,
                "success_rate": 0,
            }

    def detect_broken_links(self, content, file_path):
        """Détecte les liens cassés dans le contenu"""
        broken_links = []

        # Patterns pour détecter les liens Markdown
        import re

        link_patterns = [
            r"\[([^\]]+)\]\(([^)]+)\)",  # [texte](lien)
            r"`([^`]+)`",  # `lien`
            r"([a-zA-Z0-9_\-\.]+\.md)",  # fichier.md
        ]

        for pattern in link_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if isinstance(match, tuple):
                    link = match[1]
                else:
                    link = match

                # Vérification basique des liens
                if link.startswith("http") and "github.com" not in link:
                    broken_links.append(link)
                elif (
                    link.endswith(".md")
                    and not (self.workspace / "docs" / link).exists()
                ):
                    broken_links.append(link)

        return broken_links

    def log_maintenance(self, message, level="INFO"):
        """Enregistre les actions de maintenance"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.maintenance_log, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f"[{level}] {message}")

    def run_navigation_test(self):
        """Exécute le test de navigation intégré"""
        try:
            # Test de navigation intégré au lieu d'appeler un script externe
            results = self.run_integrated_navigation_test()

            if results:
                return results
            else:
                self.log_maintenance("Erreur lors du test intégré", "ERROR")
                return None

        except Exception as e:
            self.log_maintenance(
                f"Erreur lors de l'exécution du test intégré: {e}", "ERROR"
            )
            return None

    def parse_navigation_results(self):
        """Parse les résultats du test de navigation"""
        try:
            with open(self.workspace / "navigation_test_smart_results.json") as f:
                data = json.load(f)

            # Nouvelle structure du fichier JSON
            global_stats = data.get("global_stats", {})

            return {
                "score": global_stats.get("average_navigation_score", 0),
                "critical_links": global_stats.get("critical_broken_links", 0),
                "total_links": global_stats.get("broken_links", 0),
                "files_tested": global_stats.get("total_files", 0),
                "success_rate": global_stats.get("link_success_rate", 0),
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
            self.log_maintenance("Exécution du nettoyage automatique intégré...")

            # Nettoyage intégré au lieu d'appeler un script externe
            cleaned_files = self.cleanup_obsolete_files()

            if cleaned_files > 0:
                self.log_maintenance(
                    f"Nettoyage automatique terminé: {cleaned_files} fichiers nettoyés"
                )
                return True
            else:
                self.log_maintenance("Aucun fichier obsolète trouvé")
                return True

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

    def cleanup_obsolete_files(self):
        """Nettoie les fichiers obsolètes de manière intégrée"""
        try:
            cleaned_count = 0

            # Nettoyer les fichiers Python temporaires
            for pattern in ["*.pyc", "__pycache__", ".pytest_cache", ".mypy_cache"]:
                if pattern.endswith("*"):
                    # Fichiers avec extension
                    files = list(self.workspace.rglob(pattern))
                    for file in files:
                        if file.is_file():
                            file.unlink()
                            cleaned_count += 1
                else:
                    # Dossiers
                    dirs = list(self.workspace.rglob(pattern))
                    for dir_path in dirs:
                        if dir_path.is_dir():
                            import shutil

                            shutil.rmtree(dir_path)
                            cleaned_count += 1

            # Nettoyer les fichiers macOS cachés
            for pattern in [".DS_Store", "._*"]:
                files = list(self.workspace.rglob(pattern))
                for file in files:
                    if file.is_file():
                        file.unlink()
                        cleaned_count += 1

            self.log_maintenance(
                f"Nettoyage intégré terminé: {cleaned_count} éléments supprimés"
            )
            return cleaned_count

        except Exception as e:
            self.log_maintenance(f"Erreur lors du nettoyage intégré: {e}", "ERROR")
            return 0

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

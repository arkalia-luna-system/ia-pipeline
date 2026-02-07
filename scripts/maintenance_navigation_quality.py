#!/usr/bin/env python3
"""
🔗 Maintenance Automatique de la Qualité de Navigation - Documentation Athalia
Maintient automatiquement la qualité de navigation à 80+/100
"""

import json
import logging
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Ajouter le répertoire parent au path pour importer athalia_core
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import schedule  # type: ignore[import-untyped]
except ImportError:
    schedule = None  # optionnel : pip install schedule pour tâches récurrentes

from athalia_core.analysis.architecture_analyzer import ArchitectureAnalyzer

logger = logging.getLogger(__name__)


class NavigationQualityMaintainer:
    def __init__(self):
        self.workspace = Path(__file__).parent.parent
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
        """Exécute le nettoyage automatique sécurisé si nécessaire"""
        try:
            self.log_maintenance("Exécution du nettoyage automatique sécurisé...")

            # Nettoyage sécurisé des fichiers système
            cleaned_files = self.secure_cleanup_system_files()

            if cleaned_files:
                self.log_maintenance(
                    f"Nettoyage sécurisé terminé: {len(cleaned_files)} fichiers nettoyés"
                )
                return True
            else:
                self.log_maintenance("Aucun fichier à nettoyer")
                return True

        except Exception as e:
            self.log_maintenance(
                f"Erreur lors du nettoyage automatique sécurisé: {e}", "ERROR"
            )
            return False

    def secure_cleanup_system_files(self):
        """Nettoyage sécurisé des fichiers système uniquement"""
        cleaned_files = []

        try:
            # 1. Fichiers Apple Double (.DS_Store, ._*)
            apple_double_patterns = [".DS_Store", "._*"]
            for pattern in apple_double_patterns:
                for file_path in self.workspace.rglob(pattern):
                    if file_path.is_file():
                        try:
                            # Vérification que c'est bien un fichier système
                            if self.is_safe_to_delete(file_path):
                                file_path.unlink()
                                cleaned_files.append(
                                    str(file_path.relative_to(self.workspace))
                                )
                                self.log_maintenance(
                                    f"Fichier système supprimé: {file_path.name}"
                                )
                        except Exception as e:
                            self.log_maintenance(
                                f"Impossible de supprimer {file_path}: {e}", "WARNING"
                            )

            # 2. Fichiers de cache Python
            cache_patterns = ["__pycache__", "*.pyc", "*.pyo"]
            for pattern in cache_patterns:
                if pattern == "__pycache__":
                    for cache_dir in self.workspace.rglob(pattern):
                        if cache_dir.is_dir():
                            try:
                                import shutil

                                shutil.rmtree(cache_dir)
                                cleaned_files.append(
                                    str(cache_dir.relative_to(self.workspace))
                                )
                                self.log_maintenance(
                                    f"Dossier cache supprimé: {cache_dir.name}"
                                )
                            except Exception as e:
                                self.log_maintenance(
                                    f"Impossible de supprimer {cache_dir}: {e}",
                                    "WARNING",
                                )
                else:
                    for cache_file in self.workspace.rglob(pattern):
                        if cache_file.is_file():
                            try:
                                if self.is_safe_to_delete(cache_file):
                                    cache_file.unlink()
                                    cleaned_files.append(
                                        str(cache_file.relative_to(self.workspace))
                                    )
                                    self.log_maintenance(
                                        f"Fichier cache supprimé: {cache_file.name}"
                                    )
                            except Exception as e:
                                self.log_maintenance(
                                    f"Impossible de supprimer {cache_file}: {e}",
                                    "WARNING",
                                )

            # 3. Fichiers temporaires de navigation
            temp_files = ["navigation_test_*.json", "maintenance_report_*.json"]
            for pattern in temp_files:
                for temp_file in self.workspace.glob(pattern):
                    if temp_file.is_file():
                        try:
                            # Vérification de l'âge du fichier (plus de 7 jours)
                            if self.is_old_temp_file(temp_file, days=7):
                                if self.is_safe_to_delete(temp_file):
                                    temp_file.unlink()
                                    cleaned_files.append(
                                        str(temp_file.relative_to(self.workspace))
                                    )
                                    self.log_maintenance(
                                        f"Fichier temporaire supprimé: {temp_file.name}"
                                    )
                        except Exception as e:
                            self.log_maintenance(
                                f"Impossible de supprimer {temp_file}: {e}", "WARNING"
                            )

        except Exception as e:
            self.log_maintenance(f"Erreur lors du nettoyage sécurisé: {e}", "ERROR")

        return cleaned_files

    def is_safe_to_delete(self, file_path):
        """Vérifie si un fichier peut être supprimé en toute sécurité"""
        try:
            # Ne jamais supprimer de fichiers dans docs/ ou athalia_core/
            if "docs" in str(file_path) or "athalia_core" in str(file_path):
                return False

            # Ne jamais supprimer de fichiers de configuration
            if file_path.name in [
                ".gitignore",
                "requirements.txt",
                "setup.py",
                "pyproject.toml",
            ]:
                return False

            # Ne jamais supprimer de fichiers Python source
            if file_path.suffix == ".py" and "test" not in file_path.name.lower():
                return False

            # Ne jamais supprimer de fichiers de documentation
            if file_path.suffix in [".md", ".rst", ".txt"]:
                return False

            # Vérifier que c'est bien un fichier système ou cache
            safe_patterns = [
                ".DS_Store",
                "._",
                "__pycache__",
                ".pyc",
                ".pyo",
                "Thumbs.db",
            ]
            return any(pattern in file_path.name for pattern in safe_patterns)

        except Exception:
            return False

    def is_old_temp_file(self, file_path, days=7):
        """Vérifie si un fichier temporaire est ancien"""
        try:
            import time

            current_time = time.time()
            file_time = file_path.stat().st_mtime
            days_old = (current_time - file_time) / (24 * 3600)
            return days_old > days
        except Exception:
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
        """Planifie la maintenance automatique (nécessite: pip install schedule)."""
        if schedule is None:
            self.log_maintenance(
                "⚠️ Pour le mode planifié, installez: pip install schedule", "WARNING"
            )
            return
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
        """Exécute la maintenance planifiée (nécessite: pip install schedule)."""
        if schedule is None:
            self.log_maintenance(
                "⚠️ Mode planifié non disponible. Installez: pip install schedule",
                "WARNING",
            )
            return
        self.log_maintenance("🔄 Démarrage de la maintenance planifiée...")

        try:
            max_iterations = 10080  # Maximum 1 semaine (7 jours * 24h * 60min)
            iteration = 0

            while iteration < max_iterations:
                schedule.run_pending()
                time.sleep(60)  # Vérifier toutes les minutes
                iteration += 1

                # Log de progression toutes les heures
                if iteration % 60 == 0:
                    self.log_maintenance(
                        f"🔄 Maintenance planifiée en cours... (itération {iteration})"
                    )

        except KeyboardInterrupt:
            self.log_maintenance(
                "⚠️ Maintenance planifiée interrompue par l'utilisateur"
            )
        except Exception as e:
            self.log_maintenance(
                f"❌ Erreur lors de la maintenance planifiée: {e}", "ERROR"
            )
        finally:
            self.log_maintenance("🏁 Maintenance planifiée terminée")


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

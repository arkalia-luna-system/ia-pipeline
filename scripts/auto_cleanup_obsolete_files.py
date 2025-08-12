#!/usr/bin/env python3
"""
🧹 Nettoyage Automatique des Fichiers Obsolètes - Documentation Athalia
Supprime automatiquement les fichiers qui polluent la navigation
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class ObsoleteFileCleaner:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.docs_dir = self.workspace / "docs"
        self.cleanup_report_file = self.workspace / "cleanup_obsolete_files_report.json"

        # Critères de suppression
        self.obsolete_patterns = [
            r"\._",  # Fichiers Apple Double
            r"\.DS_Store",  # Fichiers macOS
            r"Thumbs\.db",  # Fichiers Windows
            r"desktop\.ini",  # Fichiers Windows
        ]

        # Fichiers avec de nombreux liens cassés (à évaluer pour suppression)
        self.high_broken_links_threshold = 10

    def identify_obsolete_files(self):
        """Identifie les fichiers obsolètes"""
        print("🔍 Identification des fichiers obsolètes...")

        obsolete_files = []

        # 1. Fichiers système et parasites
        for pattern in self.obsolete_patterns:
            for file_path in self.docs_dir.rglob(f"*{pattern}*"):
                obsolete_files.append(
                    {
                        "file": str(file_path.relative_to(self.workspace)),
                        "type": "fichier_systeme",
                        "reason": f"Pattern système: {pattern}",
                        "priority": "HAUTE",
                    }
                )

        # 2. Fichiers avec noms trop longs (problème macOS)
        for file_path in self.docs_dir.rglob("*.md"):
            if len(str(file_path)) > 200:
                obsolete_files.append(
                    {
                        "file": str(file_path.relative_to(self.workspace)),
                        "type": "nom_trop_long",
                        "reason": "Nom de fichier trop long (>200 caractères)",
                        "priority": "HAUTE",
                    }
                )

        # 3. Fichiers avec de nombreux liens cassés
        high_broken_links_files = self.identify_high_broken_links_files()
        obsolete_files.extend(high_broken_links_files)

        return obsolete_files

    def identify_high_broken_links_files(self):
        """Identifie les fichiers avec de nombreux liens cassés"""
        print("🔍 Identification des fichiers avec de nombreux liens cassés...")

        high_broken_links_files = []

        try:
            # Exécuter le test de navigation pour obtenir les métriques
            result = subprocess.run(
                ["python", "scripts/test_navigation_quality_smart.py"],
                capture_output=True,
                text=True,
                cwd=self.workspace,
            )

            if result.returncode == 0:
                # Parser les résultats pour identifier les fichiers problématiques
                navigation_results = self.parse_navigation_results()

                if navigation_results and "problematic_files" in navigation_results:
                    for file_info in navigation_results["problematic_files"]:
                        if (
                            file_info.get("severity", 0)
                            > self.high_broken_links_threshold
                        ):
                            high_broken_links_files.append(
                                {
                                    "file": file_info["file"],
                                    "type": "liens_casses_massifs",
                                    "reason": (
                                        f"{file_info['severity']} liens cassés détectés"
                                    ),
                                    "priority": "MOYENNE",
                                }
                            )

        except Exception as e:
            print(f"⚠️ Erreur lors de l'identification des fichiers à liens cassés: {e}")

        return high_broken_links_files

    def parse_navigation_results(self):
        """Parse les résultats du test de navigation"""
        try:
            with open(self.workspace / "navigation_test_smart_results.json") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Erreur lors du parsing des résultats: {e}")
            return None

    def evaluate_file_for_deletion(self, file_info):
        """Évalue si un fichier doit être supprimé"""
        file_path = self.workspace / file_info["file"]

        # Critères de suppression
        deletion_criteria = {
            "fichier_systeme": True,  # Toujours supprimer
            "nom_trop_long": True,  # Toujours supprimer
            "liens_casses_massifs": self.should_delete_broken_links_file(file_path),
        }

        return deletion_criteria.get(file_info["type"], False)

    def should_delete_broken_links_file(self, file_path):
        """Détermine si un fichier avec de nombreux liens cassés doit être supprimé"""
        try:
            # Vérifier si le fichier contient des informations utiles
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Critères pour la suppression
            if len(content) < 1000:  # Fichier très court
                return True

            # Vérifier si c'est un rapport de correction obsolète
            if "CORRECTION" in file_path.name and "2025" in file_path.name:
                return True

            # Vérifier si c'est un plan obsolète
            if "PLAN" in file_path.name and "2025" in file_path.name:
                return True

            return False

        except Exception:
            return True  # En cas d'erreur, supprimer par précaution

    def backup_file(self, file_path):
        """Sauvegarde un fichier avant suppression"""
        backup_dir = self.workspace / "backups" / "obsolete_files_cleanup"
        backup_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
        backup_path = backup_dir / backup_name

        try:
            import shutil

            shutil.copy2(file_path, backup_path)
            return str(backup_path.relative_to(self.workspace))
        except Exception as e:
            print(f"⚠️ Erreur lors de la sauvegarde de {file_path}: {e}")
            return None

    def delete_file(self, file_path):
        """Supprime un fichier de manière sécurisée"""
        try:
            # Sauvegarde avant suppression
            backup_path = self.backup_file(file_path)

            # Suppression du fichier
            file_path.unlink()

            return {
                "success": True,
                "backup_path": backup_path,
                "message": "Fichier supprimé avec succès",
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Erreur lors de la suppression",
            }

    def cleanup_obsolete_files(self, obsolete_files, dry_run=True):
        """Nettoie les fichiers obsolètes"""
        print(
            f"🧹 Nettoyage des fichiers obsolètes (Mode: {'SIMULATION' if dry_run else 'EXÉCUTION'})..."
        )

        cleanup_results = []
        files_to_delete = []

        for file_info in obsolete_files:
            if self.evaluate_file_for_deletion(file_info):
                file_path = self.workspace / file_info["file"]

                if file_path.exists():
                    files_to_delete.append(
                        {"file_info": file_info, "file_path": file_path}
                    )

        print(f"📋 {len(files_to_delete)} fichiers identifiés pour suppression")

        for file_data in files_to_delete:
            file_info = file_data["file_info"]
            file_path = file_data["file_path"]

            print(f"  • {file_info['file']} - {file_info['reason']}")

            if not dry_run:
                result = self.delete_file(file_path)
                cleanup_results.append(
                    {"file": file_info["file"], "action": "supprimé", "result": result}
                )
            else:
                cleanup_results.append(
                    {
                        "file": file_info["file"],
                        "action": "serait_supprimé",
                        "result": {
                            "success": True,
                            "message": "Simulation - fichier non supprimé",
                        },
                    }
                )

        return cleanup_results

    def generate_cleanup_report(self, obsolete_files, cleanup_results):
        """Génère un rapport de nettoyage"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_obsolete_files": len(obsolete_files),
                "files_deleted": len(
                    [r for r in cleanup_results if r["action"] == "supprimé"]
                ),
                "files_simulated": len(
                    [r for r in cleanup_results if r["action"] == "serait_supprimé"]
                ),
            },
            "obsolete_files": obsolete_files,
            "cleanup_results": cleanup_results,
            "recommendations": self.generate_recommendations(
                obsolete_files, cleanup_results
            ),
        }

        return report

    def generate_recommendations(self, obsolete_files, cleanup_results):
        """Génère des recommandations basées sur le nettoyage"""
        recommendations = []

        # Recommandations générales
        if obsolete_files:
            recommendations.append(
                {
                    "type": "NETTOYAGE",
                    "message": f"{len(obsolete_files)} fichiers obsolètes identifiés",
                    "action": "Continuer le nettoyage régulier",
                }
            )

        # Recommandations spécifiques
        high_priority_files = [f for f in obsolete_files if f["priority"] == "HAUTE"]
        if high_priority_files:
            recommendations.append(
                {
                    "type": "URGENT",
                    "message": f"{len(high_priority_files)} fichiers haute priorité",
                    "action": "Supprimer immédiatement",
                }
            )

        return recommendations

    def save_report(self, report):
        """Sauvegarde le rapport de nettoyage"""
        with open(self.cleanup_report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"💾 Rapport sauvegardé dans {self.cleanup_report_file}")

    def display_summary(self, report):
        """Affiche un résumé du nettoyage"""
        print("\n" + "=" * 60)
        print("🧹 RÉSUMÉ DU NETTOYAGE AUTOMATIQUE")
        print("=" * 60)

        print(
            f"📁 Fichiers obsolètes identifiés : {report['summary']['total_obsolete_files']}"
        )
        print(f"🗑️ Fichiers supprimés : {report['summary']['files_deleted']}")
        print(f"🔍 Fichiers simulés : {report['summary']['files_simulated']}")

        print("\n💡 Recommandations :")
        for rec in report["recommendations"]:
            print(f"  • {rec['type']} : {rec['message']} - {rec['action']}")

        print("\n✅ Nettoyage terminé !")

    def run_cleanup(self, dry_run=True):
        """Exécute le nettoyage complet"""
        print("🚀 Démarrage du nettoyage automatique des fichiers obsolètes...")
        print("=" * 60)

        # 1. Identification des fichiers obsolètes
        obsolete_files = self.identify_obsolete_files()

        if not obsolete_files:
            print("✅ Aucun fichier obsolète identifié")
            return True

        # 2. Nettoyage des fichiers
        cleanup_results = self.cleanup_obsolete_files(obsolete_files, dry_run)

        # 3. Génération du rapport
        report = self.generate_cleanup_report(obsolete_files, cleanup_results)

        # 4. Sauvegarde du rapport
        self.save_report(report)

        # 5. Affichage du résumé
        self.display_summary(report)

        return True


def main():
    """Fonction principale"""
    cleaner = ObsoleteFileCleaner()

    # Vérifier les arguments
    dry_run = "--dry-run" in sys.argv or "-d" in sys.argv

    try:
        success = cleaner.run_cleanup(dry_run=dry_run)
        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\n⚠️ Nettoyage interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

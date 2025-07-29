#!/usr/bin/env python3
"""
Script de monitoring système pour Athalia
Surveille les performances, l'espace disque, et l'état des processus
"""

import os
import psutil
import json
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SystemMonitor:
    """Moniteur système pour Athalia"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.monitoring_data = {}

    def get_system_info(self):
        """Récupère les informations système"""
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage(self.project_path).percent,
            "timestamp": datetime.now().isoformat()
        }

    def get_project_stats(self):
        """Récupère les statistiques du projet"""
        stats = {
            "total_files": 0,
            "python_files": 0,
            "data_files": 0,
            "log_files": 0,
            "backup_files": 0
        }

        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                stats["total_files"] += 1
                if file.endswith('.py'):
                    stats["python_files"] += 1
                elif file.endswith(('.json', '.db', '.csv')):
                    stats["data_files"] += 1
                elif file.endswith('.log'):
                    stats["log_files"] += 1
                elif 'backup' in root.lower():
                    stats["backup_files"] += 1

        return stats

    def check_critical_paths(self):
        """Vérifie les chemins critiques"""
        critical_paths = [
            "athalia_core/",
            "tests/",
            "docs/",
            "data/",
            "logs/",
            "requirements.txt"
        ]

        status = {}
        for path in critical_paths:
            full_path = self.project_path / path
            status[path] = {
                "exists": full_path.exists(),
                "size": full_path.stat().st_size if full_path.exists() else 0
            }

        return status

    def generate_report(self):
        """Génère un rapport complet"""
        report = {
            "system": self.get_system_info(),
            "project": self.get_project_stats(),
            "paths": self.check_critical_paths()
        }

        return report

    def save_report(self, report: dict):
        """Sauvegarde le rapport"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.project_path / "data" / "reports" / f"system_monitor_{timestamp}.json"
        
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"📊 Rapport système sauvegardé: {report_file}")
        return report_file

    def monitor(self):
        """Exécute le monitoring complet"""
        logger.info("🔍 Démarrage du monitoring système...")
        
        report = self.generate_report()
        report_file = self.save_report(report)
        
        # Affichage des alertes
        if report["system"]["cpu_percent"] > 80:
            logger.warning("⚠️ Utilisation CPU élevée!")
        
        if report["system"]["memory_percent"] > 80:
            logger.warning("⚠️ Utilisation mémoire élevée!")
        
        if report["system"]["disk_usage"] > 90:
            logger.warning("⚠️ Espace disque critique!")
        
        logger.info("✅ Monitoring terminé")
        return report


def main():
    """Fonction principale"""
    monitor = SystemMonitor()
    report = monitor.monitor()
    
    print("\n📊 RAPPORT SYSTÈME:")
    print(f"CPU: {report['system']['cpu_percent']}%")
    print(f"Mémoire: {report['system']['memory_percent']}%")
    print(f"Disque: {report['system']['disk_usage']}%")
    print(f"Fichiers Python: {report['project']['python_files']}")
    print(f"Fichiers de données: {report['project']['data_files']}")


if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Script de suivi de progression CI/CD professionnelle
Gère les métriques et rapports de progression
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class CIProgressTracker:
    """Gestionnaire de progression CI/CD professionnelle"""

    def __init__(self, progress_file: str = "ci_progress.json"):
        self.progress_file = progress_file
        self.metrics = self._load_metrics()

    def _load_metrics(self) -> Dict[str, Any]:
        """Charge les métriques existantes"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Erreur chargement métriques: {e}")
        
        # Métriques par défaut
        default_metrics: Dict[str, Any] = {
            "level": 1,
            "status": "not_started",
            "tests_passed": "none",
            "security_score": 0,
            "performance_score": 0,
            "coverage": 0,
            "last_update": datetime.now().isoformat(),
            "next_level": "basic",
            "branch": "ci-cd-professional",
            "actor": "unknown"
        }
        return default_metrics

    def update_metrics(self, level: int, results: Dict[str, Any]) -> None:
        """Met à jour les métriques après chaque niveau"""
        self.metrics.update({
            "level": level,
            "status": results.get("status", "unknown"),
            "tests_passed": results.get("tests_passed", "unknown"),
            "security_score": results.get("security_score", 0),
            "performance_score": results.get("performance_score", 0),
            "coverage": results.get("coverage", 0),
            "last_update": datetime.now().isoformat(),
            "next_level": self._get_next_level(level),
            "branch": results.get("branch", "ci-cd-professional"),
            "actor": results.get("actor", "unknown")
        })
        
        # Sauvegarder les métriques
        self._save_metrics()

    def _get_next_level(self, current_level: int) -> str:
        """Détermine le prochain niveau"""
        levels = {
            1: "security",
            2: "performance", 
            3: "multi-env",
            4: "deployment",
            5: "production"
        }
        return levels.get(current_level, "completed")

    def _save_metrics(self) -> None:
        """Sauvegarde les métriques"""
        try:
            with open(self.progress_file, "w", encoding="utf-8") as f:
                json.dump(self.metrics, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Erreur sauvegarde métriques: {e}")

    def generate_report(self) -> str:
        """Génère un rapport de progression"""
        level_names = {
            1: "Tests de Base",
            2: "Tests de Sécurité", 
            3: "Tests de Performance",
            4: "Multi-Environnement",
            5: "Déploiement Continu"
        }
        
        current_level = self.metrics["level"]
        level_name = level_names.get(current_level, "Inconnu")
        
        report = f"""
# 📊 RAPPORT DE PROGRESSION CI/CD PRO

## 🎯 Niveau Actuel: {current_level}/5 - {level_name}

### 📈 Métriques:
- **Status:** {self.metrics['status']}
- **Tests passants:** {self.metrics['tests_passed']}
- **Score sécurité:** {self.metrics['security_score']}/100
- **Score performance:** {self.metrics['performance_score']}/100
- **Couverture:** {self.metrics['coverage']}%

### 🚀 Prochaines étapes:
- **Niveau {current_level + 1}:** {self._get_next_level(current_level).title() if current_level < 5 else "Finalisation"}

### 📅 Dernière mise à jour: {self.metrics['last_update']}
### 🌿 Branche: {self.metrics['branch']}
### 👤 Acteur: {self.metrics['actor']}

### 📋 Progression par niveau:
"""
        
        for level in range(1, 6):
            status = "✅" if level <= current_level else "⏳"
            report += f"- **Niveau {level}:** {level_names.get(level, 'Inconnu')} {status}\n"
        
        if current_level == 5:
            report += """
### 🏆 FÉLICITATIONS !
Tu as atteint le niveau maximum de CI/CD professionnel !
Prêt pour la migration vers develop/main.
"""
        
        return report

    def get_level_status(self, level: int) -> Dict[str, Any]:
        """Obtient le statut d'un niveau spécifique"""
        if level > self.metrics["level"]:
            return {
                "status": "pending",
                "message": f"Niveau {level} en attente"
            }
        elif level == self.metrics["level"]:
            return {
                "status": "current",
                "message": f"Niveau {level} en cours"
            }
        else:
            return {
                "status": "completed",
                "message": f"Niveau {level} terminé"
            }

    def export_metrics(self, output_file: str) -> bool:
        """Exporte les métriques vers un fichier"""
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(self.metrics, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Erreur export métriques: {e}")
            return False


def main() -> None:
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Suivi de progression CI/CD professionnelle")
    parser.add_argument(
        "action", choices=["report", "update", "status", "export"], 
        help="Action à effectuer"
    )
    parser.add_argument("--level", type=int, help="Niveau pour l'action")
    parser.add_argument("--file", default="ci_progress.json", help="Fichier de métriques")
    parser.add_argument("--output", help="Fichier de sortie pour export")
    
    args = parser.parse_args()
    
    tracker = CIProgressTracker(args.file)
    
    if args.action == "report":
        print(tracker.generate_report())
    
    elif args.action == "update":
        if not args.level:
            print("❌ Niveau requis pour l'action update")
            return
        
        # Simulation de mise à jour
        results = {
            "status": "success",
            "tests_passed": f"level_{args.level}",
            "security_score": 85 if args.level >= 2 else 0,
            "performance_score": 90 if args.level >= 3 else 0,
            "coverage": 75 if args.level >= 4 else 0,
            "branch": "ci-cd-professional",
            "actor": "athalia"
        }
        
        tracker.update_metrics(args.level, results)
        print(f"✅ Métriques mises à jour pour le niveau {args.level}")
    
    elif args.action == "status":
        if not args.level:
            print("❌ Niveau requis pour l'action status")
            return
        
        status = tracker.get_level_status(args.level)
        print(f"📊 Statut niveau {args.level}: {status['message']} ({status['status']})")
    
    elif args.action == "export":
        output_file = args.output or f"ci_progress_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        if tracker.export_metrics(output_file):
            print(f"✅ Métriques exportées vers {output_file}")
        else:
            print("❌ Échec de l'export")


if __name__ == "__main__":
    main() 
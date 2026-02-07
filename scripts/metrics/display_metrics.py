#!/usr/bin/env python3
"""
Script pour afficher les métriques du projet Athalia
Utilisé dans le workflow GitHub Actions
"""

import json
import sys
from pathlib import Path


def display_metrics(metrics_file: str = "data/metrics.json"):
    """Affiche les métriques du projet de manière formatée"""

    if not Path(metrics_file).exists():
        print("❌ Fichier metrics.json non trouvé!")
        sys.exit(1)

    try:
        with open(metrics_file, encoding="utf-8") as f:
            data = json.load(f)

        summary = data.get("summary", {})
        collection_info = data.get("collection_info", {})

        print("=" * 60)
        print("📊 ATHALIA PROJECT METRICS")
        print("=" * 60)
        print(f"🕒 Generated: {collection_info.get('collection_date', 'Unknown')}")
        print(f"🐍 Python Files: {summary.get('total_python_files', 0):,}")
        print(f"📝 Lines of Code: {summary.get('lines_of_code', 0):,}")
        print(f"🧪 Tests: {summary.get('collected_tests', 0):,}")
        print(f"🛡️ Security Commands: {summary.get('security_commands', 0):,}")
        print(f"📊 HTML Dashboards: {summary.get('html_dashboards', 0):,}")
        print(f"🔧 Utility Scripts: {summary.get('utility_scripts', 0):,}")
        print(f"📚 Documentation: {summary.get('documentation_files', 0):,}")
        print("=" * 60)

    except Exception as e:
        print(f"❌ Erreur lors de la lecture des métriques: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Utiliser l'argument en ligne de commande ou le fichier par défaut
    metrics_file = sys.argv[1] if len(sys.argv) > 1 else "data/metrics.json"
    display_metrics(metrics_file)

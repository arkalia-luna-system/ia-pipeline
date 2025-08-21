#!/usr/bin/env python3
"""
Script pour créer un badge des métriques du projet.
Utilisé par le workflow GitHub Actions.
"""

import json
import sys
import urllib.parse
from pathlib import Path


def create_metrics_badge():
    """Crée un badge avec les métriques principales du projet."""

    metrics_file = Path("data/metrics.json")

    if not metrics_file.exists():
        print("❌ Fichier metrics.json non trouvé")
        sys.exit(1)

    try:
        with open(metrics_file) as f:
            data = json.load(f)

        summary = data.get("summary", {})
        python_files = summary.get("total_python_files", 0)
        lines_of_code = summary.get("lines_of_code", 0)
        tests = summary.get("collected_tests", 0)

        # Créer le texte du badge
        badge_text = (
            f"{python_files:,} modules | {lines_of_code:,} lines | {tests:,} tests"
        )

        # URL du badge
        encoded_text = urllib.parse.quote(badge_text)
        badge_url = f"https://img.shields.io/badge/Metrics-{encoded_text}-blue"

        print(f"✅ Badge créé: {badge_url}")

        # Sauvegarder pour usage ultérieur
        badge_file = Path("data/metrics_badge.txt")
        badge_file.parent.mkdir(parents=True, exist_ok=True)

        with open(badge_file, "w") as f:
            f.write(badge_url)

        print(f"💾 Badge sauvegardé dans {badge_file}")

        return badge_url

    except Exception as e:
        print(f"❌ Erreur lors de la création du badge: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_metrics_badge()

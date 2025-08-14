#!/usr/bin/env python3
import argparse
import os
import sys

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

try:
    from athalia_core.core.main import main as athalia_main
except ImportError as e:
    print(f"Erreur d'import: {e}")
    print("Vérifiez que athalia_core est installé et accessible")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Audit intelligent d'un projet Athalia/Arkalia"
    )
    parser.add_argument(
        "--project",
        type=str,
        default=".",
        help="Chemin du projet à auditer (défaut: .)",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["audit", "scan", "security"],
        default="audit",
        help="Mode d'audit (défaut: audit)",
    )

    args = parser.parse_args()

    try:
        print(f"🔍 Lancement de l'audit ATHALIA sur: {args.project}")
        print(f"📊 Mode: {args.mode}")

        # Lancer l'interface principale d'ATHALIA
        athalia_main()

    except Exception as e:
        print(f"❌ Erreur lors de l'audit: {e}")
        sys.exit(1)

    print("✅ Audit terminé avec succès")
    sys.exit(0)


if __name__ == "__main__":
    main()

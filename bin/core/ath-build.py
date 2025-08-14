#!/usr/bin/env python3
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
    try:
        print("🔨 Lancement du build ATHALIA...")
        athalia_main()
        print("✅ Build terminé avec succès")
    except Exception as e:
        print(f"❌ Erreur lors du build: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

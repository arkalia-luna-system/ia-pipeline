#!/usr/bin/env python3
"""
Script de nettoyage des fichiers Apple Double
Supprime les fichiers ._* qui causent des problèmes
"""

import os
import sys
from pathlib import Path


def cleanup_apple_double_files(directory: str = ".") -> int:
    """Nettoie les fichiers Apple Double dans le répertoire spécifié"""
    removed_count = 0
    directory_path = Path(directory)

    print(f"🔍 Recherche de fichiers Apple Double dans {directory_path.absolute()}...")

    # Rechercher tous les fichiers ._*
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.startswith("._"):
                file_path = Path(root) / file
                try:
                    file_path.unlink()
                    print(f"🗑️  Supprimé: {file_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"❌ Erreur suppression {file_path}: {e}")

    return removed_count


def main():
    """Fonction principale"""
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "."

    try:
        removed_count = cleanup_apple_double_files(directory)

        if removed_count > 0:
            print(
                f"\n✅ Nettoyage terminé: {removed_count} fichiers Apple Double "
                "supprimés"
            )
        else:
            print("\n✅ Aucun fichier Apple Double trouvé")

    except Exception as e:
        print(f"❌ Erreur lors du nettoyage: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

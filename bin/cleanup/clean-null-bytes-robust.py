#!/usr/bin/env python3
"""
Script robuste de nettoyage des octets null et fichiers Apple Double
Version améliorée avec gestion d'erreurs et validation
"""

import os
import sys


def clean_null_bytes_in_file(file_path):
    """Nettoie les octets null d'un fichier"""
    try:
        # Lire le fichier en mode binaire
        with open(file_path, "rb") as f:
            content = f.read()

        # Vérifier s'il y a des octets null
        if b"\x00" in content:
            # Supprimer les octets null
            cleaned_content = content.replace(b"\x00", b"")

            # Écrire le contenu nettoyé
            with open(file_path, "wb") as f:
                f.write(cleaned_content)

            return True
        return False
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {e}")
        return False


def remove_apple_double_files(directory):
    """Supprime les fichiers Apple Double (._*)"""
    removed_count = 0
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("._"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"🗑️  Supprimé: {file_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression de {file_path}: {e}")
    return removed_count


def clean_project_files():
    """Nettoie tous les fichiers du projet"""
    print("🧹 NETTOYAGE ROBUSTE DES OCTETS NULL ET FICHIERS APPLE DOUBLE")
    print("=" * 60)

    # Répertoires à traiter
    directories = [
        "athalia_core",
        "scripts",
        "tools",
        "bin",
        "tests",
        "config",
        "docs",
        "plugins",
    ]

    # Exclure .venv et autres répertoires système
    exclude_dirs = {".venv", ".git", "__pycache__", ".pytest_cache", "node_modules"}

    total_cleaned = 0
    total_apple_removed = 0

    for directory in directories:
        if not os.path.exists(directory):
            continue

        print(f"\n📁 Traitement de {directory}/")

        # Supprimer les fichiers Apple Double
        apple_removed = remove_apple_double_files(directory)
        total_apple_removed += apple_removed

        # Nettoyer les octets null
        for root, dirs, files in os.walk(directory):
            # Exclure les répertoires système
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if file.endswith(
                    (
                        ".py",
                        ".md",
                        ".txt",
                        ".yaml",
                        ".yml",
                        ".json",
                        ".ini",
                        ".cfg",
                        ".toml",
                    )
                ):
                    file_path = os.path.join(root, file)
                    if clean_null_bytes_in_file(file_path):
                        print(f"✨ Nettoyé: {file_path}")
                        total_cleaned += 1

    print("\n📊 RÉSUMÉ:")
    print(f"   Fichiers nettoyés (octets null): {total_cleaned}")
    print(f"   Fichiers Apple Double supprimés: {total_apple_removed}")
    print(f"   Total d'actions: {total_cleaned + total_apple_removed}")

    return total_cleaned + total_apple_removed


if __name__ == "__main__":
    try:
        actions = clean_project_files()
        if actions > 0:
            print(f"\n✅ Nettoyage terminé avec succès! {actions} actions effectuées.")
        else:
            print("\n✅ Aucun fichier à nettoyer trouvé.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n⚠️  Nettoyage interrompu par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors du nettoyage: {e}")
        sys.exit(1)

#!/usr/bin/env python3
"""
Script robuste pour nettoyer tous les octets null de tous les fichiers Python
"""

import os
import sys


def clean_null_bytes_in_file(file_path):
    """Nettoie les octets null d'un fichier"""
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        if b"\x00" in content:
            original_size = len(content)
            cleaned_content = content.replace(b"\x00", b"")
            new_size = len(cleaned_content)

            with open(file_path, "wb") as f:
                f.write(cleaned_content)

            print(f"✨ Nettoyé: {file_path} ({original_size} -> {new_size} bytes)")
            return True
        return False
    except Exception as e:
        print(f"❌ Erreur: {file_path} - {e}")
        return False


def main():
    print("🧹 NETTOYAGE COMPLET DES OCTETS NULL")
    print("=" * 50)

    # Trouver tous les fichiers Python avec octets null
    files_with_null = []
    for root, dirs, files in os.walk("."):
        # Exclure les répertoires système
        dirs[:] = [
            d
            for d in dirs
            if d
            not in {".git", ".venv", "__pycache__", ".pytest_cache", "node_modules"}
        ]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as f:
                        if b"\x00" in f.read():
                            files_with_null.append(file_path)
                except Exception:
                    continue

    if not files_with_null:
        print("✨ Aucun fichier avec octets null trouvé")
        return 0

    print(f"📋 {len(files_with_null)} fichiers avec octets null trouvés")

    cleaned = 0
    errors = 0

    for file_path in files_with_null:
        if clean_null_bytes_in_file(file_path):
            cleaned += 1
        else:
            errors += 1

    print("\n📊 Résumé:")
    print(f"  - {cleaned} fichiers nettoyés")
    print(f"  - {errors} erreurs")
    print(f"  - Total traité: {cleaned + errors}")

    return cleaned


if __name__ == "__main__":
    try:
        cleaned = main()
        if cleaned > 0:
            print(f"\n✅ Nettoyage terminé avec succès! {cleaned} fichiers nettoyés.")
        else:
            print("\n✅ Aucun fichier à nettoyer trouvé.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n⚠️  Nettoyage interrompu par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors du nettoyage: {e}")
        sys.exit(1)

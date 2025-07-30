#!/usr/bin/env python3
"""
Script pour nettoyer les bytes null des fichiers Python
"""

import os
import glob
import sys


def clean_null_bytes(file_path):
    """Nettoie les bytes null d'un fichier"""
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        if b"\x00" in content:
            original_size = len(content)
            content = content.replace(b"\x00", b"")
            new_size = len(content)

            with open(file_path, "wb") as f:
                f.write(content)

            print(f"✅ Nettoyé: {file_path} ({original_size} -> {new_size} bytes)")
            return True
        else:
            return False
    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")
        return False


def main():
    """Fonction principale"""
    patterns = [
        "athalia_core/**/*.py",
        "tests/**/*.py",
        "bin/*.py",
        "scripts/*.py",
        "tools/**/*.py",
    ]

    total_files = 0
    cleaned_files = 0

    for pattern in patterns:
        for file_path in glob.glob(pattern, recursive=True):
            total_files += 1
            if clean_null_bytes(file_path):
                cleaned_files += 1

    print(f"\n📊 RÉSUMÉ:")
    print(f"   Fichiers traités: {total_files}")
    print(f"   Fichiers nettoyés: {cleaned_files}")

    if cleaned_files > 0:
        print("✅ Nettoyage terminé avec succès!")
    else:
        print("ℹ️  Aucun fichier à nettoyer")


if __name__ == "__main__":
    main()

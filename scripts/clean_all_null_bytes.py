#!/usr/bin/env python3
"""
Script pour nettoyer tous les caractères null de tous les fichiers Python
"""

from pathlib import Path


def clean_null_bytes_in_file(file_path):
    """Nettoie les caractères null d'un fichier"""
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        # Supprimer les caractères null
        cleaned_content = content.replace(b"\x00", b"")

        if cleaned_content != content:
            with open(file_path, "wb") as f:
                f.write(cleaned_content)
            return True
        return False
    except Exception as e:
        print(f"Erreur lors du nettoyage de {file_path}: {e}")
        return False


def main():
    """Fonction principale"""
    project_root = Path.cwd()
    cleaned_count = 0

    print("🧹 NETTOYAGE COMPLET DES CARACTÈRES NULL")
    print("=" * 50)

    # Parcourir tous les fichiers Python
    for py_file in project_root.rglob("*.py"):
        if ".venv" in str(py_file):
            continue

        if clean_null_bytes_in_file(py_file):
            print(f"✅ Nettoyé: {py_file}")
            cleaned_count += 1

    print("=" * 50)
    print(f"📊 Total de fichiers nettoyés: {cleaned_count}")
    print("✅ Nettoyage terminé!")


if __name__ == "__main__":
    main()

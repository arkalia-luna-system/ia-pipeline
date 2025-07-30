#!/usr/bin/env python3
"""
Script pour identifier le fichier problématique avec des bytes null
"""

import os
import glob
import ast


def test_file(file_path):
    """Teste si un fichier peut être parsé par ast"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Test si le contenu contient des bytes null
        if "\x00" in content:
            print(f"❌ BYTES NULL DÉTECTÉS: {file_path}")
            return False

        # Test si le fichier peut être parsé
        ast.parse(content)
        return True
    except UnicodeDecodeError as e:
        print(f"❌ ERREUR D'ENCODAGE: {file_path} - {e}")
        return False
    except SyntaxError as e:
        print(f"❌ ERREUR DE SYNTAXE: {file_path} - {e}")
        return False
    except Exception as e:
        print(f"❌ ERREUR INCONNUE: {file_path} - {e}")
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
    problematic_files = 0

    for pattern in patterns:
        for file_path in glob.glob(pattern, recursive=True):
            total_files += 1
            if not test_file(file_path):
                problematic_files += 1

    print(f"\n📊 RÉSUMÉ:")
    print(f"   Fichiers testés: {total_files}")
    print(f"   Fichiers problématiques: {problematic_files}")

    if problematic_files == 0:
        print("✅ Tous les fichiers sont valides!")


if __name__ == "__main__":
    main()

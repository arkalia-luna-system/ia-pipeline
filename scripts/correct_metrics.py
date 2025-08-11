#!/usr/bin/env python3
"""
🔧 ATHALIA METRICS CORRECTOR
Script pour corriger automatiquement toutes les métriques fausses dans la documentation
"""

import os
from pathlib import Path

# Métriques correctes à appliquer partout
CORRECT_METRICS = {
    "79 modules": "153 modules",
    "79 Modules": "153 Modules",
    "79 files": "153 files",
    "79 fichiers": "153 fichiers",
    "169 fichiers": "245 fichiers",
    "169 fichiers de test": "245 fichiers de test",
    "18,446": "24,243",
    "18,446 lines": "24,243 lines",
    "18,446 Lines": "24,243 Lines",
    "18,446 lignes": "24,243 lignes",
    "scripts-9": "scripts-43",
    "9 scripts": "43 scripts",
    "9 commandes": "43 commandes",
}


def find_markdown_files() -> list[Path]:
    """Trouve tous les fichiers markdown du projet."""
    md_files = []

    # Chercher dans tous les dossiers
    for root, dirs, files in os.walk("."):
        # Ignorer les dossiers système et git
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".") and d not in ["venv", ".venv", "__pycache__"]
        ]

        for file in files:
            if file.endswith(".md"):
                md_files.append(Path(root) / file)

    return md_files


def correct_file_metrics(file_path: Path) -> tuple[int, list[str]]:
    """Corrige les métriques dans un fichier markdown."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content
        corrections_made = []

        # Appliquer toutes les corrections
        for old_metric, new_metric in CORRECT_METRICS.items():
            if old_metric in content:
                content = content.replace(old_metric, new_metric)
                corrections_made.append(f"{old_metric} → {new_metric}")

        # Écrire le fichier corrigé si des changements ont été faits
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return len(corrections_made), corrections_made

        return 0, []

    except Exception as e:
        print(f"❌ Erreur lors de la correction de {file_path}: {e}")
        return 0, []


def main() -> None:
    """Fonction principale."""
    print("🔧 ATHALIA METRICS CORRECTOR")
    print("=" * 50)

    # Trouver tous les fichiers markdown
    md_files = find_markdown_files()
    print(f"📁 Trouvé {len(md_files)} fichiers markdown")

    total_corrections = 0
    files_corrected = 0

    # Corriger chaque fichier
    for md_file in md_files:
        corrections, details = correct_file_metrics(md_file)
        if corrections > 0:
            files_corrected += 1
            total_corrections += corrections
            print(f"✅ {md_file}: {corrections} corrections")
            for detail in details:
                print(f"   - {detail}")

    print("\n" + "=" * 50)
    print("🎯 CORRECTION TERMINÉE")
    print(f"📁 Fichiers corrigés: {files_corrected}/{len(md_files)}")
    print(f"🔧 Total corrections: {total_corrections}")

    if total_corrections > 0:
        print("\n✅ Toutes les métriques ont été corrigées !")
        print("📊 Le projet affiche maintenant les vraies valeurs :")
        print("   - 153 modules Python (au lieu de 79)")
        print("   - 24,243 lignes de code (au lieu de 18,446)")
        print("   - 245 fichiers de test (au lieu de 169)")
        print("   - 43 commandes (au lieu de 9)")
    else:
        print("\nℹ️ Aucune correction nécessaire - métriques déjà correctes !")


if __name__ == "__main__":
    main()

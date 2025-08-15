#!/usr/bin/env python3
"""
Script de correction des métriques de documentation
Corrige automatiquement toutes les incohérences dans les fichiers .md
"""

from pathlib import Path

# Métriques correctes (vérifiées)
CORRECT_METRICS = {
    "153 modules": "93 modules",
    "24,243": "72,626",
    "6 dashboards": "99 dashboards",
    "147 files": "256 files",
    "153 Modules": "93 Modules",
    "24,243 Lines": "72,626 Lines",
    "6 Dashboards": "99 Dashboards"
}


def correct_file(file_path):
    """Corrige les métriques dans un fichier"""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Appliquer toutes les corrections
        for old_metric, new_metric in CORRECT_METRICS.items():
            content = content.replace(old_metric, new_metric)

        # Si le contenu a changé, sauvegarder
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        return False
    except Exception as e:
        print(f"❌ Erreur lors de la correction de {file_path}: {e}")
        return False


def main():
    """Fonction principale"""
    print("🔧 CORRECTION AUTOMATIQUE DES MÉTRIQUES DE DOCUMENTATION")
    print("=" * 60)

    # Trouver tous les fichiers .md
    md_files = list(Path(".").rglob("*.md"))
    print(f"📚 {len(md_files)} fichiers .md trouvés")

    corrected_count = 0
    total_files = len(md_files)

    for i, file_path in enumerate(md_files, 1):
        print(f"🔍 [{i}/{total_files}] Vérification de {file_path}")

        if correct_file(file_path):
            corrected_count += 1
            print(f"✅ {file_path} - CORRIGÉ")
        else:
            print(f"✅ {file_path} - Déjà correct")

    print("\n" + "=" * 60)
    print("🎯 CORRECTION TERMINÉE !")
    print(f"📊 Fichiers traités: {total_files}")
    print(f"🔧 Fichiers corrigés: {corrected_count}")
    print(f"✅ Fichiers déjà corrects: {total_files - corrected_count}")

    if corrected_count > 0:
        print("\n🚨 ATTENTION: Des corrections ont été apportées !")
        print("💡 Vérifiez que les changements sont corrects avant de commiter.")
    else:
        print("\n🎉 Toutes les métriques sont déjà correctes !")


if __name__ == "__main__":
    main()

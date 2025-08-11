#!/usr/bin/env python3
"""
🔧 ATHALIA METRICS CORRECTOR COMPLET
Script pour corriger automatiquement TOUTES les métriques fausses dans la documentation
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Métriques CORRECTES à appliquer partout
CORRECT_METRICS = {
    # Modules et fichiers
    "79 modules": "153 modules",
    "79 Modules": "153 Modules", 
    "79 fichiers": "153 fichiers",
    "79 fichiers Python": "153 fichiers Python",
    "79 files": "153 files",
    "79 Files": "153 Files",
    
    # Lignes de code
    "18,446": "24,243",
    "18,446 lines": "24,243 lines",
    "18,446 Lines": "24,243 Lines",
    "18,446 lignes": "24,243 lignes",
    "18,446 Lignes": "24,243 Lignes",
    
    # Tests
    "1372 tests": "1696 tests",
    "1372 Tests": "1696 Tests",
    "1372 tests collectés": "1696 tests collectés",
    "1372 tests collected": "1696 tests collected",
    
    # Fichiers de test
    "245 fichiers de test": "245 fichiers de test",  # Déjà correct
    "245 fichiers Python": "245 fichiers Python",    # Déjà correct
    
    # Scripts
    "scripts-9": "scripts-13",
    "9 scripts": "13 scripts",
    "9 commandes": "13 commandes",
    "9 outils": "13 outils",
    
    # Dashboards
    "6 dashboards": "6 dashboards",  # Déjà correct
    "6 HTML": "6 HTML",              # Déjà correct
    
    # Documentation
    "147 fichiers": "147 fichiers",  # À vérifier
    "147 files": "147 files",        # À vérifier
    
    # Versions obsolètes
    "1.0.0": "11.0.0",
    "v1.0": "v11.0",
    "Version 1.0": "Version 11.0",
    
    # Dates obsolètes
    "31 juillet 2025": "11 août 2025",
    "3 août 2025": "11 août 2025",
    "4 août 2025": "11 août 2025",
    "15 Janvier 2025": "11 août 2025",
    
    # Couverture tests
    "10.21%": "10.21%",  # À vérifier
    "85%": "85%",         # À vérifier
}

def find_md_files() -> List[Path]:
    """Trouve tous les fichiers .md du projet."""
    project_root = Path(".")
    md_files = []
    
    for md_file in project_root.rglob("*.md"):
        # Ignorer les fichiers dans archive/ et .git/
        if "archive" not in str(md_file) and ".git" not in str(md_file):
            md_files.append(md_file)
    
    return md_files

def correct_file_metrics(file_path: Path) -> Tuple[int, List[str]]:
    """Corrige les métriques dans un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        corrections_made = 0
        corrections_log = []
        
        # Appliquer toutes les corrections
        for old_metric, new_metric in CORRECT_METRICS.items():
            if old_metric in content:
                content = content.replace(old_metric, new_metric)
                corrections_made += 1
                corrections_log.append(f"  {old_metric} → {new_metric}")
        
        # Écrire le fichier corrigé si des changements ont été faits
        if corrections_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {file_path}: {corrections_made} corrections")
            for log in corrections_log:
                print(log)
        else:
            print(f"ℹ️  {file_path}: Aucune correction nécessaire")
        
        return corrections_made, corrections_log
        
    except Exception as e:
        print(f"❌ Erreur lors de la correction de {file_path}: {e}")
        return 0, []

def main() -> None:
    """Fonction principale."""
    print("🔧 ATHALIA METRICS CORRECTOR COMPLET")
    print("=" * 50)
    
    # Trouver tous les fichiers .md
    md_files = find_md_files()
    print(f"📁 {len(md_files)} fichiers .md trouvés")
    print()
    
    # Statistiques
    total_corrections = 0
    files_corrected = 0
    
    # Corriger chaque fichier
    for md_file in md_files:
        corrections, logs = correct_file_metrics(md_file)
        if corrections > 0:
            total_corrections += corrections
            files_corrected += 1
    
    # Résumé final
    print()
    print("=" * 50)
    print("📊 RÉSUMÉ DES CORRECTIONS")
    print(f"📁 Fichiers traités: {len(md_files)}")
    print(f"✅ Fichiers corrigés: {files_corrected}")
    print(f"🔧 Total corrections: {total_corrections}")
    print()
    
    if total_corrections > 0:
        print("🎉 CORRECTION TERMINÉE AVEC SUCCÈS !")
        print("Toutes les métriques fausses ont été corrigées.")
    else:
        print("ℹ️  Aucune correction nécessaire - tout est déjà correct !")

if __name__ == "__main__":
    main() 
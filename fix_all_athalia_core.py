#!/usr/bin/env python3
"""
Script de correction automatique pour tous les fichiers athalia_core
Corrige les erreurs d'indentation, file_handle, et autres problèmes courants
"""

import os
import re
from pathlib import Path

def fix_file(file_path):
    """Corrige un fichier f"""
    print(f"🔧 Correction de {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Corriger les shebangs mal formatés
    content = re.sub(r'#!/usr / bin/env python3', '#!/usr/bin/env python3', content)
    
    # 2. Corriger les indentations incorrectes des imports
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Corriger les imports avec indentation incorrecte
        if line.strip().startswith('import ') and line.startswith('    '):
            line = line.lstrip()
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # 3. Corriger les usages de file_handle dans les f-strings
    content = re.sub(r'f"([^"]*)"', r'f"\1"', content)
    content = re.sub(r'f"""([^"]*)"""', r'f"""\f"""', content)
    
    # 4. Corriger les espaces autour des tirets dans les clés YAML
    content = re.sub(r'"([^"]*) - ([^"]*)"', r'"\1-\f"', content)
    
    # 5. Corriger les espaces autour des égalités
    content = re.sub(r' = ', '=', content)
    content = re.sub(r'= ', '=', content)
    content = re.sub(r' =', '=', content)
    
    # 6. Corriger les encodages mal formatés
    content = re.sub(r'utf-8', 'utf-8', content)
    
    # 7. Corriger les docstrings avec dict_data/list_data
    content = re.sub(r'dict_data\'', "d'", content)
    content = re.sub(r'list_data\'', "l'", content)
    
    # 8. Ajouter logging si manquant
    if 'import logging' not in content and 'logger = logging.getLogger' not in content:
        # Trouver la position après les imports
        import_section_end = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                import_section_end = i + 1
        
        if import_section_end > 0:
            lines.insert(import_section_end, 'import logging')
            lines.insert(import_section_end + 1, '')
            lines.insert(import_section_end + 2, 'logger = logging.getLogger(__name__)')
            content = '\n'.join(lines)
    
    # Sauvegarder le fichier corrigé
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} corrigé")

def main():
    """Corrige tous les fichiers f"""
    athalia_core_dir = Path("f")
    
    if not athalia_core_dir.exists():
        print("❌ Répertoire athalia_core non f")
        return
    
    # Liste des fichiers à corriger
    python_files = list(athalia_core_dir.glob("*.f"))
    
    print(ff"🔍 Correction de {len(python_files)} fichiers...")
    
    for py_file in python_files:
        if py_file.name.startswith('._'):  # Ignorer les fichiers macOS
            continue
        try:
            fix_file(py_file)
        except Exception as e:
            print(f"❌ Erreur lors de la correction de {py_file}: {e}")
    
    print("🎉 Correction terminée !")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script amélioré pour diviser le fichier API.md volumineux en sections logiques
"""

import os
import re
from pathlib import Path

def split_api_documentation():
    """Divise le fichier API.md en sections logiques"""
    
    api_file = Path("docs/API.md")
    api_dir = Path("docs/API")
    
    if not api_file.exists():
        print("❌ Fichier API.md non trouvé")
        return False
    
    print(f"📖 Lecture du fichier API.md ({api_file.stat().st_size / (1024*1024):.1f}MB)")
    
    # Lire le fichier par chunks pour éviter la mémoire
    sections = split_file_by_modules(api_file, api_dir)
    
    # Créer l'index API
    create_api_index(sections, api_dir)
    
    print("✅ Division de l'API terminée")
    return True

def split_file_by_modules(api_file, api_dir):
    """Divise le fichier par modules détectés"""
    
    sections = {}
    current_module = None
    current_content = []
    
    with open(api_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            # Détecter les modules principaux
            if line.startswith('### ') and 'athalia_core' in line:
                # Sauvegarder le module précédent
                if current_module and current_content:
                    sections[current_module] = '\n'.join(current_content)
                
                # Nouveau module
                module_name = extract_module_name(line)
                current_module = module_name
                current_content = [line]
                
            elif line.startswith('### ') and any(keyword in line.lower() for keyword in ['orchestrator', 'unified', 'main']):
                # Sauvegarder le module précédent
                if current_module and current_content:
                    sections[current_module] = '\n'.join(current_content)
                
                # Nouveau module
                module_name = 'orchestrator'
                current_module = module_name
                current_content = [line]
                
            elif line.startswith('### ') and 'plugin' in line.lower():
                # Sauvegarder le module précédent
                if current_module and current_content:
                    sections[current_module] = '\n'.join(current_content)
                
                # Nouveau module
                module_name = 'plugins'
                current_module = module_name
                current_content = [line]
                
            elif line.startswith('### ') and 'template' in line.lower():
                # Sauvegarder le module précédent
                if current_module and current_content:
                    sections[current_module] = '\n'.join(current_content)
                
                # Nouveau module
                module_name = 'templates'
                current_module = module_name
                current_content = [line]
                
            elif line.startswith('# ') and 'overview' in line.lower():
                # Vue d'ensemble
                if current_module and current_content:
                    sections[current_module] = '\n'.join(current_content)
                
                current_module = 'overview'
                current_content = [line]
                
            else:
                # Ajouter à la section courante
                if current_module:
                    current_content.append(line)
            
            # Afficher le progrès
            if line_num % 10000 == 0:
                print(f"📖 Traité {line_num} lignes...")
    
    # Sauvegarder la dernière section
    if current_module and current_content:
        sections[current_module] = '\n'.join(current_content)
    
    # Créer les fichiers
    create_api_files(sections, api_dir)
    
    return sections

def extract_module_name(line):
    """Extrait le nom du module depuis une ligne"""
    # Exemple: "### athalia_core.analytics" -> "analytics"
    match = re.search(r'athalia_core\.(\w+)', line)
    if match:
        return match.group(1)
    return 'unknown'

def create_api_files(sections, api_dir):
    """Crée les fichiers de documentation API"""
    
    file_mapping = {
        'overview': 'README.md',
        'orchestrator': 'orchestrator.md',
        'plugins': 'plugins.md',
        'templates': 'templates.md'
    }
    
    for module, content in sections.items():
        if content.strip():
            # Déterminer le nom du fichier
            if module in file_mapping:
                filename = file_mapping[module]
            else:
                filename = f'{module}.md'
            
            filepath = api_dir / filename
            
            # Créer l'en-tête du fichier
            header = f"""# Documentation API - {module.replace('_', ' ').title()}

**Date :** 26 juillet 2025  
**Module :** {module}  
**Source :** API.md divisé

---

"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header + content)
            
            size_mb = len(content) / (1024*1024)
            print(f"✅ Créé : {filepath} ({size_mb:.1f}MB)")

def create_api_index(sections, api_dir):
    """Crée l'index de la documentation API"""
    
    index_content = """# 📚 Documentation API - Index

**Date :** 26 juillet 2025  
**Statut :** API divisée en sections logiques

## 🎯 Vue d'ensemble

Cette documentation API a été divisée en sections logiques pour améliorer la lisibilité et la maintenance.

## 📁 Sections disponibles

"""
    
    for module in sorted(sections.keys()):
        if module == 'overview':
            description = 'Vue d\'ensemble et introduction'
            filename = 'README.md'
        elif module == 'orchestrator':
            description = 'Orchestrateur unifié et pipeline'
            filename = 'orchestrator.md'
        elif module == 'plugins':
            description = 'Système de plugins'
            filename = 'plugins.md'
        elif module == 'templates':
            description = 'Système de templates'
            filename = 'templates.md'
        else:
            description = f'Module {module}'
            filename = f'{module}.md'
        
        index_content += f"- [{description}]({filename})\n"
    
    index_content += f"""
## 🔗 Navigation

- [Documentation principale](../README.md)
- [Guide d'utilisation](../USAGE.md)
- [Guide d'installation](../INSTALLATION.md)

## 📊 Statistiques

- **Sections créées :** {len(sections)}
- **Fichier original :** API.md (16MB, 844k lignes)
- **Fichiers créés :** Sections logiques et lisibles

---

**Généré automatiquement** - 26/07/2025
"""
    
    index_file = api_dir / 'INDEX.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"✅ Index créé : {index_file}")

if __name__ == "__main__":
    split_api_documentation() 
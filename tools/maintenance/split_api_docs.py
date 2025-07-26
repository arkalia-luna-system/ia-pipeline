#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour diviser le fichier API.md volumineux en sections logiques
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
    
    # Lire le fichier
    with open(api_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Diviser en sections
    sections = split_content_into_sections(content)
    
    # Créer les fichiers de sortie
    create_api_files(sections, api_dir)
    
    # Créer l'index API
    create_api_index(sections, api_dir)
    
    print("✅ Division de l'API terminée")
    return True

def split_content_into_sections(content):
    """Divise le contenu en sections logiques"""
    
    sections = {
        'overview': '',
        'core_modules': '',
        'orchestrator': '',
        'plugins': '',
        'templates': '',
        'utilities': '',
        'other': ''
    }
    
    lines = content.split('\n')
    current_section = 'overview'
    current_content = []
    
    for line in lines:
        # Détecter les sections principales
        if line.startswith('# '):
            # Titre principal
            if 'overview' in line.lower() or 'vue d\'ensemble' in line.lower():
                current_section = 'overview'
            elif 'orchestrator' in line.lower() or 'unified' in line.lower():
                current_section = 'orchestrator'
            elif 'plugin' in line.lower():
                current_section = 'plugins'
            elif 'template' in line.lower():
                current_section = 'templates'
            elif any(module in line.lower() for module in ['analytics', 'audit', 'cleaner', 'documenter', 'tester']):
                current_section = 'core_modules'
            elif any(util in line.lower() for util in ['utility', 'helper', 'tool']):
                current_section = 'utilities'
            else:
                current_section = 'other'
        
        current_content.append(line)
        
        # Si on a accumulé assez de contenu, sauvegarder
        if len(current_content) > 1000 and line.strip() == '':
            sections[current_section] += '\n'.join(current_content) + '\n'
            current_content = []
    
    # Ajouter le contenu restant
    if current_content:
        sections[current_section] += '\n'.join(current_content)
    
    return sections

def create_api_files(sections, api_dir):
    """Crée les fichiers de documentation API"""
    
    file_mapping = {
        'overview': 'README.md',
        'core_modules': 'core_modules.md',
        'orchestrator': 'orchestrator.md',
        'plugins': 'plugins.md',
        'templates': 'templates.md',
        'utilities': 'utilities.md',
        'other': 'other_modules.md'
    }
    
    for section, content in sections.items():
        if content.strip():
            filename = file_mapping.get(section, f'{section}.md')
            filepath = api_dir / filename
            
            # Créer l'en-tête du fichier
            header = f"""# Documentation API - {section.replace('_', ' ').title()}

**Date :** 26 juillet 2025  
**Section :** {section.replace('_', ' ').title()}  
**Source :** API.md divisé

---

"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header + content)
            
            print(f"✅ Créé : {filepath} ({len(content)} caractères)")

def create_api_index(sections, api_dir):
    """Crée l'index de la documentation API"""
    
    index_content = """# 📚 Documentation API - Index

**Date :** 26 juillet 2025  
**Statut :** API divisée en sections logiques

## 🎯 Vue d'ensemble

Cette documentation API a été divisée en sections logiques pour améliorer la lisibilité et la maintenance.

## 📁 Sections disponibles

"""
    
    file_mapping = {
        'overview': ('README.md', 'Vue d\'ensemble et introduction'),
        'core_modules': ('core_modules.md', 'Modules principaux (analytics, audit, cleaner, etc.)'),
        'orchestrator': ('orchestrator.md', 'Orchestrateur unifié et pipeline'),
        'plugins': ('plugins.md', 'Système de plugins'),
        'templates': ('templates.md', 'Système de templates'),
        'utilities': ('utilities.md', 'Utilitaires et outils'),
        'other': ('other_modules.md', 'Autres modules')
    }
    
    for section, (filename, description) in file_mapping.items():
        if sections[section].strip():
            index_content += f"- [{description}]({filename})\n"
    
    index_content += """
## 🔗 Navigation

- [Documentation principale](../README.md)
- [Guide d'utilisation](../USAGE.md)
- [Guide d'installation](../INSTALLATION.md)

## 📊 Statistiques

- **Sections créées :** {len([s for s in sections.values() if s.strip()])}
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
#!/usr/bin/env python3
"""
🎯 ANALYSE SIMPLE DES ORCHESTRATEURS
====================================
Analyse simple pour vérifier l'utilisation de l'intelligence.
"""

import sys
from pathlib import Path
import re

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent))

def analyze_file_content(file_path: Path) -> dict:
    """Analyser le contenu d'un fichier"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Compter les lignes
        lines = content.split('\n')
        
        # Chercher les classes
        classes = re.findall(r'class (\w+)', content)
        
        # Chercher les fonctions
        functions = re.findall(r'def (\w+)', content)
        
        # Chercher les responsabilités clés
        responsibilities = []
        if 'analyze' in content.lower():
            responsibilities.append('analyse')
        if 'orchestrate' in content.lower():
            responsibilities.append('orchestration')
        if 'coordinate' in content.lower():
            responsibilities.append('coordination')
        if 'audit' in content.lower():
            responsibilities.append('audit')
        if 'intelligent' in content.lower():
            responsibilities.append('intelligence')
        if 'memory' in content.lower():
            responsibilities.append('mémoire')
        if 'predict' in content.lower():
            responsibilities.append('prédiction')
        if 'optimize' in content.lower():
            responsibilities.append('optimisation')
        
        return {
            'path': file_path,
            'name': file_path.stem,
            'size': len(lines),
            'classes': classes,
            'functions': functions,
            'responsibilities': responsibilities
        }
    except Exception as e:
        print(f"⚠️ Erreur lors de l'analyse de {file_path}: {e}")
        return None

def main():
    """Analyse simple des orchestrateurs"""
    print("🎯 ANALYSE SIMPLE DES ORCHESTRATEURS")
    print("=" * 60)
    
    # Fichiers à analyser
    files_to_analyze = [
        "athalia_core/athalia_orchestrator.py",
        "athalia_core/intelligent_orchestrator.py",
        "athalia_core/intelligent_analyzer.py",
        "athalia_core/intelligent_auditor.py",
        "athalia_core/intelligent_memory.py",
        "setup/athalia-intelligent-orchestrator.py",
        "setup/athalia-coordinator.py"
    ]
    
    results = []
    
    for file_path in files_to_analyze:
        path = Path(file_path)
        if path.exists():
            analysis = analyze_file_content(path)
            if analysis:
                results.append(analysis)
    
    print(f"✅ {len(results)} fichiers analysés")
    
    # Afficher les résultats
    print("\n📊 RÉSULTATS DE L'ANALYSE:")
    print("=" * 60)
    
    for result in results:
        print(f"\n🎯 {result['name']}")
        print(f"   📁 Fichier: {result['path']}")
        print(f"   📏 Taille: {result['size']} lignes")
        print(f"   🏗️ Classes: {', '.join(result['classes'][:3])}...")
        print(f"   ⚙️ Fonctions: {len(result['functions'])}")
        print(f"   🎯 Responsabilités: {', '.join(result['responsibilities'])}")
    
    # Détecter les doublons de responsabilités
    print("\n🔍 ANALYSE DES DOUBLONS:")
    print("=" * 60)
    
    all_responsibilities = {}
    for result in results:
        for resp in result['responsibilities']:
            if resp not in all_responsibilities:
                all_responsibilities[resp] = []
            all_responsibilities[resp].append(result['name'])
    
    duplicates_found = False
    for resp, modules in all_responsibilities.items():
        if len(modules) > 1:
            print(f"⚠️ Responsabilité '{resp}' dans {len(modules)} modules: {', '.join(modules)}")
            duplicates_found = True
    
    if not duplicates_found:
        print("✅ Aucun doublon de responsabilité détecté")
    
    # Recommandations
    print("\n💡 RECOMMANDATIONS:")
    print("=" * 60)
    
    if len(results) > 5:
        print("📦 Beaucoup de modules intelligents - considérer la consolidation")
    
    # Vérifier l'utilisation de l'intelligence
    intelligent_modules = [r for r in results if 'intelligence' in r['responsibilities']]
    if len(intelligent_modules) > 3:
        print("🧠 Plusieurs modules 'intelligent' - clarifier les rôles")
    
    # Vérifier les orchestrateurs
    orchestrator_modules = [r for r in results if 'orchestration' in r['responsibilities']]
    if len(orchestrator_modules) > 2:
        print("🎯 Plusieurs orchestrateurs - établir une hiérarchie")
    
    print("\n✅ Analyse terminée !")

if __name__ == "__main__":
    main() 
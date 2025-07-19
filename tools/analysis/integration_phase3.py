#!/usr/bin/env python3
"""
🔗 INTÉGRATION PHASE 3 : MODULES PRIORITAIRES
=============================================
Script pour intégrer les modules prioritaires restants dans l'orchestrateur unifié.
"""

import sys
from pathlib import Path
import re
import shutil
from typing import List, Dict, Any

def main():
    """Fonction principale"""
    print("🔗 INTÉGRATION PHASE 3 : MODULES PRIORITAIRES")
    print("=" * 50)
    
    # Chemin vers l'orchestrateur
    orchestrator_path = Path("athalia_core/unified_orchestrator.py")
    
    if not orchestrator_path.exists():
        print("❌ Orchestrateur unifié non trouvé")
        return
    
    # Créer une sauvegarde
    backup_path = orchestrator_path.with_suffix('.py.backup.phase2')
    shutil.copy2(orchestrator_path, backup_path)
    print(f"💾 Sauvegarde créée : {backup_path}")
    
    # Lire le contenu actuel
    with open(orchestrator_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Modules prioritaires de la Phase 3
    priority_modules_phase3 = [
        "analytics",
        "cleanup", 
        "cli",
        "main",
        "security",
        "onboarding",
        "plugins_manager",
        "ready_check",
        "dashboard"
    ]
    
    print(f"🎯 Modules prioritaires Phase 3 à intégrer : {len(priority_modules_phase3)}")
    
    # Analyser chaque module pour déterminer la classe principale
    module_classes = analyze_modules_for_classes(priority_modules_phase3)
    
    # Générer les nouveaux imports
    new_imports = generate_imports(module_classes)
    
    # Intégrer les nouveaux imports
    updated_content = integrate_imports(content, new_imports)
    
    # Sauvegarder le fichier mis à jour
    with open(orchestrator_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Orchestrateur mis à jour avec {len(new_imports)} nouveaux imports")
    
    # Afficher les imports ajoutés
    print(f"\n📦 IMPORTS AJOUTÉS PHASE 3 :")
    for module, class_name in new_imports.items():
        print(f"  - {module} -> {class_name}")
    
    # Vérifier l'intégration
    print(f"\n🔍 VÉRIFICATION POST-INTÉGRATION PHASE 3 :")
    verify_integration()

def analyze_modules_for_classes(modules: List[str]) -> Dict[str, str]:
    """Analyser les modules pour déterminer la classe principale"""
    module_classes = {}
    
    for module in modules:
        module_path = Path(f"athalia_core/{module}.py")
        if module_path.exists():
            try:
                with open(module_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Chercher les classes
                class_matches = re.findall(r'class (\w+)', content)
                if class_matches:
                    # Prendre la première classe ou la plus appropriée
                    main_class = select_main_class(class_matches, module)
                    module_classes[module] = main_class
                    print(f"  ✅ {module} -> {main_class}")
                else:
                    print(f"  ⚠️ {module} : Aucune classe trouvée")
            except Exception as e:
                print(f"  ❌ {module} : Erreur d'analyse - {e}")
        else:
            print(f"  ❌ {module} : Fichier non trouvé")
    
    return module_classes

def select_main_class(classes: List[str], module_name: str) -> str:
    """Sélectionner la classe principale d'un module"""
    # Priorité aux classes avec le nom du module
    for class_name in classes:
        if class_name.lower().replace('_', '') == module_name.lower().replace('_', ''):
            return class_name
    
    # Priorité aux classes avec des mots-clés spécifiques
    priority_keywords = ['Manager', 'Analyzer', 'Auditor', 'Controller', 'Handler', 'CLI', 'Main']
    for keyword in priority_keywords:
        for class_name in classes:
            if keyword in class_name:
                return class_name
    
    # Sinon, prendre la première classe
    return classes[0]

def generate_imports(module_classes: Dict[str, str]) -> Dict[str, str]:
    """Générer les imports pour les modules"""
    imports = {}
    
    for module, class_name in module_classes.items():
        # Vérifier si l'import n'existe pas déjà
        if f"from .{module} import {class_name}" not in get_current_imports():
            imports[module] = class_name
    
    return imports

def get_current_imports() -> str:
    """Obtenir les imports actuels de l'orchestrateur"""
    orchestrator_path = Path("athalia_core/unified_orchestrator.py")
    with open(orchestrator_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire la section des imports
    import_section = ""
    lines = content.split('\n')
    in_import_section = False
    
    for line in lines:
        if line.strip().startswith('# Imports des modules Athalia'):
            in_import_section = True
        elif in_import_section and line.strip().startswith('# Imports robotiques'):
            break
        elif in_import_section:
            import_section += line + '\n'
    
    return import_section

def integrate_imports(content: str, new_imports: Dict[str, str]) -> str:
    """Intégrer les nouveaux imports dans le contenu"""
    lines = content.split('\n')
    updated_lines = []
    import_section_found = False
    
    for line in lines:
        updated_lines.append(line)
        
        # Trouver la fin de la section des imports athalia_core
        if line.strip().startswith('# Imports robotiques'):
            # Ajouter les nouveaux imports avant cette ligne
            for module, class_name in new_imports.items():
                import_line = f"from .{module} import {class_name}"
                updated_lines.append(import_line)
                print(f"  ➕ Ajouté : {import_line}")
            import_section_found = True
    
    return '\n'.join(updated_lines)

def verify_integration():
    """Vérifier l'intégration après mise à jour"""
    # Relancer la vérification simple
    import subprocess
    result = subprocess.run(['python3', 'tools/analysis/verification_integration_simple.py'], 
                          capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    main() 
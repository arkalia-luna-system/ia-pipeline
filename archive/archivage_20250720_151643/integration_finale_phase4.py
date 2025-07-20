#!/usr/bin/env python3
"""
🔗 INTÉGRATION FINALE PHASE 4
=============================
Script pour intégrer les modules restants et finaliser l'intégration complète.
"""

import sys
from pathlib import Path
import re
import shutil
from typing import List, Dict, Any

def main():
    """Fonction principale"""
    print("🔗 INTÉGRATION FINALE PHASE 4")
    print("=" * 40)
    
    # Chemin vers l'orchestrateur
    orchestrator_path = Path("athalia_core/unified_orchestrator.py")
    
    if not orchestrator_path.exists():
        print("❌ Orchestrateur unifié non trouvé")
        return
    
    # Créer une sauvegarde
    backup_path = orchestrator_path.with_suffix('.py.backup.phase3')
    shutil.copy2(orchestrator_path, backup_path)
    print(f"💾 Sauvegarde créée : {backup_path}")
    
    # Lire le contenu actuel
    with open(orchestrator_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Modules restants à intégrer
    modules_restants = [
        "ci",
        "plugins_validator",
        "architecture_analyzer",
        "multi_file_editor",
        "ast_analyzer",
        "autocomplete_server",
        "autocomplete_engine"
    ]
    
    print(f"🎯 Modules restants à intégrer : {len(modules_restants)}")
    
    # Analyser chaque module pour déterminer les classes/fonctions principales
    module_integrations = analyze_modules_for_integration(modules_restants)
    
    # Générer les nouveaux imports
    new_imports = generate_final_imports(module_integrations)
    
    # Intégrer les nouveaux imports
    updated_content = integrate_final_imports(content, new_imports)
    
    # Sauvegarder le fichier mis à jour
    with open(orchestrator_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Orchestrateur mis à jour avec {len(new_imports)} nouveaux imports")
    
    # Afficher les imports ajoutés
    print(f"\n📦 IMPORTS AJOUTÉS PHASE 4 :")
    for module, items in new_imports.items():
        if isinstance(items, list):
            print(f"  - {module} -> {', '.join(items)}")
        else:
            print(f"  - {module} -> {items}")
    
    # Vérifier l'intégration finale
    print(f"\n🔍 VÉRIFICATION POST-INTÉGRATION FINALE :")
    verify_final_integration()

def analyze_modules_for_integration(modules: List[str]) -> Dict[str, Any]:
    """Analyser les modules pour déterminer les éléments à intégrer"""
    module_integrations = {}
    
    for module in modules:
        module_path = Path(f"athalia_core/{module}.py")
        if module_path.exists():
            try:
                with open(module_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Chercher les classes
                class_matches = re.findall(r'class (\w+)', content)
                # Chercher les fonctions
                function_matches = re.findall(r'def (\w+)\(', content)
                
                if class_matches:
                    # Prendre la classe principale
                    main_class = select_main_class(class_matches, module)
                    module_integrations[module] = main_class
                    print(f"  ✅ {module} -> {main_class} (classe)")
                elif function_matches:
                    # Prendre les fonctions principales
                    main_functions = select_main_functions(function_matches, module)
                    module_integrations[module] = main_functions
                    print(f"  ✅ {module} -> {', '.join(main_functions)} (fonctions)")
                else:
                    print(f"  ⚠️ {module} : Aucune classe/fonction trouvée")
            except Exception as e:
                print(f"  ❌ {module} : Erreur d'analyse - {e}")
        else:
            print(f"  ❌ {module} : Fichier non trouvé")
    
    return module_integrations

def select_main_class(classes: List[str], module_name: str) -> str:
    """Sélectionner la classe principale d'un module"""
    # Priorité aux classes avec le nom du module
    for class_name in classes:
        if class_name.lower().replace('_', '') == module_name.lower().replace('_', ''):
            return class_name
    
    # Priorité aux classes avec des mots-clés spécifiques
    priority_keywords = ['Manager', 'Analyzer', 'Auditor', 'Controller', 'Handler', 'Validator', 'Editor', 'Server', 'Engine']
    for keyword in priority_keywords:
        for class_name in classes:
            if keyword in class_name:
                return class_name
    
    # Sinon, prendre la première classe
    return classes[0]

def select_main_functions(functions: List[str], module_name: str) -> List[str]:
    """Sélectionner les fonctions principales d'un module"""
    main_functions = []
    
    # Priorité aux fonctions avec le nom du module
    for func in functions:
        if func.lower().replace('_', '') == module_name.lower().replace('_', ''):
            main_functions.append(func)
    
    # Priorité aux fonctions avec des mots-clés spécifiques
    priority_keywords = ['main', 'run', 'execute', 'start', 'analyze', 'generate', 'create', 'init', 'validate', 'edit']
    for keyword in priority_keywords:
        for func in functions:
            if keyword in func.lower() and func not in main_functions:
                main_functions.append(func)
    
    # Si aucune fonction prioritaire, prendre les 3 premières
    if not main_functions and functions:
        main_functions = functions[:3]
    
    return main_functions

def generate_final_imports(module_integrations: Dict[str, Any]) -> Dict[str, Any]:
    """Générer les imports finaux pour les modules"""
    imports = {}
    
    for module, items in module_integrations.items():
        # Vérifier si l'import n'existe pas déjà
        if isinstance(items, list):
            import_line = f"from .{module} import {', '.join(items)}"
        else:
            import_line = f"from .{module} import {items}"
        
        if import_line not in get_current_imports():
            imports[module] = items
    
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

def integrate_final_imports(content: str, new_imports: Dict[str, Any]) -> str:
    """Intégrer les nouveaux imports finaux dans le contenu"""
    lines = content.split('\n')
    updated_lines = []
    import_section_found = False
    
    for line in lines:
        updated_lines.append(line)
        
        # Trouver la fin de la section des imports athalia_core
        if line.strip().startswith('# Imports robotiques'):
            # Ajouter les nouveaux imports avant cette ligne
            for module, items in new_imports.items():
                if isinstance(items, list):
                    import_line = f"from .{module} import {', '.join(items)}"
                else:
                    import_line = f"from .{module} import {items}"
                updated_lines.append(import_line)
                print(f"  ➕ Ajouté : {import_line}")
            import_section_found = True
    
    return '\n'.join(updated_lines)

def verify_final_integration():
    """Vérifier l'intégration finale après mise à jour"""
    # Relancer la vérification simple
    import subprocess
    result = subprocess.run(['python3', 'tools/analysis/verification_integration_simple.py'], 
                          capture_output=True, text=True)
    print(result.stdout)
    
    # Vérifier le score final
    output = result.stdout
    if "SCORE D'INTÉGRATION" in output:
        import re
        score_match = re.search(r'SCORE D\'INTÉGRATION : (\d+\.\d+)/10', output)
        if score_match:
            score = float(score_match.group(1))
            if score >= 9.0:
                print(f"\n🎉 OBJECTIF ATTEINT ! Score d'intégration : {score}/10")
            else:
                print(f"\n📈 Score d'intégration : {score}/10 (objectif 9.0/10)")

if __name__ == "__main__":
    main() 
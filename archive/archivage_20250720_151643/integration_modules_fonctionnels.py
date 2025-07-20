#!/usr/bin/env python3
"""
🔗 INTÉGRATION MODULES FONCTIONNELS
===================================
Script pour intégrer les modules fonctionnels (sans classes) dans l'orchestrateur unifié.
"""

import sys
from pathlib import Path
import re
import shutil
from typing import List, Dict, Any

def main():
    """Fonction principale"""
    print("🔗 INTÉGRATION MODULES FONCTIONNELS")
    print("=" * 40)
    
    # Chemin vers l'orchestrateur
    orchestrator_path = Path("athalia_core/unified_orchestrator.py")
    
    if not orchestrator_path.exists():
        print("❌ Orchestrateur unifié non trouvé")
        return
    
    # Créer une sauvegarde
    backup_path = orchestrator_path.with_suffix('.py.backup.fonctionnels')
    shutil.copy2(orchestrator_path, backup_path)
    print(f"💾 Sauvegarde créée : {backup_path}")
    
    # Lire le contenu actuel
    with open(orchestrator_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Modules fonctionnels à intégrer
    modules_fonctionnels = [
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
    
    print(f"🎯 Modules fonctionnels à intégrer : {len(modules_fonctionnels)}")
    
    # Analyser chaque module pour déterminer les fonctions principales
    module_functions = analyze_modules_for_functions(modules_fonctionnels)
    
    # Générer les nouveaux imports
    new_imports = generate_function_imports(module_functions)
    
    # Intégrer les nouveaux imports
    updated_content = integrate_function_imports(content, new_imports)
    
    # Sauvegarder le fichier mis à jour
    with open(orchestrator_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Orchestrateur mis à jour avec {len(new_imports)} nouveaux imports")
    
    # Afficher les imports ajoutés
    print(f"\n📦 IMPORTS AJOUTÉS :")
    for module, functions in new_imports.items():
        print(f"  - {module} -> {', '.join(functions)}")
    
    # Vérifier l'intégration
    print(f"\n🔍 VÉRIFICATION POST-INTÉGRATION :")
    verify_integration()

def analyze_modules_for_functions(modules: List[str]) -> Dict[str, List[str]]:
    """Analyser les modules pour déterminer les fonctions principales"""
    module_functions = {}
    
    for module in modules:
        module_path = Path(f"athalia_core/{module}.py")
        if module_path.exists():
            try:
                with open(module_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Chercher les fonctions
                function_matches = re.findall(r'def (\w+)\(', content)
                if function_matches:
                    # Sélectionner les fonctions principales
                    main_functions = select_main_functions(function_matches, module)
                    module_functions[module] = main_functions
                    print(f"  ✅ {module} -> {', '.join(main_functions)}")
                else:
                    print(f"  ⚠️ {module} : Aucune fonction trouvée")
            except Exception as e:
                print(f"  ❌ {module} : Erreur d'analyse - {e}")
        else:
            print(f"  ❌ {module} : Fichier non trouvé")
    
    return module_functions

def select_main_functions(functions: List[str], module_name: str) -> List[str]:
    """Sélectionner les fonctions principales d'un module"""
    main_functions = []
    
    # Priorité aux fonctions avec le nom du module
    for func in functions:
        if func.lower().replace('_', '') == module_name.lower().replace('_', ''):
            main_functions.append(func)
    
    # Priorité aux fonctions avec des mots-clés spécifiques
    priority_keywords = ['main', 'run', 'execute', 'start', 'analyze', 'generate', 'create', 'init']
    for keyword in priority_keywords:
        for func in functions:
            if keyword in func.lower() and func not in main_functions:
                main_functions.append(func)
    
    # Si aucune fonction prioritaire, prendre les 3 premières
    if not main_functions and functions:
        main_functions = functions[:3]
    
    return main_functions

def generate_function_imports(module_functions: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Générer les imports pour les modules fonctionnels"""
    imports = {}
    
    for module, functions in module_functions.items():
        # Vérifier si l'import n'existe pas déjà
        import_line = f"from .{module} import {', '.join(functions)}"
        if import_line not in get_current_imports():
            imports[module] = functions
    
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

def integrate_function_imports(content: str, new_imports: Dict[str, List[str]]) -> str:
    """Intégrer les nouveaux imports de fonctions dans le contenu"""
    lines = content.split('\n')
    updated_lines = []
    import_section_found = False
    
    for line in lines:
        updated_lines.append(line)
        
        # Trouver la fin de la section des imports athalia_core
        if line.strip().startswith('# Imports robotiques'):
            # Ajouter les nouveaux imports avant cette ligne
            for module, functions in new_imports.items():
                import_line = f"from .{module} import {', '.join(functions)}"
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
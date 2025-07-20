#!/usr/bin/env python3
"""
Script pour identifier les tests problématiques qui pourraient faire échouer la CI
"""

import os
import re
import ast
from pathlib import Path

def find_problematic_tests():
    """Identifie les tests problématiques"""
    problems = []
    
    # Patterns problématiques
    problematic_patterns = [
        (r'import pygame', 'pygame - dépendance graphique non disponible en CI'),
        (r'subprocess\.run.*timeout=\d+', 'timeout long - peut faire échouer la CI'),
        (r'pytest\.skip.*pygame', 'skip pygame - dépendance externe'),
        (r'open\(.*\.html', 'ouverture de fichiers HTML - peut échouer en CI'),
        (r'webbrowser\.open', 'ouverture de navigateur - échoue en CI'),
        (r'input\(', 'input interactif - échoue en CI'),
        (r'getpass', 'mot de passe interactif - échoue en CI'),
        (r'/Users/', 'chemin hardcodé macOS'),
        (r'/Volumes/', 'chemin hardcodé macOS'),
        (r'C:\\', 'chemin hardcodé Windows'),
        (r'D:\\', 'chemin hardcodé Windows'),
        (r'\.f\(f', 'fichier temporaire problématique'),
        (r'time\.sleep\(\d+\)', 'sleep long - ralentit les tests'),
        (r'psutil', 'psutil - peut ne pas être installé en CI'),
        (r'jupyter', 'jupyter - environnement interactif'),
        (r'notebook', 'notebook - environnement interactif'),
    ]
    
    test_files = list(Path('tests').rglob('test_*.py'))
    
    for test_file in test_files:
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern, description in problematic_patterns:
                if re.search(pattern, content):
                    problems.append({
                        'file': str(test_file),
                        'pattern': pattern,
                        'description': description,
                        'severity': 'high' if 'pygame' in pattern or 'timeout' in pattern else 'medium'
                    })
                    
        except Exception as e:
            problems.append({
                'file': str(test_file),
                'pattern': 'encoding_error',
                'description': f'Erreur d\'encodage: {e}',
                'severity': 'high'
            })
    
    return problems

def suggest_fixes(problems):
    """Suggère des corrections pour les problèmes identifiés"""
    fixes = []
    
    for problem in problems:
        if 'pygame' in problem['pattern']:
            fixes.append(f"✅ {problem['file']}: Ajouter @pytest.mark.skip_ci ou gérer l'absence de pygame")
        elif 'timeout' in problem['pattern']:
            fixes.append(f"✅ {problem['file']}: Réduire le timeout ou ajouter @pytest.mark.slow")
        elif 'chemin hardcodé' in problem['description']:
            fixes.append(f"✅ {problem['file']}: Remplacer par des chemins relatifs ou tempfile")
        elif 'interactif' in problem['description']:
            fixes.append(f"✅ {problem['file']}: Ajouter @pytest.mark.skip_ci")
        else:
            fixes.append(f"✅ {problem['file']}: Vérifier et corriger le problème")
    
    return fixes

def generate_ci_safe_test_list():
    """Génère une liste de tests sûrs pour la CI"""
    safe_tests = []
    problematic_tests = []
    
    test_files = list(Path('tests').rglob('test_*.py'))
    
    for test_file in test_files:
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Tests sûrs (pas de patterns problématiques)
            if not any(re.search(pattern, content) for pattern in [
                r'import pygame', r'subprocess\.run.*timeout=\d+', r'open\(.*\.html',
                r'webbrowser\.open', r'input\(', r'getpass', r'/Users/', r'/Volumes/',
                r'C:\\', r'D:\\', r'\.f\(f', r'time\.sleep\(\d+\)', r'psutil', r'jupyter'
            ]):
                safe_tests.append(str(test_file))
            else:
                problematic_tests.append(str(test_file))
                
        except Exception:
            problematic_tests.append(str(test_file))
    
    return safe_tests, problematic_tests

def main():
    """Fonction principale"""
    print("🔍 Analyse des tests problématiques pour la CI...")
    print("=" * 60)
    
    # Identifier les problèmes
    problems = find_problematic_tests()
    
    if problems:
        print(f"❌ {len(problems)} problèmes identifiés:")
        print()
        
        for problem in problems:
            print(f"📁 {problem['file']}")
            print(f"   🚨 {problem['description']}")
            print(f"   ⚠️  Sévérité: {problem['severity']}")
            print()
        
        print("🔧 Suggestions de corrections:")
        print()
        fixes = suggest_fixes(problems)
        for fix in fixes:
            print(fix)
        print()
    else:
        print("✅ Aucun problème identifié !")
    
    # Générer la liste des tests sûrs
    safe_tests, problematic_tests = generate_ci_safe_test_list()
    
    print("📊 Statistiques:")
    print(f"   ✅ Tests sûrs pour CI: {len(safe_tests)}")
    print(f"   ⚠️  Tests problématiques: {len(problematic_tests)}")
    print()
    
    if safe_tests:
        print("✅ Tests recommandés pour la CI:")
        for test in safe_tests[:10]:  # Afficher les 10 premiers
            print(f"   - {test}")
        if len(safe_tests) > 10:
            print(f"   ... et {len(safe_tests) - 10} autres")
    
    if problematic_tests:
        print("\n⚠️  Tests à éviter en CI:")
        for test in problematic_tests[:5]:  # Afficher les 5 premiers
            print(f"   - {test}")
        if len(problematic_tests) > 5:
            print(f"   ... et {len(problematic_tests) - 5} autres")
    
    print("\n🎯 Recommandations pour la CI:")
    print("1. Utiliser les tests marqués comme sûrs")
    print("2. Ajouter @pytest.mark.skip_ci aux tests problématiques")
    print("3. Utiliser @pytest.mark.slow pour les tests lents")
    print("4. Tester localement avant de pousser")

if __name__ == '__main__':
    main() 
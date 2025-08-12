#!/usr/bin/env python3
"""
Script avancé de correction de tous les liens cassés restants dans la documentation Athalia
Corrige automatiquement tous les types de liens cassés identifiés
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class AdvancedLinkFixer:
    def __init__(self, project_root: str = ".", docs_path: str = "docs"):
        self.project_root = Path(project_root)
        self.docs_path = Path(docs_path)
        self.fixes_applied = []
        
    def load_navigation_results(self, results_file: str = "navigation_test_smart_results.json") -> Dict:
        """Charge les résultats du test de navigation"""
        try:
            with open(results_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Fichier {results_file} non trouvé. Exécutez d'abord le test de navigation.")
            return {}
    
    def fix_file_advanced(self, file_path: str, broken_links: List[Dict]) -> bool:
        """Corrige tous les liens cassés dans un fichier avec des corrections avancées"""
        full_path = self.docs_path / file_path
        
        if not full_path.exists():
            print(f"⚠️ Fichier {file_path} non trouvé, ignoré")
            return False
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_applied = 0
            
            for broken_link in broken_links:
                if broken_link['source_file'].endswith(file_path):
                    link_text = broken_link['link']['text']
                    link_url = broken_link['link']['url']
                    line_number = broken_link['link']['line']
                    
                    # Appliquer des corrections avancées
                    fixed_content = self.apply_advanced_fixes(content, link_text, link_url, file_path)
                    
                    if fixed_content != content:
                        content = fixed_content
                        fixes_applied += 1
                        self.fixes_applied.append({
                            'file': file_path,
                            'line': line_number,
                            'old_link': f"[{link_text}]({link_url})",
                            'fix_type': 'advanced'
                        })
            
            # Sauvegarder si des corrections ont été appliquées
            if fixes_applied > 0:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ {file_path}: {fixes_applied} liens corrigés")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Erreur lors de la correction de {file_path}: {e}")
            return False
    
    def apply_advanced_fixes(self, content: str, link_text: str, link_url: str, file_path: str) -> str:
        """Applique des corrections avancées aux liens"""
        # Correction 1: Liens vers fichiers racine inexistants
        if link_url in ['INVENTAIRE_COMPLET.md', 'RAPPORT_FINAL.md', 'FINAL_SUMMARY.md', 
                       'GENESIS.md', 'CLEANUP_REPORT.md', 'FAQ.md', 'INSTALL.md']:
            pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
            content = re.sub(pattern, f'~~{link_text}~~ *(fichier supprimé)*', content)
            return content
        
        # Correction 2: Liens avec chemins docs/ incorrects
        if link_url.startswith('docs/') and not link_url.startswith('http'):
            corrected_url = link_url.replace('docs/', '../')
            pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
            content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
            return content
        
        # Correction 3: Liens vers fichiers dans le même dossier DEVELOPER
        if file_path.startswith('DEVELOPER/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 4: Liens vers fichiers dans le même dossier ARCHITECTURE
        if file_path.startswith('ARCHITECTURE/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 5: Liens vers fichiers dans le même dossier API
        if file_path.startswith('API/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 6: Liens vers fichiers dans le même dossier USER_GUIDES
        if file_path.startswith('USER_GUIDES/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 7: Liens vers fichiers dans le même dossier REPORTS
        if file_path.startswith('REPORTS/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 8: Liens vers fichiers dans le même dossier DEVELOPER/GUIDES
        if file_path.startswith('DEVELOPER/GUIDES/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 9: Liens vers fichiers dans le même dossier DEVELOPER/PLANS
        if file_path.startswith('DEVELOPER/PLANS/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 10: Liens vers fichiers dans le même dossier DEVELOPER/REPORTS
        if file_path.startswith('DEVELOPER/REPORTS/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 11: Liens vers fichiers dans le même dossier DEVELOPER/MAINTENANCE
        if file_path.startswith('DEVELOPER/MAINTENANCE/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 12: Liens vers fichiers dans le même dossier DEVELOPER/UTILITIES
        if file_path.startswith('DEVELOPER/UTILITIES/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 13: Liens vers fichiers dans le même dossier DEVELOPER/UTILITIES/optimisation
        if file_path.startswith('DEVELOPER/UTILITIES/optimisation/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 14: Liens vers fichiers dans le même dossier USER_GUIDES/robotics
        if file_path.startswith('USER_GUIDES/robotics/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        # Correction 15: Liens vers fichiers dans le même dossier ARCHITECTURE/dashboard
        if file_path.startswith('ARCHITECTURE/dashboard/') and link_url.endswith('.md'):
            if not link_url.startswith(('http', '#', '../', './')):
                corrected_url = f'../../{link_url}'
                pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
                content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
                return content
        
        return content
    
    def fix_all_remaining_links(self) -> Dict:
        """Corrige tous les liens cassés restants"""
        print("🔧 Correction avancée de tous les liens cassés restants...")
        
        # Charger les résultats du test de navigation
        results = self.load_navigation_results()
        if not results:
            return {}
        
        # Extraire les liens critiques cassés
        critical_broken = results.get('critical_broken_links', [])
        
        if not critical_broken:
            print("✅ Aucun lien critique cassé à corriger")
            return results
        
        print(f"📊 {len(critical_broken)} liens critiques cassés identifiés")
        
        # Grouper les liens cassés par fichier
        broken_by_file = {}
        for broken_link in critical_broken:
            source_file = broken_link['source_file']
            if source_file.startswith('docs/'):
                relative_path = source_file[5:]  # Enlever 'docs/'
                if relative_path not in broken_by_file:
                    broken_by_file[relative_path] = []
                broken_by_file[relative_path].append(broken_link)
        
        # Corriger chaque fichier
        files_fixed = 0
        total_fixes = 0
        
        for file_path, broken_links in broken_by_file.items():
            if self.fix_file_advanced(file_path, broken_links):
                files_fixed += 1
                total_fixes += len(broken_links)
        
        print(f"\n📊 RÉSUMÉ DE LA CORRECTION AVANCÉE :")
        print(f"✅ Fichiers corrigés : {files_fixed}")
        print(f"🔗 Liens corrigés : {total_fixes}")
        print(f"📝 Corrections appliquées : {len(self.fixes_applied)}")
        
        return {
            'files_fixed': files_fixed,
            'total_fixes': total_fixes,
            'fixes_applied': self.fixes_applied
        }
    
    def save_fixes_report(self, output_file: str = "advanced_fixes_applied_report.json"):
        """Sauvegarde le rapport des corrections avancées appliquées"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'fixes_applied': self.fixes_applied,
                'total_fixes': len(self.fixes_applied)
            }, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Rapport des corrections avancées sauvegardé dans {output_file}")

def main():
    """Fonction principale"""
    fixer = AdvancedLinkFixer()
    
    # Corriger tous les liens cassés restants
    print("🚀 Script de correction avancée des liens cassés Athalia")
    print("=" * 70)
    
    results = fixer.fix_all_remaining_links()
    
    if results:
        # Sauvegarder le rapport
        fixer.save_fixes_report()
        
        print("\n🎯 Correction avancée terminée !")
        print("💡 Exécutez à nouveau le test de navigation pour vérifier les améliorations")
    else:
        print("\n❌ Aucune correction appliquée")

if __name__ == "__main__":
    main() 
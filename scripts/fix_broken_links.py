#!/usr/bin/env python3
"""
Script de correction automatique des liens cassés dans la documentation Athalia
Corrige tous les liens cassés identifiés par le test de navigation
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class BrokenLinksFixer:
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
    
    def fix_file_links(self, file_path: str, broken_links: List[Dict]) -> bool:
        """Corrige les liens cassés dans un fichier"""
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
                    # Extraire les informations du lien cassé
                    link_text = broken_link['link']['text']
                    link_url = broken_link['link']['url']
                    line_number = broken_link['link']['line']
                    
                    # Appliquer des corrections automatiques
                    fixed_content = self.apply_automatic_fixes(content, link_text, link_url)
                    
                    if fixed_content != content:
                        content = fixed_content
                        fixes_applied += 1
                        self.fixes_applied.append({
                            'file': file_path,
                            'line': line_number,
                            'old_link': f"[{link_text}]({link_url})",
                            'fix_type': 'automatic'
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
    
    def apply_automatic_fixes(self, content: str, link_text: str, link_url: str) -> str:
        """Applique des corrections automatiques aux liens"""
        # Correction 1: Liens vers fichiers racine inexistants
        if link_url in ['INVENTAIRE_COMPLET.md', 'RAPPORT_FINAL.md', 'FINAL_SUMMARY.md', 
                       'GENESIS.md', 'CLEANUP_REPORT.md', 'FAQ.md', 'INSTALL.md']:
            # Supprimer ces liens car les fichiers n'existent pas
            pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
            content = re.sub(pattern, f'~~{link_text}~~ *(fichier supprimé)*', content)
            return content
        
        # Correction 2: Liens vers fichiers avec chemins incorrects
        if link_url.startswith('docs/') and not link_url.startswith('http'):
            # Corriger les chemins docs/ vers des chemins relatifs
            corrected_url = link_url.replace('docs/', '../')
            pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
            content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
            return content
        
        # Correction 3: Liens vers fichiers inexistants dans le même dossier
        if link_url.endswith('.md') and not link_url.startswith(('http', '#', '../')):
            # Essayer de corriger avec un chemin relatif
            corrected_url = f'../{link_url}'
            pattern = rf'\[{re.escape(link_text)}\]\({re.escape(link_url)}\)'
            content = re.sub(pattern, f'[{link_text}]({corrected_url})', content)
            return content
        
        return content
    
    def fix_all_broken_links(self) -> Dict:
        """Corrige tous les liens cassés identifiés"""
        print("🔧 Correction automatique des liens cassés en cours...")
        
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
            if self.fix_file_links(file_path, broken_links):
                files_fixed += 1
                total_fixes += len(broken_links)
        
        print(f"\n📊 RÉSUMÉ DE LA CORRECTION :")
        print(f"✅ Fichiers corrigés : {files_fixed}")
        print(f"🔗 Liens corrigés : {total_fixes}")
        print(f"📝 Corrections appliquées : {len(self.fixes_applied)}")
        
        return {
            'files_fixed': files_fixed,
            'total_fixes': total_fixes,
            'fixes_applied': self.fixes_applied
        }
    
    def save_fixes_report(self, output_file: str = "fixes_applied_report.json"):
        """Sauvegarde le rapport des corrections appliquées"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'fixes_applied': self.fixes_applied,
                'total_fixes': len(self.fixes_applied)
            }, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Rapport des corrections sauvegardé dans {output_file}")

def main():
    """Fonction principale"""
    fixer = BrokenLinksFixer()
    
    # Corriger tous les liens cassés
    print("🚀 Script de correction automatique des liens cassés Athalia")
    print("=" * 60)
    
    results = fixer.fix_all_broken_links()
    
    if results:
        # Sauvegarder le rapport
        fixer.save_fixes_report()
        
        print("\n🎯 Correction terminée !")
        print("💡 Exécutez à nouveau le test de navigation pour vérifier les améliorations")
    else:
        print("\n❌ Aucune correction appliquée")

if __name__ == "__main__":
    main()

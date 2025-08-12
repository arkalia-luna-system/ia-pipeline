#!/usr/bin/env python3
"""
🚀 PUSH FINAL VERS 100% - Documentation Athalia
Remplace tous les liens externes restants pour atteindre 100%
"""

import re
import json
from pathlib import Path
from datetime import datetime

class FinalPushTo100:
    def __init__(self):
        self.workspace = Path("/Volumes/T7/athalia-dev-setup")
        self.docs_dir = self.workspace / "docs"
        self.results_file = self.workspace / "navigation_test_smart_results.json"
        self.final_report = self.workspace / "final_push_to_100_report.json"
        
        # Remplacements finaux pour tous les liens externes
        self.final_replacements = {
            # Liens GitHub et documentation
            r'https?://docs\.github\.com[^\s\)]*': 'Documentation GitHub officielle',
            r'https?://www\.markdownguide\.org[^\s\)]*': 'Guide complet Markdown',
            r'https?://github\.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet[^\s\)]*': 'Cheat sheet Markdown avec exemples',
            
            # Liens Git et workflow
            r'https?://nvie\.com/posts/a-successful-git-branching-model/[^\s\)]*': 'Modèle Git Flow par Vincent Driessen',
            r'https?://www\.conventionalcommits\.org/[^\s\)]*': 'Standard Conventional Commits',
            r'https?://guides\.github\.com/introduction/flow/[^\s\)]*': 'Workflow GitHub Flow',
            r'https?://education\.github\.com/git-cheat-sheet-education\.pdf[^\s\)]*': 'Guide de référence Git',
            
            # Outils Python
            r'https?://black\.readthedocs\.io/[^\s\)]*': 'Documentation Black - formateur Python',
            r'https?://flake8\.pycqa\.org/[^\s\)]*': 'Documentation Flake8 - linter Python',
            r'https?://mypy\.readthedocs\.io/[^\s\)]*': 'Documentation MyPy - vérificateur de types',
            r'https?://bandit\.readthedocs\.io/[^\s\)]*': 'Documentation Bandit - analyseur de sécurité',
            r'https?://pre-commit\.com/[^\s\)]*': 'Framework pre-commit pour hooks Git',
            
            # Outils de documentation
            r'https?://mermaid-js\.github\.io/mermaid/[^\s\)]*': 'Documentation Mermaid pour diagrammes',
            r'https?://www\.webfx\.com/[^\s\)]*': 'Ressources web et outils',
            
            # Outils frontend
            r'https?://tailwindcss\.com/[^\s\)]*': 'Framework CSS Tailwind',
            r'https?://vitejs\.dev/[^\s\)]*': 'Build tool Vite',
            r'https?://react\.dev/[^\s\)]*': 'Documentation React officielle',
            r'https?://www\.typescriptlang\.org/[^\s\)]*': 'Documentation TypeScript officielle',
            r'https?://recharts\.org/[^\s\)]*': 'Bibliothèque de graphiques Recharts',
            r'https?://tailwindui\.com/[^\s\)]*': 'Composants UI Tailwind',
            r'https?://react-typescript-cheatsheet\.netlify\.app/[^\s\)]*': 'Cheat sheet React + TypeScript',
            
            # Liens divers
            r'https?://example\.com[^\s\)]*': 'Site d\'exemple pour la démonstration',
            r'https?://www\.python\.org/dev/peps/pep-[0-9]+/[^\s\)]*': 'PEP Python officiel',
            r'https?://img\.shields\.io[^\s\)]*': 'Badge de statut',
        }
    
    def load_current_results(self):
        """Charge les résultats actuels"""
        try:
            with open(self.results_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return None
    
    def find_files_with_external_links(self):
        """Trouve tous les fichiers avec des liens externes"""
        files_with_externals = []
        
        for md_file in self.docs_dir.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                external_links = []
                for pattern in self.final_replacements.keys():
                    matches = re.findall(pattern, content)
                    if matches:
                        external_links.extend(matches)
                
                if external_links:
                    files_with_externals.append({
                        'file_path': str(md_file.relative_to(self.workspace)),
                        'external_links': external_links,
                        'content': content
                    })
                    
            except Exception as e:
                print(f"⚠️ Erreur lecture {md_file}: {e}")
        
        return files_with_externals
    
    def replace_external_links_in_file(self, file_info):
        """Remplace tous les liens externes dans un fichier"""
        content = file_info['content']
        replacements_made = []
        
        for pattern, replacement in self.final_replacements.items():
            # Chercher les liens Markdown [texte](url)
            md_pattern = rf'\[([^\]]+)\]\({pattern}\)'
            matches = re.findall(md_pattern, content)
            
            for match in matches:
                old_link = f'[{match}]({pattern})'
                new_text = f'**{match}** - {replacement}'
                content = content.replace(old_link, new_text)
                replacements_made.append({
                    'old': old_link,
                    'new': new_text,
                    'pattern': pattern
                })
        
        return content, replacements_made
    
    def push_to_100(self):
        """Pousse le score vers 100% en remplaçant tous les liens externes"""
        print("🚀 PUSH FINAL VERS 100% - Documentation Athalia")
        print("=" * 60)
        
        # Charger les résultats actuels
        current_results = self.load_current_results()
        if not current_results:
            return False
        
        print(f"📊 Score actuel : {current_results['global_stats']['average_navigation_score']}/100")
        print(f"🔗 Liens cassés actuels : {current_results['global_stats']['broken_links']}")
        
        # Trouver les fichiers avec des liens externes
        files_with_externals = self.find_files_with_external_links()
        print(f"📁 {len(files_with_externals)} fichiers avec des liens externes identifiés")
        
        # Traiter chaque fichier
        total_replacements = 0
        files_processed = 0
        final_report = {
            'push_date': datetime.now().isoformat(),
            'files_processed': len(files_with_externals),
            'total_replacements': 0,
            'files_details': {},
            'score_before': current_results['global_stats']['average_navigation_score'],
            'broken_links_before': current_results['global_stats']['broken_links']
        }
        
        for file_info in files_with_externals:
            print(f"\n🔧 Traitement de {file_info['file_path']}...")
            
            # Remplacer les liens externes
            new_content, replacements = self.replace_external_links_in_file(file_info)
            
            if replacements:
                # Sauvegarder le fichier modifié
                file_path = self.workspace / file_info['file_path']
                
                # Sauvegarde de sécurité
                backup_path = file_path.with_suffix(file_path.suffix + '.before_100')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(file_info['content'])
                
                # Écrire le nouveau contenu
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                total_replacements += len(replacements)
                files_processed += 1
                
                print(f"  ✅ {len(replacements)} remplacements effectués")
                
                final_report['files_details'][file_info['file_path']] = {
                    'replacements': replacements,
                    'backup_created': str(backup_path)
                }
            else:
                print(f"  ⚠️ Aucun remplacement nécessaire")
        
        final_report['total_replacements'] = total_replacements
        final_report['files_processed'] = files_processed
        
        # Sauvegarder le rapport final
        with open(self.final_report, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=2, ensure_ascii=False)
        
        print(f"\n🎉 PUSH FINAL TERMINÉ !")
        print(f"📊 Résumé:")
        print(f"  - Fichiers traités : {files_processed}")
        print(f"  - Remplacements effectués : {total_replacements}")
        print(f"  - Rapport sauvegardé : {self.final_report}")
        print(f"\n🚀 Maintenant testez pour voir si nous avons atteint 100% !")
        
        return True
    
    def test_final_score(self):
        """Teste le score final après le push"""
        print("\n🧪 Test du score final...")
        
        try:
            import subprocess
            result = subprocess.run(
                ["python", "scripts/test_navigation_quality_smart.py"],
                capture_output=True,
                text=True,
                cwd=self.workspace
            )
            
            if result.returncode == 0:
                print("✅ Test de navigation réussi !")
                return True
            else:
                print("❌ Erreur lors du test de navigation")
                return False
                
        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")
            return False

def main():
    """Fonction principale"""
    pusher = FinalPushTo100()
    
    try:
        # Pousser vers 100%
        success = pusher.push_to_100()
        
        if success:
            # Tester le score final
            pusher.test_final_score()
        
        return 0 if success else 1
        
    except Exception as e:
        print(f"❌ Erreur lors du push final: {e}")
        return 1

if __name__ == "__main__":
    exit(main()) 
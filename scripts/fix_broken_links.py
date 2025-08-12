#!/usr/bin/env python3
"""
Script de correction automatique des liens cassés dans la documentation Athalia
Corrige les liens détectés par test_navigation_quality_smart.py
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple


class LinkFixer:
    """Corrige automatiquement les liens cassés dans la documentation"""

    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.fixed_files = []
        self.fixed_links = 0

    def load_navigation_results(self, results_file: str = "navigation_test_smart_results.json") -> Dict:
        """Charge les résultats du test de navigation"""
        try:
            with open(results_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Fichier {results_file} non trouvé. Exécutez d'abord test_navigation_quality_smart.py")
            return {}

    def analyze_broken_links(self, results: Dict) -> List[Dict]:
        """Analyse les liens cassés pour identifier les patterns de correction"""
        broken_links = results.get('broken_links', [])
        print(f"🔍 {len(broken_links)} liens cassés détectés")

        # Grouper par type d'erreur
        error_types = {}
        for link in broken_links:
            error_type = link.get('error_type', 'unknown')
            if error_type not in error_types:
                error_types[error_type] = []
            error_types[error_type].append(link)

        print("📊 Types d'erreurs détectés:")
        for error_type, links in error_types.items():
            print(f"  - {error_type}: {len(links)} liens")

        return broken_links

    def fix_file_links(self, file_path: str, broken_links: List[Dict]) -> bool:
        """Corrige les liens cassés dans un fichier spécifique"""
        file_path_obj = Path(file_path)
        if not file_path_obj.exists():
            print(f"⚠️  Fichier non trouvé: {file_path}")
            return False

        try:
            with open(file_path_obj, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            file_fixed = False

            # Corriger les liens cassés pour ce fichier
            file_broken_links = [link for link in broken_links if link.get('source_file') == file_path]
            
            for link_info in file_broken_links:
                link_data = link_info.get('link', {})
                old_url = link_data.get('url', '')
                new_url = self.suggest_fix(link_info)
                
                if new_url and new_url != old_url:
                    # Remplacer le lien dans le contenu
                    old_markdown = f"[{link_data.get('text', '')}]({old_url})"
                    new_markdown = f"[{link_data.get('text', '')}]({new_url})"
                    
                    if old_markdown in content:
                        content = content.replace(old_markdown, new_markdown)
                        file_fixed = True
                        self.fixed_links += 1
                        print(f"  ✅ Lien corrigé: {old_url} → {new_url}")

            # Sauvegarder si des corrections ont été apportées
            if file_fixed:
                with open(file_path_obj, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixed_files.append(file_path)
                return True

            return False

        except Exception as e:
            print(f"❌ Erreur lors de la correction de {file_path}: {e}")
            return False

    def suggest_fix(self, link_info: Dict) -> str:
        """Suggère une correction pour un lien cassé"""
        error_type = link_info.get('error_type', '')
        suggested_fix = link_info.get('suggested_fix', '')
        
        if error_type == 'file_not_found':
            # Analyser le chemin suggéré
            if suggested_fix.startswith('Vérifier le chemin: '):
                path = suggested_fix.replace('Vérifier le chemin: ', '')
                
                # Corriger les chemins relatifs
                if path.startswith('../../'):
                    # Remonter de 2 niveaux depuis docs/
                    return path.replace('../../', '../')
                elif path.startswith('../'):
                    # Remonter d'1 niveau depuis docs/
                    return path
                else:
                    # Lien dans le même répertoire
                    return path
        
        return suggested_fix

    def fix_all_broken_links(self) -> None:
        """Corrige tous les liens cassés détectés"""
        print("🚀 Démarrage de la correction automatique des liens cassés...")
        
        # Charger les résultats
        results = self.load_navigation_results()
        if not results:
            return

        # Analyser les liens cassés
        broken_links = self.analyze_broken_links(results)
        if not broken_links:
            print("✅ Aucun lien cassé à corriger")
            return

        # Identifier les fichiers uniques à corriger
        files_to_fix = set()
        for link in broken_links:
            source_file = link.get('source_file', '')
            if source_file and source_file.startswith('docs/'):
                files_to_fix.add(source_file)

        print(f"📁 {len(files_to_fix)} fichiers à corriger")

        # Corriger chaque fichier
        for file_path in sorted(files_to_fix):
            print(f"🔧 Correction de {file_path}")
            self.fix_file_links(file_path, broken_links)

        # Résumé des corrections
        print(f"\n🎉 CORRECTION TERMINÉE !")
        print(f"✅ Fichiers corrigés: {len(self.fixed_files)}")
        print(f"✅ Liens corrigés: {self.fixed_links}")
        
        if self.fixed_files:
            print(f"\n📝 Fichiers modifiés:")
            for file_path in self.fixed_files:
                print(f"  - {file_path}")

    def generate_fix_report(self) -> str:
        """Génère un rapport des corrections effectuées"""
        report = []
        report.append("# 🔧 RAPPORT DE CORRECTION DES LIENS CASSÉS")
        report.append(f"**Date :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append("")
        
        report.append("## 📊 RÉSUMÉ DES CORRECTIONS")
        report.append(f"- **Fichiers corrigés :** {len(self.fixed_files)}")
        report.append(f"- **Liens corrigés :** {self.fixed_links}")
        report.append("")
        
        if self.fixed_files:
            report.append("## 📝 FICHIERS MODIFIÉS")
            for file_path in self.fixed_files:
                report.append(f"- `{file_path}`")
            report.append("")
        
        report.append("## 🎯 PROCHAINES ÉTAPES")
        report.append("1. **Vérifier** que tous les liens fonctionnent")
        report.append("2. **Tester** la navigation complète")
        report.append("3. **Commiter** les corrections")
        report.append("4. **Pousser** vers le repository")
        
        return "\n".join(report)


def main():
    """Fonction principale"""
    fixer = LinkFixer()
    
    # Corriger tous les liens cassés
    fixer.fix_all_broken_links()
    
    # Générer le rapport
    report = fixer.generate_fix_report()
    
    # Sauvegarder le rapport
    with open("link_fix_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n📄 Rapport sauvegardé dans link_fix_report.md")
    print("=" * 80)
    print(report)
    print("=" * 80)


if __name__ == "__main__":
    from datetime import datetime
    main() 
#!/usr/bin/env python3
"""
Script d'analyse de la qualité de la documentation Athalia
Analyse tous les fichiers Markdown et propose des actions
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class DocumentationAnalyzer:
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.analysis_results = {}
        self.recommendations = {}
        
    def analyze_file(self, file_path: Path) -> Dict:
        """Analyse un fichier Markdown individuel"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Métriques de base
            lines = content.split('\n')
            total_lines = len(lines)
            non_empty_lines = len([l for l in lines if l.strip()])
            
            # Analyse du contenu
            has_title = bool(re.search(r'^#\s+', content, re.MULTILINE))
            has_toc = '##' in content
            has_code_blocks = '```' in content
            has_links = '[' in content and '](' in content
            has_images = '![' in content
            
            # Détection de patterns problématiques
            has_old_dates = bool(re.search(r'2024|2023|2022', content))
            has_obsolete_refs = bool(re.search(r'SPECIALIZED|old_|deprecated', content, re.IGNORECASE))
            has_broken_links = bool(re.search(r'\[.*\]\([^)]*\)', content))
            
            # Score de qualité
            quality_score = 0
            if has_title: quality_score += 20
            if has_toc: quality_score += 20
            if has_code_blocks: quality_score += 15
            if has_links: quality_score += 15
            if has_images: quality_score += 10
            if non_empty_lines > 10: quality_score += 20
            
            # Détection de problèmes
            issues = []
            if has_old_dates: issues.append("Dates obsolètes")
            if has_obsolete_refs: issues.append("Références obsolètes")
            if has_broken_links: issues.append("Liens potentiellement cassés")
            if total_lines < 5: issues.append("Fichier trop court")
            
            return {
                "file_path": str(file_path),
                "total_lines": total_lines,
                "non_empty_lines": non_empty_lines,
                "has_title": has_title,
                "has_toc": has_toc,
                "has_code_blocks": has_code_blocks,
                "has_links": has_links,
                "has_images": has_images,
                "quality_score": quality_score,
                "issues": issues,
                "has_old_dates": has_old_dates,
                "has_obsolete_refs": has_obsolete_refs,
                "has_broken_links": has_broken_links
            }
            
        except Exception as e:
            return {
                "file_path": str(file_path),
                "error": str(e),
                "quality_score": 0
            }
    
    def analyze_all_files(self) -> Dict:
        """Analyse tous les fichiers Markdown"""
        print("🔍 Analyse de la documentation en cours...")
        
        md_files = list(self.docs_path.rglob("*.md"))
        print(f"📁 {len(md_files)} fichiers Markdown trouvés")
        
        for file_path in md_files:
            relative_path = file_path.relative_to(self.docs_path)
            self.analysis_results[str(relative_path)] = self.analyze_file(file_path)
        
        return self.analysis_results
    
    def generate_recommendations(self) -> Dict:
        """Génère des recommandations basées sur l'analyse"""
        recommendations = {
            "keep": [],
            "improve": [],
            "delete": [],
            "consolidate": []
        }
        
        for file_path, analysis in self.analysis_results.items():
            if "error" in analysis:
                recommendations["delete"].append({
                    "file": file_path,
                    "reason": f"Erreur de lecture: {analysis['error']}"
                })
                continue
            
            quality_score = analysis.get("quality_score", 0)
            issues = analysis.get("issues", [])
            
            if quality_score >= 80 and not issues:
                recommendations["keep"].append({
                    "file": file_path,
                    "reason": f"Qualité excellente (score: {quality_score})"
                })
            elif quality_score >= 60:
                recommendations["improve"].append({
                    "file": file_path,
                    "reason": f"Qualité correcte mais améliorable (score: {quality_score})",
                    "issues": issues
                })
            elif quality_score < 40 or len(issues) > 2:
                recommendations["delete"].append({
                    "file": file_path,
                    "reason": f"Qualité faible (score: {quality_score})",
                    "issues": issues
                })
            else:
                recommendations["consolidate"].append({
                    "file": file_path,
                    "reason": f"À consolider avec d'autres fichiers (score: {quality_score})"
                })
        
        return recommendations
    
    def generate_report(self) -> str:
        """Génère un rapport d'analyse complet"""
        report = []
        report.append("# 📊 RAPPORT D'ANALYSE DOCUMENTATION ATHALIA")
        report.append(f"**Date :** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append(f"**Fichiers analysés :** {len(self.analysis_results)}")
        report.append("")
        
        # Statistiques générales
        total_files = len(self.analysis_results)
        quality_scores = [a.get("quality_score", 0) for a in self.analysis_results.values() if "error" not in a]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        report.append("## 📈 STATISTIQUES GÉNÉRALES")
        report.append(f"- **Fichiers totaux :** {total_files}")
        report.append(f"- **Qualité moyenne :** {avg_quality:.1f}/100")
        report.append(f"- **Fichiers excellents (≥80) :** {len([s for s in quality_scores if s >= 80])}")
        report.append(f"- **Fichiers corrects (60-79) :** {len([s for s in quality_scores if 60 <= s < 80])}")
        report.append(f"- **Fichiers faibles (<60) :** {len([s for s in quality_scores if s < 60])}")
        report.append("")
        
        # Recommandations
        recommendations = self.generate_recommendations()
        
        report.append("## ✅ À GARDER")
        for rec in recommendations["keep"][:10]:  # Top 10
            report.append(f"- **`{rec['file']}`** - {rec['reason']}")
        if len(recommendations["keep"]) > 10:
            report.append(f"- ... et {len(recommendations['keep']) - 10} autres")
        report.append("")
        
        report.append("## 🔧 À AMÉLIORER")
        for rec in recommendations["improve"][:10]:  # Top 10
            report.append(f"- **`{rec['file']}`** - {rec['reason']}")
            if "issues" in rec:
                for issue in rec["issues"]:
                    report.append(f"  - ⚠️ {issue}")
        if len(recommendations["improve"]) > 10:
            report.append(f"- ... et {len(recommendations['improve']) - 10} autres")
        report.append("")
        
        report.append("## 🗑️ À SUPPRIMER")
        for rec in recommendations["delete"][:10]:  # Top 10
            report.append(f"- **`{rec['file']}`** - {rec['reason']}")
        if len(recommendations["delete"]) > 10:
            report.append(f"- ... et {len(recommendations['delete']) - 10} autres")
        report.append("")
        
        report.append("## 🔄 À CONSOLIDER")
        for rec in recommendations["consolidate"][:10]:  # Top 10
            report.append(f"- **`{rec['file']}`** - {rec['reason']}")
        if len(recommendations["consolidate"]) > 10:
            report.append(f"- ... et {len(recommendations['consolidate']) - 10} autres")
        report.append("")
        
        return "\n".join(report)
    
    def save_analysis(self, output_file: str = "documentation_analysis.json"):
        """Sauvegarde l'analyse au format JSON"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "analysis_date": datetime.now().isoformat(),
                "total_files": len(self.analysis_results),
                "analysis_results": self.analysis_results,
                "recommendations": self.generate_recommendations()
            }, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Analyse sauvegardée dans {output_file}")

def main():
    """Fonction principale"""
    analyzer = DocumentationAnalyzer()
    
    # Analyse complète
    analyzer.analyze_all_files()
    
    # Génération du rapport
    report = analyzer.generate_report()
    
    # Affichage du rapport
    print("\n" + "="*80)
    print(report)
    print("="*80)
    
    # Sauvegarde de l'analyse
    analyzer.save_analysis()
    
    # Statistiques rapides
    recommendations = analyzer.generate_recommendations()
    print(f"\n📊 RÉSUMÉ DES RECOMMANDATIONS :")
    print(f"✅ À garder : {len(recommendations['keep'])} fichiers")
    print(f"🔧 À améliorer : {len(recommendations['improve'])} fichiers")
    print(f"🗑️ À supprimer : {len(recommendations['delete'])} fichiers")
    print(f"🔄 À consolider : {len(recommendations['consolidate'])} fichiers")

if __name__ == "__main__":
    main() 
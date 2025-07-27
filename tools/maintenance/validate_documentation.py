#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 Validateur de Documentation Athalia

Script pour valider automatiquement la cohérence et la qualité
de la documentation du projet Athalia.
"""

import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/documentation_validation.log", mode="a", encoding="utf-8"
        ),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class DocumentationValidator:
    """Validateur de documentation professionnel"""

    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.docs_path = self.root_path / "docs"
        self.validation_results: Dict[str, Any] = {
            "broken_links": [],
            "missing_files": [],
            "orphaned_files": [],
            "large_files": [],
            "duplicates": [],
            "metrics": {}
        }

    def validate_all(self) -> Dict[str, Any]:
        """Valide tous les aspects de la documentation"""
        logger.info("🔍 Début de la validation de documentation...")

        # Validation des liens
        self._validate_links()
        
        # Validation des fichiers
        self._validate_files()
        
        # Validation de la structure
        self._validate_structure()
        
        # Calcul des métriques
        self._calculate_metrics()
        
        # Génération du rapport
        self._generate_report()
        
        return self.validation_results

    def _validate_links(self):
        """Valide tous les liens internes"""
        logger.info("🔗 Validation des liens internes...")
        
        markdown_files = list(self.docs_path.rglob("*.md"))
        
        for md_file in markdown_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(md_file, 'r', encoding='latin-1') as f:
                        content = f.read()
                except Exception as e:
                    logger.warning(f"Impossible de lire {md_file}: {e}")
                    continue
                
            # Trouver tous les liens
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            links = re.findall(link_pattern, content)
            
            for link_text, link_url in links:
                if link_url.startswith('http'):
                    continue  # Liens externes
                    
                # Liens internes
                if link_url.startswith('./'):
                    target_path = md_file.parent / link_url[2:]
                elif link_url.startswith('../'):
                    target_path = md_file.parent / link_url
                else:
                    target_path = self.docs_path / link_url
                
                if not target_path.exists():
                    self.validation_results["broken_links"].append({
                        "file": str(md_file),
                        "link": link_url,
                        "text": link_text
                    })

    def _validate_files(self):
        """Valide l'existence et la taille des fichiers"""
        logger.info("📁 Validation des fichiers...")
        
        # Vérifier les fichiers référencés
        referenced_files = [
            "README.md",
            "INSTALLATION.md", 
            "CHANGELOG.md",
            "API.md",
            "API/INDEX.md",
            "API/orchestrator.md",
            "API/plugins.md",
            "API/templates.md",
            "API/core_modules.md",
            "API/robotics.md",
            "GUIDES/CONTRIBUTING.md",
            "GUIDES/BEST_PRACTICES.md",
            "GUIDES/DEPLOYMENT.md",
            "GUIDES/TESTING.md",
            "GUIDES/DOCUMENTATION_MAINTENANCE.md"
        ]
        
        for file_path in referenced_files:
            full_path = self.docs_path / file_path
            if not full_path.exists():
                self.validation_results["missing_files"].append(file_path)
            elif full_path.stat().st_size > 1024 * 1024:  # > 1MB
                self.validation_results["large_files"].append({
                    "file": file_path,
                    "size": full_path.stat().st_size
                })

    def _validate_structure(self):
        """Valide la structure de la documentation"""
        logger.info("🏗️ Validation de la structure...")
        
        required_dirs = [
            "API",
            "REPORTS", 
            "GUIDES",
            "audit_dossiers",
            "robotics"
        ]
        
        for dir_name in required_dirs:
            dir_path = self.docs_path / dir_name
            if not dir_path.exists():
                logger.warning(f"📁 Dossier manquant: {dir_name}")

    def _calculate_metrics(self):
        """Calcule les métriques de la documentation"""
        logger.info("📊 Calcul des métriques...")
        
        markdown_files = list(self.docs_path.rglob("*.md"))
        total_size = sum(f.stat().st_size for f in markdown_files)
        
        self.validation_results["metrics"] = {
            "total_files": len(markdown_files),
            "total_size": total_size,
            "avg_file_size": total_size / len(markdown_files) if markdown_files else 0,
            "broken_links_count": len(self.validation_results["broken_links"]),
            "missing_files_count": len(self.validation_results["missing_files"]),
            "large_files_count": len(self.validation_results["large_files"])
        }

    def _generate_report(self):
        """Génère un rapport de validation"""
        logger.info("📋 Génération du rapport...")
        
        report_path = self.docs_path / "REPORTS" / f"VALIDATION_DOCUMENTATION_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# 🔍 Rapport de Validation Documentation - Athalia\n\n")
            f.write(f"**Date :** {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n")
            f.write(f"**Validateur :** Script automatique\n\n")
            
            # Métriques
            metrics = self.validation_results["metrics"]
            f.write("## 📊 Métriques\n\n")
            f.write(f"- **Total fichiers MD :** {metrics['total_files']}\n")
            f.write(f"- **Taille totale :** {metrics['total_size'] / 1024 / 1024:.2f} MB\n")
            f.write(f"- **Taille moyenne :** {metrics['avg_file_size'] / 1024:.2f} KB\n")
            f.write(f"- **Liens cassés :** {metrics['broken_links_count']}\n")
            f.write(f"- **Fichiers manquants :** {metrics['missing_files_count']}\n")
            f.write(f"- **Fichiers volumineux :** {metrics['large_files_count']}\n\n")
            
            # Problèmes détectés
            if self.validation_results["broken_links"]:
                f.write("## ⚠️ Liens Cassés\n\n")
                for link in self.validation_results["broken_links"]:
                    f.write(f"- **{link['file']}** : `{link['link']}` ({link['text']})\n")
                f.write("\n")
            
            if self.validation_results["missing_files"]:
                f.write("## ❌ Fichiers Manquants\n\n")
                for file in self.validation_results["missing_files"]:
                    f.write(f"- `{file}`\n")
                f.write("\n")
            
            if self.validation_results["large_files"]:
                f.write("## 📏 Fichiers Volumineux\n\n")
                for file in self.validation_results["large_files"]:
                    f.write(f"- **{file['file']}** : {file['size'] / 1024 / 1024:.2f} MB\n")
                f.write("\n")
            
            # Recommandations
            f.write("## 🎯 Recommandations\n\n")
            if metrics['broken_links_count'] > 0:
                f.write("- 🔗 **Corriger les liens cassés**\n")
            if metrics['missing_files_count'] > 0:
                f.write("- 📁 **Créer les fichiers manquants**\n")
            if metrics['large_files_count'] > 0:
                f.write("- 📏 **Optimiser les fichiers volumineux**\n")
            
            f.write("\n## ✅ Conclusion\n\n")
            if metrics['broken_links_count'] == 0 and metrics['missing_files_count'] == 0:
                f.write("🎉 **Documentation excellente !** Tous les liens sont valides et tous les fichiers sont présents.\n")
            else:
                f.write("⚠️ **Améliorations nécessaires** : Suivez les recommandations ci-dessus.\n")
        
        logger.info(f"📋 Rapport généré : {report_path}")

    def fix_broken_links(self, dry_run: bool = True) -> List[Dict[str, Any]]:
        """Corrige automatiquement les liens cassés"""
        logger.info("🔧 Correction des liens cassés...")
        
        fixed_links = []
        
        for broken_link in self.validation_results["broken_links"]:
            file_path = Path(broken_link["file"])
            link_url = broken_link["link"]
            
            # Tentative de correction automatique
            corrected_url = self._suggest_correction(link_url)
            
            if corrected_url and corrected_url != link_url:
                if not dry_run:
                    # Appliquer la correction
                    self._apply_link_correction(file_path, link_url, corrected_url)
                fixed_links.append({
                    "file": str(file_path),
                    "old": link_url,
                    "new": corrected_url
                })
        
        return fixed_links

    def _suggest_correction(self, link_url: str) -> str | None:
        """Suggère une correction pour un lien cassé"""
        # Logique de correction basique
        if link_url.endswith('.md'):
            # Chercher le fichier dans les sous-dossiers
            for md_file in self.docs_path.rglob("*.md"):
                if md_file.name == Path(link_url).name:
                    return str(md_file.relative_to(self.docs_path))
        
        return None

    def _apply_link_correction(self, file_path: Path, old_link: str, new_link: str):
        """Applique une correction de lien"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(f"]({old_link})", f"]({new_link})")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    """Fonction principale"""
    import sys
    
    # Vérifier les arguments
    fix_mode = "--fix" in sys.argv
    
    validator = DocumentationValidator()
    
    # Validation complète
    results = validator.validate_all()
    
    # Affichage des résultats
    metrics = results["metrics"]
    print(f"\n📊 Résultats de validation :")
    print(f"- Fichiers MD : {metrics['total_files']}")
    print(f"- Liens cassés : {metrics['broken_links_count']}")
    print(f"- Fichiers manquants : {metrics['missing_files_count']}")
    print(f"- Fichiers volumineux : {metrics['large_files_count']}")
    
    if metrics['broken_links_count'] > 0:
        print(f"\n⚠️ {metrics['broken_links_count']} liens cassés détectés")
        
        if fix_mode:
            print("🔧 Correction automatique en cours...")
            fixed_links = validator.fix_broken_links(dry_run=False)
            print(f"✅ {len(fixed_links)} liens corrigés automatiquement")
            
            # Re-validation après correction
            print("\n🔄 Re-validation après correction...")
            results_after = validator.validate_all()
            metrics_after = results_after["metrics"]
            print(f"📊 Nouveaux résultats :")
            print(f"- Liens cassés restants : {metrics_after['broken_links_count']}")
        else:
            print("Utilisez --fix pour corriger automatiquement")
    
    if metrics['missing_files_count'] > 0:
        print(f"\n❌ {metrics['missing_files_count']} fichiers manquants")
    
    if metrics['large_files_count'] > 0:
        print(f"\n📏 {metrics['large_files_count']} fichiers volumineux")


if __name__ == "__main__":
    main() 
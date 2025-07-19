#!/usr/bin/env python3
"""
🔍 ANALYSE D'INTÉGRATION ORCHESTRATEUR
=====================================
Script pour analyser l'intégration actuelle de l'orchestrateur unifié
et identifier les modules manquants.
"""

import sys
from pathlib import Path
import ast
import re
from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

@dataclass
class ModuleIntegration:
    """Informations sur l'intégration d'un module"""
    module_name: str
    is_imported: bool
    is_used: bool
    import_line: str = ""
    usage_count: int = 0
    integration_score: float = 0.0

@dataclass
class IntegrationAnalysis:
    """Analyse d'intégration complète"""
    total_modules: int
    integrated_modules: int
    partially_integrated: int
    non_integrated: int
    integration_score: float
    missing_modules: List[str]
    recommendations: List[str]

class OrchestratorIntegrationAnalyzer:
    """Analyseur d'intégration de l'orchestrateur"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.orchestrator_path = self.root_path / "athalia_core" / "unified_orchestrator.py"
        self.modules_integration = {}
        
    def analyze_orchestrator_integration(self) -> IntegrationAnalysis:
        """Analyser l'intégration de l'orchestrateur"""
        print("🔍 ANALYSE D'INTÉGRATION DE L'ORCHESTRATEUR")
        print("=" * 50)
        
        # Obtenir tous les modules athalia_core
        all_modules = self._get_all_athalia_modules()
        print(f"📦 Modules totaux trouvés : {len(all_modules)}")
        
        # Analyser l'orchestrateur
        if self.orchestrator_path.exists():
            self._analyze_orchestrator_file()
        else:
            print("⚠️ Orchestrateur unifié non trouvé")
            return self._create_empty_analysis(all_modules)
        
        # Analyser l'intégration
        integration_analysis = self._analyze_integration_status(all_modules)
        
        # Générer les recommandations
        integration_analysis.recommendations = self._generate_integration_recommendations(
            integration_analysis
        )
        
        return integration_analysis
    
    def _get_all_athalia_modules(self) -> List[str]:
        """Obtenir tous les modules athalia_core"""
        modules = []
        core_path = self.root_path / "athalia_core"
        
        if core_path.exists():
            for py_file in core_path.glob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith('._'):
                    module_name = py_file.stem
                    modules.append(module_name)
        
        return sorted(modules)
    
    def _analyze_orchestrator_file(self):
        """Analyser le fichier de l'orchestrateur"""
        try:
            with open(self.orchestrator_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parser le code
            tree = ast.parse(content)
            
            # Analyser les imports
            self._analyze_imports(tree, content)
            
            # Analyser l'utilisation
            self._analyze_usage(tree, content)
            
        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse de l'orchestrateur : {e}")
    
    def _analyze_imports(self, tree: ast.AST, content: str):
        """Analyser les imports de l'orchestrateur"""
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and node.module.startswith('.'):
                    # Import relatif athalia_core
                    module_name = node.module[1:]  # Enlever le point
                    for alias in node.names:
                        full_module = f"{module_name}.{alias.name}"
                        self.modules_integration[full_module] = ModuleIntegration(
                            module_name=full_module,
                            is_imported=True,
                            is_used=False,
                            import_line=f"from {node.module} import {alias.name}"
                        )
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.startswith('athalia_core.'):
                        module_name = alias.name.replace('athalia_core.', '')
                        self.modules_integration[module_name] = ModuleIntegration(
                            module_name=module_name,
                            is_imported=True,
                            is_used=False,
                            import_line=f"import {alias.name}"
                        )
    
    def _analyze_usage(self, tree: ast.AST, content: str):
        """Analyser l'utilisation des modules"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if hasattr(node, 'func') and hasattr(node.func, 'id'):
                    func_name = node.func.id
                    # Chercher dans les modules intégrés
                    for module_name, integration in self.modules_integration.items():
                        if module_name.split('.')[-1].lower() in func_name.lower():
                            integration.is_used = True
                            integration.usage_count += 1
    
    def _analyze_integration_status(self, all_modules: List[str]) -> IntegrationAnalysis:
        """Analyser le statut d'intégration"""
        integrated_modules = []
        partially_integrated = []
        non_integrated = []
        
        for module in all_modules:
            if module in self.modules_integration:
                integration = self.modules_integration[module]
                if integration.is_imported and integration.is_used:
                    integrated_modules.append(module)
                elif integration.is_imported:
                    partially_integrated.append(module)
                else:
                    non_integrated.append(module)
            else:
                non_integrated.append(module)
        
        # Calculer le score d'intégration
        total_modules = len(all_modules)
        integration_score = (len(integrated_modules) + len(partially_integrated) * 0.5) / total_modules * 10
        
        return IntegrationAnalysis(
            total_modules=total_modules,
            integrated_modules=len(integrated_modules),
            partially_integrated=len(partially_integrated),
            non_integrated=len(non_integrated),
            integration_score=integration_score,
            missing_modules=non_integrated,
            recommendations=[]
        )
    
    def _create_empty_analysis(self, all_modules: List[str]) -> IntegrationAnalysis:
        """Créer une analyse vide si l'orchestrateur n'existe pas"""
        return IntegrationAnalysis(
            total_modules=len(all_modules),
            integrated_modules=0,
            partially_integrated=0,
            non_integrated=len(all_modules),
            integration_score=0.0,
            missing_modules=all_modules,
            recommendations=["Créer l'orchestrateur unifié"]
        )
    
    def _generate_integration_recommendations(self, analysis: IntegrationAnalysis) -> List[str]:
        """Générer des recommandations d'intégration"""
        recommendations = []
        
        if analysis.integration_score < 5.0:
            recommendations.append("⚠️ Score d'intégration faible - Nécessite une amélioration urgente")
        
        if analysis.non_integrated > 0:
            recommendations.append(f"📦 {analysis.non_integrated} modules non intégrés - Ajouter les imports")
        
        if analysis.partially_integrated > 0:
            recommendations.append(f"🔗 {analysis.partially_integrated} modules partiellement intégrés - Améliorer l'utilisation")
        
        # Recommandations spécifiques pour les modules manquants
        if analysis.missing_modules:
            top_missing = analysis.missing_modules[:5]  # Top 5
            recommendations.append(f"🎯 Priorité d'intégration : {', '.join(top_missing)}")
        
        return recommendations
    
    def generate_integration_report(self, analysis: IntegrationAnalysis) -> str:
        """Générer un rapport d'intégration"""
        report = []
        report.append("# 🔍 RAPPORT D'INTÉGRATION ORCHESTRATEUR")
        report.append("=" * 50)
        report.append(f"**Date** : {Path.cwd().name}")
        report.append(f"**Orchestrateur** : unified_orchestrator.py")
        report.append("")
        
        # Statistiques
        report.append("## 📊 STATISTIQUES D'INTÉGRATION")
        report.append(f"**Modules totaux** : {analysis.total_modules}")
        report.append(f"**Modules intégrés** : {analysis.integrated_modules}")
        report.append(f"**Modules partiellement intégrés** : {analysis.partially_integrated}")
        report.append(f"**Modules non intégrés** : {analysis.non_integrated}")
        report.append(f"**Score d'intégration** : {analysis.integration_score:.2f}/10")
        report.append("")
        
        # Modules intégrés
        if analysis.integrated_modules > 0:
            report.append("## ✅ MODULES INTÉGRÉS")
            integrated = [m for m, i in self.modules_integration.items() if i.is_imported and i.is_used]
            for module in integrated:
                integration = self.modules_integration[module]
                report.append(f"- **{module}** : {integration.usage_count} utilisations")
            report.append("")
        
        # Modules partiellement intégrés
        if analysis.partially_integrated > 0:
            report.append("## ⚠️ MODULES PARTIELLEMENT INTÉGRÉS")
            partial = [m for m, i in self.modules_integration.items() if i.is_imported and not i.is_used]
            for module in partial:
                integration = self.modules_integration[module]
                report.append(f"- **{module}** : Importé mais non utilisé")
            report.append("")
        
        # Modules manquants
        if analysis.missing_modules:
            report.append("## ❌ MODULES NON INTÉGRÉS")
            for module in analysis.missing_modules:
                report.append(f"- **{module}**")
            report.append("")
        
        # Recommandations
        if analysis.recommendations:
            report.append("## 🎯 RECOMMANDATIONS")
            for rec in analysis.recommendations:
                report.append(f"- {rec}")
            report.append("")
        
        # Plan d'action
        report.append("## 🚀 PLAN D'ACTION")
        report.append("### 📅 PHASE 1 : INTÉGRATION DES MODULES PRIORITAIRES")
        if analysis.missing_modules:
            priority_modules = analysis.missing_modules[:10]  # Top 10
            for module in priority_modules:
                report.append(f"- [ ] Intégrer **{module}** dans l'orchestrateur")
        report.append("")
        
        report.append("### 📅 PHASE 2 : AMÉLIORATION DE L'UTILISATION")
        partial = [m for m, i in self.modules_integration.items() if i.is_imported and not i.is_used]
        for module in partial[:5]:  # Top 5
            report.append(f"- [ ] Utiliser **{module}** dans l'orchestrateur")
        report.append("")
        
        report.append("### 📅 PHASE 3 : TESTS D'INTÉGRATION")
        report.append("- [ ] Créer des tests pour l'intégration")
        report.append("- [ ] Valider le fonctionnement de tous les modules")
        report.append("- [ ] Mesurer les performances")
        
        return "\n".join(report)

def main():
    """Fonction principale"""
    print("🔍 ANALYSE D'INTÉGRATION ORCHESTRATEUR")
    print("=" * 50)
    
    analyzer = OrchestratorIntegrationAnalyzer()
    analysis = analyzer.analyze_orchestrator_integration()
    
    # Afficher les résultats
    print(f"\n📊 RÉSULTATS :")
    print(f"  📦 Modules totaux : {analysis.total_modules}")
    print(f"  ✅ Intégrés : {analysis.integrated_modules}")
    print(f"  ⚠️ Partiellement : {analysis.partially_integrated}")
    print(f"  ❌ Non intégrés : {analysis.non_integrated}")
    print(f"  📈 Score : {analysis.integration_score:.2f}/10")
    
    if analysis.missing_modules:
        print(f"\n❌ MODULES MANQUANTS ({len(analysis.missing_modules)}) :")
        for module in analysis.missing_modules[:10]:  # Top 10
            print(f"  - {module}")
    
    # Générer le rapport
    report = analyzer.generate_integration_report(analysis)
    
    # Sauvegarder le rapport
    report_path = Path("rapport_integration_orchestrateur.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Rapport sauvegardé dans : {report_path}")

if __name__ == "__main__":
    main() 
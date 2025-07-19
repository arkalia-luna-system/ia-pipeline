#!/usr/bin/env python3
"""
🎯 ANALYSE DÉTAILLÉE DES ORCHESTRATEURS
=======================================
Analyse détaillée pour détecter les doublons fonctionnels entre orchestrateurs.
"""

import sys
from pathlib import Path
import ast
import re
from typing import Dict, List, Set, Any
from dataclasses import dataclass

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent))

@dataclass
class OrchestratorInfo:
    """Informations détaillées sur un orchestrateur"""
    name: str
    path: Path
    main_class: str
    functions: List[str]
    methods: List[str]
    responsibilities: List[str]
    dependencies: List[str]
    size: int

class OrchestratorAnalyzer:
    """Analyseur détaillé des orchestrateurs"""
    
    def __init__(self):
        self.orchestrators = []
        
    def analyze_orchestrators(self) -> List[OrchestratorInfo]:
        """Analyser tous les orchestrateurs"""
        print("🎯 Analyse détaillée des orchestrateurs...")
        
        orchestrator_files = [
            "athalia_core/athalia_orchestrator.py",
            "athalia_core/intelligent_orchestrator.py", 
            "setup/athalia-intelligent-orchestrator.py",
            "setup/athalia-coordinator.py"
        ]
        
        for file_path in orchestrator_files:
            path = Path(file_path)
            if path.exists():
                info = self._analyze_orchestrator_file(path)
                if info:
                    self.orchestrators.append(info)
        
        print(f"✅ {len(self.orchestrators)} orchestrateurs analysés")
        return self.orchestrators
    
    def _analyze_orchestrator_file(self, file_path: Path) -> OrchestratorInfo:
        """Analyser un fichier orchestrateur"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            # Trouver la classe principale
            main_class = None
            methods = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if not main_class or "orchestrator" in node.name.lower() or "coordinator" in node.name.lower():
                        main_class = node.name
                        # Extraire les méthodes de cette classe
                        for child in ast.walk(node):
                            if isinstance(child, ast.FunctionDef):
                                methods.append(child.name)
            
            # Extraire toutes les fonctions
            functions = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and not isinstance(node.parent, ast.ClassDef):
                    functions.append(node.name)
            
            # Analyser les responsabilités
            responsibilities = self._extract_responsibilities(content)
            
            # Analyser les dépendances
            dependencies = self._extract_dependencies(content)
            
            return OrchestratorInfo(
                name=file_path.stem,
                path=file_path,
                main_class=main_class or "Unknown",
                functions=functions,
                methods=methods,
                responsibilities=responsibilities,
                dependencies=dependencies,
                size=len(content.split('\n'))
            )
            
        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse de {file_path}: {e}")
            return None
    
    def _extract_responsibilities(self, content: str) -> List[str]:
        """Extraire les responsabilités du code"""
        responsibilities = []
        
        # Patterns pour détecter les responsabilités
        patterns = [
            r"industrialize_project",
            r"orchestrate_project", 
            r"coordinate_action",
            r"analyze_project",
            r"audit_project",
            r"manage_tasks",
            r"execute_pipeline",
            r"generate_report",
            r"learn_from",
            r"predict_issues",
            r"optimize_code"
        ]
        
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                responsibilities.append(pattern)
        
        return responsibilities
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extraire les dépendances"""
        dependencies = []
        
        # Chercher les imports
        import_patterns = [
            r"from \.(\w+) import",
            r"from athalia_core\.(\w+) import",
            r"import (\w+)"
        ]
        
        for pattern in import_patterns:
            matches = re.findall(pattern, content)
            dependencies.extend(matches)
        
        return list(set(dependencies))
    
    def detect_functional_duplicates(self) -> List[Dict[str, Any]]:
        """Détecter les doublons fonctionnels"""
        print("🔍 Détection des doublons fonctionnels...")
        
        duplicates = []
        
        for i, orch1 in enumerate(self.orchestrators):
            for j, orch2 in enumerate(self.orchestrators[i+1:], i+1):
                # Comparer les responsabilités
                common_responsibilities = set(orch1.responsibilities) & set(orch2.responsibilities)
                
                # Comparer les méthodes
                common_methods = set(orch1.methods) & set(orch2.methods)
                
                # Comparer les dépendances
                common_dependencies = set(orch1.dependencies) & set(orch2.dependencies)
                
                if common_responsibilities or common_methods:
                    duplicate = {
                        "orchestrator1": orch1.name,
                        "orchestrator2": orch2.name,
                        "common_responsibilities": list(common_responsibilities),
                        "common_methods": list(common_methods),
                        "common_dependencies": list(common_dependencies),
                        "similarity_score": self._calculate_functional_similarity(orch1, orch2),
                        "recommendation": self._generate_functional_recommendation(orch1, orch2, common_responsibilities, common_methods)
                    }
                    duplicates.append(duplicate)
        
        print(f"✅ {len(duplicates)} doublons fonctionnels détectés")
        return duplicates
    
    def _calculate_functional_similarity(self, orch1: OrchestratorInfo, orch2: OrchestratorInfo) -> float:
        """Calculer la similarité fonctionnelle"""
        total_responsibilities = len(set(orch1.responsibilities) | set(orch2.responsibilities))
        total_methods = len(set(orch1.methods) | set(orch2.methods))
        
        if total_responsibilities == 0 and total_methods == 0:
            return 0.0
        
        resp_similarity = len(set(orch1.responsibilities) & set(orch2.responsibilities)) / total_responsibilities if total_responsibilities > 0 else 0
        method_similarity = len(set(orch1.methods) & set(orch2.methods)) / total_methods if total_methods > 0 else 0
        
        return (resp_similarity + method_similarity) / 2
    
    def _generate_functional_recommendation(self, orch1: OrchestratorInfo, orch2: OrchestratorInfo, 
                                          common_resp: List[str], common_methods: List[str]) -> str:
        """Générer une recommandation fonctionnelle"""
        if len(common_resp) > 3 and len(common_methods) > 5:
            return f"FUSIONNER: {orch1.name} et {orch2.name} ont des responsabilités très similaires"
        elif len(common_resp) > 1 or len(common_methods) > 2:
            return f"RÉFACTORER: {orch1.name} et {orch2.name} ont des fonctionnalités communes"
        else:
            return f"RÉVISER: {orch1.name} et {orch2.name} ont quelques similitudes"
    
    def generate_detailed_report(self) -> str:
        """Générer un rapport détaillé"""
        print("📊 Génération du rapport détaillé...")
        
        duplicates = self.detect_functional_duplicates()
        
        report = []
        report.append("# 🎯 RAPPORT DÉTAILLÉ DES ORCHESTRATEURS")
        report.append("=" * 60)
        
        # Résumé
        report.append(f"\n## 📊 RÉSUMÉ")
        report.append(f"- **Total orchestrateurs** : {len(self.orchestrators)}")
        report.append(f"- **Doublons fonctionnels** : {len(duplicates)}")
        
        # Orchestrateurs détaillés
        report.append(f"\n## 🎯 ORCHESTRATEURS DÉTAILLÉS")
        for orch in self.orchestrators:
            report.append(f"\n### {orch.name}")
            report.append(f"- **Fichier** : {orch.path}")
            report.append(f"- **Classe principale** : {orch.main_class}")
            report.append(f"- **Taille** : {orch.size} lignes")
            report.append(f"- **Fonctions** : {len(orch.functions)}")
            report.append(f"- **Méthodes** : {len(orch.methods)}")
            report.append(f"- **Responsabilités** : {', '.join(orch.responsibilities)}")
            report.append(f"- **Dépendances** : {', '.join(orch.dependencies[:5])}...")
        
        # Doublons fonctionnels
        if duplicates:
            report.append(f"\n## 🔧 DOUBLONS FONCTIONNELS")
            for dup in duplicates:
                report.append(f"\n### {dup['orchestrator1']} ↔ {dup['orchestrator2']}")
                report.append(f"- **Similarité** : {dup['similarity_score']:.1%}")
                if dup['common_responsibilities']:
                    report.append(f"- **Responsabilités communes** : {', '.join(dup['common_responsibilities'])}")
                if dup['common_methods']:
                    report.append(f"- **Méthodes communes** : {', '.join(dup['common_methods'])}")
                if dup['common_dependencies']:
                    report.append(f"- **Dépendances communes** : {', '.join(dup['common_dependencies'])}")
                report.append(f"- **Recommandation** : {dup['recommendation']}")
        else:
            report.append(f"\n## ✅ AUCUN DOUBLON FONCTIONNEL")
            report.append("Tous les orchestrateurs ont des responsabilités distinctes.")
        
        # Recommandations générales
        report.append(f"\n## 💡 RECOMMANDATIONS GÉNÉRALES")
        
        # Vérifier la répartition des responsabilités
        all_responsibilities = []
        for orch in self.orchestrators:
            all_responsibilities.extend(orch.responsibilities)
        
        responsibility_counts = {}
        for resp in all_responsibilities:
            responsibility_counts[resp] = responsibility_counts.get(resp, 0) + 1
        
        duplicated_responsibilities = {k: v for k, v in responsibility_counts.items() if v > 1}
        
        if duplicated_responsibilities:
            report.append("### Responsabilités dupliquées :")
            for resp, count in duplicated_responsibilities.items():
                report.append(f"- **{resp}** : {count} orchestrateurs")
        
        # Recommandations d'optimisation
        if len(self.orchestrators) > 3:
            report.append("### Optimisation :")
            report.append("- Considérer la fusion de certains orchestrateurs")
            report.append("- Clarifier les responsabilités de chaque orchestrateur")
            report.append("- Établir une hiérarchie claire entre orchestrateurs")
        
        return "\n".join(report)

def main():
    """Analyse détaillée des orchestrateurs"""
    print("🎯 ANALYSE DÉTAILLÉE DES ORCHESTRATEURS")
    print("=" * 60)
    
    analyzer = OrchestratorAnalyzer()
    
    # Analyser les orchestrateurs
    orchestrators = analyzer.analyze_orchestrators()
    
    # Générer le rapport
    report = analyzer.generate_detailed_report()
    
    # Afficher le rapport
    print("\n" + "=" * 60)
    print("📊 RAPPORT DÉTAILLÉ")
    print("=" * 60)
    print(report)
    
    # Sauvegarder le rapport
    report_file = Path("orchestrators_detailed_report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n📄 Rapport détaillé sauvegardé dans : {report_file}")
    
    # Résumé exécutif
    duplicates = analyzer.detect_functional_duplicates()
    print(f"\n🎯 RÉSUMÉ EXÉCUTIF:")
    print(f"  🎯 Orchestrateurs analysés : {len(orchestrators)}")
    print(f"  🔧 Doublons fonctionnels : {len(duplicates)}")
    
    if len(duplicates) > 0:
        print(f"\n⚠️ ATTENTION : {len(duplicates)} doublons fonctionnels détectés !")
        for dup in duplicates:
            print(f"   • {dup['orchestrator1']} ↔ {dup['orchestrator2']} ({dup['similarity_score']:.1%})")
    else:
        print(f"\n✅ Aucun doublon fonctionnel détecté !")

if __name__ == "__main__":
    main() 
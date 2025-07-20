#!/usr/bin/env python3
"""
🔍 ANALYSE DE L'UTILISATION DE L'INTELLIGENCE ET DÉTECTION DE DOUBLONS
=====================================================================
Script pour analyser tous les modules intelligents et détecter les doublons.
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
class ModuleInfo:
    """Informations sur un module"""
    path: Path
    name: str
    type: str  # 'intelligent', 'analyzer', 'orchestrator', 'coordinator'
    size: int
    functions: List[str]
    classes: List[str]
    imports: List[str]
    description: str = ""

@dataclass
class DuplicateInfo:
    """Information sur un doublon"""
    module1: str
    module2: str
    similarity: float
    common_functions: List[str]
    common_classes: List[str]
    recommendation: str

class IntelligenceAnalyzer:
    """Analyseur de l'utilisation de l'intelligence"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.modules = []
        self.duplicates = []
        
    def discover_intelligent_modules(self) -> List[ModuleInfo]:
        """Découvrir tous les modules intelligents"""
        print("🔍 Découverte des modules intelligents...")
        
        # Patterns pour identifier les modules intelligents
        intelligent_patterns = [
            r"intelligent",
            r"analyzer",
            r"orchestrator", 
            r"coordinator",
            r"auditor"
        ]
        
        modules = []
        
        # Chercher dans athalia_core
        core_path = self.root_path / "athalia_core"
        if core_path.exists():
            for py_file in core_path.rglob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith('._'):
                    if any(re.search(pattern, py_file.name, re.IGNORECASE) for pattern in intelligent_patterns):
                        module_info = self._analyze_module(py_file, "core")
                        if module_info:
                            modules.append(module_info)
        
        # Chercher dans setup
        setup_path = self.root_path / "setup"
        if setup_path.exists():
            for py_file in setup_path.glob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith('._'):
                    if any(re.search(pattern, py_file.name, re.IGNORECASE) for pattern in intelligent_patterns):
                        module_info = self._analyze_module(py_file, "setup")
                        if module_info:
                            modules.append(module_info)
        
        # Chercher dans tests
        tests_path = self.root_path / "tests"
        if tests_path.exists():
            for py_file in tests_path.rglob("*.py"):
                if py_file.name != "__init__.py" and not py_file.name.startswith('._'):
                    if any(re.search(pattern, py_file.name, re.IGNORECASE) for pattern in intelligent_patterns):
                        module_info = self._analyze_module(py_file, "test")
                        if module_info:
                            modules.append(module_info)
        
        self.modules = modules
        print(f"✅ {len(modules)} modules intelligents découverts")
        return modules
    
    def _analyze_module(self, file_path: Path, module_type: str) -> ModuleInfo:
        """Analyser un module Python"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parser le code
            tree = ast.parse(content)
            
            # Extraire les fonctions
            functions = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
            
            # Extraire les classes
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)
            
            # Extraire les imports
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")
            
            # Déterminer le type
            file_name = file_path.name.lower()
            if "intelligent" in file_name:
                module_type_name = "intelligent"
            elif "analyzer" in file_name:
                module_type_name = "analyzer"
            elif "orchestrator" in file_name:
                module_type_name = "orchestrator"
            elif "coordinator" in file_name:
                module_type_name = "coordinator"
            elif "auditor" in file_name:
                module_type_name = "auditor"
            else:
                module_type_name = "other"
            
            # Extraire la description du docstring
            description = ""
            for node in ast.walk(tree):
                if isinstance(node, ast.Module) and node.body:
                    first_node = node.body[0]
                    if isinstance(first_node, ast.Expr) and isinstance(first_node.value, ast.Str):
                        description = first_node.value.s.split('\n')[0]
                        break
            
            return ModuleInfo(
                path=file_path,
                name=file_path.stem,
                type=module_type_name,
                size=len(content.split('\n')),
                functions=functions,
                classes=classes,
                imports=imports,
                description=description
            )
            
        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse de {file_path}: {e}")
            return None
    
    def detect_duplicates(self) -> List[DuplicateInfo]:
        """Détecter les doublons entre modules"""
        print("🔍 Détection des doublons...")
        
        duplicates = []
        
        for i, module1 in enumerate(self.modules):
            for j, module2 in enumerate(self.modules[i+1:], i+1):
                similarity = self._calculate_similarity(module1, module2)
                
                if similarity > 0.3:  # Seuil de similarité
                    common_functions = set(module1.functions) & set(module2.functions)
                    common_classes = set(module1.classes) & set(module2.classes)
                    
                    if common_functions or common_classes:
                        duplicate = DuplicateInfo(
                            module1=f"{module1.path.parent.name}/{module1.name}",
                            module2=f"{module2.path.parent.name}/{module2.name}",
                            similarity=similarity,
                            common_functions=list(common_functions),
                            common_classes=list(common_classes),
                            recommendation=self._generate_duplicate_recommendation(module1, module2, similarity)
                        )
                        duplicates.append(duplicate)
        
        self.duplicates = duplicates
        print(f"✅ {len(duplicates)} doublons détectés")
        return duplicates
    
    def _calculate_similarity(self, module1: ModuleInfo, module2: ModuleInfo) -> float:
        """Calculer la similarité entre deux modules"""
        # Similarité basée sur les fonctions et classes communes
        common_functions = len(set(module1.functions) & set(module2.functions))
        common_classes = len(set(module1.classes) & set(module2.classes))
        
        total_functions = len(set(module1.functions) | set(module2.functions))
        total_classes = len(set(module1.classes) | set(module2.classes))
        
        if total_functions == 0 and total_classes == 0:
            return 0.0
        
        function_similarity = common_functions / total_functions if total_functions > 0 else 0
        class_similarity = common_classes / total_classes if total_classes > 0 else 0
        
        return (function_similarity + class_similarity) / 2
    
    def _generate_duplicate_recommendation(self, module1: ModuleInfo, module2: ModuleInfo, similarity: float) -> str:
        """Générer une recommandation pour un doublon"""
        if similarity > 0.7:
            return f"FUSIONNER: {module1.name} et {module2.name} sont très similaires"
        elif similarity > 0.5:
            return f"RÉFACTORER: {module1.name} et {module2.name} ont des parties communes"
        else:
            return f"RÉVISER: {module1.name} et {module2.name} ont quelques similitudes"
    
    def analyze_intelligence_usage(self) -> Dict[str, Any]:
        """Analyser l'utilisation de l'intelligence"""
        print("🧠 Analyse de l'utilisation de l'intelligence...")
        
        # Statistiques par type
        type_stats = {}
        for module in self.modules:
            if module.type not in type_stats:
                type_stats[module.type] = []
            type_stats[module.type].append(module)
        
        # Analyse des imports
        all_imports = []
        for module in self.modules:
            all_imports.extend(module.imports)
        
        import_stats = {}
        for imp in all_imports:
            if imp not in import_stats:
                import_stats[imp] = 0
            import_stats[imp] += 1
        
        # Recommandations
        recommendations = []
        
        # Vérifier les doublons
        if self.duplicates:
            recommendations.append(f"🔧 {len(self.duplicates)} doublons détectés - fusion recommandée")
        
        # Vérifier la répartition
        if len(type_stats.get("intelligent", [])) > 3:
            recommendations.append("📦 Trop de modules 'intelligent' - consolidation recommandée")
        
        if len(type_stats.get("orchestrator", [])) > 2:
            recommendations.append("🎯 Plusieurs orchestrateurs - unification recommandée")
        
        return {
            "total_modules": len(self.modules),
            "type_distribution": {k: len(v) for k, v in type_stats.items()},
            "duplicates_count": len(self.duplicates),
            "top_imports": sorted(import_stats.items(), key=lambda x: x[1], reverse=True)[:10],
            "recommendations": recommendations
        }
    
    def generate_report(self) -> str:
        """Générer un rapport complet"""
        print("📊 Génération du rapport...")
        
        report = []
        report.append("# 🔍 RAPPORT D'ANALYSE DE L'INTELLIGENCE")
        report.append("=" * 60)
        
        # Résumé
        usage_analysis = self.analyze_intelligence_usage()
        report.append(f"\n## 📊 RÉSUMÉ")
        report.append(f"- **Total modules intelligents** : {usage_analysis['total_modules']}")
        report.append(f"- **Doublons détectés** : {usage_analysis['duplicates_count']}")
        report.append(f"- **Types de modules** : {len(usage_analysis['type_distribution'])}")
        
        # Distribution par type
        report.append(f"\n## 📦 DISTRIBUTION PAR TYPE")
        for module_type, count in usage_analysis['type_distribution'].items():
            report.append(f"- **{module_type}** : {count} modules")
        
        # Modules détaillés
        report.append(f"\n## 📋 MODULES DÉTAILLÉS")
        for module in self.modules:
            report.append(f"\n### {module.path.parent.name}/{module.name}")
            report.append(f"- **Type** : {module.type}")
            report.append(f"- **Taille** : {module.size} lignes")
            report.append(f"- **Fonctions** : {len(module.functions)}")
            report.append(f"- **Classes** : {len(module.classes)}")
            if module.description:
                report.append(f"- **Description** : {module.description}")
        
        # Doublons
        if self.duplicates:
            report.append(f"\n## 🔧 DOUBLONS DÉTECTÉS")
            for dup in self.duplicates:
                report.append(f"\n### {dup.module1} ↔ {dup.module2}")
                report.append(f"- **Similarité** : {dup.similarity:.1%}")
                if dup.common_functions:
                    report.append(f"- **Fonctions communes** : {', '.join(dup.common_functions)}")
                if dup.common_classes:
                    report.append(f"- **Classes communes** : {', '.join(dup.common_classes)}")
                report.append(f"- **Recommandation** : {dup.recommendation}")
        
        # Recommandations
        if usage_analysis['recommendations']:
            report.append(f"\n## 💡 RECOMMANDATIONS")
            for rec in usage_analysis['recommendations']:
                report.append(f"- {rec}")
        
        # Imports les plus utilisés
        report.append(f"\n## 📚 IMPORTS LES PLUS UTILISÉS")
        for import_name, count in usage_analysis['top_imports']:
            report.append(f"- **{import_name}** : {count} fois")
        
        return "\n".join(report)

def main():
    """Analyse complète de l'utilisation de l'intelligence"""
    print("🔍 ANALYSE DE L'UTILISATION DE L'INTELLIGENCE")
    print("=" * 60)
    
    analyzer = IntelligenceAnalyzer()
    
    # Découvrir les modules
    modules = analyzer.discover_intelligent_modules()
    
    # Détecter les doublons
    duplicates = analyzer.detect_duplicates()
    
    # Analyser l'utilisation
    usage = analyzer.analyze_intelligence_usage()
    
    # Générer le rapport
    report = analyzer.generate_report()
    
    # Afficher le rapport
    print("\n" + "=" * 60)
    print("📊 RAPPORT FINAL")
    print("=" * 60)
    print(report)
    
    # Sauvegarder le rapport
    report_file = Path("intelligence_analysis_report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n📄 Rapport sauvegardé dans : {report_file}")
    
    # Résumé exécutif
    print(f"\n🎯 RÉSUMÉ EXÉCUTIF:")
    print(f"  📦 Modules intelligents : {usage['total_modules']}")
    print(f"  🔧 Doublons détectés : {usage['duplicates_count']}")
    print(f"  💡 Recommandations : {len(usage['recommendations'])}")
    
    if usage['duplicates_count'] > 0:
        print(f"\n⚠️ ATTENTION : {usage['duplicates_count']} doublons détectés !")
        print("   Consultez le rapport pour les détails.")
    else:
        print(f"\n✅ Aucun doublon détecté !")

if __name__ == "__main__":
    main() 
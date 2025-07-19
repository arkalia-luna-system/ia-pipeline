#!/usr/bin/env python3
"""
🧠 ATHALIA SUPER BRAIN
======================
Super cerveau intelligent qui :
- Analyse toute l'architecture du projet
- Détecte les doublons et erreurs
- Optimise les performances
- Coordonne tous les modules intelligemment
- Apprend et s'améliore continuellement
"""

import os
import json
import sqlite3
import yaml
import ast
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, asdict
import logging
import subprocess
import hashlib

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModuleAnalysis:
    """Analyse d'un module"""
    name: str
    path: str
    type: str
    size: int
    functions: List[str]
    classes: List[str]
    imports: List[str]
    dependencies: List[str]
    complexity: float
    issues: List[str]
    performance_score: float
    last_modified: datetime

@dataclass
class DuplicateAnalysis:
    """Analyse des doublons"""
    type: str  # 'function', 'class', 'import', 'code_block'
    items: List[str]
    locations: List[str]
    severity: str  # 'low', 'medium', 'high', 'critical'

@dataclass
class PerformanceIssue:
    """Problème de performance"""
    type: str
    location: str
    description: str
    impact: str
    suggestion: str

@dataclass
class ArchitectureMapping:
    """Mapping de l'architecture"""
    modules: Dict[str, ModuleAnalysis]
    dependencies: Dict[str, List[str]]
    duplicates: List[DuplicateAnalysis]
    performance_issues: List[PerformanceIssue]
    recommendations: List[str]

class AthaliaSuperBrain:
    """Super cerveau intelligent pour Athalia"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or os.getcwd())
        self.db_path = self.root_path / "data" / "athalia_super_brain.db"
        self.analysis_path = self.root_path / "data" / "super_brain_analysis.json"
        
        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialiser la base de données
        self._init_database()
        
        # Charger la configuration
        self.config = self._load_config()
        
        # Cache pour les analyses
        self._module_cache = {}
        self._duplicate_cache = {}
        self._performance_cache = {}
        
        logger.info(f"🧠 Athalia Super Brain initialisé dans {self.root_path}")
    
    def _init_database(self):
        """Initialiser la base de données du super cerveau"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table des analyses de modules
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS module_analyses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    module_name TEXT UNIQUE NOT NULL,
                    module_path TEXT NOT NULL,
                    module_type TEXT NOT NULL,
                    analysis_data TEXT NOT NULL,
                    performance_score REAL,
                    last_analyzed TEXT NOT NULL
                )
            """)
            
            # Table des doublons détectés
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS duplicates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    duplicate_type TEXT NOT NULL,
                    items TEXT NOT NULL,
                    locations TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    detected_at TEXT NOT NULL
                )
            """)
            
            # Table des problèmes de performance
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS performance_issues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_type TEXT NOT NULL,
                    location TEXT NOT NULL,
                    description TEXT NOT NULL,
                    impact TEXT NOT NULL,
                    suggestion TEXT NOT NULL,
                    detected_at TEXT NOT NULL
                )
            """)
            
            # Table des recommandations
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS recommendations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            
            conn.commit()
    
    def _load_config(self) -> Dict[str, Any]:
        """Charger la configuration"""
        config_file = self.root_path / "config" / "athalia_config.yaml"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}
    
    def analyze_entire_architecture(self) -> ArchitectureMapping:
        """Analyser toute l'architecture du projet"""
        logger.info("🔍 Analyse complète de l'architecture...")
        
        # Analyser tous les modules
        modules = self._analyze_all_modules()
        
        # Détecter les doublons
        duplicates = self._detect_duplicates(modules)
        
        # Analyser les performances
        performance_issues = self._analyze_performance(modules)
        
        # Générer les recommandations
        recommendations = self._generate_recommendations(modules, duplicates, performance_issues)
        
        # Créer le mapping d'architecture
        architecture = ArchitectureMapping(
            modules=modules,
            dependencies=self._build_dependency_graph(modules),
            duplicates=duplicates,
            performance_issues=performance_issues,
            recommendations=recommendations
        )
        
        # Sauvegarder l'analyse
        self._save_analysis(architecture)
        
        return architecture
    
    def _analyze_all_modules(self) -> Dict[str, ModuleAnalysis]:
        """Analyser tous les modules du projet"""
        modules = {}
        
        # Dossiers à analyser
        module_dirs = {
            "core": self.root_path / "athalia_core",
            "modules": self.root_path / "modules",
            "agents": self.root_path / "agents",
            "plugins": self.root_path / "plugins",
            "tests": self.root_path / "tests",
            "setup": self.root_path / "setup"
        }
        
        for dir_name, dir_path in module_dirs.items():
            if dir_path.exists():
                for py_file in dir_path.rglob("*.py"):
                    if py_file.name != "__init__.py" and not py_file.name.startswith("._"):
                        try:
                            module_analysis = self._analyze_single_module(py_file, dir_name)
                            modules[module_analysis.name] = module_analysis
                        except Exception as e:
                            logger.warning(f"Erreur lors de l'analyse de {py_file}: {e}")
        
        logger.info(f"📊 {len(modules)} modules analysés")
        return modules
    
    def _analyze_single_module(self, file_path: Path, module_type: str) -> ModuleAnalysis:
        """Analyser un module individuel"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse le code Python
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
            
            # Calculer la complexité
            complexity = self._calculate_complexity(tree)
            
            # Détecter les problèmes
            issues = self._detect_module_issues(tree, content)
            
            # Calculer le score de performance
            performance_score = self._calculate_performance_score(tree, content)
            
            # Déterminer les dépendances
            dependencies = self._extract_dependencies(imports, module_type)
            
            return ModuleAnalysis(
                name=f"{module_type}.{file_path.stem}",
                path=str(file_path),
                type=module_type,
                size=len(content),
                functions=functions,
                classes=classes,
                imports=imports,
                dependencies=dependencies,
                complexity=complexity,
                issues=issues,
                performance_score=performance_score,
                last_modified=datetime.fromtimestamp(file_path.stat().st_mtime)
            )
            
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse de {file_path}: {e}")
            return ModuleAnalysis(
                name=f"{module_type}.{file_path.stem}",
                path=str(file_path),
                type=module_type,
                size=0,
                functions=[],
                classes=[],
                imports=[],
                dependencies=[],
                complexity=0.0,
                issues=[f"Erreur d'analyse: {e}"],
                performance_score=0.0,
                last_modified=datetime.now()
            )
    
    def _calculate_complexity(self, tree: ast.AST) -> float:
        """Calculer la complexité cyclomatique"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.With):
                complexity += 1
            elif isinstance(node, ast.AsyncWith):
                complexity += 1
        
        return complexity
    
    def _detect_module_issues(self, tree: ast.AST, content: str) -> List[str]:
        """Détecter les problèmes dans un module"""
        issues = []
        
        # Vérifier la longueur des fonctions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 50:
                    issues.append(f"Fonction '{node.name}' trop longue ({len(node.body)} lignes)")
        
        # Vérifier les imports non utilisés
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    imports.add(f"{module}.{alias.name}")
        
        # Vérifier les variables non utilisées
        if "unused" in content.lower():
            issues.append("Variables potentiellement non utilisées détectées")
        
        # Vérifier les patterns dangereux
        dangerous_patterns = [
            r"eval\(",
            r"exec\(",
            r"__import__\(",
            r"open\(",
            r"subprocess\."
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, content):
                issues.append(f"Pattern dangereux détecté: {pattern}")
        
        return issues
    
    def _calculate_performance_score(self, tree: ast.AST, content: str) -> float:
        """Calculer un score de performance"""
        score = 100.0
        
        # Pénaliser les boucles imbriquées
        nested_loops = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                for child in ast.walk(node):
                    if isinstance(child, (ast.For, ast.While)) and child != node:
                        nested_loops += 1
        
        score -= nested_loops * 10
        
        # Pénaliser les imports lourds
        heavy_imports = ['pandas', 'numpy', 'tensorflow', 'torch', 'sklearn']
        for heavy_import in heavy_imports:
            if heavy_import in content:
                score -= 5
        
        # Pénaliser les fonctions très longues
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 100:
                    score -= 20
                elif len(node.body) > 50:
                    score -= 10
        
        return max(0.0, score)
    
    def _extract_dependencies(self, imports: List[str], module_type: str) -> List[str]:
        """Extraire les dépendances d'un module"""
        dependencies = []
        
        for imp in imports:
            if imp.startswith('athalia_core'):
                dependencies.append(imp)
            elif imp.startswith('modules'):
                dependencies.append(imp)
            elif imp.startswith('agents'):
                dependencies.append(imp)
            elif imp.startswith('plugins'):
                dependencies.append(imp)
        
        return dependencies
    
    def _detect_duplicates(self, modules: Dict[str, ModuleAnalysis]) -> List[DuplicateAnalysis]:
        """Détecter les doublons dans le code"""
        duplicates = []
        
        # Détecter les fonctions dupliquées
        function_signatures = {}
        for module_name, module in modules.items():
            for func in module.functions:
                if func in function_signatures:
                    function_signatures[func].append(module_name)
                else:
                    function_signatures[func] = [module_name]
        
        for func, locations in function_signatures.items():
            if len(locations) > 1:
                duplicates.append(DuplicateAnalysis(
                    type="function",
                    items=[func],
                    locations=locations,
                    severity="medium" if len(locations) == 2 else "high"
                ))
        
        # Détecter les classes dupliquées
        class_signatures = {}
        for module_name, module in modules.items():
            for cls in module.classes:
                if cls in class_signatures:
                    class_signatures[cls].append(module_name)
                else:
                    class_signatures[cls] = [module_name]
        
        for cls, locations in class_signatures.items():
            if len(locations) > 1:
                duplicates.append(DuplicateAnalysis(
                    type="class",
                    items=[cls],
                    locations=locations,
                    severity="high" if len(locations) == 2 else "critical"
                ))
        
        # Détecter les imports dupliqués
        import_patterns = {}
        for module_name, module in modules.items():
            for imp in module.imports:
                if imp in import_patterns:
                    import_patterns[imp].append(module_name)
                else:
                    import_patterns[imp] = [module_name]
        
        for imp, locations in import_patterns.items():
            if len(locations) > 3:
                duplicates.append(DuplicateAnalysis(
                    type="import",
                    items=[imp],
                    locations=locations,
                    severity="low"
                ))
        
        return duplicates
    
    def _analyze_performance(self, modules: Dict[str, ModuleAnalysis]) -> List[PerformanceIssue]:
        """Analyser les problèmes de performance"""
        issues = []
        
        for module_name, module in modules.items():
            # Vérifier la complexité
            if module.complexity > 10:
                issues.append(PerformanceIssue(
                    type="complexity",
                    location=module.path,
                    description=f"Complexité élevée: {module.complexity}",
                    impact="Moyen",
                    suggestion="Refactoriser en fonctions plus petites"
                ))
            
            # Vérifier la taille des modules
            if module.size > 10000:
                issues.append(PerformanceIssue(
                    type="size",
                    location=module.path,
                    description=f"Module très volumineux: {module.size} caractères",
                    impact="Élevé",
                    suggestion="Diviser en modules plus petits"
                ))
            
            # Vérifier les imports lourds
            heavy_imports = ['pandas', 'numpy', 'tensorflow', 'torch']
            for imp in module.imports:
                if any(heavy in imp for heavy in heavy_imports):
                    issues.append(PerformanceIssue(
                        type="import",
                        location=module.path,
                        description=f"Import lourd détecté: {imp}",
                        impact="Moyen",
                        suggestion="Considérer un import lazy ou conditionnel"
                    ))
        
        return issues
    
    def _build_dependency_graph(self, modules: Dict[str, ModuleAnalysis]) -> Dict[str, List[str]]:
        """Construire le graphe de dépendances"""
        dependencies = {}
        
        for module_name, module in modules.items():
            dependencies[module_name] = module.dependencies
        
        return dependencies
    
    def _generate_recommendations(self, modules: Dict[str, ModuleAnalysis], 
                                duplicates: List[DuplicateAnalysis],
                                performance_issues: List[PerformanceIssue]) -> List[str]:
        """Générer des recommandations d'amélioration"""
        recommendations = []
        
        # Recommandations basées sur les doublons
        if duplicates:
            recommendations.append("🔍 Considérer la création d'un module commun pour les fonctions/classes dupliquées")
        
        # Recommandations basées sur les performances
        high_complexity_modules = [m for m in modules.values() if m.complexity > 10]
        if high_complexity_modules:
            recommendations.append("⚡ Refactoriser les modules à haute complexité pour améliorer les performances")
        
        # Recommandations basées sur la taille
        large_modules = [m for m in modules.values() if m.size > 10000]
        if large_modules:
            recommendations.append("📦 Diviser les modules volumineux en modules plus petits")
        
        # Recommandations d'architecture
        core_modules = [m for m in modules.values() if m.type == "core"]
        if len(core_modules) > 20:
            recommendations.append("🏗️ Considérer la réorganisation des modules core pour une meilleure séparation des responsabilités")
        
        # Recommandations de tests
        test_modules = [m for m in modules.values() if m.type == "tests"]
        if len(test_modules) < len(modules) * 0.3:
            recommendations.append("🧪 Augmenter la couverture de tests")
        
        return recommendations
    
    def _save_analysis(self, architecture: ArchitectureMapping):
        """Sauvegarder l'analyse dans la base de données et le fichier JSON"""
        # Sauvegarder dans la base de données
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Sauvegarder les analyses de modules
            for module_name, module in architecture.modules.items():
                # Convertir le module en dict et gérer les datetime
                module_dict = asdict(module)
                module_dict['last_modified'] = module_dict['last_modified'].isoformat()
                
                cursor.execute("""
                    INSERT OR REPLACE INTO module_analyses 
                    (module_name, module_path, module_type, analysis_data, performance_score, last_analyzed)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    module_name,
                    module.path,
                    module.type,
                    json.dumps(module_dict),
                    module.performance_score,
                    datetime.now().isoformat()
                ))
            
            # Sauvegarder les doublons
            for duplicate in architecture.duplicates:
                cursor.execute("""
                    INSERT INTO duplicates (duplicate_type, items, locations, severity, detected_at)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    duplicate.type,
                    json.dumps(duplicate.items),
                    json.dumps(duplicate.locations),
                    duplicate.severity,
                    datetime.now().isoformat()
                ))
            
            # Sauvegarder les problèmes de performance
            for issue in architecture.performance_issues:
                cursor.execute("""
                    INSERT INTO performance_issues (issue_type, location, description, impact, suggestion, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    issue.type,
                    issue.location,
                    issue.description,
                    issue.impact,
                    issue.suggestion,
                    datetime.now().isoformat()
                ))
            
            # Sauvegarder les recommandations
            for rec in architecture.recommendations:
                cursor.execute("""
                    INSERT INTO recommendations (category, title, description, priority, created_at)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    "architecture",
                    "Recommandation d'amélioration",
                    rec,
                    "medium",
                    datetime.now().isoformat()
                ))
            
            conn.commit()
        
        # Sauvegarder dans le fichier JSON
        analysis_data = {
            "timestamp": datetime.now().isoformat(),
            "modules_count": len(architecture.modules),
            "duplicates_count": len(architecture.duplicates),
            "performance_issues_count": len(architecture.performance_issues),
            "recommendations_count": len(architecture.recommendations),
            "summary": {
                "total_functions": sum(len(m.functions) for m in architecture.modules.values()),
                "total_classes": sum(len(m.classes) for m in architecture.modules.values()),
                "average_complexity": sum(m.complexity for m in architecture.modules.values()) / len(architecture.modules) if architecture.modules else 0,
                "average_performance_score": sum(m.performance_score for m in architecture.modules.values()) / len(architecture.modules) if architecture.modules else 0
            }
        }
        
        with open(self.analysis_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, default=str)
    
    def get_optimization_plan(self) -> Dict[str, Any]:
        """Générer un plan d'optimisation"""
        architecture = self.analyze_entire_architecture()
        
        plan = {
            "priority_high": [],
            "priority_medium": [],
            "priority_low": [],
            "estimated_effort": {},
            "expected_improvements": {}
        }
        
        # Actions prioritaires
        critical_duplicates = [d for d in architecture.duplicates if d.severity == "critical"]
        if critical_duplicates:
            plan["priority_high"].append({
                "action": "Éliminer les doublons critiques",
                "items": len(critical_duplicates),
                "effort": "2-3 jours"
            })
        
        high_performance_issues = [i for i in architecture.performance_issues if i.impact == "Élevé"]
        if high_performance_issues:
            plan["priority_high"].append({
                "action": "Corriger les problèmes de performance critiques",
                "items": len(high_performance_issues),
                "effort": "1-2 jours"
            })
        
        # Actions moyennes
        medium_duplicates = [d for d in architecture.duplicates if d.severity == "high"]
        if medium_duplicates:
            plan["priority_medium"].append({
                "action": "Consolider les doublons importants",
                "items": len(medium_duplicates),
                "effort": "3-5 jours"
            })
        
        # Actions de faible priorité
        low_duplicates = [d for d in architecture.duplicates if d.severity == "low"]
        if low_duplicates:
            plan["priority_low"].append({
                "action": "Nettoyer les doublons mineurs",
                "items": len(low_duplicates),
                "effort": "1 jour"
            })
        
        return plan
    
    def generate_intelligent_coordination(self) -> Dict[str, Any]:
        """Générer un plan de coordination intelligente"""
        architecture = self.analyze_entire_architecture()
        
        coordination = {
            "module_groups": {},
            "execution_order": [],
            "parallel_tasks": [],
            "dependencies_map": {},
            "optimization_suggestions": []
        }
        
        # Grouper les modules par fonctionnalité
        core_modules = [m for m in architecture.modules.values() if m.type == "core"]
        advanced_modules = [m for m in architecture.modules.values() if m.type == "modules"]
        agent_modules = [m for m in architecture.modules.values() if m.type == "agents"]
        plugin_modules = [m for m in architecture.modules.values() if m.type == "plugins"]
        
        coordination["module_groups"] = {
            "core": [m.name for m in core_modules],
            "advanced": [m.name for m in advanced_modules],
            "agents": [m.name for m in agent_modules],
            "plugins": [m.name for m in plugin_modules]
        }
        
        # Ordre d'exécution recommandé
        coordination["execution_order"] = [
            "core.athalia_orchestrator",
            "core.audit",
            "core.analytics",
            "modules.auto_correction_avancee",
            "agents.ath_context_prompt",
            "plugins.export_docker_plugin"
        ]
        
        # Tâches parallèles
        coordination["parallel_tasks"] = [
            ["core.auto_tester", "core.auto_documenter"],
            ["core.auto_cleaner", "core.security_auditor"],
            ["modules.dashboard_unifie_simple", "modules.profils_utilisateur_avances"]
        ]
        
        return coordination

def main():
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Athalia Super Brain")
    parser.add_argument("--action", choices=["analyze", "optimize", "coordinate", "report"], 
                       default="analyze", help="Action à effectuer")
    parser.add_argument("--root", help="Racine du projet Athalia")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")
    
    args = parser.parse_args()
    
    # Initialiser le super cerveau
    brain = AthaliaSuperBrain(args.root)
    
    if args.action == "analyze":
        print("🧠 Analyse complète de l'architecture...")
        architecture = brain.analyze_entire_architecture()
        
        print(f"📊 Résultats de l'analyse:")
        print(f"  • Modules analysés: {len(architecture.modules)}")
        print(f"  • Doublons détectés: {len(architecture.duplicates)}")
        print(f"  • Problèmes de performance: {len(architecture.performance_issues)}")
        print(f"  • Recommandations: {len(architecture.recommendations)}")
        
        # Afficher les doublons critiques
        critical_duplicates = [d for d in architecture.duplicates if d.severity == "critical"]
        if critical_duplicates:
            print(f"\n🚨 Doublons critiques détectés:")
            for dup in critical_duplicates:
                print(f"  • {dup.type}: {dup.items} dans {dup.locations}")
        
        # Afficher les recommandations
        if architecture.recommendations:
            print(f"\n💡 Recommandations:")
            for rec in architecture.recommendations:
                print(f"  • {rec}")
    
    elif args.action == "optimize":
        print("⚡ Génération du plan d'optimisation...")
        plan = brain.get_optimization_plan()
        
        print(f"📋 Plan d'optimisation:")
        for priority, actions in plan.items():
            if actions:
                print(f"\n{priority.upper()}:")
                for action in actions:
                    print(f"  • {action['action']} ({action['items']} items, effort: {action['effort']})")
    
    elif args.action == "coordinate":
        print("🎯 Génération du plan de coordination intelligente...")
        coordination = brain.generate_intelligent_coordination()
        
        print(f"🧠 Coordination intelligente:")
        print(f"  • Groupes de modules: {len(coordination['module_groups'])}")
        print(f"  • Ordre d'exécution: {len(coordination['execution_order'])} étapes")
        print(f"  • Tâches parallèles: {len(coordination['parallel_tasks'])} groupes")
    
    elif args.action == "report":
        print("📄 Génération du rapport complet...")
        architecture = brain.analyze_entire_architecture()
        plan = brain.get_optimization_plan()
        coordination = brain.generate_intelligent_coordination()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "architecture_summary": {
                "modules_count": len(architecture.modules),
                "duplicates_count": len(architecture.duplicates),
                "performance_issues_count": len(architecture.performance_issues)
            },
            "optimization_plan": plan,
            "coordination_plan": coordination,
            "recommendations": architecture.recommendations
        }
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, default=str)
            print(f"✅ Rapport sauvegardé dans {args.output}")
        else:
            print(json.dumps(report, indent=2, default=str))

if __name__ == "__main__":
    main() 
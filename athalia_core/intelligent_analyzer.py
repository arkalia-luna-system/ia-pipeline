#!/usr/bin/env python3
"""
🧠 ANALYSEUR INTELLIGENT ATHALIA - ORCHESTRATEUR PRINCIPAL
==========================================================
Orchestrateur principal qui coordonne tous les modules d'analyse :
- AST Analyzer (analyse de base)
- Pattern Detector (détection de patterns et doublons)
- Architecture Analyzer (analyse d'architecture)
- Performance Analyzer (analyse de performance)
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import json

from .ast_analyzer import ASTAnalyzer
from .pattern_detector import PatternDetector
from .architecture_analyzer import ArchitectureAnalyzer
from .performance_analyzer import PerformanceAnalyzer

# Import de l'orchestrateur unifié (optionnel)
try:
    from .unified_orchestrator import UnifiedOrchestrator
    UNIFIED_ORCHESTRATOR_AVAILABLE = True
except ImportError:
    UNIFIED_ORCHESTRATOR_AVAILABLE = False

logger = logging.getLogger(__name__)

@dataclass
class ComprehensiveAnalysis:
    """Analyse complète du projet"""
    project_name: str
    analysis_date: datetime
    ast_analysis: Dict[str, Any]
    pattern_analysis: Dict[str, Any]
    architecture_analysis: Dict[str, Any]
    performance_analysis: Dict[str, Any]
    overall_score: float
    recommendations: List[str]
    optimization_plan: Dict[str, Any]

class IntelligentAnalyzer:
    """Orchestrateur principal de l'analyse intelligente"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        
        # Initialiser tous les analyseurs spécialisés
        self.ast_analyzer = ASTAnalyzer()
        self.pattern_detector = PatternDetector(self.root_path)
        self.architecture_analyzer = ArchitectureAnalyzer(self.root_path)
        self.performance_analyzer = PerformanceAnalyzer(self.root_path)
        
        logger.info(f"🧠 Intelligent Analyzer initialisé dans {self.root_path}")
    
    def analyze_project_comprehensive(self, project_path: str = None) -> ComprehensiveAnalysis:
        """Analyser un projet de manière complète avec tous les modules"""
        project_path = Path(project_path or self.root_path)
        project_name = project_path.name
        
        logger.info(f"🧠 Analyse complète du projet: {project_name}")
        
        # 1. Analyse AST de base
        logger.info("📊 Étape 1/4: Analyse AST de base...")
        ast_analysis = self._perform_ast_analysis(project_path)
        
        # 2. Analyse des patterns et doublons
        logger.info("🔍 Étape 2/4: Analyse des patterns et doublons...")
        pattern_analysis = self.pattern_detector.analyze_project_patterns(project_path)
        
        # 3. Analyse d'architecture
        logger.info("🏗️ Étape 3/4: Analyse d'architecture...")
        architecture_analysis = self.architecture_analyzer.analyze_entire_architecture()
        
        # 4. Analyse de performance
        logger.info("⚡ Étape 4/4: Analyse de performance...")
        performance_analysis = self.performance_analyzer.analyze_project_performance(project_path)
        
        # Calculer le score global
        overall_score = self._calculate_overall_score(
            ast_analysis, pattern_analysis, architecture_analysis, performance_analysis
        )
        
        # Générer les recommandations globales
        recommendations = self._generate_comprehensive_recommendations(
            pattern_analysis, architecture_analysis, performance_analysis
        )
        
        # Créer le plan d'optimisation
        optimization_plan = self._create_optimization_plan(
            pattern_analysis, architecture_analysis, performance_analysis
        )
        
        # Créer l'analyse complète
        comprehensive_analysis = ComprehensiveAnalysis(
            project_name=project_name,
            analysis_date=datetime.now(),
            ast_analysis=ast_analysis,
            pattern_analysis=pattern_analysis,
            architecture_analysis=architecture_analysis,
            performance_analysis=performance_analysis,
            overall_score=overall_score,
            recommendations=recommendations,
            optimization_plan=optimization_plan
        )
        
        # Sauvegarder l'analyse complète
        self._save_comprehensive_analysis(comprehensive_analysis)
        
        logger.info(f"✅ Analyse complète terminée - Score global: {overall_score:.1f}/100")
        
        return comprehensive_analysis
    
    def _perform_ast_analysis(self, project_path: Path) -> Dict[str, Any]:
        """Effectuer l'analyse AST de base"""
        python_files = list(project_path.rglob("*.py"))
        file_analyses = []
        
        for py_file in python_files:
            try:
                file_analysis = self.ast_analyzer.analyze_file(py_file)
                if file_analysis:
                    file_analyses.append({
                        "file_path": str(file_analysis.file_path),
                        "functions_count": len(file_analysis.functions),
                        "classes_count": len(file_analysis.classes),
                        "complexity_score": file_analysis.complexity_score,
                        "total_lines": file_analysis.total_lines
                    })
            except Exception as e:
                logger.warning(f"Erreur lors de l'analyse AST de {py_file}: {e}")
        
        return {
            "files_analyzed": len(file_analyses),
            "total_files": len(python_files),
            "file_details": file_analyses,
            "summary": {
                "total_functions": sum(f["functions_count"] for f in file_analyses),
                "total_classes": sum(f["classes_count"] for f in file_analyses),
                "average_complexity": sum(f["complexity_score"] for f in file_analyses) / len(file_analyses) if file_analyses else 0
            }
        }
    
    def _calculate_overall_score(self, ast_analysis: Dict[str, Any], 
                               pattern_analysis: Dict[str, Any],
                               architecture_analysis: Any,
                               performance_analysis: Any) -> float:
        """Calculer le score global basé sur toutes les analyses"""
        scores = []
        weights = []
        
        # Score AST (complexité et structure)
        if ast_analysis["files_analyzed"] > 0:
            avg_complexity = ast_analysis["summary"]["average_complexity"]
            ast_score = max(0, 100 - (avg_complexity * 3))
            scores.append(ast_score)
            weights.append(2.0)
        
        # Score Patterns (qualité du code)
        pattern_score = 100
        if pattern_analysis["duplicates"]:
            pattern_score -= len(pattern_analysis["duplicates"]) * 5
        if pattern_analysis["antipatterns"]:
            pattern_score -= len(pattern_analysis["antipatterns"]) * 3
        pattern_score = max(0, pattern_score)
        scores.append(pattern_score)
        weights.append(2.5)
        
        # Score Architecture (structure du projet)
        arch_score = 100
        if architecture_analysis.performance_issues:
            arch_score -= len(architecture_analysis.performance_issues) * 4
        arch_score = max(0, arch_score)
        scores.append(arch_score)
        weights.append(2.0)
        
        # Score Performance
        perf_score = performance_analysis.overall_score
        scores.append(perf_score)
        weights.append(3.5)
        
        # Calculer la moyenne pondérée
        total_score = sum(score * weight for score, weight in zip(scores, weights))
        total_weight = sum(weights)
        
        return total_score / total_weight if total_weight > 0 else 100.0
    
    def _generate_comprehensive_recommendations(self, pattern_analysis: Dict[str, Any],
                                              architecture_analysis: Any,
                                              performance_analysis: Any) -> List[str]:
        """Générer des recommandations globales"""
        recommendations = []
        
        # Recommandations des patterns
        if pattern_analysis["duplicates"]:
            high_severity_duplicates = [d for d in pattern_analysis["duplicates"] if d.severity in ["high", "medium"]]
            if high_severity_duplicates:
                recommendations.append(f"🔧 {len(high_severity_duplicates)} doublons critiques - fusion prioritaire")
        
        if pattern_analysis["antipatterns"]:
            high_impact_antipatterns = [a for a in pattern_analysis["antipatterns"] if a.impact in ["high", "critical"]]
            if high_impact_antipatterns:
                recommendations.append(f"⚠️ {len(high_impact_antipatterns)} anti-patterns critiques - refactoring urgent")
        
        # Recommandations d'architecture
        if architecture_analysis.performance_issues:
            recommendations.append(f"🏗️ {len(architecture_analysis.performance_issues)} problèmes d'architecture détectés")
        
        # Recommandations de performance
        if performance_analysis.issues:
            high_impact_perf_issues = [i for i in performance_analysis.issues if i.impact in ["high", "critical"]]
            if high_impact_perf_issues:
                recommendations.append(f"⚡ {len(high_impact_perf_issues)} problèmes de performance critiques")
        
        # Recommandations générales
        if recommendations:
            recommendations.append("📊 Considérer l'implémentation d'un système de métriques continues")
            recommendations.append("🔄 Planifier des sessions de refactoring régulières")
        
        return recommendations
    
    def _create_optimization_plan(self, pattern_analysis: Dict[str, Any],
                                architecture_analysis: Any,
                                performance_analysis: Any) -> Dict[str, Any]:
        """Créer un plan d'optimisation global"""
        plan = {
            "priority_tasks": [],
            "medium_priority_tasks": [],
            "low_priority_tasks": [],
            "estimated_effort": 0,
            "expected_improvement": 0
        }
        
        # Tâches prioritaires (impact élevé)
        if pattern_analysis["duplicates"]:
            high_severity_duplicates = [d for d in pattern_analysis["duplicates"] if d.severity == "high"]
            if high_severity_duplicates:
                plan["priority_tasks"].append({
                    "task": "merge_high_severity_duplicates",
                    "description": f"Fusionner {len(high_severity_duplicates)} doublons critiques",
                    "effort": "high",
                    "impact": "high"
                })
                plan["estimated_effort"] += len(high_severity_duplicates) * 2  # heures
        
        if performance_analysis.issues:
            critical_perf_issues = [i for i in performance_analysis.issues if i.impact == "critical"]
            if critical_perf_issues:
                plan["priority_tasks"].append({
                    "task": "fix_critical_performance_issues",
                    "description": f"Corriger {len(critical_perf_issues)} problèmes de performance critiques",
                    "effort": "high",
                    "impact": "high"
                })
                plan["estimated_effort"] += len(critical_perf_issues) * 3  # heures
        
        # Tâches de priorité moyenne
        if pattern_analysis["antipatterns"]:
            medium_impact_antipatterns = [a for a in pattern_analysis["antipatterns"] if a.impact == "medium"]
            if medium_impact_antipatterns:
                plan["medium_priority_tasks"].append({
                    "task": "refactor_medium_impact_antipatterns",
                    "description": f"Refactoriser {len(medium_impact_antipatterns)} anti-patterns",
                    "effort": "medium",
                    "impact": "medium"
                })
                plan["estimated_effort"] += len(medium_impact_antipatterns) * 1.5  # heures
        
        # Calculer l'amélioration attendue
        total_improvement = 0
        if performance_analysis.issues:
            total_improvement += sum(i.estimated_improvement for i in performance_analysis.issues)
        
        plan["expected_improvement"] = total_improvement
        
        return plan
    
    def _save_comprehensive_analysis(self, analysis: ComprehensiveAnalysis):
        """Sauvegarder l'analyse complète"""
        output_file = self.root_path / "data" / f"comprehensive_analysis_{analysis.project_name}_{analysis.analysis_date.strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convertir en dictionnaire pour la sérialisation JSON
        analysis_dict = {
            "project_name": analysis.project_name,
            "analysis_date": analysis.analysis_date.isoformat(),
            "overall_score": analysis.overall_score,
            "recommendations": analysis.recommendations,
            "optimization_plan": analysis.optimization_plan,
            "ast_analysis": analysis.ast_analysis,
            "pattern_analysis": {
                "summary": analysis.pattern_analysis["summary"],
                "duplicates_count": len(analysis.pattern_analysis["duplicates"]),
                "antipatterns_count": len(analysis.pattern_analysis["antipatterns"])
            },
            "architecture_analysis": {
                "modules_count": len(analysis.architecture_analysis.modules),
                "performance_issues_count": len(analysis.architecture_analysis.performance_issues)
            },
            "performance_analysis": {
                "overall_score": analysis.performance_analysis.overall_score,
                "issues_count": len(analysis.performance_analysis.issues)
            }
        }
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_dict, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Analyse sauvegardée dans {output_file}")
    
    def get_learning_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'apprentissage de tous les modules"""
        return {
            "ast_insights": "Analyse AST de base disponible",
            "pattern_insights": self.pattern_detector.get_learning_insights(),
            "architecture_insights": self.architecture_analyzer.get_optimization_plan(),
            "performance_insights": self.performance_analyzer.get_performance_insights()
        }
    
    def generate_intelligent_coordination(self) -> Dict[str, Any]:
        """Générer une coordination intelligente"""
        return {
            "timestamp": datetime.now().isoformat(),
            "modules_available": {
                "ast_analyzer": True,
                "pattern_detector": True,
                "architecture_analyzer": True,
                "performance_analyzer": True,
                "unified_orchestrator": UNIFIED_ORCHESTRATOR_AVAILABLE
            },
            "recommendations": [
                "Utiliser l'analyse complète pour les projets complexes",
                "Activer l'orchestrateur unifié pour l'industrialisation complète"
            ]
        }
    
    def orchestrate_with_unified(self, project_path: str = None, 
                               config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Utiliser l'orchestrateur unifié pour une orchestration complète"""
        if not UNIFIED_ORCHESTRATOR_AVAILABLE:
            logger.warning("Orchestrateur unifié non disponible, utilisation de l'analyse standard")
            return self.analyze_project_comprehensive(project_path)
        
        logger.info("🎯 Utilisation de l'orchestrateur unifié")
        unified_orchestrator = UnifiedOrchestrator(self.root_path)
        return unified_orchestrator.orchestrate_project_complete(project_path, config)

def main():
    """Fonction principale pour l'analyse en ligne de commande"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Analyseur intelligent Athalia")
    parser.add_argument("--project-path", type=str, help="Chemin du projet à analyser")
    parser.add_argument("--output", type=str, help="Fichier de sortie pour le rapport")
    
    args = parser.parse_args()
    
    # Initialiser l'analyseur
    analyzer = IntelligentAnalyzer()
    
    # Effectuer l'analyse
    analysis = analyzer.analyze_project_comprehensive(args.project_path)
    
    # Afficher les résultats
    print(f"\n🧠 ANALYSE COMPLÈTE - {analysis.project_name}")
    print("=" * 50)
    print(f"Score global: {analysis.overall_score:.1f}/100")
    print(f"Date d'analyse: {analysis.analysis_date}")
    
    print(f"\n📊 RÉSUMÉ:")
    print(f"- Fichiers analysés: {analysis.ast_analysis['files_analyzed']}")
    print(f"- Doublons détectés: {analysis.pattern_analysis['summary']['total_duplicates']}")
    print(f"- Anti-patterns: {analysis.pattern_analysis['summary']['total_antipatterns']}")
    print(f"- Problèmes de performance: {len(analysis.performance_analysis['issues'])}")
    
    print(f"\n💡 RECOMMANDATIONS:")
    for i, rec in enumerate(analysis.recommendations, 1):
        print(f"{i}. {rec}")
    
    print(f"\n🚀 PLAN D'OPTIMISATION:")
    plan = analysis.optimization_plan
    print(f"- Effort estimé: {plan['estimated_effort']:.1f} heures")
    print(f"- Amélioration attendue: {plan['expected_improvement']:.1f}%")
    
    if plan['priority_tasks']:
        print(f"- Tâches prioritaires: {len(plan['priority_tasks'])}")
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(asdict(analysis), f, indent=2, ensure_ascii=False)
        print(f"\n💾 Rapport sauvegardé dans {args.output}")

if __name__ == "__main__":
    main() 
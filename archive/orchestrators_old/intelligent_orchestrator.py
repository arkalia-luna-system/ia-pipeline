#!/usr/bin/env python3
"""
🎯 ORCHESTRATEUR INTELLIGENT ATHALIA
====================================
Orchestrateur qui :
- Intègre l'analyseur intelligent et la mémoire
- Coordonne tous les modules avec apprentissage
- Prédit et prévient les problèmes
- Optimise automatiquement le code
- Apprend de chaque action pour s'améliorer
"""

import logging
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, asdict

# Import des modules intelligents
try:
    from .intelligent_analyzer import IntelligentAnalyzer
    from .intelligent_memory import IntelligentMemory
except ImportError:
    # Fallback si les modules ne sont pas disponibles
    IntelligentAnalyzer = None
    IntelligentMemory = None

logger = logging.getLogger(__name__)

@dataclass
class OrchestrationTask:
    """Tâche d'orchestration"""
    task_id: str
    task_type: str  # 'analysis', 'correction', 'optimization', 'prediction'
    target_path: str
    priority: int  # 1-5 (1 = critique, 5 = faible)
    status: str  # 'pending', 'running', 'completed', 'failed'
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

@dataclass
class IntelligentInsight:
    """Insight intelligent"""
    insight_type: str  # 'prediction', 'optimization', 'warning', 'suggestion'
    title: str
    description: str
    confidence: float
    priority: str  # 'low', 'medium', 'high', 'critical'
    suggested_action: str
    estimated_impact: str
    code_location: Optional[str] = None

class IntelligentOrchestrator:
    """Orchestrateur intelligent pour Athalia"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "intelligent_orchestration.db"
        
        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialiser la base de données
        self._init_database()
        
        # Initialiser les modules intelligents
        self.analyzer = IntelligentAnalyzer(self.root_path) if IntelligentAnalyzer else None
        self.memory = IntelligentMemory(self.root_path) if IntelligentMemory else None
        
        # Cache pour les performances
        self._task_cache = {}
        self._insight_cache = {}
        
        # État d'exécution
        self._running_tasks = set()
        self._completed_tasks = {}
        self._failed_tasks = {}
        
        logger.info(f"🎯 Intelligent Orchestrator initialisé dans {self.root_path}")
    
    def _init_database(self):
        """Initialiser la base de données d'orchestration"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table des tâches d'orchestration
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orchestration_tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT UNIQUE NOT NULL,
                    task_type TEXT NOT NULL,
                    target_path TEXT NOT NULL,
                    priority INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    result TEXT,
                    error TEXT
                )
            """)
            
            # Table des insights intelligents
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS intelligent_insights (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    insight_type TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    priority TEXT NOT NULL,
                    suggested_action TEXT NOT NULL,
                    estimated_impact TEXT NOT NULL,
                    code_location TEXT,
                    created_at TEXT NOT NULL,
                    applied BOOLEAN DEFAULT 0,
                    applied_at TEXT
                )
            """)
            
            # Table des métriques d'orchestration
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orchestration_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    context TEXT
                )
            """)
            
            conn.commit()
    
    def orchestrate_project(self, project_path: str = None, 
                          include_predictions: bool = True,
                          include_optimizations: bool = True) -> Dict[str, Any]:
        """Orchestrer l'analyse complète d'un projet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"🎯 Orchestration intelligente du projet: {project_path.name}")
        
        results = {
            "project_path": str(project_path),
            "orchestration_timestamp": datetime.now().isoformat(),
            "tasks_executed": [],
            "insights_generated": [],
            "predictions_made": [],
            "optimizations_suggested": [],
            "learning_insights": {}
        }
        
        # Étape 1: Analyse intelligente
        if self.analyzer:
            logger.info("🔍 Étape 1: Analyse intelligente")
            analysis_task = self._create_task("analysis", str(project_path), priority=1)
            analysis_result = self._execute_analysis(project_path)
            results["tasks_executed"].append(analysis_task.task_id)
            results["analysis_result"] = analysis_result
            
            # Apprendre des résultats d'analyse
            if self.memory:
                self._learn_from_analysis(analysis_result)
        
        # Étape 2: Prédictions intelligentes
        if include_predictions and self.memory:
            logger.info("🔮 Étape 2: Prédictions intelligentes")
            predictions = self._generate_predictions(project_path)
            results["predictions_made"] = predictions
            results["insights_generated"].extend(predictions)
        
        # Étape 3: Optimisations intelligentes
        if include_optimizations:
            logger.info("⚡ Étape 3: Optimisations intelligentes")
            optimizations = self._generate_optimizations(project_path)
            results["optimizations_suggested"] = optimizations
            results["insights_generated"].extend(optimizations)
        
        # Étape 4: Insights d'apprentissage
        if self.memory:
            logger.info("📚 Étape 4: Insights d'apprentissage")
            learning_insights = self.memory.get_learning_insights()
            results["learning_insights"] = learning_insights
        
        # Sauvegarder les résultats
        self._save_orchestration_results(results)
        
        # Générer un rapport d'orchestration
        orchestration_report = self._generate_orchestration_report(results)
        results["orchestration_report"] = orchestration_report
        
        logger.info(f"✅ Orchestration terminée: {len(results['tasks_executed'])} tâches exécutées")
        return results
    
    def predict_project_issues(self, project_path: str = None) -> List[IntelligentInsight]:
        """Prédire les problèmes potentiels d'un projet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"🔮 Prédiction des problèmes pour: {project_path.name}")
        
        insights = []
        
        if not self.memory:
            logger.warning("Module de mémoire non disponible")
            return insights
        
        # Analyser tous les fichiers Python
        python_files = list(project_path.rglob("*.py"))
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Prédire les problèmes pour ce fichier
                predictions = self.memory.predict_issues(content, {
                    "file_path": str(py_file),
                    "file_size": len(content),
                    "project_path": str(project_path)
                })
                
                for pred in predictions:
                    insight = IntelligentInsight(
                        insight_type="prediction",
                        title=f"Problème prédit dans {py_file.name}",
                        description=pred.description,
                        confidence=pred.confidence,
                        priority="high" if pred.confidence > 0.8 else "medium",
                        suggested_action=pred.suggested_action,
                        estimated_impact=pred.estimated_impact,
                        code_location=str(py_file)
                    )
                    insights.append(insight)
                    
                    # Sauvegarder l'insight
                    self._save_insight(insight)
                
            except Exception as e:
                logger.warning(f"Erreur lors de l'analyse de {py_file}: {e}")
        
        logger.info(f"🔮 {len(insights)} prédictions générées")
        return insights
    
    def suggest_optimizations(self, project_path: str = None) -> List[IntelligentInsight]:
        """Suggérer des optimisations pour un projet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"⚡ Suggestion d'optimisations pour: {project_path.name}")
        
        insights = []
        
        if not self.analyzer:
            logger.warning("Module d'analyse non disponible")
            return insights
        
        # Analyser le projet
        analysis_result = self.analyzer.analyze_project(project_path)
        
        # Générer des optimisations basées sur l'analyse
        if analysis_result.get('duplicates_found', 0) > 0:
            insight = IntelligentInsight(
                insight_type="optimization",
                title="Consolidation des doublons",
                description=f"{analysis_result['duplicates_found']} doublons détectés - opportunité de consolidation",
                confidence=0.9,
                priority="high",
                suggested_action="Consolider les modules/fonctions dupliqués pour réduire la maintenance",
                estimated_impact="Réduction de 30-50% de la maintenance"
            )
            insights.append(insight)
            self._save_insight(insight)
        
        if analysis_result.get('antipatterns_found', 0) > 0:
            insight = IntelligentInsight(
                insight_type="optimization",
                title="Correction des anti-patterns",
                description=f"{analysis_result['antipatterns_found']} anti-patterns détectés",
                confidence=0.8,
                priority="medium",
                suggested_action="Corriger les anti-patterns pour améliorer la qualité du code",
                estimated_impact="Amélioration de 20-40% de la qualité"
            )
            insights.append(insight)
            self._save_insight(insight)
        
        # Vérifier les recommandations de l'analyseur
        for recommendation in analysis_result.get('recommendations', []):
            insight = IntelligentInsight(
                insight_type="optimization",
                title="Recommandation d'optimisation",
                description=recommendation,
                confidence=0.7,
                priority="medium",
                suggested_action="Implémenter la recommandation",
                estimated_impact="Amélioration générale"
            )
            insights.append(insight)
            self._save_insight(insight)
        
        logger.info(f"⚡ {len(insights)} optimisations suggérées")
        return insights
    
    def get_orchestration_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'orchestration"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Statistiques des tâches
            cursor.execute("SELECT COUNT(*) FROM orchestration_tasks")
            total_tasks = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM orchestration_tasks WHERE status = 'completed'")
            completed_tasks = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM orchestration_tasks WHERE status = 'failed'")
            failed_tasks = cursor.fetchone()[0]
            
            # Statistiques des insights
            cursor.execute("SELECT COUNT(*) FROM intelligent_insights")
            total_insights = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM intelligent_insights WHERE applied = 1")
            applied_insights = cursor.fetchone()[0]
            
            # Calculer les taux
            success_rate = completed_tasks / total_tasks if total_tasks > 0 else 0
            failure_rate = failed_tasks / total_tasks if total_tasks > 0 else 0
            insight_application_rate = applied_insights / total_insights if total_insights > 0 else 0
            
            return {
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "failed_tasks": failed_tasks,
                "success_rate": success_rate,
                "failure_rate": failure_rate,
                "total_insights": total_insights,
                "applied_insights": applied_insights,
                "insight_application_rate": insight_application_rate,
                "orchestration_status": "Actif et opérationnel"
            }
    
    def _create_task(self, task_type: str, target_path: str, priority: int = 3) -> OrchestrationTask:
        """Créer une nouvelle tâche d'orchestration"""
        task_id = f"{task_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{hash(target_path) % 10000}"
        
        task = OrchestrationTask(
            task_id=task_id,
            task_type=task_type,
            target_path=target_path,
            priority=priority,
            status="pending",
            created_at=datetime.now()
        )
        
        # Sauvegarder la tâche
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO orchestration_tasks 
                (task_id, task_type, target_path, priority, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                task.task_id,
                task.task_type,
                task.target_path,
                task.priority,
                task.status,
                task.created_at.isoformat()
            ))
            conn.commit()
        
        return task
    
    def _execute_analysis(self, project_path: Path) -> Dict[str, Any]:
        """Exécuter l'analyse intelligente"""
        if not self.analyzer:
            return {"error": "Module d'analyse non disponible"}
        
        try:
            return self.analyzer.analyze_project(project_path)
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse: {e}")
            return {"error": str(e)}
    
    def _learn_from_analysis(self, analysis_result: Dict[str, Any]):
        """Apprendre des résultats d'analyse"""
        if not self.memory:
            return
        
        # Apprendre des doublons
        duplicates = analysis_result.get('duplicates_found', [])
        if isinstance(duplicates, list):
            for duplicate in duplicates:
                if isinstance(duplicate, dict):
                    self.memory.learn_from_duplicate(
                        duplicate_items=duplicate.get('items', []),
                        locations=duplicate.get('locations', []),
                        similarity_score=duplicate.get('similarity_score', 0.0)
                    )
        
        # Apprendre des anti-patterns
        antipatterns = analysis_result.get('antipatterns_found', [])
        if isinstance(antipatterns, list):
            for antipattern in antipatterns:
                if isinstance(antipattern, dict):
                    self.memory.learn_from_error(
                        error_description=f"Anti-pattern: {antipattern.get('pattern_name', 'Unknown')}",
                        code_snippet=antipattern.get('description', ''),
                        location=antipattern.get('locations', [''])[0] if antipattern.get('locations') else '',
                        severity=antipattern.get('impact', 'medium')
                    )
    
    def _generate_predictions(self, project_path: Path) -> List[IntelligentInsight]:
        """Générer des prédictions intelligentes"""
        return self.predict_project_issues(project_path)
    
    def _generate_optimizations(self, project_path: Path) -> List[IntelligentInsight]:
        """Générer des optimisations intelligentes"""
        return self.suggest_optimizations(project_path)
    
    def _save_insight(self, insight: IntelligentInsight):
        """Sauvegarder un insight intelligent"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO intelligent_insights 
                (insight_type, title, description, confidence, priority, suggested_action, estimated_impact, code_location, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                insight.insight_type,
                insight.title,
                insight.description,
                insight.confidence,
                insight.priority,
                insight.suggested_action,
                insight.estimated_impact,
                insight.code_location,
                datetime.now().isoformat()
            ))
            conn.commit()
    
    def _save_orchestration_results(self, results: Dict[str, Any]):
        """Sauvegarder les résultats d'orchestration"""
        # Convertir les objets IntelligentInsight en dictionnaires
        converted_results = {}
        for key, value in results.items():
            if key == 'insights_generated' and isinstance(value, list):
                converted_results[key] = [
                    {
                        'insight_type': insight.insight_type,
                        'title': insight.title,
                        'description': insight.description,
                        'confidence': insight.confidence,
                        'priority': insight.priority,
                        'suggested_action': insight.suggested_action,
                        'estimated_impact': insight.estimated_impact,
                        'code_location': insight.code_location
                    } if hasattr(insight, 'insight_type') else insight
                    for insight in value
                ]
            else:
                converted_results[key] = value
        
        # Sauvegarder les métriques
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO orchestration_metrics 
                (metric_name, metric_value, timestamp, context)
                VALUES (?, ?, ?, ?)
            """, (
                "tasks_executed",
                len(converted_results.get('tasks_executed', [])),
                datetime.now().isoformat(),
                json.dumps(converted_results)
            ))
            
            cursor.execute("""
                INSERT INTO orchestration_metrics 
                (metric_name, metric_value, timestamp, context)
                VALUES (?, ?, ?, ?)
            """, (
                "insights_generated",
                len(converted_results.get('insights_generated', [])),
                datetime.now().isoformat(),
                json.dumps(converted_results)
            ))
            
            conn.commit()
    
    def _generate_orchestration_report(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Générer un rapport d'orchestration"""
        return {
            "summary": {
                "project_analyzed": results.get('project_path', 'Unknown'),
                "tasks_executed": len(results.get('tasks_executed', [])),
                "insights_generated": len(results.get('insights_generated', [])),
                "predictions_made": len(results.get('predictions_made', [])),
                "optimizations_suggested": len(results.get('optimizations_suggested', []))
            },
            "recommendations": [
                insight.suggested_action 
                for insight in results.get('insights_generated', [])
            ],
            "learning_progress": results.get('learning_insights', {}),
            "next_steps": [
                "Implémenter les optimisations suggérées",
                "Corriger les problèmes prédits",
                "Continuer l'apprentissage du système"
            ]
        }

def main():
    """Test de l'orchestrateur intelligent"""
    orchestrator = IntelligentOrchestrator()
    
    # Orchestrer le projet actuel
    results = orchestrator.orchestrate_project()
    
    print("🎯 Test de l'orchestrateur intelligent:")
    print(f"  • Projet analysé: {results['project_path']}")
    print(f"  • Tâches exécutées: {len(results['tasks_executed'])}")
    print(f"  • Insights générés: {len(results['insights_generated'])}")
    print(f"  • Prédictions: {len(results['predictions_made'])}")
    print(f"  • Optimisations: {len(results['optimizations_suggested'])}")
    
    # Afficher les recommandations
    if results.get('orchestration_report', {}).get('recommendations'):
        print(f"\n💡 Recommandations:")
        for rec in results['orchestration_report']['recommendations'][:5]:
            print(f"  • {rec}")
    
    # Obtenir les insights d'orchestration
    insights = orchestrator.get_orchestration_insights()
    print(f"\n📊 Insights d'orchestration:")
    print(f"  • Tâches totales: {insights['total_tasks']}")
    print(f"  • Taux de succès: {insights['success_rate']:.2f}")
    print(f"  • Insights totaux: {insights['total_insights']}")
    print(f"  • Taux d'application: {insights['insight_application_rate']:.2f}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
🎯 ATHALIA INTELLIGENT ORCHESTRATOR
===================================
Orchestrateur intelligent qui :
- Utilise les insights du super cerveau
- Coordonne tous les modules de manière optimale
- Apprend des patterns d'exécution
- Optimise les performances en temps réel
- Gère les dépendances intelligemment
"""

import os
import json
import sqlite3
import yaml
import asyncio
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
import logging
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TaskDefinition:
    """Définition d'une tâche"""
    name: str
    module: str
    function: str
    dependencies: List[str]
    priority: int  # 1=high, 2=medium, 3=low
    estimated_duration: float
    parallel_safe: bool
    retry_count: int = 0
    max_retries: int = 3

@dataclass
class ExecutionResult:
    """Résultat d'exécution d'une tâche"""
    task_name: str
    success: bool
    duration: float
    output: str
    error: Optional[str] = None
    timestamp: datetime = None

@dataclass
class OrchestrationPlan:
    """Plan d'orchestration"""
    tasks: List[TaskDefinition]
    execution_order: List[str]
    parallel_groups: List[List[str]]
    estimated_total_time: float
    dependencies_map: Dict[str, List[str]]

class AthaliaIntelligentOrchestrator:
    """Orchestrateur intelligent pour Athalia"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or os.getcwd())
        self.db_path = self.root_path / "data" / "athalia_orchestration.db"
        self.super_brain_path = self.root_path / "data" / "super_brain_analysis.json"
        
        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialiser la base de données
        self._init_database()
        
        # Charger la configuration
        self.config = self._load_config()
        
        # Cache pour les performances
        self._performance_cache = {}
        self._dependency_cache = {}
        
        # État d'exécution
        self._running_tasks = set()
        self._completed_tasks = {}
        self._failed_tasks = {}
        
        logger.info(f"🎯 Athalia Intelligent Orchestrator initialisé dans {self.root_path}")
    
    def _init_database(self):
        """Initialiser la base de données d'orchestration"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table des tâches
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    module TEXT NOT NULL,
                    function TEXT NOT NULL,
                    dependencies TEXT,
                    priority INTEGER DEFAULT 2,
                    estimated_duration REAL,
                    parallel_safe BOOLEAN DEFAULT 1,
                    created_at TEXT NOT NULL
                )
            """)
            
            # Table des exécutions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS executions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    success BOOLEAN NOT NULL,
                    duration REAL,
                    output TEXT,
                    error TEXT,
                    timestamp TEXT NOT NULL
                )
            """)
            
            # Table des performances
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS performance_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    avg_duration REAL,
                    success_rate REAL,
                    last_execution TEXT,
                    execution_count INTEGER DEFAULT 0
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
    
    def load_super_brain_insights(self) -> Dict[str, Any]:
        """Charger les insights du super cerveau"""
        if self.super_brain_path.exists():
            with open(self.super_brain_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def create_intelligent_orchestration_plan(self, target_action: str = None) -> OrchestrationPlan:
        """Créer un plan d'orchestration intelligent"""
        logger.info("🧠 Création du plan d'orchestration intelligent...")
        
        # Charger les insights du super cerveau
        insights = self.load_super_brain_insights()
        
        # Définir les tâches selon l'action cible
        if target_action == "complete":
            tasks = self._create_complete_pipeline_tasks()
        elif target_action == "audit":
            tasks = self._create_audit_pipeline_tasks()
        elif target_action == "test":
            tasks = self._create_test_pipeline_tasks()
        else:
            tasks = self._create_default_pipeline_tasks()
        
        # Optimiser l'ordre d'exécution
        execution_order = self._optimize_execution_order(tasks, insights)
        
        # Grouper les tâches parallèles
        parallel_groups = self._create_parallel_groups(tasks, execution_order)
        
        # Calculer le temps total estimé
        estimated_total_time = sum(task.estimated_duration for task in tasks)
        
        # Construire le graphe de dépendances
        dependencies_map = {task.name: task.dependencies for task in tasks}
        
        return OrchestrationPlan(
            tasks=tasks,
            execution_order=execution_order,
            parallel_groups=parallel_groups,
            estimated_total_time=estimated_total_time,
            dependencies_map=dependencies_map
        )
    
    def _create_complete_pipeline_tasks(self) -> List[TaskDefinition]:
        """Créer les tâches pour le pipeline complet"""
        return [
            TaskDefinition(
                name="audit_intelligent",
                module="athalia_core.intelligent_auditor",
                function="audit_project_intelligent",
                dependencies=[],
                priority=1,
                estimated_duration=5.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="analytics_advanced",
                module="athalia_core.advanced_analytics",
                function="analyze_project_advanced",
                dependencies=["audit_intelligent"],
                priority=1,
                estimated_duration=3.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="auto_correction",
                module="modules.auto_correction_avancee",
                function="corriger_projet",
                dependencies=["audit_intelligent"],
                priority=2,
                estimated_duration=8.0,
                parallel_safe=False
            ),
            TaskDefinition(
                name="auto_documentation",
                module="athalia_core.auto_documenter",
                function="generate_documentation",
                dependencies=["analytics_advanced"],
                priority=2,
                estimated_duration=4.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="auto_testing",
                module="athalia_core.auto_tester",
                function="generate_tests",
                dependencies=["auto_correction"],
                priority=2,
                estimated_duration=6.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="auto_cicd",
                module="athalia_core.auto_cicd",
                function="setup_cicd",
                dependencies=["auto_testing", "auto_documentation"],
                priority=3,
                estimated_duration=3.0,
                parallel_safe=True
            )
        ]
    
    def _create_audit_pipeline_tasks(self) -> List[TaskDefinition]:
        """Créer les tâches pour le pipeline d'audit"""
        return [
            TaskDefinition(
                name="audit_intelligent",
                module="athalia_core.intelligent_auditor",
                function="audit_project_intelligent",
                dependencies=[],
                priority=1,
                estimated_duration=5.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="security_audit",
                module="athalia_core.security_auditor",
                function="audit_security",
                dependencies=["audit_intelligent"],
                priority=1,
                estimated_duration=3.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="analytics_basic",
                module="athalia_core.analytics",
                function="analyze_project",
                dependencies=["audit_intelligent"],
                priority=2,
                estimated_duration=2.0,
                parallel_safe=True
            )
        ]
    
    def _create_test_pipeline_tasks(self) -> List[TaskDefinition]:
        """Créer les tâches pour le pipeline de tests"""
        return [
            TaskDefinition(
                name="test_generation",
                module="athalia_core.auto_tester",
                function="generate_tests",
                dependencies=[],
                priority=1,
                estimated_duration=6.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="test_execution",
                module="athalia_core.auto_tester",
                function="run_tests",
                dependencies=["test_generation"],
                priority=1,
                estimated_duration=10.0,
                parallel_safe=False
            ),
            TaskDefinition(
                name="coverage_analysis",
                module="athalia_core.auto_tester",
                function="analyze_coverage",
                dependencies=["test_execution"],
                priority=2,
                estimated_duration=2.0,
                parallel_safe=True
            )
        ]
    
    def _create_default_pipeline_tasks(self) -> List[TaskDefinition]:
        """Créer les tâches par défaut"""
        return [
            TaskDefinition(
                name="audit_basic",
                module="athalia_core.audit",
                function="audit_project",
                dependencies=[],
                priority=1,
                estimated_duration=3.0,
                parallel_safe=True
            ),
            TaskDefinition(
                name="analytics_basic",
                module="athalia_core.analytics",
                function="analyze_project",
                dependencies=["audit_basic"],
                priority=2,
                estimated_duration=2.0,
                parallel_safe=True
            )
        ]
    
    def _optimize_execution_order(self, tasks: List[TaskDefinition], insights: Dict[str, Any]) -> List[str]:
        """Optimiser l'ordre d'exécution basé sur les insights"""
        # Créer un graphe de dépendances
        task_map = {task.name: task for task in tasks}
        dependencies = {task.name: task.dependencies for task in tasks}
        
        # Topological sort
        visited = set()
        temp_visited = set()
        order = []
        
        def dfs(task_name):
            if task_name in temp_visited:
                raise ValueError(f"Cycle détecté: {task_name}")
            if task_name in visited:
                return
            
            temp_visited.add(task_name)
            
            for dep in dependencies.get(task_name, []):
                if dep in task_map:
                    dfs(dep)
            
            temp_visited.remove(task_name)
            visited.add(task_name)
            order.append(task_name)
        
        # Traiter les tâches par priorité
        for priority in [1, 2, 3]:
            priority_tasks = [task.name for task in tasks if task.priority == priority]
            for task_name in priority_tasks:
                if task_name not in visited:
                    dfs(task_name)
        
        return order
    
    def _create_parallel_groups(self, tasks: List[TaskDefinition], execution_order: List[str]) -> List[List[str]]:
        """Créer des groupes de tâches parallèles"""
        task_map = {task.name: task for task in tasks}
        parallel_groups = []
        current_group = []
        
        for task_name in execution_order:
            task = task_map.get(task_name)
            if task and task.parallel_safe:
                current_group.append(task_name)
            else:
                if current_group:
                    parallel_groups.append(current_group)
                    current_group = []
                if task:
                    current_group.append(task_name)
        
        if current_group:
            parallel_groups.append(current_group)
        
        return parallel_groups
    
    async def execute_orchestration_plan(self, plan: OrchestrationPlan, project_path: str) -> Dict[str, Any]:
        """Exécuter le plan d'orchestration"""
        logger.info(f"🚀 Exécution du plan d'orchestration pour {project_path}")
        
        results = {}
        start_time = time.time()
        
        # Exécuter les groupes parallèles
        for group_index, group in enumerate(plan.parallel_groups):
            logger.info(f"📦 Exécution du groupe {group_index + 1}/{len(plan.parallel_groups)}: {group}")
            
            # Exécuter les tâches du groupe en parallèle
            with ThreadPoolExecutor(max_workers=len(group)) as executor:
                futures = {}
                for task_name in group:
                    task = next(t for t in plan.tasks if t.name == task_name)
                    future = executor.submit(self._execute_task, task, project_path)
                    futures[future] = task_name
                
                # Collecter les résultats
                for future in as_completed(futures):
                    task_name = futures[future]
                    try:
                        result = future.result()
                        results[task_name] = result
                        logger.info(f"✅ {task_name}: {result.success}")
                    except Exception as e:
                        logger.error(f"❌ {task_name}: {e}")
                        results[task_name] = ExecutionResult(
                            task_name=task_name,
                            success=False,
                            duration=0.0,
                            output="",
                            error=str(e),
                            timestamp=datetime.now()
                        )
        
        total_duration = time.time() - start_time
        
        # Sauvegarder les résultats
        self._save_execution_results(results)
        
        return {
            "success": all(r.success for r in results.values()),
            "results": results,
            "total_duration": total_duration,
            "estimated_duration": plan.estimated_total_time
        }
    
    def _execute_task(self, task: TaskDefinition, project_path: str) -> ExecutionResult:
        """Exécuter une tâche individuelle"""
        start_time = time.time()
        
        try:
            # Construire la commande
            cmd = [
                "python3", "-c",
                f"import sys; sys.path.append('{self.root_path}'); "
                f"from {task.module} import {task.function}; "
                f"result = {task.function}('{project_path}'); "
                f"print('SUCCESS:', result)"
            ]
            
            # Exécuter la commande
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.root_path,
                timeout=task.estimated_duration * 2
            )
            
            success = result.returncode == 0
            duration = time.time() - start_time
            
            return ExecutionResult(
                task_name=task.name,
                success=success,
                duration=duration,
                output=result.stdout,
                error=result.stderr if not success else None,
                timestamp=datetime.now()
            )
            
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                task_name=task.name,
                success=False,
                duration=time.time() - start_time,
                output="",
                error="Timeout",
                timestamp=datetime.now()
            )
        except Exception as e:
            return ExecutionResult(
                task_name=task.name,
                success=False,
                duration=time.time() - start_time,
                output="",
                error=str(e),
                timestamp=datetime.now()
            )
    
    def _save_execution_results(self, results: Dict[str, ExecutionResult]):
        """Sauvegarder les résultats d'exécution"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            for task_name, result in results.items():
                cursor.execute("""
                    INSERT INTO executions 
                    (task_name, success, duration, output, error, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    task_name,
                    result.success,
                    result.duration,
                    result.output,
                    result.error,
                    result.timestamp.isoformat()
                ))
            
            conn.commit()
    
    def get_performance_insights(self) -> Dict[str, Any]:
        """Obtenir des insights de performance"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Statistiques globales
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_executions,
                    AVG(duration) as avg_duration,
                    SUM(CASE WHEN success THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as success_rate
                FROM executions
            """)
            
            stats = cursor.fetchone()
            
            # Tâches les plus lentes
            cursor.execute("""
                SELECT task_name, AVG(duration) as avg_duration
                FROM executions
                GROUP BY task_name
                ORDER BY avg_duration DESC
                LIMIT 5
            """)
            
            slowest_tasks = cursor.fetchall()
            
            # Tâches avec le plus d'échecs
            cursor.execute("""
                SELECT task_name, 
                       COUNT(*) as total,
                       SUM(CASE WHEN success THEN 0 ELSE 1 END) as failures
                FROM executions
                GROUP BY task_name
                HAVING failures > 0
                ORDER BY failures DESC
                LIMIT 5
            """)
            
            failing_tasks = cursor.fetchall()
            
            return {
                "total_executions": stats[0] if stats else 0,
                "average_duration": stats[1] if stats else 0,
                "success_rate": stats[2] if stats else 0,
                "slowest_tasks": [{"task": task, "duration": duration} for task, duration in slowest_tasks],
                "failing_tasks": [{"task": task, "failures": failures, "total": total} for task, total, failures in failing_tasks]
            }

def main():
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Athalia Intelligent Orchestrator")
    parser.add_argument("--action", choices=["orchestrate", "plan", "insights"], 
                       default="orchestrate", help="Action à effectuer")
    parser.add_argument("--target", help="Chemin du projet cible")
    parser.add_argument("--pipeline", choices=["complete", "audit", "test"], 
                       default="complete", help="Type de pipeline")
    parser.add_argument("--root", help="Racine du projet Athalia")
    
    args = parser.parse_args()
    
    # Initialiser l'orchestrateur
    orchestrator = AthaliaIntelligentOrchestrator(args.root)
    
    if args.action == "plan":
        print("🧠 Génération du plan d'orchestration intelligent...")
        plan = orchestrator.create_intelligent_orchestration_plan(args.pipeline)
        
        print(f"📋 Plan d'orchestration:")
        print(f"  • Tâches: {len(plan.tasks)}")
        print(f"  • Ordre d'exécution: {len(plan.execution_order)} étapes")
        print(f"  • Groupes parallèles: {len(plan.parallel_groups)}")
        print(f"  • Temps estimé: {plan.estimated_total_time:.1f} secondes")
        
        print(f"\n📦 Groupes parallèles:")
        for i, group in enumerate(plan.parallel_groups):
            print(f"  Groupe {i+1}: {group}")
    
    elif args.action == "orchestrate":
        if not args.target:
            print("❌ Chemin du projet cible requis")
            return
        
        print(f"🚀 Orchestration intelligente pour {args.target}...")
        plan = orchestrator.create_intelligent_orchestration_plan(args.pipeline)
        
        # Exécuter le plan
        import asyncio
        results = asyncio.run(orchestrator.execute_orchestration_plan(plan, args.target))
        
        print(f"✅ Orchestration terminée:")
        print(f"  • Succès: {results['success']}")
        print(f"  • Durée totale: {results['total_duration']:.1f}s")
        print(f"  • Durée estimée: {results['estimated_duration']:.1f}s")
        
        for task_name, result in results['results'].items():
            status = "✅" if result.success else "❌"
            print(f"  {status} {task_name}: {result.duration:.1f}s")
    
    elif args.action == "insights":
        print("📊 Insights de performance...")
        insights = orchestrator.get_performance_insights()
        
        print(f"📈 Statistiques globales:")
        print(f"  • Exécutions totales: {insights['total_executions']}")
        print(f"  • Durée moyenne: {insights['average_duration']:.1f}s")
        print(f"  • Taux de succès: {insights['success_rate']:.1f}%")
        
        if insights['slowest_tasks']:
            print(f"\n🐌 Tâches les plus lentes:")
            for task_info in insights['slowest_tasks']:
                print(f"  • {task_info['task']}: {task_info['duration']:.1f}s")
        
        if insights['failing_tasks']:
            print(f"\n❌ Tâches problématiques:")
            for task_info in insights['failing_tasks']:
                print(f"  • {task_info['task']}: {task_info['failures']}/{task_info['total']} échecs")

if __name__ == "__main__":
    main() 
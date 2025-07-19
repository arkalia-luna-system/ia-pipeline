#!/usr/bin/env python3
"""
🚀 ATHALIA INTELLIGENT COORDINATOR
==================================
Système de coordination intelligente qui :
- Gère tous les modules Athalia
- Apprend de chaque action
- Coordonne les interactions entre modules
- Met à jour la documentation automatiquement
- Optimise les performances du système
"""

import os
import json
import logging
import subprocess
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import sqlite3
import hashlib

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModuleInfo:
    """Informations sur un module"""
    name: str
    path: str
    type: str  # 'core', 'module', 'agent', 'plugin'
    status: str  # 'active', 'inactive', 'error'
    last_used: Optional[datetime] = None
    usage_count: int = 0
    dependencies: List[str] = None
    description: str = ""

@dataclass
class ActionRecord:
    """Enregistrement d'une action"""
    action: str
    module: str
    success: bool
    timestamp: datetime
    duration: float
    details: Dict[str, Any]
    context: Dict[str, Any]

class AthaliaCoordinator:
    """Coordinateur intelligent pour Athalia"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or os.getcwd())
        self.db_path = self.root_path / "data" / "athalia_coordination.db"
        self.learning_db_path = self.root_path / "data" / "athalia_learning.json"
        
        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialiser les bases de données
        self._init_databases()
        
        # Charger les modules
        self.modules = self._discover_modules()
        
        logger.info(f"🚀 Athalia Coordinator initialisé dans {self.root_path}")
    
    def _init_databases(self):
        """Initialiser les bases de données"""
        # Base de données SQLite pour la coordination
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table des modules
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS modules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    path TEXT NOT NULL,
                    type TEXT NOT NULL,
                    status TEXT DEFAULT 'active',
                    last_used TEXT,
                    usage_count INTEGER DEFAULT 0,
                    dependencies TEXT,
                    description TEXT
                )
            """)
            
            # Table des actions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS actions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    action TEXT NOT NULL,
                    module TEXT NOT NULL,
                    success BOOLEAN NOT NULL,
                    timestamp TEXT NOT NULL,
                    duration REAL,
                    details TEXT,
                    context TEXT
                )
            """)
            
            # Table des patterns d'apprentissage
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS learning_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_type TEXT NOT NULL,
                    pattern_data TEXT NOT NULL,
                    confidence REAL DEFAULT 1.0,
                    created_at TEXT NOT NULL
                )
            """)
            
            conn.commit()
        
        # Base de données JSON pour l'apprentissage
        if not self.learning_db_path.exists():
            self.learning_db_path.write_text(json.dumps({
                "actions_history": [],
                "user_preferences": {},
                "module_usage": {},
                "alias_usage": {},
                "error_patterns": {},
                "success_patterns": {},
                "last_update": datetime.now().isoformat()
            }, indent=2))
    
    def _discover_modules(self) -> Dict[str, ModuleInfo]:
        """Découvrir tous les modules disponibles"""
        modules = {}
        
        # Modules core
        core_path = self.root_path / "athalia_core"
        if core_path.exists():
            for py_file in core_path.glob("*.py"):
                if py_file.name != "__init__.py":
                    module_name = py_file.stem
                    modules[f"core.{module_name}"] = ModuleInfo(
                        name=module_name,
                        path=str(py_file),
                        type="core",
                        status="active",
                        description=f"Module core {module_name}"
                    )
        
        # Modules avancés
        modules_path = self.root_path / "modules"
        if modules_path.exists():
            for py_file in modules_path.glob("*.py"):
                if py_file.name != "__init__.py":
                    module_name = py_file.stem
                    modules[f"module.{module_name}"] = ModuleInfo(
                        name=module_name,
                        path=str(py_file),
                        type="module",
                        status="active",
                        description=f"Module avancé {module_name}"
                    )
        
        # Agents
        agents_path = self.root_path / "agents"
        if agents_path.exists():
            for py_file in agents_path.glob("*.py"):
                if py_file.name != "__init__.py":
                    module_name = py_file.stem
                    modules[f"agent.{module_name}"] = ModuleInfo(
                        name=module_name,
                        path=str(py_file),
                        type="agent",
                        status="active",
                        description=f"Agent {module_name}"
                    )
        
        # Plugins
        plugins_path = self.root_path / "plugins"
        if plugins_path.exists():
            for py_file in plugins_path.glob("*_plugin.py"):
                module_name = py_file.stem.replace("_plugin", "")
                modules[f"plugin.{module_name}"] = ModuleInfo(
                    name=module_name,
                    path=str(py_file),
                    type="plugin",
                    status="active",
                    description=f"Plugin {module_name}"
                )
        
        logger.info(f"🔍 {len(modules)} modules découverts")
        return modules
    
    def record_action(self, action: str, module: str, success: bool, 
                     duration: float = 0.0, details: Dict = None, 
                     context: Dict = None) -> None:
        """Enregistrer une action pour l'apprentissage"""
        try:
            # Enregistrer dans SQLite
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO actions (action, module, success, timestamp, duration, details, context)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    action,
                    module,
                    success,
                    datetime.now().isoformat(),
                    duration,
                    json.dumps(details or {}),
                    json.dumps(context or {})
                ))
                
                # Mettre à jour les statistiques du module
                cursor.execute("""
                    UPDATE modules 
                    SET usage_count = usage_count + 1, last_used = ?
                    WHERE name = ?
                """, (datetime.now().isoformat(), module))
                
                conn.commit()
            
            # Enregistrer dans JSON pour compatibilité
            learning_data = json.loads(self.learning_db_path.read_text())
            
            # Ajouter à l'historique
            record = {
                "action": action,
                "module": module,
                "success": success,
                "timestamp": datetime.now().isoformat(),
                "duration": duration,
                "details": details or {},
                "context": context or {}
            }
            learning_data["actions_history"].append(record)
            
            # Mettre à jour les statistiques d'usage
            if module not in learning_data["module_usage"]:
                learning_data["module_usage"][module] = 0
            learning_data["module_usage"][module] += 1
            
            # Analyser les patterns
            if not success:
                if "error_patterns" not in learning_data:
                    learning_data["error_patterns"] = {}
                if action not in learning_data["error_patterns"]:
                    learning_data["error_patterns"][action] = 0
                learning_data["error_patterns"][action] += 1
            
            learning_data["last_update"] = datetime.now().isoformat()
            
            self.learning_db_path.write_text(json.dumps(learning_data, indent=2))
            
            logger.info(f"📊 Action enregistrée: {action} ({module}) - {'✅' if success else '❌'}")
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'enregistrement de l'action: {e}")
    
    def get_module_recommendations(self, context: Dict = None) -> List[str]:
        """Obtenir des recommandations de modules basées sur le contexte"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Analyser l'historique récent
                cursor.execute("""
                    SELECT module, COUNT(*) as usage, AVG(CASE WHEN success THEN 1 ELSE 0 END) as success_rate
                    FROM actions 
                    WHERE timestamp > datetime('now', '-7 days')
                    GROUP BY module
                    ORDER BY usage DESC, success_rate DESC
                    LIMIT 10
                """)
                
                recommendations = []
                for module, usage, success_rate in cursor.fetchall():
                    if success_rate > 0.7:  # Seuil de succès de 70%
                        recommendations.append(module)
                
                return recommendations
                
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'obtention des recommandations: {e}")
            return []
    
    def analyze_system_health(self) -> Dict[str, Any]:
        """Analyser la santé du système"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Statistiques globales
                cursor.execute("SELECT COUNT(*) FROM actions")
                total_actions = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM actions WHERE success = 1")
                successful_actions = cursor.fetchone()[0]
                
                success_rate = (successful_actions / total_actions * 100) if total_actions > 0 else 0
                
                # Modules les plus utilisés
                cursor.execute("""
                    SELECT module, COUNT(*) as usage
                    FROM actions
                    GROUP BY module
                    ORDER BY usage DESC
                    LIMIT 5
                """)
                top_modules = [{"module": module, "usage": usage} for module, usage in cursor.fetchall()]
                
                # Patterns d'erreur
                cursor.execute("""
                    SELECT action, COUNT(*) as error_count
                    FROM actions
                    WHERE success = 0
                    GROUP BY action
                    ORDER BY error_count DESC
                    LIMIT 5
                """)
                error_patterns = [{"action": action, "count": count} for action, count in cursor.fetchall()]
                
                return {
                    "total_actions": total_actions,
                    "success_rate": success_rate,
                    "top_modules": top_modules,
                    "error_patterns": error_patterns,
                    "system_status": "healthy" if success_rate > 80 else "warning" if success_rate > 60 else "critical"
                }
                
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'analyse de la santé: {e}")
            return {"error": str(e)}
    
    def update_documentation(self) -> None:
        """Mettre à jour la documentation automatiquement"""
        try:
            docs_path = self.root_path / "docs"
            docs_path.mkdir(exist_ok=True)
            
            # Mettre à jour la documentation des modules
            modules_doc = docs_path / "MODULES.md"
            
            with open(modules_doc, 'w', encoding='utf-8') as f:
                f.write("# 📚 Modules Athalia/Arkalia\n\n")
                f.write(f"**Dernière mise à jour :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Grouper par type
                by_type = {}
                for module_id, module_info in self.modules.items():
                    module_type = module_info.type
                    if module_type not in by_type:
                        by_type[module_type] = []
                    by_type[module_type].append(module_info)
                
                for module_type, modules_list in by_type.items():
                    f.write(f"## {module_type.upper()}\n\n")
                    
                    for module in modules_list:
                        f.write(f"### {module.name}\n")
                        f.write(f"- **Chemin :** `{module.path}`\n")
                        f.write(f"- **Statut :** {module.status}\n")
                        f.write(f"- **Utilisations :** {module.usage_count}\n")
                        if module.description:
                            f.write(f"- **Description :** {module.description}\n")
                        f.write("\n")
            
            # Mettre à jour la documentation des alias
            self._update_alias_documentation()
            
            logger.info("✅ Documentation mise à jour")
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la mise à jour de la documentation: {e}")
    
    def _update_alias_documentation(self) -> None:
        """Mettre à jour la documentation des alias"""
        try:
            alias_doc = self.root_path / "docs" / "ALIAS.md"
            
            # Lire les alias existants
            alias_file = self.root_path / "setup" / "alias-unified.sh"
            if not alias_file.exists():
                return
            
            aliases = []
            with open(alias_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('alias ath-'):
                        alias_name = line.split('=')[0].replace('alias ', '').strip()
                        aliases.append(alias_name)
            
            # Générer la documentation
            with open(alias_doc, 'w', encoding='utf-8') as f:
                f.write("# 🚀 Alias Athalia/Arkalia\n\n")
                f.write(f"**Dernière mise à jour :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("## 📋 Liste des Alias\n\n")
                f.write("| Alias | Description |\n")
                f.write("|-------|-------------|\n")
                
                for alias in sorted(aliases):
                    f.write(f"| `{alias}` | À documenter |\n")
                
                # Statistiques d'usage
                learning_data = json.loads(self.learning_db_path.read_text())
                if learning_data.get("module_usage"):
                    f.write("\n## 📊 Statistiques d'Usage\n\n")
                    f.write("| Alias | Utilisations |\n")
                    f.write("|-------|--------------|\n")
                    
                    sorted_usage = sorted(learning_data["module_usage"].items(), 
                                        key=lambda x: x[1], reverse=True)
                    for alias, count in sorted_usage[:10]:
                        f.write(f"| `{alias}` | {count} |\n")
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la mise à jour des alias: {e}")
    
    def coordinate_action(self, action: str, target: str = None, 
                         context: Dict = None) -> Dict[str, Any]:
        """Coordonner une action entre les modules"""
        start_time = datetime.now()
        success = False
        result = {}
        
        try:
            logger.info(f"🎯 Coordination de l'action: {action}")
            
            # Analyser le contexte
            context = context or {}
            current_dir = Path.cwd()
            context["current_directory"] = str(current_dir)
            context["python_files"] = len(list(current_dir.glob("*.py")))
            context["has_tests"] = (current_dir / "tests").exists()
            context["has_requirements"] = (current_dir / "requirements.txt").exists()
            
            # Déterminer les modules à utiliser
            if action == "generate":
                module = "generation"
                cmd = ["python3", "-m", "athalia_core.cli", "generate", target]
            elif action == "test":
                module = "auto_tester"
                cmd = ["python3", "-m", "pytest", "tests/"]
            elif action == "audit":
                module = "audit"
                cmd = ["python3", self.root_path / "athalia_unified.py", target, "--action", "audit"]
            elif action == "clean":
                module = "cleanup"
                cmd = ["find", ".", "-name", "*.pyc", "-delete"]
            else:
                module = "unknown"
                cmd = ["echo", f"Action {action} non reconnue"]
            
            # Exécuter l'action
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=current_dir)
            success = result.returncode == 0
            
            # Enregistrer l'action
            duration = (datetime.now() - start_time).total_seconds()
            self.record_action(action, module, success, duration, {
                "command": " ".join(cmd),
                "returncode": result.returncode,
                "stdout": result.stdout[:500],  # Limiter la taille
                "stderr": result.stderr[:500]
            }, context)
            
            return {
                "success": success,
                "module": module,
                "duration": duration,
                "output": result.stdout,
                "error": result.stderr if not success else None
            }
            
        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            self.record_action(action, "coordinator", False, duration, {"error": str(e)}, context)
            logger.error(f"❌ Erreur lors de la coordination: {e}")
            return {"success": False, "error": str(e)}
    
    def get_learning_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'apprentissage"""
        try:
            learning_data = json.loads(self.learning_db_path.read_text())
            
            # Analyser les patterns
            total_actions = len(learning_data.get("actions_history", []))
            successful_actions = len([a for a in learning_data.get("actions_history", []) if a.get("success")])
            
            # Actions les plus populaires
            usage_stats = learning_data.get("module_usage", {})
            top_actions = sorted(usage_stats.items(), key=lambda x: x[1], reverse=True)[:5]
            
            # Patterns d'erreur
            error_patterns = learning_data.get("error_patterns", {})
            top_errors = sorted(error_patterns.items(), key=lambda x: x[1], reverse=True)[:5]
            
            return {
                "total_actions": total_actions,
                "success_rate": (successful_actions / total_actions * 100) if total_actions > 0 else 0,
                "top_actions": top_actions,
                "top_errors": top_errors,
                "recommendations": self._generate_recommendations(learning_data)
            }
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'obtention des insights: {e}")
            return {"error": str(e)}
    
    def _generate_recommendations(self, learning_data: Dict) -> List[str]:
        """Générer des recommandations basées sur l'apprentissage"""
        recommendations = []
        
        # Analyser les patterns d'erreur
        error_patterns = learning_data.get("error_patterns", {})
        if error_patterns:
            most_error_action = max(error_patterns.items(), key=lambda x: x[1])
            recommendations.append(f"Action '{most_error_action[0]}' a {most_error_action[1]} erreurs - considérer une amélioration")
        
        # Recommandations basées sur l'usage
        usage_stats = learning_data.get("module_usage", {})
        if usage_stats:
            least_used = min(usage_stats.items(), key=lambda x: x[1])
            recommendations.append(f"Module '{least_used[0]}' peu utilisé ({least_used[1]} fois) - à découvrir")
        
        return recommendations

def main():
    """Fonction principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Athalia Intelligent Coordinator")
    parser.add_argument("--action", choices=["coordinate", "analyze", "update-docs", "insights"], 
                       default="analyze", help="Action à effectuer")
    parser.add_argument("--target", help="Cible de l'action")
    parser.add_argument("--root", help="Racine du projet Athalia")
    
    args = parser.parse_args()
    
    # Initialiser le coordinateur
    coordinator = AthaliaCoordinator(args.root)
    
    if args.action == "coordinate":
        if not args.target:
            print("❌ Cible requise pour l'action 'coordinate'")
            return
        
        result = coordinator.coordinate_action("generate", args.target)
        print(f"🎯 Résultat: {'✅' if result['success'] else '❌'}")
        if result.get('output'):
            print(result['output'])
        if result.get('error'):
            print(f"❌ Erreur: {result['error']}")
    
    elif args.action == "analyze":
        health = coordinator.analyze_system_health()
        print("🔍 Analyse de la santé du système:")
        print(f"  📊 Actions totales: {health.get('total_actions', 0)}")
        print(f"  ✅ Taux de succès: {health.get('success_rate', 0):.1f}%")
        print(f"  🏥 Statut: {health.get('system_status', 'unknown')}")
    
    elif args.action == "update-docs":
        coordinator.update_documentation()
        print("✅ Documentation mise à jour")
    
    elif args.action == "insights":
        insights = coordinator.get_learning_insights()
        print("🧠 Insights d'apprentissage:")
        print(f"  📈 Actions totales: {insights.get('total_actions', 0)}")
        print(f"  ✅ Taux de succès: {insights.get('success_rate', 0):.1f}%")
        
        if insights.get('recommendations'):
            print("  💡 Recommandations:")
            for rec in insights['recommendations']:
                print(f"    • {rec}")

if __name__ == "__main__":
    main() 
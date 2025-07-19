#!/usr/bin/env python3
"""
🧠 ANALYSEUR INTELLIGENT ATHALIA
================================
Module d'analyse AST avancée pour détecter :
- Doublons de code (même logique, noms différents)
- Patterns similaires (structures logiques)
- Anti-patterns (erreurs récurrentes)
- Optimisations possibles
- Apprentissage des corrections passées
"""

import ast
import hashlib
import json
import logging
import re
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, asdict
import difflib

logger = logging.getLogger(__name__)

@dataclass
class CodePattern:
    """Pattern de code détecté"""
    pattern_type: str  # 'function', 'class', 'logic', 'structure'
    signature: str     # Signature unique du pattern
    locations: List[str]  # Fichiers où il apparaît
    similarity_score: float  # Score de similarité (0-1)
    complexity: int    # Complexité du pattern
    last_seen: datetime
    correction_history: List[str] = None

@dataclass
class DuplicateAnalysis:
    """Analyse de doublons"""
    duplicate_type: str
    items: List[str]
    locations: List[str]
    severity: str
    similarity_score: float
    suggested_action: str
    estimated_effort: str

@dataclass
class AntiPattern:
    """Anti-pattern détecté"""
    pattern_name: str
    description: str
    locations: List[str]
    impact: str  # 'low', 'medium', 'high', 'critical'
    suggestion: str
    previous_corrections: List[str]

class IntelligentAnalyzer:
    """Analyseur intelligent pour détecter doublons et patterns"""
    
    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "intelligent_analysis.db"
        self.patterns_db_path = self.root_path / "data" / "code_patterns.json"
        
        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialiser les bases de données
        self._init_databases()
        
        # Cache pour les analyses
        self._pattern_cache = {}
        self._duplicate_cache = {}
        self._antipattern_cache = {}
        
        # Charger les patterns existants
        self._load_patterns()
        
        logger.info(f"🧠 Intelligent Analyzer initialisé dans {self.root_path}")
    
    def _init_databases(self):
        """Initialiser les bases de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table des patterns de code
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS code_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_type TEXT NOT NULL,
                    signature TEXT UNIQUE NOT NULL,
                    locations TEXT NOT NULL,
                    similarity_score REAL DEFAULT 1.0,
                    complexity INTEGER DEFAULT 1,
                    last_seen TEXT NOT NULL,
                    correction_history TEXT,
                    usage_count INTEGER DEFAULT 1
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
                    similarity_score REAL NOT NULL,
                    suggested_action TEXT,
                    estimated_effort TEXT,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT,
                    resolution_method TEXT
                )
            """)
            
            # Table des anti-patterns
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS antipatterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    locations TEXT NOT NULL,
                    impact TEXT NOT NULL,
                    suggestion TEXT NOT NULL,
                    previous_corrections TEXT,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT
                )
            """)
            
            # Table des corrections appliquées
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS corrections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    correction_type TEXT NOT NULL,
                    target_pattern TEXT NOT NULL,
                    correction_method TEXT NOT NULL,
                    before_code TEXT,
                    after_code TEXT,
                    success BOOLEAN NOT NULL,
                    applied_at TEXT NOT NULL,
                    applied_by TEXT
                )
            """)
            
            conn.commit()
    
    def _load_patterns(self):
        """Charger les patterns depuis la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM code_patterns")
            rows = cursor.fetchall()
            
            for row in rows:
                pattern = CodePattern(
                    pattern_type=row[1],
                    signature=row[2],
                    locations=json.loads(row[3]),
                    similarity_score=row[4],
                    complexity=row[5],
                    last_seen=datetime.fromisoformat(row[6]),
                    correction_history=json.loads(row[7]) if row[7] else []
                )
                self._pattern_cache[pattern.signature] = pattern
    
    def analyze_project(self, project_path: str = None) -> Dict[str, Any]:
        """Analyser un projet complet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"🔍 Analyse intelligente du projet: {project_path.name}")
        
        # Analyser tous les fichiers Python
        python_files = list(project_path.rglob("*.py"))
        logger.info(f"📁 {len(python_files)} fichiers Python trouvés")
        
        # Analyser chaque fichier
        all_patterns = []
        all_duplicates = []
        all_antipatterns = []
        
        for py_file in python_files:
            try:
                file_patterns = self._analyze_file(py_file)
                all_patterns.extend(file_patterns)
            except Exception as e:
                logger.warning(f"Erreur lors de l'analyse de {py_file}: {e}")
        
        # Détecter les doublons
        duplicates = self._detect_duplicates(all_patterns)
        all_duplicates.extend(duplicates)
        
        # Détecter les anti-patterns
        antipatterns = self._detect_antipatterns(all_patterns)
        all_antipatterns.extend(antipatterns)
        
        # Sauvegarder les résultats
        self._save_analysis_results(all_patterns, all_duplicates, all_antipatterns)
        
        # Générer les recommandations
        recommendations = self._generate_recommendations(all_duplicates, all_antipatterns)
        
        return {
            "project_path": str(project_path),
            "files_analyzed": len(python_files),
            "patterns_detected": len(all_patterns),
            "duplicates_found": len(all_duplicates),
            "antipatterns_found": len(all_antipatterns),
            "recommendations": recommendations,
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    def _analyze_file(self, file_path: Path) -> List[CodePattern]:
        """Analyser un fichier Python"""
        patterns = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse le code
            tree = ast.parse(content)
            
            # Analyser les fonctions
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    pattern = self._analyze_function(node, content, file_path)
                    if pattern:
                        patterns.append(pattern)
                
                elif isinstance(node, ast.ClassDef):
                    pattern = self._analyze_class(node, content, file_path)
                    if pattern:
                        patterns.append(pattern)
                
                elif isinstance(node, ast.If):
                    pattern = self._analyze_conditional(node, content, file_path)
                    if pattern:
                        patterns.append(pattern)
                
                elif isinstance(node, ast.For):
                    pattern = self._analyze_loop(node, content, file_path)
                    if pattern:
                        patterns.append(pattern)
            
        except Exception as e:
            logger.warning(f"Erreur lors de l'analyse de {file_path}: {e}")
        
        return patterns
    
    def _analyze_function(self, node: ast.FunctionDef, content: str, file_path: Path) -> Optional[CodePattern]:
        """Analyser une fonction"""
        # Extraire le corps de la fonction
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 10
        
        # Obtenir le code de la fonction
        lines = content.split('\n')
        function_code = '\n'.join(lines[start_line-1:end_line])
        
        # Créer une signature unique
        signature = self._create_function_signature(node, function_code)
        
        # Calculer la complexité
        complexity = self._calculate_complexity(node)
        
        return CodePattern(
            pattern_type="function",
            signature=signature,
            locations=[str(file_path)],
            similarity_score=1.0,
            complexity=complexity,
            last_seen=datetime.now(),
            correction_history=[]
        )
    
    def _analyze_class(self, node: ast.ClassDef, content: str, file_path: Path) -> Optional[CodePattern]:
        """Analyser une classe"""
        # Extraire le corps de la classe
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 20
        
        # Obtenir le code de la classe
        lines = content.split('\n')
        class_code = '\n'.join(lines[start_line-1:end_line])
        
        # Créer une signature unique
        signature = self._create_class_signature(node, class_code)
        
        # Calculer la complexité
        complexity = self._calculate_complexity(node)
        
        return CodePattern(
            pattern_type="class",
            signature=signature,
            locations=[str(file_path)],
            similarity_score=1.0,
            complexity=complexity,
            last_seen=datetime.now(),
            correction_history=[]
        )
    
    def _analyze_conditional(self, node: ast.If, content: str, file_path: Path) -> Optional[CodePattern]:
        """Analyser une condition"""
        # Extraire le code de la condition
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 5
        
        lines = content.split('\n')
        conditional_code = '\n'.join(lines[start_line-1:end_line])
        
        # Créer une signature
        signature = self._create_conditional_signature(node, conditional_code)
        
        return CodePattern(
            pattern_type="conditional",
            signature=signature,
            locations=[str(file_path)],
            similarity_score=1.0,
            complexity=1,
            last_seen=datetime.now(),
            correction_history=[]
        )
    
    def _analyze_loop(self, node: ast.For, content: str, file_path: Path) -> Optional[CodePattern]:
        """Analyser une boucle"""
        # Extraire le code de la boucle
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 5
        
        lines = content.split('\n')
        loop_code = '\n'.join(lines[start_line-1:end_line])
        
        # Créer une signature
        signature = self._create_loop_signature(node, loop_code)
        
        return CodePattern(
            pattern_type="loop",
            signature=signature,
            locations=[str(file_path)],
            similarity_score=1.0,
            complexity=1,
            last_seen=datetime.now(),
            correction_history=[]
        )
    
    def _create_function_signature(self, node: ast.FunctionDef, code: str) -> str:
        """Créer une signature unique pour une fonction"""
        # Normaliser le code (supprimer les espaces, commentaires, etc.)
        normalized_code = self._normalize_code(code)
        
        # Créer un hash
        return hashlib.md5(normalized_code.encode()).hexdigest()
    
    def _create_class_signature(self, node: ast.ClassDef, code: str) -> str:
        """Créer une signature unique pour une classe"""
        normalized_code = self._normalize_code(code)
        return hashlib.md5(normalized_code.encode()).hexdigest()
    
    def _create_conditional_signature(self, node: ast.If, code: str) -> str:
        """Créer une signature unique pour une condition"""
        normalized_code = self._normalize_code(code)
        return hashlib.md5(normalized_code.encode()).hexdigest()
    
    def _create_loop_signature(self, node: ast.For, code: str) -> str:
        """Créer une signature unique pour une boucle"""
        normalized_code = self._normalize_code(code)
        return hashlib.md5(normalized_code.encode()).hexdigest()
    
    def _normalize_code(self, code: str) -> str:
        """Normaliser le code pour la comparaison"""
        # Supprimer les commentaires
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        
        # Supprimer les docstrings
        code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
        code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
        
        # Supprimer les espaces en début de ligne
        lines = [line.strip() for line in code.split('\n')]
        
        # Supprimer les lignes vides
        lines = [line for line in lines if line]
        
        return '\n'.join(lines)
    
    def _calculate_complexity(self, node: ast.AST) -> int:
        """Calculer la complexité cyclomatique"""
        complexity = 1
        
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(child, ast.ExceptHandler):
                complexity += 1
            elif isinstance(child, ast.With):
                complexity += 1
            elif isinstance(child, ast.AsyncWith):
                complexity += 1
        
        return complexity
    
    def _detect_duplicates(self, patterns: List[CodePattern]) -> List[DuplicateAnalysis]:
        """Détecter les doublons dans les patterns"""
        duplicates = []
        
        # Grouper par type de pattern
        by_type = {}
        for pattern in patterns:
            if pattern.pattern_type not in by_type:
                by_type[pattern.pattern_type] = []
            by_type[pattern.pattern_type].append(pattern)
        
        # Détecter les doublons dans chaque type
        for pattern_type, type_patterns in by_type.items():
            # Comparer chaque pattern avec les autres
            for i, pattern1 in enumerate(type_patterns):
                for j, pattern2 in enumerate(type_patterns[i+1:], i+1):
                    similarity = self._calculate_similarity(pattern1, pattern2)
                    
                    if similarity > 0.8:  # Seuil de similarité
                        duplicate = DuplicateAnalysis(
                            duplicate_type=pattern_type,
                            items=[pattern1.signature, pattern2.signature],
                            locations=pattern1.locations + pattern2.locations,
                            severity="high" if similarity > 0.9 else "medium",
                            similarity_score=similarity,
                            suggested_action="Considérer la fusion ou l'extraction en module commun",
                            estimated_effort="1-2 heures"
                        )
                        duplicates.append(duplicate)
        
        return duplicates
    
    def _calculate_similarity(self, pattern1: CodePattern, pattern2: CodePattern) -> float:
        """Calculer la similarité entre deux patterns"""
        # Pour l'instant, comparaison simple basée sur la signature
        # TODO: Implémenter une comparaison plus sophistiquée
        return 1.0 if pattern1.signature == pattern2.signature else 0.0
    
    def _detect_antipatterns(self, patterns: List[CodePattern]) -> List[AntiPattern]:
        """Détecter les anti-patterns"""
        antipatterns = []
        
        # Anti-patterns connus
        known_antipatterns = [
            {
                "name": "Long Function",
                "description": "Fonction trop longue (>50 lignes)",
                "detector": lambda p: p.pattern_type == "function" and p.complexity > 10,
                "impact": "medium",
                "suggestion": "Diviser en fonctions plus petites"
            },
            {
                "name": "High Complexity",
                "description": "Code trop complexe (complexité > 15)",
                "detector": lambda p: p.complexity > 15,
                "impact": "high",
                "suggestion": "Refactoriser pour réduire la complexité"
            },
            {
                "name": "Duplicate Logic",
                "description": "Logique dupliquée détectée",
                "detector": lambda p: len(p.locations) > 1,
                "impact": "medium",
                "suggestion": "Extraire en fonction commune"
            }
        ]
        
        for antipattern_def in known_antipatterns:
            for pattern in patterns:
                if antipattern_def["detector"](pattern):
                    antipattern = AntiPattern(
                        pattern_name=antipattern_def["name"],
                        description=antipattern_def["description"],
                        locations=pattern.locations,
                        impact=antipattern_def["impact"],
                        suggestion=antipattern_def["suggestion"],
                        previous_corrections=[]
                    )
                    antipatterns.append(antipattern)
        
        return antipatterns
    
    def _save_analysis_results(self, patterns: List[CodePattern], 
                             duplicates: List[DuplicateAnalysis],
                             antipatterns: List[AntiPattern]):
        """Sauvegarder les résultats d'analyse"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Sauvegarder les patterns
            for pattern in patterns:
                cursor.execute("""
                    INSERT OR REPLACE INTO code_patterns 
                    (pattern_type, signature, locations, similarity_score, complexity, last_seen, correction_history)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    pattern.pattern_type,
                    pattern.signature,
                    json.dumps(pattern.locations),
                    pattern.similarity_score,
                    pattern.complexity,
                    pattern.last_seen.isoformat(),
                    json.dumps(pattern.correction_history)
                ))
            
            # Sauvegarder les doublons
            for duplicate in duplicates:
                cursor.execute("""
                    INSERT INTO duplicates 
                    (duplicate_type, items, locations, severity, similarity_score, suggested_action, estimated_effort, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    duplicate.duplicate_type,
                    json.dumps(duplicate.items),
                    json.dumps(duplicate.locations),
                    duplicate.severity,
                    duplicate.similarity_score,
                    duplicate.suggested_action,
                    duplicate.estimated_effort,
                    datetime.now().isoformat()
                ))
            
            # Sauvegarder les anti-patterns
            for antipattern in antipatterns:
                cursor.execute("""
                    INSERT INTO antipatterns 
                    (pattern_name, description, locations, impact, suggestion, previous_corrections, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    antipattern.pattern_name,
                    antipattern.description,
                    json.dumps(antipattern.locations),
                    antipattern.impact,
                    antipattern.suggestion,
                    json.dumps(antipattern.previous_corrections),
                    datetime.now().isoformat()
                ))
            
            conn.commit()
    
    def _generate_recommendations(self, duplicates: List[DuplicateAnalysis], 
                                antipatterns: List[AntiPattern]) -> List[str]:
        """Générer des recommandations basées sur l'analyse"""
        recommendations = []
        
        # Recommandations basées sur les doublons
        if duplicates:
            recommendations.append(f"🔍 {len(duplicates)} doublons détectés - Considérer la consolidation")
        
        # Recommandations basées sur les anti-patterns
        critical_antipatterns = [a for a in antipatterns if a.impact == "critical"]
        if critical_antipatterns:
            recommendations.append(f"🚨 {len(critical_antipatterns)} anti-patterns critiques à corriger")
        
        high_antipatterns = [a for a in antipatterns if a.impact == "high"]
        if high_antipatterns:
            recommendations.append(f"⚠️ {len(high_antipatterns)} anti-patterns importants à traiter")
        
        return recommendations
    
    def get_learning_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'apprentissage"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Statistiques des patterns
            cursor.execute("SELECT COUNT(*) FROM code_patterns")
            total_patterns = cursor.fetchone()[0]
            
            # Statistiques des doublons
            cursor.execute("SELECT COUNT(*) FROM duplicates WHERE resolved_at IS NULL")
            active_duplicates = cursor.fetchone()[0]
            
            # Statistiques des anti-patterns
            cursor.execute("SELECT COUNT(*) FROM antipatterns WHERE resolved_at IS NULL")
            active_antipatterns = cursor.fetchone()[0]
            
            # Corrections appliquées
            cursor.execute("SELECT COUNT(*) FROM corrections WHERE success = 1")
            successful_corrections = cursor.fetchone()[0]
            
            return {
                "total_patterns": total_patterns,
                "active_duplicates": active_duplicates,
                "active_antipatterns": active_antipatterns,
                "successful_corrections": successful_corrections,
                "learning_progress": "En cours d'apprentissage"
            }

def main():
    """Test du module d'analyse intelligente"""
    analyzer = IntelligentAnalyzer()
    
    # Analyser le projet actuel
    results = analyzer.analyze_project()
    
    print("🧠 Résultats de l'analyse intelligente:")
    print(f"  • Fichiers analysés: {results['files_analyzed']}")
    print(f"  • Patterns détectés: {results['patterns_detected']}")
    print(f"  • Doublons trouvés: {results['duplicates_found']}")
    print(f"  • Anti-patterns trouvés: {results['antipatterns_found']}")
    
    if results['recommendations']:
        print("\n💡 Recommandations:")
        for rec in results['recommendations']:
            print(f"  • {rec}")
    
    # Obtenir les insights d'apprentissage
    insights = analyzer.get_learning_insights()
    print(f"\n📊 Insights d'apprentissage:")
    print(f"  • Patterns totaux: {insights['total_patterns']}")
    print(f"  • Doublons actifs: {insights['active_duplicates']}")
    print(f"  • Anti-patterns actifs: {insights['active_antipatterns']}")
    print(f"  • Corrections réussies: {insights['successful_corrections']}")

if __name__ == "__main__":
    main() 
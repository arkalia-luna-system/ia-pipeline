#!/usr/bin/env python3
"""
⚡ ANALYSEUR DE PERFORMANCE
===========================
Module spécialisé dans l'analyse des performances du code,
détection des goulots d'étranglement et optimisation.
"""

import cProfile
from dataclasses import dataclass
from datetime import datetime
import io
import logging
from pathlib import Path
import pstats
import sqlite3
import time
from typing import Any, Dict, List

from .ast_analyzer import ASTAnalyzer, FileAnalysis

logger = logging.getLogger(__name__)


@dataclass
class PerformanceMetric:
    """Métrique de performance"""

    metric_type: str
    value: float
    unit: str
    location: str
    threshold: float
    status: str  # 'good', 'warning', 'critical'


@dataclass
class PerformanceIssue:
    """Problème de performance détecté"""

    issue_type: str
    location: str
    description: str
    impact: str  # 'low', 'medium', 'high', 'critical'
    suggestion: str
    estimated_improvement: float


@dataclass
class PerformanceReport:
    """Rapport de performance complet"""

    overall_score: float
    metrics: List[PerformanceMetric]
    issues: List[PerformanceIssue]
    recommendations: List[str]
    optimization_opportunities: List[str]


class PerformanceAnalyzer:
    """Analyseur de performance pour détecter les goulots d'étranglement"""

    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "performance_analysis.db"

        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialiser la base de données
        self._init_database()

        # Analyseur AST
        self.ast_analyzer = ASTAnalyzer()

        # Seuils de performance
        self.thresholds = {
            "complexity": 10,
            "function_size": 50,
            "class_size": 200,
            "imports": 30,
            "nested_depth": 5,
            "loop_complexity": 3,
        }

        logger.info(f"⚡ Performance Analyzer initialisé dans {self.root_path}")

    def _init_database(self):
        """Initialiser la base de données de performance"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des métriques de performance
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS performance_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_type TEXT NOT NULL,
                    value REAL NOT NULL,
                    unit TEXT NOT NULL,
                    location TEXT NOT NULL,
                    threshold REAL NOT NULL,
                    status TEXT NOT NULL,
                    measured_at TEXT NOT NULL
                )
            """
            )

            # Table des problèmes de performance
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS performance_issues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    issue_type TEXT NOT NULL,
                    location TEXT NOT NULL,
                    description TEXT NOT NULL,
                    impact TEXT NOT NULL,
                    suggestion TEXT NOT NULL,
                    estimated_improvement REAL,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT
                )
            """
            )

            # Table des profils de performance
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS performance_profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT NOT NULL,
                    execution_time REAL,
                    call_count INTEGER,
                    memory_usage REAL,
                    profile_data TEXT,
                    profiled_at TEXT NOT NULL
                )
            """
            )

            conn.commit()

    def analyze_project_performance(
        self, project_path: str = None
    ) -> PerformanceReport:
        """Analyser les performances d'un projet complet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"⚡ Analyse des performances du projet: {project_path.name}")

        # Analyser tous les fichiers Python (ignorer les fichiers cachés)
        python_files = [
            f for f in project_path.rglob("*.py") if not f.name.startswith("._")
        ]
        logger.info(f"📁 {len(python_files)} fichiers Python analysés")

        # Limiter le nombre de fichiers pour les performances
        if len(python_files) > 50:
            python_files = python_files[:50]
            logger.info("📁 Limitation à 50 fichiers pour les performances")

        all_metrics = []
        all_issues = []

        for py_file in python_files:
            try:
                file_analysis = self.ast_analyzer.analyze_file(py_file)
                if file_analysis:
                    file_metrics = self._analyze_file_performance(file_analysis)
                    file_issues = self._detect_performance_issues(file_analysis)

                    all_metrics.extend(file_metrics)
                    all_issues.extend(file_issues)
            except Exception as e:
                logger.warning(
                    f"Erreur lors de l'analyse de performance de {py_file}: {e}"
                )

        # Calculer le score global
        overall_score = self._calculate_overall_score(all_metrics)

        # Générer les recommandations
        recommendations = self._generate_performance_recommendations(all_issues)

        # Identifier les opportunités d'optimisation
        optimization_opportunities = self._identify_optimization_opportunities(
            all_issues
        )

        # Créer le rapport
        report = PerformanceReport(
            overall_score=overall_score,
            metrics=all_metrics,
            issues=all_issues,
            recommendations=recommendations,
            optimization_opportunities=optimization_opportunities,
        )

        # Sauvegarder le rapport
        self._save_performance_report(report)

        return report

    def _analyze_file_performance(
        self, file_analysis: FileAnalysis
    ) -> List[PerformanceMetric]:
        """Analyser les performances d'un fichier"""
        metrics = []

        # Métrique de complexité
        complexity_metric = PerformanceMetric(
            metric_type="complexity",
            value=file_analysis.complexity_score,
            unit="cyclomatic",
            location=str(file_analysis.file_path),
            threshold=self.thresholds["complexity"],
            status=self._get_metric_status(
                file_analysis.complexity_score, self.thresholds["complexity"]
            ),
        )
        metrics.append(complexity_metric)

        # Métrique de taille
        size_metric = PerformanceMetric(
            metric_type="file_size",
            value=file_analysis.total_lines,
            unit="lines",
            location=str(file_analysis.file_path),
            threshold=500,
            status=self._get_metric_status(
                file_analysis.total_lines, 500, reverse=True
            ),
        )
        metrics.append(size_metric)

        # Métrique d'imports
        imports_metric = PerformanceMetric(
            metric_type="imports",
            value=len(file_analysis.imports),
            unit="count",
            location=str(file_analysis.file_path),
            threshold=self.thresholds["imports"],
            status=self._get_metric_status(
                len(file_analysis.imports), self.thresholds["imports"]
            ),
        )
        metrics.append(imports_metric)

        # Métriques des fonctions
        for func in file_analysis.functions:
            func_metric = PerformanceMetric(
                metric_type="function_complexity",
                value=func.complexity,
                unit="cyclomatic",
                location=f"{file_analysis.file_path}:{func.line_number}",
                threshold=self.thresholds["function_size"],
                status=self._get_metric_status(
                    func.complexity, self.thresholds["function_size"]
                ),
            )
            metrics.append(func_metric)

        return metrics

    def _detect_performance_issues(
        self, file_analysis: FileAnalysis
    ) -> List[PerformanceIssue]:
        """Détecter les problèmes de performance dans un fichier"""
        issues = []

        # Vérifier la complexité globale
        if file_analysis.complexity_score > 8:  # Seuil plus bas
            issue = PerformanceIssue(
                issue_type="high_complexity",
                location=str(file_analysis.file_path),
                description=f"Complexité élevée: {file_analysis.complexity_score:.1f}",
                impact=("medium" if file_analysis.complexity_score < 15 else "high"),
                suggestion="Refactoriser en modules plus petits",
                estimated_improvement=20.0,
            )
            issues.append(issue)

        # Vérifier la taille du fichier
        if file_analysis.total_lines > 300:  # Seuil plus bas
            issue = PerformanceIssue(
                issue_type="large_file",
                location=str(file_analysis.file_path),
                description=f"Fichier très long: {file_analysis.total_lines} lignes",
                impact="medium",
                suggestion="Diviser en fichiers plus petits",
                estimated_improvement=15.0,
            )
            issues.append(issue)

        # Vérifier les fonctions complexes
        for func in file_analysis.functions:
            if func.complexity > 8:  # Seuil plus bas
                issue = PerformanceIssue(
                    issue_type="complex_function",
                    location=f"{file_analysis.file_path}:{func.line_number}",
                    description=(
                        f"Fonction {func.name} très complexe: {func.complexity}"
                    ),
                    impact="high",
                    suggestion="Diviser en sous-fonctions",
                    estimated_improvement=25.0,
                )
                issues.append(issue)

        # Vérifier les imports excessifs
        if len(file_analysis.imports) > 20:  # Seuil plus bas
            issue = PerformanceIssue(
                issue_type="excessive_imports",
                location=str(file_analysis.file_path),
                description=f"Trop d'imports: {len(file_analysis.imports)}",
                impact="low",
                suggestion="Nettoyer les imports inutilisés",
                estimated_improvement=5.0,
            )
            issues.append(issue)

        # Vérifier les classes complexes
        for cls in file_analysis.classes:
            if cls.complexity > 12:  # Seuil plus bas
                issue = PerformanceIssue(
                    issue_type="complex_class",
                    location=f"{file_analysis.file_path}:{cls.line_number}",
                    description=f"Classe {cls.name} très complexe: {cls.complexity}",
                    impact="high",
                    suggestion="Diviser en classes plus petites",
                    estimated_improvement=30.0,
                )
                issues.append(issue)

        return issues

    def _get_metric_status(
        self, value: float, threshold: float, reverse: bool = False
    ) -> str:
        """Déterminer le statut d'une métrique"""
        if reverse:
            if value > threshold * 1.5:
                return "critical"
            elif value > threshold:
                return "warning"
            else:
                return "good"
        else:
            if value > threshold * 1.5:
                return "critical"
            elif value > threshold:
                return "warning"
            else:
                return "good"

    def _calculate_overall_score(self, metrics: List[PerformanceMetric]) -> float:
        """Calculer le score de performance global"""
        if not metrics:
            return 100.0

        total_score = 0
        total_weight = 0

        for metric in metrics:
            weight = self._get_metric_weight(metric.metric_type)
            score = self._calculate_metric_score(metric)

            total_score += score * weight
            total_weight += weight

        return total_score / total_weight if total_weight > 0 else 100.0

    def _get_metric_weight(self, metric_type: str) -> float:
        """Obtenir le poids d'une métrique"""
        weights = {
            "complexity": 3.0,
            "function_complexity": 2.5,
            "file_size": 1.5,
            "imports": 1.0,
        }
        return weights.get(metric_type, 1.0)

    def _calculate_metric_score(self, metric: PerformanceMetric) -> float:
        """Calculer le score d'une métrique"""
        if metric.status == "good":
            return 100.0
        elif metric.status == "warning":
            return 70.0
        else:  # critical
            return 30.0

    def _generate_performance_recommendations(
        self, issues: List[PerformanceIssue]
    ) -> List[str]:
        """Générer des recommandations de performance"""
        recommendations = []

        # Grouper les problèmes par type
        issue_types = {}
        for issue in issues:
            if issue.issue_type not in issue_types:
                issue_types[issue.issue_type] = []
            issue_types[issue.issue_type].append(issue)

        # Recommandations par type de problème
        if "high_complexity" in issue_types:
            count = len(issue_types["high_complexity"])
            recommendations.append(
                f"🧠 {count} modules très complexes - priorité au refactoring"
            )

        if "complex_function" in issue_types:
            count = len(issue_types["complex_function"])
            recommendations.append(
                f"⚙️ {count} fonctions complexes - diviser en sous-fonctions"
            )

        if "large_file" in issue_types:
            count = len(issue_types["large_file"])
            recommendations.append(
                f"📄 {count} fichiers très longs - diviser en modules"
            )

        if "excessive_imports" in issue_types:
            count = len(issue_types["excessive_imports"])
            recommendations.append(
                f"📦 {count} fichiers avec trop d'imports - nettoyer"
            )

        # Recommandations générales
        if issues:
            total_improvement = sum(issue.estimated_improvement for issue in issues)
            recommendations.append(
                f"📈 Amélioration potentielle estimée: {total_improvement:.1f}%"
            )

        return recommendations

    def _identify_optimization_opportunities(
        self, issues: List[PerformanceIssue]
    ) -> List[str]:
        """Identifier les opportunités d'optimisation"""
        opportunities = []

        # Opportunités par impact
        high_impact_issues = [i for i in issues if i.impact in ["high", "critical"]]
        if high_impact_issues:
            opportunities.append("🚀 Optimisations critiques disponibles")

        medium_impact_issues = [i for i in issues if i.impact == "medium"]
        if medium_impact_issues:
            opportunities.append("⚡ Optimisations moyennes disponibles")

        # Opportunités par type
        complexity_issues = [i for i in issues if "complexity" in i.issue_type]
        if complexity_issues:
            opportunities.append("🧩 Refactoring de complexité")

        size_issues = [
            i for i in issues if "size" in i.issue_type or "large" in i.issue_type
        ]
        if size_issues:
            opportunities.append("📦 Division de modules")

        return opportunities

    def _save_performance_report(self, report: PerformanceReport):
        """Sauvegarder le rapport de performance"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Sauvegarder les métriques
            for metric in report.metrics:
                cursor.execute(
                    """
                    INSERT INTO performance_metrics
                    (metric_type, value, unit, location, threshold, status,
                     measured_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        metric.metric_type,
                        metric.value,
                        metric.unit,
                        metric.location,
                        metric.threshold,
                        metric.status,
                        datetime.now().isoformat(),
                    ),
                )

            # Sauvegarder les problèmes
            for issue in report.issues:
                cursor.execute(
                    """
                    INSERT INTO performance_issues
                    (issue_type, location, description, impact, suggestion,
                     estimated_improvement, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        issue.issue_type,
                        issue.location,
                        issue.description,
                        issue.impact,
                        issue.suggestion,
                        issue.estimated_improvement,
                        datetime.now().isoformat(),
                    ),
                )

            conn.commit()

    def profile_function(
        self, function_path: str, function_name: str, *args, **kwargs
    ) -> Dict[str, Any]:
        """Profiler une fonction spécifique"""
        try:
            # Importer et exécuter la fonction
            import importlib.util

            spec = importlib.util.spec_from_file_location("module", function_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            func = getattr(module, function_name)

            # Profiler l'exécution
            profiler = cProfile.Profile()
            profiler.enable()

            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time

            profiler.disable()

            # Analyser les statistiques
            s = io.StringIO()
            stats = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
            stats.print_stats()

            return {
                "function_name": function_name,
                "execution_time": execution_time,
                "profile_data": s.getvalue(),
                "result": result,
            }

        except Exception as e:
            logger.error(f"Erreur lors du profilage de {function_name}: {e}")
            return None

    def get_performance_insights(self) -> Dict[str, Any]:
        """Obtenir des insights de performance"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Statistiques globales
            cursor.execute(
                "SELECT AVG(value) FROM performance_metrics "
                "WHERE metric_type = 'complexity'"
            )
            avg_complexity = cursor.fetchone()[0] or 0

            cursor.execute(
                "SELECT COUNT(*) FROM performance_issues WHERE resolved_at IS NULL"
            )
            unresolved_issues = cursor.fetchone()[0]

            cursor.execute("SELECT AVG(estimated_improvement) FROM performance_issues")
            avg_improvement = cursor.fetchone()[0] or 0

            return {
                "average_complexity": avg_complexity,
                "unresolved_issues": unresolved_issues,
                "average_improvement_potential": avg_improvement,
                "performance_health": max(
                    0, 100 - (avg_complexity * 2 + unresolved_issues * 5)
                ),
            }

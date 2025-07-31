#!/usr/bin/env python3
"""
Module d'analytics pour Athalia
Analyse et métriques de projets
"""

import json
import logging
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import yaml

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception  # type: ignore

logger = logging.getLogger(__name__)


class AnalyticsEngine:
    """Moteur d'analyse pour projets"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.metrics: Dict[str, Any] = {}
        self.reports: List[Any] = []

    def analyze_code_complexity(self) -> Dict[str, Any]:
        """Analyse la complexité cyclomatique du code"""
        complexity_data = {
            "average_complexity": 0,
            "max_complexity": 0,
            "files_analyzed": 0,
            "complexity_distribution": {},
        }

        try:
            python_files = list(self.project_path.rglob("*.py"))
            total_complexity = 0
            max_complexity = 0

            for py_file in python_files:
                try:
                    with open(py_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Analyse simple de complexité basée sur les structures de contrôle
                    complexity = self._calculate_file_complexity(content)
                    total_complexity += complexity
                    max_complexity = max(max_complexity, complexity)

                    # Distribution de complexité
                    if complexity <= 3:
                        complexity_data["complexity_distribution"]["low"] = (
                            complexity_data["complexity_distribution"].get("low", 0) + 1
                        )
                    elif complexity <= 7:
                        complexity_data["complexity_distribution"]["medium"] = (
                            complexity_data["complexity_distribution"].get("medium", 0)
                            + 1
                        )
                    else:
                        complexity_data["complexity_distribution"]["high"] = (
                            complexity_data["complexity_distribution"].get("high", 0)
                            + 1
                        )

                    complexity_data["files_analyzed"] += 1

                except Exception as e:
                    logger.warning(f"Impossible d'analyser {py_file}: {e}")

            if complexity_data["files_analyzed"] > 0:
                complexity_data["average_complexity"] = (
                    total_complexity / complexity_data["files_analyzed"]
                )
                complexity_data["max_complexity"] = max_complexity

        except Exception as e:
            logger.error(f"Erreur analyse complexité: {e}")

        self.metrics["code_complexity"] = complexity_data
        return complexity_data

    def _calculate_file_complexity(self, content: str) -> int:
        """Calcule la complexité cyclomatique d'un fichier"""
        complexity = 1  # Base complexity

        # Compter les structures de contrôle
        patterns = [
            r"\bif\b",
            r"\belif\b",
            r"\belse\b",
            r"\bfor\b",
            r"\bwhile\b",
            r"\band\b",
            r"\bor\b",
            r"\bexcept\b",
            r"\bwith\b",
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content)
            complexity += len(matches)

        return complexity

    def analyze_test_coverage(self) -> Dict[str, Any]:
        """Analyse la couverture de tests"""
        coverage_data = {
            "test_files_count": 0,
            "test_functions_count": 0,
            "test_classes_count": 0,
            "test_coverage_percentage": 0,
        }

        try:
            # Chercher les fichiers de test
            test_patterns = ["test_*.py", "*_test.py", "tests/"]
            test_files = []

            for pattern in test_patterns:
                if pattern.endswith("/"):
                    test_dir = self.project_path / pattern.rstrip("/")
                    if test_dir.exists():
                        test_files.extend(list(test_dir.rglob("*.py")))
                else:
                    test_files.extend(list(self.project_path.rglob(pattern)))

            coverage_data["test_files_count"] = len(set(test_files))

            # Compter les fonctions de test
            test_functions = 0
            test_classes = 0

            for test_file in set(test_files):
                try:
                    with open(test_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Compter les fonctions de test
                    test_func_pattern = r"def\s+test_"
                    test_functions += len(re.findall(test_func_pattern, content))

                    # Compter les classes de test
                    test_class_pattern = r"class\s+\w+.*Test"
                    test_classes += len(re.findall(test_class_pattern, content))

                except Exception as e:
                    logger.warning(f"Impossible d'analyser {test_file}: {e}")

            coverage_data["test_functions_count"] = test_functions
            coverage_data["test_classes_count"] = test_classes

        except Exception as e:
            logger.error(f"Erreur analyse couverture tests: {e}")

        self.metrics["test_coverage"] = coverage_data
        return coverage_data

    def analyze_dependencies(self) -> Dict[str, Any]:
        """Analyse les dépendances du projet"""
        dependencies_data = {
            "total_dependencies": 0,
            "direct_dependencies": 0,
            "indirect_dependencies": 0,
            "dependency_list": [],
        }

        try:
            # Chercher requirements.txt
            requirements_files = [
                self.project_path / "requirements.txt",
                self.project_path / "pyproject.toml",
                self.project_path / "setup.py",
            ]

            for req_file in requirements_files:
                if req_file.exists():
                    try:
                        with open(req_file, "r", encoding="utf-8") as f:
                            content = f.read()

                        if req_file.name == "requirements.txt":
                            # Analyser requirements.txt
                            deps = [
                                line.strip()
                                for line in content.split("\n")
                                if line.strip() and not line.startswith("#")
                            ]
                            dependencies_data["dependency_list"].extend(deps)

                        elif req_file.name == "pyproject.toml":
                            # Analyser pyproject.toml
                            import tomllib

                            try:
                                data = tomllib.loads(content)
                                if (
                                    "project" in data
                                    and "dependencies" in data["project"]
                                ):
                                    deps = data["project"]["dependencies"]
                                    dependencies_data["dependency_list"].extend(deps)
                            except Exception as dep_error:
                                logger.debug(f"Erreur analyse dépendance: {dep_error}")
                                continue

                        elif req_file.name == "setup.py":
                            # Analyser setup.py
                            install_requires_pattern = (
                                r"install_requires\s*=\s*\[(.*?)\]"
                            )
                            matches = re.findall(
                                install_requires_pattern, content, re.DOTALL
                            )
                            for match in matches:
                                deps = [
                                    dep.strip().strip("\"'") for dep in match.split(",")
                                ]
                                dependencies_data["dependency_list"].extend(deps)

                    except Exception as e:
                        logger.warning(f"Impossible d'analyser {req_file}: {e}")

            # Nettoyer et compter les dépendances
            clean_deps = []
            for dep in dependencies_data["dependency_list"]:
                if dep and not dep.startswith("#"):
                    clean_deps.append(dep)

            dependencies_data["dependency_list"] = clean_deps
            dependencies_data["direct_dependencies"] = len(clean_deps)
            dependencies_data["total_dependencies"] = len(clean_deps)  # Simplifié

        except Exception as e:
            logger.error(f"Erreur analyse dépendances: {e}")

        self.metrics["dependencies"] = dependencies_data
        return dependencies_data

    def analyze_performance_metrics(self) -> Dict[str, Any]:
        """Analyse les métriques de performance"""
        performance_data = {
            "average_execution_time": 0,
            "memory_usage": "0MB",
            "cpu_usage": 0,
            "performance_logs": [],
        }

        try:
            # Chercher les logs de performance
            log_files = list(self.project_path.rglob("*.log"))
            performance_logs = []

            for log_file in log_files:
                try:
                    with open(log_file, "r", encoding="utf-8") as f:
                        for line in f:
                            if any(
                                keyword in line.lower()
                                for keyword in [
                                    "execution",
                                    "memory",
                                    "cpu",
                                    "performance",
                                ]
                            ):
                                performance_logs.append(line.strip())
                except Exception as e:
                    logger.warning(f"Impossible de lire {log_file}: {e}")

            performance_data["performance_logs"] = performance_logs

            # Analyser les logs pour extraire des métriques
            execution_times = []
            memory_usage = []

            for log in performance_logs:
                # Extraire le temps d'exécution
                time_match = re.search(r"(\d+\.?\d*)\s*s", log)
                if time_match:
                    execution_times.append(float(time_match.group(1)))

                # Extraire l'utilisation mémoire
                memory_match = re.search(r"(\d+)\s*MB", log)
                if memory_match:
                    memory_usage.append(int(memory_match.group(1)))

            if execution_times:
                performance_data["average_execution_time"] = sum(execution_times) / len(
                    execution_times
                )

            if memory_usage:
                performance_data["memory_usage"] = (
                    f"{sum(memory_usage) / len(memory_usage):.0f}MB"
                )

        except Exception as e:
            logger.error(f"Erreur analyse performance: {e}")

        self.metrics["performance"] = performance_data
        return performance_data

    def analyze_security_metrics(self) -> Dict[str, Any]:
        """Analyse les métriques de sécurité"""
        security_data = {
            "security_score": 100,
            "vulnerabilities_count": 0,
            "high_severity_count": 0,
            "medium_severity_count": 0,
            "low_severity_count": 0,
            "vulnerabilities": [],
        }

        try:
            # Chercher les rapports de sécurité
            security_files = list(self.project_path.rglob("*security*.json")) + list(
                self.project_path.rglob("*security*.yaml")
            )

            for sec_file in security_files:
                try:
                    with open(sec_file, "r", encoding="utf-8") as f:
                        if sec_file.suffix == ".json":
                            data = json.load(f)
                        else:
                            data = yaml.safe_load(f)

                        if "vulnerabilities" in data:
                            vulns = data["vulnerabilities"]
                            security_data["vulnerabilities"].extend(vulns)
                            security_data["vulnerabilities_count"] += len(vulns)

                            for vuln in vulns:
                                severity = vuln.get("severity", "low").lower()
                                if severity == "high":
                                    security_data["high_severity_count"] += 1
                                elif severity == "medium":
                                    security_data["medium_severity_count"] += 1
                                else:
                                    security_data["low_severity_count"] += 1

                        if "score" in data:
                            security_data["security_score"] = min(
                                security_data["security_score"], data["score"]
                            )

                except Exception as e:
                    logger.warning(f"Impossible d'analyser {sec_file}: {e}")

            # Calculer le score de sécurité
            if security_data["vulnerabilities_count"] > 0:
                security_data["security_score"] = max(
                    0,
                    100
                    - (security_data["high_severity_count"] * 20)
                    - (security_data["medium_severity_count"] * 10),
                )

        except Exception as e:
            logger.error(f"Erreur analyse sécurité: {e}")

        self.metrics["security"] = security_data
        return security_data

    def analyze_documentation_coverage(self) -> Dict[str, Any]:
        """Analyse la couverture de documentation"""
        doc_data = {
            "documentation_files": 0,
            "readme_exists": False,
            "api_docs_exists": False,
            "doc_coverage_percentage": 0,
            "documentation_types": [],
        }

        try:
            # Chercher les fichiers de documentation
            doc_patterns = ["README*", "*.md", "docs/", "documentation/"]
            doc_files = []

            for pattern in doc_patterns:
                if pattern.endswith("/"):
                    doc_dir = self.project_path / pattern.rstrip("/")
                    if doc_dir.exists():
                        doc_files.extend(list(doc_dir.rglob("*")))
                else:
                    doc_files.extend(list(self.project_path.rglob(pattern)))

            doc_data["documentation_files"] = len(set(doc_files))

            # Vérifier les types de documentation
            for doc_file in set(doc_files):
                if doc_file.name.lower().startswith("readme"):
                    doc_data["readme_exists"] = True
                elif "api" in doc_file.name.lower():
                    doc_data["api_docs_exists"] = True

                # Ajouter le type de documentation
                if doc_file.suffix == ".md":
                    doc_data["documentation_types"].append("markdown")
                elif doc_file.suffix == ".rst":
                    doc_data["documentation_types"].append("rst")
                elif doc_file.suffix == ".txt":
                    doc_data["documentation_types"].append("text")

            # Calculer le pourcentage de couverture
            total_files = len(list(self.project_path.rglob("*.py")))
            if total_files > 0:
                doc_data["doc_coverage_percentage"] = min(
                    100, (doc_data["documentation_files"] / total_files) * 100
                )

        except Exception as e:
            logger.error(f"Erreur analyse documentation: {e}")

        self.metrics["documentation"] = doc_data
        return doc_data

    def analyze_git_metrics(self) -> Dict[str, Any]:
        """Analyse les métriques Git"""
        git_data = {
            "commits_count": 0,
            "contributors_count": 0,
            "last_commit_date": "",
            "branch_count": 0,
            "repository_age_days": 0,
        }

        try:
            git_data = self._get_git_metrics()
        except Exception as e:
            logger.error(f"Erreur analyse Git: {e}")

        self.metrics["git"] = git_data
        return git_data

    def _get_git_metrics(self) -> Dict[str, Any]:
        """Récupère les métriques Git"""
        git_data = {
            "commits_count": 0,
            "contributors_count": 0,
            "last_commit_date": "",
            "branch_count": 0,
            "repository_age_days": 0,
        }

        try:
            # Vérifier si c'est un repo Git
            if (self.project_path / ".git").exists():
                # Compter les commits
                result = validate_and_run(
                    ["git", "rev-list", "--count", "HEAD"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    git_data["commits_count"] = int(result.stdout.strip())

                # Compter les contributeurs
                result = validate_and_run(
                    ["git", "shortlog", "-s", "-n"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    git_data["contributors_count"] = len(
                        result.stdout.strip().split("\n")
                    )

                # Date du dernier commit
                result = validate_and_run(
                    ["git", "log", "-1", "--format=%cd", "--date=short"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    git_data["last_commit_date"] = result.stdout.strip()

                # Compter les branches
                result = validate_and_run(
                    ["git", "branch", "-r"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    git_data["branch_count"] = len(result.stdout.strip().split("\n"))

        except Exception as e:
            logger.warning(f"Impossible d'obtenir les métriques Git: {e}")

        return git_data

    def generate_comprehensive_report(self) -> Dict[str, Any]:
        """Génère un rapport complet d'analyse"""
        # Exécuter toutes les analyses
        self.analyze_code_complexity()
        self.analyze_test_coverage()
        self.analyze_dependencies()
        self.analyze_performance_metrics()
        self.analyze_security_metrics()
        self.analyze_documentation_coverage()
        self.analyze_git_metrics()

        # Calculer le score global
        project_score = self.calculate_project_score(self.metrics)

        # Générer les recommandations
        recommendations = self.generate_recommendations(self.metrics)

        report = {
            "summary": {
                "project_path": str(self.project_path),
                "analysis_date": datetime.now().isoformat(),
                "overall_score": project_score["overall_score"],
            },
            "detailed_metrics": self.metrics,
            "recommendations": recommendations,
            "timestamp": datetime.now().isoformat(),
        }

        self.reports.append(report)
        return report

    def calculate_project_score(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calcule le score global du projet"""
        category_scores = {}
        total_score = 0
        max_score = 0

        # Score de complexité du code (inversé)
        if "code_complexity" in metrics:
            complexity = metrics["code_complexity"].get("average_complexity", 0)
            if complexity <= 3:
                category_scores["code_complexity"] = 100
            elif complexity <= 7:
                category_scores["code_complexity"] = 75
            else:
                category_scores["code_complexity"] = 50
            total_score += category_scores["code_complexity"]
            max_score += 100

        # Score de couverture de tests
        if "test_coverage" in metrics:
            test_files = metrics["test_coverage"].get("test_files_count", 0)
            if test_files >= 10:
                category_scores["test_coverage"] = 100
            elif test_files >= 5:
                category_scores["test_coverage"] = 75
            elif test_files >= 1:
                category_scores["test_coverage"] = 50
            else:
                category_scores["test_coverage"] = 0
            total_score += category_scores["test_coverage"]
            max_score += 100

        # Score de sécurité
        if "security" in metrics:
            security_score = metrics["security"].get("security_score", 100)
            category_scores["security"] = security_score
            total_score += security_score
            max_score += 100

        # Score de documentation
        if "documentation" in metrics:
            doc_coverage = metrics["documentation"].get("doc_coverage_percentage", 0)
            category_scores["documentation"] = doc_coverage
            total_score += doc_coverage
            max_score += 100

        overall_score = (total_score / max_score * 100) if max_score > 0 else 0

        return {
            "overall_score": round(overall_score, 2),
            "category_scores": category_scores,
        }

    def generate_recommendations(self, metrics: Dict[str, Any]) -> List[Dict[str, str]]:
        """Génère des recommandations basées sur les métriques"""
        recommendations = []

        # Recommandations pour la complexité du code
        if "code_complexity" in metrics:
            complexity = metrics["code_complexity"].get("average_complexity", 0)
            if complexity > 7:
                recommendations.append(
                    {
                        "category": "code_complexity",
                        "suggestion": (
                            "Considérer la refactorisation pour réduire la "
                            "complexité cyclomatique"
                        ),
                    }
                )

        # Recommandations pour les tests
        if "test_coverage" in metrics:
            test_files = metrics["test_coverage"].get("test_files_count", 0)
            if test_files < 5:
                recommendations.append(
                    {
                        "category": "test_coverage",
                        "suggestion": (
                            "Augmenter la couverture de tests en ajoutant plus de "
                            "fichiers de test"
                        ),
                    }
                )

        # Recommandations pour la sécurité
        if "security" in metrics:
            security_score = metrics["security"].get("security_score", 100)
            if security_score < 80:
                recommendations.append(
                    {
                        "category": "security",
                        "suggestion": (
                            "Réviser et corriger les vulnérabilités de sécurité "
                            "identifiées"
                        ),
                    }
                )

        # Recommandations pour la documentation
        if "documentation" in metrics:
            doc_coverage = metrics["documentation"].get("doc_coverage_percentage", 0)
            if doc_coverage < 50:
                recommendations.append(
                    {
                        "category": "documentation",
                        "suggestion": "Améliorer la documentation du projet",
                    }
                )

        return recommendations

    def export_metrics_to_json(self, output_path: str) -> bool:
        """Exporte les métriques en JSON"""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(self.metrics, f, indent=2, default=str)
            return True
        except Exception as e:
            logger.error(f"Erreur export JSON: {e}")
            return False

    def export_metrics_to_yaml(self, output_path: str) -> bool:
        """Exporte les métriques en YAML"""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                yaml.dump(self.metrics, f, default_flow_style=False)
            return True
        except Exception as e:
            logger.error(f"Erreur export YAML: {e}")
            return False

    def analyze_trends(self, historical_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyse les tendances des métriques"""
        trends = {
            "score_trend": "stable",
            "complexity_trend": "stable",
            "improvement_rate": 0,
        }

        if len(historical_data) < 2:
            return trends

        # Analyser la tendance du score
        scores = [data.get("score", 0) for data in historical_data]
        if len(scores) >= 2:
            if scores[-1] > scores[0]:
                trends["score_trend"] = "improving"
                trends["improvement_rate"] = (
                    (scores[-1] - scores[0]) / scores[0]
                ) * 100
            elif scores[-1] < scores[0]:
                trends["score_trend"] = "declining"

        # Analyser la tendance de complexité
        complexities = [data.get("complexity", 0) for data in historical_data]
        if len(complexities) >= 2:
            if complexities[-1] < complexities[0]:
                trends["complexity_trend"] = "improving"
            elif complexities[-1] > complexities[0]:
                trends["complexity_trend"] = "declining"

        return trends

    def compare_with_baseline(
        self, baseline: Dict[str, Any], current: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Compare les métriques actuelles avec une baseline"""
        comparison = {"improvements": [], "regressions": [], "unchanged": []}

        for category in baseline:
            if category in current:
                baseline_value = baseline[category]
                current_value = current[category]

                if isinstance(baseline_value, dict) and isinstance(current_value, dict):
                    # Comparaison de dictionnaires
                    for key in baseline_value:
                        if key in current_value:
                            if current_value[key] > baseline_value[key]:
                                comparison["improvements"].append(f"{category}.{key}")
                            elif current_value[key] < baseline_value[key]:
                                comparison["regressions"].append(f"{category}.{key}")
                            else:
                                comparison["unchanged"].append(f"{category}.{key}")
                else:
                    # Comparaison de valeurs simples
                    if current_value > baseline_value:
                        comparison["improvements"].append(category)
                    elif current_value < baseline_value:
                        comparison["regressions"].append(category)
                    else:
                        comparison["unchanged"].append(category)

        return comparison

    def generate_visualization_data(self) -> Dict[str, Any]:
        """Génère des données pour visualisation"""
        viz_data = {
            "charts": {
                "complexity_distribution": self.metrics.get("code_complexity", {}).get(
                    "complexity_distribution", {}
                ),
                "security_score": self.metrics.get("security", {}).get(
                    "security_score", 0
                ),
                "test_coverage": self.metrics.get("test_coverage", {}).get(
                    "test_files_count", 0
                ),
            },
            "metrics_summary": {
                "overall_score": self.calculate_project_score(self.metrics)[
                    "overall_score"
                ],
                "total_files": self.metrics.get("code_complexity", {}).get(
                    "files_analyzed", 0
                ),
                "total_dependencies": self.metrics.get("dependencies", {}).get(
                    "total_dependencies", 0
                ),
            },
            "trends": {"score_trend": "stable", "complexity_trend": "stable"},
        }

        return viz_data


def generate_analytics_report(project_path: str = ".") -> Dict[str, Any]:
    """Fonction utilitaire pour générer un rapport d'analytics"""
    analytics = AnalyticsEngine(project_path)
    return analytics.generate_comprehensive_report()


def analyze_project_metrics(project_path: str = ".") -> Dict[str, Any]:
    """Analyse les métriques d'un projet"""
    engine = AnalyticsEngine(project_path)
    return engine.generate_comprehensive_report()


def analyze_project(project_path: str = ".") -> Dict[str, Any]:
    """Analyse complète d'un projet"""
    engine = AnalyticsEngine(project_path)

    # Analyser toutes les métriques
    complexity = engine.analyze_code_complexity()
    coverage = engine.analyze_test_coverage()
    dependencies = engine.analyze_dependencies()
    performance = engine.analyze_performance_metrics()
    security = engine.analyze_security_metrics()
    documentation = engine.analyze_documentation_coverage()
    git_metrics = engine.analyze_git_metrics()

    # Générer le rapport complet
    report = engine.generate_comprehensive_report()

    # Calculer le score global
    score_data = engine.calculate_project_score(report)

    # Structure de retour
    return {
        "project_name": Path(project_path).name,
        "structure": {
            "complexity": complexity,
            "coverage": coverage,
            "dependencies": dependencies,
            "performance": performance,
            "security": security,
            "documentation": documentation,
            "git": git_metrics,
        },
        "score": score_data["overall_score"],
        "metrics": report,
        "recommendations": engine.generate_recommendations(report),
        "timestamp": datetime.now().isoformat(),
    }


def generate_heatmap_data(project_path: str = ".") -> Dict[str, Any]:
    """Génère les données pour une heatmap de complexité du code"""
    engine = AnalyticsEngine(project_path)

    heatmap_data = {
        "heatmap_data": [],
        "total_files": 0,
        "max_complexity": 0,
        "file_types": {},
    }

    try:
        python_files = list(Path(project_path).rglob("*.py"))
        heatmap_data["total_files"] = len(python_files)

        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                complexity = engine._calculate_file_complexity(content)
                heatmap_data["max_complexity"] = max(
                    heatmap_data["max_complexity"], complexity
                )

                # Données pour la heatmap
                heatmap_data["heatmap_data"].append(
                    {
                        "file": str(py_file.relative_to(project_path)),
                        "complexity": complexity,
                        "lines": len(content.splitlines()),
                        "size": len(content),
                    }
                )

                # Statistiques par type de fichier
                file_type = py_file.suffix
                if file_type not in heatmap_data["file_types"]:
                    heatmap_data["file_types"][file_type] = {
                        "count": 0,
                        "total_complexity": 0,
                        "avg_complexity": 0,
                    }

                heatmap_data["file_types"][file_type]["count"] += 1
                heatmap_data["file_types"][file_type]["total_complexity"] += complexity

            except Exception as e:
                logger.warning(f"Impossible d'analyser {py_file}: {e}")

        # Calculer les moyennes par type de fichier
        for file_type, stats in heatmap_data["file_types"].items():
            if stats["count"] > 0:
                stats["avg_complexity"] = stats["total_complexity"] / stats["count"]

    except Exception as e:
        logger.error(f"Erreur génération heatmap: {e}")

    return heatmap_data


def generate_technical_debt_analysis(project_path: str = ".") -> Dict[str, Any]:
    """Analyse de la dette technique d'un projet"""
    engine = AnalyticsEngine(project_path)

    # Analyser les métriques
    complexity = engine.analyze_code_complexity()
    coverage = engine.analyze_test_coverage()
    documentation = engine.analyze_documentation_coverage()
    security = engine.analyze_security_metrics()

    # Calculer le score de dette technique
    debt_score = 0
    debt_indicators = []

    # Complexité élevée
    if complexity.get("average_complexity", 0) > 7:
        debt_score += 20
        debt_indicators.append("Complexité cyclomatique élevée")

    # Couverture de tests faible
    if coverage.get("overall_coverage", 0) < 80:
        debt_score += 25
        debt_indicators.append("Couverture de tests insuffisante")

    # Documentation manquante
    if documentation.get("documentation_score", 0) < 70:
        debt_score += 15
        debt_indicators.append("Documentation incomplète")

    # Problèmes de sécurité
    if security.get("security_score", 0) < 80:
        debt_score += 20
        debt_indicators.append("Vulnérabilités de sécurité détectées")

    # Recommandations
    recommendations = []
    if debt_score > 50:
        recommendations.append("Priorité haute: Refactoring du code complexe")
    if coverage.get("overall_coverage", 0) < 80:
        recommendations.append("Ajouter des tests unitaires et d'intégration")
    if documentation.get("documentation_score", 0) < 70:
        recommendations.append("Améliorer la documentation du code")

    return {
        "technical_debt_score": min(debt_score, 100),
        "debt_indicators": debt_indicators,
        "recommendations": recommendations,
        "metrics": {
            "complexity": complexity,
            "coverage": coverage,
            "documentation": documentation,
            "security": security,
        },
    }


def generate_analytics_html(project_path: str = ".") -> str:
    """Génère un rapport HTML d'analytics"""
    analysis = analyze_project(project_path)

    html_template = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport Analytics - {analysis['project_name']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .metric {{
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 3px;
        }}
        .score {{ font-size: 24px; font-weight: bold; color: #007bff; }}
        .recommendation {{
            background: #fff3cd;
            padding: 10px;
            margin: 5px 0;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Rapport Analytics - {analysis['project_name']}</h1>
        <p>Généré le {analysis['timestamp']}</p>
        <div class="score">Score global: {analysis['score']}/100</div>
    </div>

    <h2>📈 Métriques</h2>
    <div class="metric">
        <h3>Complexité du code</h3>
        <p>Complexité moyenne: {analysis['structure']['complexity'].get('average_complexity', 0):.2f}</p>
        <p>Complexité maximale: {analysis['structure']['complexity'].get('max_complexity', 0)}</p>
    </div>

    <div class="metric">
        <h3>Couverture de tests</h3>
        <p>Couverture globale: {analysis['structure']['coverage'].get('overall_coverage', 0):.1f}%</p>
    </div>

    <h2>💡 Recommandations</h2>
    {''.join([f'<div class="recommendation">• {rec}</div>' for rec in analysis['recommendations']])}
</body>
</html>
"""

    return html_template

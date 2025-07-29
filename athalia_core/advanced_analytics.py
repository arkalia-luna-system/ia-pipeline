#!/usr/bin/env python3
from pathlib import Path
from typing import Dict, Any
import json
import argparse
from datetime import datetime
import ast
import logging

logger = logging.getLogger(__name__)

"""
Module d'analytics avancée pour Athalia
Génère des métriques et dashboards pour l'analyse de projets
"""


class AdvancedAnalytics:
    metrics: dict

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.metrics = {
            "complexity": {},
            "coverage": {},
            "performance": {},
            "quality": {},
            "evolution": {}
        }

    def run(self) -> Dict[str, Any]:
        """Lance l'analyse complète du projet"""
        logger.info(f"📊 Analytics avancée pour : {self.project_path.name}")

        # Calcul des métriques
        self._analyze_complexity()
        self._analyze_coverage()
        self._analyze_performance()
        self._analyze_quality()
        self._analyze_evolution()

        # Génération du dashboard
        dashboard = self._generate_dashboard()

        return {
            "metrics": self.metrics,
            "dashboard": dashboard,
            "summary": self._generate_summary()
        }

    def _analyze_complexity(self):
        """Analyse la complexité du projet"""
        complexity_data = {"complexity": {}, "average": 0, "total_files": 0}
        total_complexity = 0
        file_count = 0

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())

                complexity = self._calculate_complexity(tree)
                complexity_data["complexity"][
                    str(py_file.relative_to(self.project_path))
                ] = complexity
                total_complexity += complexity
                file_count += 1
            except Exception:
                continue

        if file_count > 0:
            complexity_data["average"] = total_complexity / file_count
            complexity_data["total_files"] = file_count

        self.metrics["complexity"] = complexity_data

    def _calculate_complexity(self, tree: ast.AST) -> int:
        """Calcule la complexité cyclomatique d'un fichier"""
        complexity = 1  # Base complexity

        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1

        return complexity

    def _analyze_coverage(self):
        """Analyse la couverture du projet"""
        coverage_data = {
            "total_lines": 0,
            "docstrings": 0,
            "comments": 0,
            "empty_lines": 0,
            "files": 0
        }

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.splitlines()
                    tree = ast.parse(content)

                coverage_data["total_lines"] += len(lines)
                coverage_data["files"] += 1

                # Compter fonctions et classes
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        coverage_data["docstrings"] += 1
                    elif isinstance(node, ast.ClassDef):
                        coverage_data["docstrings"] += 1

                # Détecter fichiers de test
                if "test" in py_file.name.lower():
                    coverage_data["files"] += 1

                # Compter les lignes de code, docstrings, commentaires et vides
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith(
                            '"""') or stripped.startswith("'''"):
                        coverage_data["docstrings"] += 1
                    elif stripped.startswith('#'):
                        coverage_data["comments"] += 1
                    elif not stripped:
                        coverage_data["empty_lines"] += 1

            except Exception:
                continue

        self.metrics["coverage"] = coverage_data

    def _analyze_performance(self):
        """Analyse les métriques de performance du projet"""
        performance_data = {
            "file_sizes": {},
            "dependencies": 0
        }

        # Analyser les tailles de fichiers
        for py_file in self.project_path.rglob("*.py"):
            try:
                size = py_file.stat().st_size
                performance_data["file_sizes"][str(
                    py_file.relative_to(self.project_path))] = size
            except Exception:
                continue

        # Compter les dépendances
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file, 'r') as f:
                    deps = [line.strip() for line in f if line.strip()
                            and not line.startswith('#')]
                    performance_data["dependencies"] = len(deps)
            except Exception:
                pass

        self.metrics["performance"] = performance_data

    def _analyze_quality(self):
        """Analyse la qualité du projet"""
        quality_data = {
            "total_lines": 0,
            "docstrings": 0,
            "comments": 0,
            "empty_lines": 0
        }

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                quality_data["total_lines"] += len(lines)

                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith(
                            '"""') or stripped.startswith("'''"):
                        quality_data["docstrings"] += 1
                    elif stripped.startswith('#'):
                        quality_data["comments"] += 1
                    elif not stripped:
                        quality_data["empty_lines"] += 1

            except Exception:
                continue

        self.metrics["quality"] = quality_data

    def _analyze_evolution(self):
        """Analyse l'évolution du projet"""
        evolution_data = {
            "last_modified": None,
            "total_files": 0
        }

        # Compter les fichiers
        for py_file in self.project_path.rglob("*.py"):
            evolution_data["total_files"] += 1
            try:
                mtime = py_file.stat().st_mtime
                if not evolution_data["last_modified"] or mtime > evolution_data["last_modified"]:
                    evolution_data["last_modified"] = mtime
            except Exception:
                continue

        self.metrics["evolution"] = evolution_data

    def _generate_dashboard(self) -> str:
        """Génère un dashboard HTML"""
        metrics = self.metrics
        complexity = metrics.get('complexity', {})
        coverage = metrics.get('coverage', {})
        quality = metrics.get('quality', {})
        performance = metrics.get('performance', {})
        average = complexity.get('average', 0.0)
        total_files = complexity.get('total_files', 0)
        total_lines = coverage.get('total_lines', 0)
        docstrings = coverage.get('docstrings', 0)
        files = coverage.get('files', 0)
        comments = quality.get('comments', 0)
        empty_lines = quality.get('empty_lines', 0)
        total_quality_lines = quality.get('total_lines', 1)
        perf_dependencies = performance.get('dependencies', 0)
        perf_file_sizes = performance.get('file_sizes', {})

        dashboard_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard Analytics - {self.project_path.name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .metric {{ background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .summary {{ background: #e8f5e8; padding: 20px; border-radius: 5px; }}
        .chart {{ text-align: center; margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>📊 Dashboard Analytics-{self.project_path.name}</h1>
    <p>Généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <div class="summary">
        <h2>📈 Résumé</h2>
        <p><strong>Complexité moyenne :</strong> {average:.2f}</p>
        <p><strong>Fichiers analysés :</strong> {total_files}</p>
        <p><strong>Lignes de code :</strong> {total_lines}</p>
        <p><strong>Fonctions :</strong> {docstrings}</p>
        <p><strong>Classes :</strong> {docstrings}</p>
        <p><strong>Fichiers de test :</strong> {files - total_files}</p>
    </div>

    <div class="metric">
        <h3>🎯 Métriques de qualité</h3>
        <p>Docstrings : {docstrings}</p>
        <p>Commentaires : {comments}</p>
        <p>Lignes vides : {empty_lines}</p>
        <p>Ratio commentaires : {comments / max(1, total_quality_lines) * 100:.1f}%</p>
    </div>

    <div class="metric">
        <h3>⚡ Performance</h3>
        <p>Dépendances : {perf_dependencies}</p>
        <p>Fichiers Python : {len(perf_file_sizes)}</p>
    </div>

    <div class="metric">
        <h3>📋 Données brutes</h3>
        <pre>{json.dumps(self.metrics, indent=2)}</pre>
    </div>
</body>
</html>
"""

        dashboard_path = self.project_path / "analytics_dashboard.html"
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(dashboard_html)

        return str(dashboard_path)

    def _generate_summary(self) -> str:
        """Génère un résumé des métriques"""
        metrics = self.metrics
        complexity = metrics.get('complexity', {})
        coverage = metrics.get('coverage', {})
        quality = metrics.get('quality', {})
        performance = metrics.get('performance', {})
        average = complexity.get('average', 0.0)
        total_files = complexity.get('total_files', 0)
        total_lines = coverage.get('total_lines', 0)
        docstrings = coverage.get('docstrings', 0)
        files = coverage.get('files', 0)
        comments = quality.get('comments', 0)
        total_quality_lines = quality.get('total_lines', 1)
        perf_dependencies = performance.get('dependencies', 0)
        perf_file_sizes = performance.get('file_sizes', {})

        summary = f"""
📊 ANALYTICS AVANCÉE-{self.project_path.name}

🎯 MÉTRIQUES PRINCIPALES:
• Complexité moyenne: {average:.2f}
• Fichiers analysés: {total_files}
• Lignes de code: {total_lines}
• Fonctions: {docstrings}
• Classes: {docstrings}
• Fichiers de test: {files - total_files}

📈 QUALITÉ:
• Docstrings: {docstrings}
• Commentaires: {comments}
• Ratio commentaires: {comments / max(1, total_quality_lines) * 100:.1f}%

⚡ PERFORMANCE:
• Dépendances: {perf_dependencies}
• Fichiers Python: {len(perf_file_sizes)}

📊 FICHIERS GÉNÉRÉS:
• Dashboard HTML: analytics_dashboard.html
"""
        return summary

    def print_report(self):
        """Affiche le rapport d'analyse"""
        logger.info(self._generate_summary())


def enrich_genesis_md(outdir, infos, perf_log=None, test_log=None):
    from pathlib import Path
    genesis = Path(outdir) / 'GENESIS.f(f'
    content = genesis.read_text() if genesis.exists() else ''
    if 'Audit IA' not in content:
        content += '\nAudit IA\n'
    genesis.write_text(content)
    return str(genesis)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analytics avancée")
    parser.add_argument("project_path", help="Chemin du projet à analyser")
    args = parser.parse_args()
    analytics = AdvancedAnalytics(args.project_path)
    result = analytics.run()
    analytics.print_report()

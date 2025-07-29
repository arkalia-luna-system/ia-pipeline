#!/usr/bin/env python3
"""
📊 MODULE ANALYTICS ATHALIA
===========================
Module d'analyse et de métriques de projets.
Fournit des analyses de base pour les tests.
"""

from pathlib import Path
from typing import Dict, Any
from datetime import datetime


def analyze_project(project_path: str = ".") -> Dict[str, Any]:
    """Analyser un projet et retourner des métriques de base"""
    project_path_obj = Path(project_path)

    # Compter les fichiers
    python_files = list(project_path_obj.rglob("*.py"))
    md_files = list(project_path_obj.rglob("*.md"))
    yaml_files = list(project_path_obj.rglob("*.yaml")) + \
        list(project_path_obj.rglob("*.yml"))

    # Calculer la taille du projet
    total_size = sum(
        f.stat().st_size for f in project_path_obj.rglob("*") if f.is_file())

    # Analyser la structure
    structure = {
        "directories": len([d for d in project_path_obj.rglob("*") if d.is_dir()]),
        "files": len([f for f in project_path_obj.rglob("*") if f.is_file()]),
        "python_files": len(python_files),
        "markdown_files": len(md_files),
        "config_files": len(yaml_files)
    }

    # Calculer un score de qualité basique
    quality_score = 75.0  # Score de base

    # Améliorer le score basé sur la structure
    if structure["python_files"] > 0:
        quality_score += 10
    if structure["markdown_files"] > 0:
        quality_score += 5
    if structure["config_files"] > 0:
        quality_score += 5

    return {
        "project_name": project_path_obj.name,
        "project_path": str(project_path_obj),
        "analysis_date": datetime.now().isoformat(),
        "structure": structure,
        "metrics": {
            "total_size_mb": total_size / (1024 * 1024),
            "quality_score": min(100, quality_score),
            "complexity": "medium"
        },
        "score": min(100, quality_score)
    }


def generate_heatmap_data(project_path: str = ".") -> Dict[str, Any]:
    """Générer des données pour une heatmap de complexité"""
    project_path_obj = Path(project_path)
    python_files = list(project_path_obj.rglob("*.py"))

    heatmap_data = []
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Complexité basique basée sur le nombre de lignes
                complexity = len(lines)

                heatmap_data.append({
                    "file": str(py_file.relative_to(project_path_obj)),
                    "complexity": complexity,
                    "lines": len(lines)
                })
        except Exception:
            continue

    return {
        "heatmap_data": heatmap_data,
        "total_files": len(heatmap_data),
        "max_complexity": max([d["complexity"] for d in heatmap_data], default=0)
    }


def generate_technical_debt_analysis(
        project_path: str = ".") -> Dict[str, Any]:
    """Analyser la dette technique du projet"""
    project_path_obj = Path(project_path)

    # Détecter les patterns de dette technique basiques
    debt_indicators = []

    # Chercher les TODO, FIXME, etc.
    for py_file in project_path_obj.rglob("*.py"):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "TODO" in content:
                    debt_indicators.append(f"TODO dans {py_file.name}")
                if "FIXME" in content:
                    debt_indicators.append(f"FIXME dans {py_file.name}")
                if "HACK" in content:
                    debt_indicators.append(f"HACK dans {py_file.name}")
        except Exception:
            continue

    return {
        "technical_debt_score": max(0, 100 - len(debt_indicators) * 5),
        "debt_indicators": debt_indicators,
        "recommendations": [
            "Réviser les TODO et FIXME",
            "Améliorer la documentation",
            "Optimiser les imports"
        ] if debt_indicators else ["Projet en bon état"]
    }


def generate_analytics_html(project_path: str = ".") -> str:
    """Générer un rapport HTML d'analytics"""
    # Si project_path est un dictionnaire, extraire le chemin
    if isinstance(project_path, dict) and "path" in project_path:
        project_path = project_path["path"]
    elif isinstance(project_path, list) and project_path:
        project_path = project_path[0]
    elif not isinstance(project_path, str):
        project_path = "."

    analysis = analyze_project(project_path)
    generate_heatmap_data(project_path)  # Variable non utilisée supprimée
    debt = generate_technical_debt_analysis(project_path)

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Analytics - {analysis['project_name']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .metric {{ margin: 10px 0; padding: 10px; background: #f5f5f5; }}
        .score {{ font-size: 24px; color: #007cba; }}
    </style>
</head>
<body>
    <h1>📊 Analytics - {analysis['project_name']}</h1>

    <div class="metric">
        <h2>Score de Qualité</h2>
        <div class="score">{analysis['score']:.1f}/100</div>
    </div>

    <div class="metric">
        <h2>Structure du Projet</h2>
        <p>Fichiers Python: {analysis['structure']['python_files']}</p>
        <p>Fichiers Markdown: {analysis['structure']['markdown_files']}</p>
        <p>Fichiers de configuration: {analysis['structure']['config_files']}</p>
    </div>

    <div class="metric">
        <h2>Dette Technique</h2>
        <p>Score: {debt['technical_debt_score']}/100</p>
        <p>Indicateurs: {len(debt['debt_indicators'])}</p>
    </div>

    <div class="metric">
        <h2>Recommandations</h2>
        <ul>
            {''.join(f'<li>{rec}</li>' for rec in debt['recommendations'])}
        </ul>
    </div>
</body>
</html>
"""

    return html_content


# Variables pour les tests
ANALYTICS_AVAILABLE = True

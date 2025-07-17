#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.audit import audit_project_intelligent
from typing import Dict, List, Any
import json
import os
import logging

logger = logging.getLogger(__name__)

"""
Module analytics IA pour visualisations avancées.
"""

def generate_heatmap_data(projects_info: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Génère les données pour une heatmap des scores d'audit."""
    heatmap_data: Dict[str, Any] = {
        'labels': [],
        'datasets': []
    }

    # Collecter les scores pour chaque projet
    for info in projects_info:
        try:
            audit = audit_project_intelligent(info['name'])
            score = audit.get('global_score', 0)
            metrics = audit.get('metrics', {})

            heatmap_data['labels'].append(info['name'])

            # Données pour chaque métrique
            metrics_data = {
                'structure': metrics.get('structure_score', 0),
                'code': metrics.get('code_score', 0),
                'tests': metrics.get('test_score', 0),
                'documentation': metrics.get('doc_score', 0),
                'security': metrics.get('security_score', 0),
                'performance': metrics.get('perf_score', 0)
            }

            heatmap_data['datasets'].append({
                'project': info['name'],
                'global_score': score,
                'metrics': metrics_data
            })

        except Exception as e:
            # En cas d'erreur, utiliser des valeurs par défaut
            heatmap_data['labels'].append(info['name'])
            heatmap_data['datasets'].append({
                'project': info['name'],
                'global_score': 0,
                'metrics': {
                    'structure': 0, 'code': 0, 'tests': 0,
                    'documentation': 0, 'security': 0, 'performance': 0
                }
            })

    return heatmap_data

def generate_technical_debt_analysis(projects_info: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyse la dette technique globale."""
    debt_analysis: Dict[str, Any] = {
        'total_projects': len(projects_info),
        'average_score': 0,
        'score_distribution': {'excellent': 0, 'good': 0, 'medium': 0, 'critical': 0},
        'common_issues': {},
        'top_suggestions': []
    }

    total_score = 0
    all_issues = []
    all_suggestions = []

    for info in projects_info:
        try:
            audit = audit_project_intelligent(info['name'])
            score = audit.get('global_score', 0)
            issues = audit.get('issues', [])
            suggestions = audit.get('suggestions', [])

            total_score += score

            # Classification du score
            if score >= 80:
                debt_analysis['score_distribution']['excellent'] += 1
            elif score >= 60:
                debt_analysis['score_distribution']['good'] += 1
            elif score >= 40:
                debt_analysis['score_distribution']['medium'] += 1
            else:
                debt_analysis['score_distribution']['critical'] += 1

            # Collecter les problèmes communs
            for issue in issues:
                issue_type = issue.split(':')[0] if ':' in issue else 'Autre'
                debt_analysis['common_issues'][issue_type] = debt_analysis['common_issues'].get(issue_type, 0) + 1

            all_issues.extend(issues)
            all_suggestions.extend(suggestions)

        except Exception:
            debt_analysis['score_distribution']['critical'] += 1

    # Calculer la moyenne
    if debt_analysis['total_projects'] > 0:
        debt_analysis['average_score'] = total_score / debt_analysis['total_projects']

    # Top suggestions (les plus fréquentes)
    suggestion_counts: Dict[str, int] = {}
    for suggestion in all_suggestions:
        suggestion_counts[suggestion] = suggestion_counts.get(suggestion, 0) + 1

    debt_analysis['top_suggestions'] = sorted(
        suggestion_counts.items(),
        key=lambda value: value[1],
        reverse=True
    )[:5]

    return debt_analysis

def generate_analytics_html(projects_info: List[Dict[str, Any]]) -> str:
    """Génère le HTML pour les analytics avancés."""
    heatmap_data = generate_heatmap_data(projects_info)
    debt_analysis = generate_technical_debt_analysis(projects_info)

    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>Analytics IA - Athalia Pipeline</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .analytics-container {{ display: flex; flex-wrap: wrap; gap: 20px; }}
        .chart-container {{ width: 45%; min-width: 400px; }}
        .debt-summary {{ background: #f5f5f5; padding: 15px; border-radius: 5px; }}
        .score-excellent {{ color: #28a745; }}
        .score-good {{ color: #ffc107; }}
        .score-medium {{ color: #fd7e14; }}
        .score-critical {{ color: #dc3545; }}
    </style>
</head>
<body>
    <h1>📊 Analytics IA - Athalia Pipeline</h1>

    <div class="debt-summary">
        <h2>Résumé de la dette technique</h2>
        <p><strong>Projets analysés:</strong> {debt_analysis['total_projects']}</p>
        <p><strong>Score moyen:</strong> <span class="score-{'excellent' if debt_analysis['average_score'] >= 80 else 'good' if debt_analysis['average_score'] >= 60 else 'medium' if debt_analysis['average_score'] >= 40 else 'critical'}">{debt_analysis['average_score']:.1f}/100</span></p>

        <h3>Distribution des scores:</h3>
        <ul>
            <li class="score-excellent">🟢 Excellent (≥80): {debt_analysis['score_distribution']['excellent']}</li>
            <li class="score-good">🟡 Bon (60-79): {debt_analysis['score_distribution']['good']}</li>
            <li class="score-medium">🟠 Moyen (40-59): {debt_analysis['score_distribution']['medium']}</li>
            <li class="score-critical">🔴 Critique (<40): {debt_analysis['score_distribution']['critical']}</li>
        </ul>
    </div>

    <div class="analytics-container">
        <div class="chart-container">
            <h2>Heatmap des scores par projet</h2>
            <canvas id="heatmapChart"></canvas>
        </div>

        <div class="chart-container">
            <h2>Problèmes les plus fréquents</h2>
            <canvas id="issuesChart"></canvas>
        </div>
    </div>

    <div class="debt-summary">
        <h3>Top suggestions d'amélioration:</h3>
        <ol>
'''
    for suggestion, count in debt_analysis['top_suggestions']:
        html += f'            <li><strong>{suggestion}</strong> (mentionné {count} fois)</li>\n'

    html += '''        </ol>
    </div>

    <script>
        // Heatmap des scores
        const heatmapCtx = document.getElementById('heatmapChart').getContext('2d');
        new Chart(heatmapCtx, {
            type: 'bar',
            data: {
                labels: ''' + json.dumps(heatmap_data['labels']) + ''',
                datasets: [{
                    label: 'Score global',
                    data: ''' + json.dumps([d['global_score'] for d in heatmap_data['datasets']]) + ''',
                    backgroundColor: function(context) {
                        const value = context.parsed.y;
                        if (value >= 80) return 'rgba(40, 167, 69, 0.8)';
                        if (value >= 60) return 'rgba(255, 193, 7, 0.8)';
                        if (value >= 40) return 'rgba(253, 126, 20, 0.8)';
                        return 'rgba(220, 53, 69, 0.8)';
                    }
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Scores globaux par projet'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
        // Problèmes les plus fréquents (exemple simplifié)
        const issuesCtx = document.getElementById('issuesChart').getContext('2d');
        new Chart(issuesCtx, {
            type: 'bar',
            data: {
                labels: ''' + json.dumps(list(debt_analysis['common_issues'].keys())) + ''',
                datasets: [{
                    label: 'Occurrences',
                    data: ''' + json.dumps(list(debt_analysis['common_issues'].values())) + ''',
                    backgroundColor: 'rgba(220, 53, 69, 0.8)'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Problèmes les plus fréquents'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    </script>
</body>
</html>'''
    return html

def save_analytics(projects_info: List[Dict[str, Any]], output_file: str = 'analytics.html'):
    """Sauvegarde les analytics dans un fichier HTML."""
    html_content = generate_analytics_html(projects_info)
    with open(output_file, 'w', encoding='utf-8') as file_handle:
        file_handle.write(html_content)
    return output_file


def analyze_project(project_path: str) -> dict:
    """Analyse un projet et retourne des métriques clés."""
    report = {
        'total_files': 0,
        'python_files': 0,
        'test_files': 0,
        'md_files': 0,
        'dirs': 0
    }
    for root, dirs, files in os.walk(project_path):
        report['dirs'] += len(dirs)
        for file_handle in files:
            report['total_files'] += 1
            if file_handle.endswith('.py'):
                report['python_files'] += 1
            if 'test' in file_handle.lower():
                report['test_files'] += 1
            if file_handle.endswith('.md'):
                report['md_files'] += 1
    return report
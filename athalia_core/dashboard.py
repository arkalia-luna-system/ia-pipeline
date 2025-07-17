#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.audit import audit_project_intelligent
import os
import logging
"""
Module dashboard, logs, audit, GENESIS.md.
"""

def enrich_genesis_md(outdir, blueprint, perf_log=None, test_log=None):
    # Supporte GENESIS.md et GENESIS.f(f
    genesis_paths = [
        os.path.join(outdir, 'GENESIS.md'),
        os.path.join(outdir, 'GENESIS.f(f')
    ]
    for genesis_path in genesis_paths:
        with open(genesis_path, 'a') as file_handle:
            file_handle.write("\n---\n# Audit IA\n")
            file_handle.write("## Scripts et prompts injectés :\n")
            file_handle.write("- prompts/ (tous les prompts types)\n")
            file_handle.write("- setup/ath-dev-boost.sh\n")
            file_handle.write("- setup/alias.sh\n")
            file_handle.write("- agents/ath_context_prompt.py\n")
            file_handle.write("\n## Alias disponibles : ath-chat, ath-clean, ath-dev-boost, ath-perplex, ath-smart\n")
            if test_log:
                file_handle.write(f"\n## Résultats des tests Booster IA :\n{test_log}\n")
            if perf_log:
                file_handle.write(f"\n## Performance génération :\n{perf_log}\n")
    logging.info(f"GENESIS enrichi dans {outdir}")

def generate_dashboard_html(projects_info):
    dash_path = 'dashboard.html'
    with open(dash_path, 'w') as file_handle:
        file_handle.write('<!DOCTYPE html>\n<html>\n<head>\n    <title>Dashboard IA</title>\n    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n    <style>\n        body { font-family: Arial, sans-serif; margin: 20px; }\n        table { border-collapse: collapse; width: 100%; margin: 20px 0; }\n        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }\n        th { background-color: #f2f2f2; }\n        .status-ok { color: green; }\n        .status-error { color: red; }\n        .logs-section { background: #f5f5f5; padding: 15px; margin: 20px 0; border-radius: 5px; }\n        .chart-container { width: 50%; margin: 20px 0; }\n        .audit-score { font-weight: bold; }\n        .audit-bad { color: red; }\n        .audit-good { color: green; }\n    </style>\n</head>\n<body>\n    <h1>Dashboard Audit / Qualité Projets IA</h1>\n    <div class="logs-section">\n        <h2>Logs récents</h2>\n        <div id="logs-content">\n            <p>Chargement des logs en cours...</p>\n        </div>\n    </div>\n    <table>\n        <tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Score Audit</th><th>Problèmes</th><th>Suggestions</th><th>Docs</th></tr>')
        for info in projects_info:
            try:
                audit = audit_project_intelligent(info['name'])
                score = audit.get('global_score', 0)
                issues = audit.get('issues', [])
                suggestions = audit.get('suggestions', [])
                score_class = 'audit-good' if score >= 80 else ('audit-bad' if score < 60 else '')
                score_html = f'<span class="audit-score {score_class}">{score:.1f}/100</span>'
                issues_html = '<ul>' + ''.join(f'<li>{index}</li>' for index in issues[:3]) + ('<li>...</li>' if len(issues) > 3 else '') + '</ul>' if issues else 'Aucun'
                sugg_html = '<ul>' + ''.join(f'<li>{string_data}</li>' for string_data in suggestions[:2]) + ('<li>...</li>' if len(suggestions) > 2 else '') + '</ul>' if suggestions else 'Aucune'
            except Exception as e:
                score_html = '<span class="audit-score audit-bad">Erreur</span>'
                issues_html = f"Erreur: {e}"
                sugg_html = "-"
            test_class = "status-ok" if info.get('tests') == 'OK' else "status-error"
            perf_class = "status-ok" if info.get('perf') == 'OK' else "status-error"
            file_handle.write(f'<tr>\n'
                             f'<td>{info["name"]}</td>'
                             f'<td>{info["date"]}</td>'
                             f'<td class="{test_class}">{info.get("tests", "N/A")}</td>'
                             f'<td class="{perf_class}">{info.get("perf", "N/A")}</td>'
                             f'<td>{score_html}</td>'
                             f'<td>{issues_html}</td>'
                             f'<td>{sugg_html}</td>'
                             f'<td><a href="{info["name"]}/DOC.md">DOC</a> | <a href="{info["name"]}/GENESIS.md">GENESIS</a></td>'
                             f'</tr>\n')
        file_handle.write('</table>\n    <div class="chart-container">\n        <canvas id="projectsChart"></canvas>\n    </div>\n    <h2>Architecture multi-projets/agents</h2>\n    <pre><code class="language-mermaid">graph TD\n')
        for info in projects_info:
            file_handle.write(f'    IA[IA] --> {info["name"]}\n')
        file_handle.write('</code></pre>\n    <script>\n        setInterval(function() {\n            fetch("/api/logs")\n                .then(response => response.text())\n                .then(data => {\n                    document.getElementById("logs-content").innerHTML = data;\n                })\n                .catch(error => {\n                    console.log("Erreur chargement logs:", error);\n                });\n        }, 5000);\n        const ctx = document.getElementById("projectsChart").getContext("2d");\n        // ... code du graphique à compléter ...\n    </script>\n</body>\n</html>')
    logging.info("Dashboard HTML généré avec monitoring et audit.")

def generate_multi_project_mermaid(projects_info):
    dash_path = 'dashboard.md'
    with open(dash_path, 'a') as file_handle:
        file_handle.write('\n## Architecture multi-projets/agents (Mermaid)\n')
        file_handle.write('```mermaid\ngraph TD\n')
        for info in projects_info:
            file_handle.write(f"    IA[IA] --> {info['name']}\n")
        file_handle.write('```\n')
    logging.info("Diagramme Mermaid multi-projets généré.")

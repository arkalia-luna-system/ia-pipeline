"""
Module dashboard, logs, audit, GENESIS.md.
"""

import os
import logging
from athalia_core.audit import audit_project_intelligent

def enrich_genesis_md(outdir, blueprint, perf_log=None, test_log=None):
    genesis_path = os.path.join(outdir, 'GENESIS.md')
    with open(genesis_path, 'a') as f:
        f.write("\n---\n# Audit IA\n")
        f.write("## Scripts et prompts injectés :\n")
        f.write("- prompts/ (tous les prompts types)\n")
        f.write("- setup/ath-dev-boost.sh\n")
        f.write("- setup/alias.sh\n")
        f.write("- agents/ath_context_prompt.py\n")
        f.write("\n## Alias disponibles : ath-chat, ath-clean, ath-dev-boost, ath-perplex, ath-smart\n")
        if test_log:
            f.write(f"\n## Résultats des tests Booster IA :\n{test_log}\n")
        if perf_log:
            f.write(f"\n## Performance génération :\n{perf_log}\n")
    logging.info(f"GENESIS.md enrichi dans {outdir}")

def generate_dashboard_html(projects_info):
    dash_path = 'dashboard.html'
    with open(dash_path, 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Dashboard IA</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .status-ok { color: green; }
        .status-error { color: red; }
        .logs-section { background: #f5f5f5; padding: 15px; margin: 20px 0; border-radius: 5px; }
        .chart-container { width: 50%; margin: 20px 0; }
        .audit-score { font-weight: bold; }
        .audit-bad { color: red; }
        .audit-good { color: green; }
    </style>
</head>
<body>
    <h1>Dashboard Audit/Qualité Projets IA</h1>
    
    <div class="logs-section">
        <h2>Logs récents</h2>
        <div id="logs-content">
            <p>Chargement des logs en cours...</p>
        </div>
    </div>
    
    <table>
        <tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Score Audit</th><th>Problèmes</th><th>Suggestions</th><th>Docs</th></tr>''')
        
        for info in projects_info:
            # Audit intelligent pour chaque projet
            try:
                audit = audit_project_intelligent(info['name'])
                score = audit.get('global_score', 0)
                issues = audit.get('issues', [])
                suggestions = audit.get('suggestions', [])
                score_class = 'audit-good' if score >= 80 else ('audit-bad' if score < 60 else '')
                score_html = f'<span class="audit-score {score_class}">{score:.1f}/100</span>'
                issues_html = '<ul>' + ''.join(f'<li>{i}</li>' for i in issues[:3]) + ('<li>...</li>' if len(issues)>3 else '') + '</ul>' if issues else 'Aucun'
                sugg_html = '<ul>' + ''.join(f'<li>{s}</li>' for s in suggestions[:2]) + ('<li>...</li>' if len(suggestions)>2 else '') + '</ul>' if suggestions else 'Aucune'
            except Exception as e:
                score_html = '<span class="audit-score audit-bad">Erreur</span>'
                issues_html = f"Erreur: {e}"
                sugg_html = "-"
            test_class = "status-ok" if info.get('tests') == 'OK' else "status-error"
            perf_class = "status-ok" if info.get('perf') == 'OK' else "status-error"
            f.write(f'''<tr>
                <td>{info['name']}</td>
                <td>{info['date']}</td>
                <td class="{test_class}">{info.get('tests', 'N/A')}</td>
                <td class="{perf_class}">{info.get('perf', 'N/A')}</td>
                <td>{score_html}</td>
                <td>{issues_html}</td>
                <td>{sugg_html}</td>
                <td><a href='{info['name']}/DOC.md'>DOC</a> | <a href='{info['name']}/GENESIS.md'>GENESIS</a></td>
            </tr>''')
        
        f.write('''</table>
    
    <div class="chart-container">
        <canvas id="projectsChart"></canvas>
    </div>
    
    <h2>Architecture multi-projets/agents</h2>
    <pre><code class="language-mermaid">graph TD\n''')
        
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        
        f.write('''</code></pre>
    
    <script>
        // Mise à jour automatique des logs
        setInterval(function() {
            fetch('/api/logs')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('logs-content').innerHTML = data;
                })
                .catch(error => {
                    console.log('Erreur chargement logs:', error);
                });
        }, 5000);
        
        // Graphique des projets
        const ctx = document.getElementById('projectsChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ''' + str([info['name'] for info in projects_info]) + ''',
                datasets: [{
                    label: 'Score Audit',
                    data: ''' + str([audit_project_intelligent(info['name']).get('global_score', 0) for info in projects_info]) + ''',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    </script>
</body>
</html>''')
    logging.info("Dashboard HTML généré avec monitoring et audit.")

def generate_multi_project_mermaid(projects_info):
    dash_path = 'dashboard.md'
    with open(dash_path, 'a') as f:
        f.write('\n## Architecture multi-projets/agents (Mermaid)\n')
        f.write('```mermaid\ngraph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('```\n')
    logging.info("Diagramme Mermaid multi-projets généré.")

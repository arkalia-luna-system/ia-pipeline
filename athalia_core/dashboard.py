"""
Module dashboard, logs, audit, GENESIS.md.
"""

import os
import logging

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
        f.write('<html><head><title>Dashboard IA</title></head><body>')
        f.write('<h1>Dashboard Audit/Qualité Projets IA</h1>')
        f.write('<table border=1><tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Docs</th></tr>')
        for info in projects_info:
            f.write(f"<tr><td>{info['name']}</td><td>{info['date']}</td><td>{info['tests']}</td><td>{info['perf']}</td><td><a href='{info['name']}/DOC.md'>DOC</a> | <a href='{info['name']}/GENESIS.md'>GENESIS</a></td></tr>")
        f.write('</table>')
        f.write('<h2>Architecture multi-projets/agents</h2>')
        f.write('<pre><code class="language-mermaid">graph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('</code></pre>')
        f.write('</body></html>')
    logging.info("Dashboard HTML généré.")

def generate_multi_project_mermaid(projects_info):
    dash_path = 'dashboard.md'
    with open(dash_path, 'a') as f:
        f.write('\n## Architecture multi-projets/agents (Mermaid)\n')
        f.write('```mermaid\ngraph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('```\n')
    logging.info("Diagramme Mermaid multi-projets généré.")

"""
Module onboarding, guides, scripts d’installation.
"""

import os
import logging

def generate_onboarding_md(blueprint, outdir):
    onboard_path = os.path.join(outdir, 'ONBOARDING.md')
    with open(onboard_path, 'w') as f:
        f.write(f"# Guide d’onboarding\n\n")
        f.write(f"## 1. Cloner le repo\n\n    git clone <repo_url>\n\n")
        f.write(f"## 2. Installer les dépendances\n\n    pip install -r requirements.txt\n\n")
        f.write(f"## 3. Lancer les tests\n\n    pytest\n\n")
        f.write(f"## 4. Lancer l’API (exemple)\n\n    python src/main.py\n\n")
        f.write(f"## 5. Générer la doc\n\n    cat DOC.md\n\n")
        f.write(f"## 6. CI/CD\n\n    Voir .github/workflows/ci.yaml\n\n")
        f.write(f"## 7. Swagger\n\n    Utiliser openapi.yaml avec Swagger UI\n\n")
    logging.info(f"ONBOARDING.md généré dans {outdir}")

def generate_onboard_cli(blueprint, outdir):
    cli_path = os.path.join(outdir, 'onboard.py')
    with open(cli_path, 'w') as f:
        f.write('''import sys\nsteps = [\n    "Cloner le repo : git clone <repo_url>",\n    "Installer les dépendances : pip install -r requirements.txt",\n    "Lancer les tests : pytest",\n    "Lancer l’API : python src/main.py",\n    "Générer la doc : cat DOC.md",\n    "CI/CD : Voir .github/workflows/ci.yaml",\n    "Swagger : Utiliser openapi.yaml avec Swagger UI",\n]\ndef main():\n    for i, step in enumerate(steps, 1):\n        input(f"[Étape {i}] {step} (Entrée pour continuer)")\nif __name__ == "__main__":\n    main()\n''')
    logging.info(f"Script CLI d’onboarding généré dans {outdir}")

def generate_onboarding_html_advanced(blueprint, outdir):
    onboard_path = os.path.join(outdir, 'ONBOARDING.html')
    with open(onboard_path, 'w') as f:
        f.write('''<html><head><title>Onboarding</title></head><body>
<h1>Guide d’onboarding interactif</h1>
<ol>
<li>Cloner le repo : <code>git clone &lt;repo_url&gt;</code></li>
<li>Installer les dépendances : <code>pip install -r requirements.txt</code></li>
<li>Lancer les tests : <code>pytest</code></li>
<li>Lancer l’API : <code>python src/main.py</code></li>
<li>Générer la doc : <code>cat DOC.md</code></li>
<li>CI/CD : Voir <code>.github/workflows/ci.yaml</code></li>
<li>Swagger : Utiliser <code>openapi.yaml</code> avec Swagger UI</li>
<li>Dashboard : <a href="../../dashboard.html">dashboard.html</a></li>
<li>Tickets : <a href="github_issues.md">github_issues.md</a></li>
<li>Doc technique : <a href="DOC.md">DOC.md</a></li>
<li>Vidéo tuto : <a href="https://www.youtube.com/results?search_query=onboarding+python+project" target="_blank">Voir exemple</a></li>
</ol>
</body></html>''')
    logging.info(f"ONBOARDING.html généré dans {outdir}")

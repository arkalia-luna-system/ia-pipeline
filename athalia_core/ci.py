"""
Module CI/CD, génération de workflows, badges, Taskfile.
"""

import os
import logging

def generate_github_ci_yaml(outdir):
    ci_dir = os.path.join(outdir, '.github', 'workflows')
    os.makedirs(ci_dir, exist_ok=True)
    ci_path = os.path.join(ci_dir, 'ci.yaml')
    with open(ci_path, 'w') as f:
        f.write('''name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - name: Set up Python\n        uses: actions/setup-python@v4\n        with:\n          python-version: '3.10'\n      - name: Install deps\n        run: pip install -r requirements.txt pytest\n      - name: Run tests\n        run: pytest\n''')
    readme_path = os.path.join(outdir, 'README.md')
    badge = f"![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yaml/badge.svg)\n"
    if os.path.exists(readme_path):
        with open(readme_path, 'r+') as f:
            content = f.read()
            if '![CI]' not in content:
                f.seek(0, 0)
                f.write(badge + content)
    logging.info(f"Workflow CI généré dans {ci_path}")

def add_coverage_badge(outdir):
    readme_path = os.path.join(outdir, 'README.md')
    badge = '![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)\n'
    if os.path.exists(readme_path):
        with open(readme_path, 'r+') as f:
            content = f.read()
            if '![Coverage]' not in content:
                f.seek(0, 0)
                f.write(badge + content)
    logging.info(f"Badge coverage ajouté dans {readme_path}")

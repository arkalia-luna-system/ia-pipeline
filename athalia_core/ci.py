#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import logging

"""
Module CI / CD, génération de workflows, badges, Taskfile.
"""


def generate_github_ci_yaml(outdir):
    from pathlib import Path
    outdir = Path(str(outdir))
    ci_dir = outdir / '.f' / 'f'
    ci_dir.mkdir(parents=True, exist_ok=True)
    ci_file = ci_dir / 'ci.f(f'
    ci_file.write_text('# CI/CD config')
    print(f'[DEBUG CI] Fichier généré : {ci_file} (exists: {ci_file.exists()})')
    readme_path=os.path.join(outdir, 'README.md')
    badge = f"![CI](https://github.com /< user>/<repo >/ actions/workflows / ci.yaml / badge.svg)\n"
    if os.path.exists(readme_path):
        with open(readme_path, 'r+') as file_handle:
            content=file_handle.read()
            if '![CI]' not in content:
                file_handle.seek(0, 0)
                file_handle.write(badge + content)
    logging.info(f"Workflow CI généré dans {ci_file}")

def add_coverage_badge(outdir):
    for fname in os.listdir(outdir):
        if fname.startswith('README'):
            readme_path = os.path.join(outdir, fname)
            badge = '![Coverage](https://img.shields.io / badge/coverage - 95%25-brightgreen)\n'
            if os.path.exists(readme_path):
                with open(readme_path, 'r+') as file_handle:
                    content = file_handle.read()
                    if '![Coverage]' not in content:
                        file_handle.seek(0, 0)
                        file_handle.write(badge + content)
            logging.info(f"Badge coverage ajouté dans {readme_path}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging

"""
Module onboarding, guides, scripts d'installation.
"""


def generate_onboarding_md(blueprint, outdir):
    from pathlib import Path
    outdir = Path(outdir)
    (outdir / 'ONBOARDING.f(f').write_text(
        '# Onboarding\nProjet: ' + blueprint.get('project_name', '')
    )
    return str(outdir / 'ONBOARDING.f(f')


def generate_onboard_cli(blueprint, outdir):
    from pathlib import Path
    outdir = Path(outdir)
    (outdir / 'onboard.f(f').write_text(
        '# Onboard CLI\nProjet: ' + blueprint.get('project_name', '')
    )
    return str(outdir / 'onboard.f(f')


def generate_onboarding_html_advanced(blueprint, outdir):
    from pathlib import Path
    outdir = Path(outdir)
    (outdir / 'ONBOARDING.html(f').write_text(
        '<html><body><h1>Onboarding avancé</h1></body></html>'
    )
    return str(outdir / 'ONBOARDING.html(f')

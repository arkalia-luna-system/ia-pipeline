#!/usr/bin/env python3

"""
Module onboarding, guides, scripts d'installation.
"""


def generate_onboarding_md(blueprint, outdir):
    from pathlib import Path

    outdir = Path(outdir)
    (outdir / "ONBOARDING.md").write_text(
        "# Onboarding\nProjet: " + blueprint.get("project_name", "")
    )
    return str(outdir / "ONBOARDING.md")


def generate_onboard_cli(blueprint, outdir):
    from pathlib import Path

    outdir = Path(outdir)
    (outdir / "onboard.py").write_text(
        "# Onboard CLI\nProjet: " + blueprint.get("project_name", "")
    )
    return str(outdir / "onboard.py")


def generate_onboarding_html_advanced(blueprint, outdir):
    from pathlib import Path

    outdir = Path(outdir)
    (outdir / "ONBOARDING.html").write_text(
        "<html><body><h1>Onboarding avancé</h1></body></html>"
    )
    return str(outdir / "ONBOARDING.html")

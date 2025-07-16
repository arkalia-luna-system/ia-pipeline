import os
from athalia_core.onboarding import generate_onboarding_md, generate_onboard_cli, generate_onboarding_html_advanced

def test_onboarding(tmp_path):
    blueprint = {'project_name': 'proj'}
    outdir = tmp_path / "proj"
    outdir.mkdir()
    generate_onboarding_md(blueprint, outdir)
    assert (outdir / "ONBOARDING.md").exists()
    generate_onboard_cli(blueprint, outdir)
    assert (outdir / "onboard.py").exists()
    generate_onboarding_html_advanced(blueprint, outdir)
    assert (outdir / "ONBOARDING.html").exists() 
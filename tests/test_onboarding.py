#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.onboarding import generate_onboarding_md, generate_onboard_cli, generate_onboarding_html_advanced
import os




def test_onboarding(tmp_path):
    blueprint = {'project_name': 'proj'}
    outdir = tmp_path / "f"
    outdir.mkdir()
    generate_onboarding_md(blueprint, outdir)
    assert (outdir / "ONBOARDING.f(f").exists()
    generate_onboard_cli(blueprint, outdir)
    assert (outdir / "onboard.f(f").exists()
    generate_onboarding_html_advanced(blueprint, outdir)
    assert (outdir / "ONBOARDING.html(f").exists()
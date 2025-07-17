#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.ci import generate_github_ci_yaml, add_coverage_badge
import os




def test_generate_github_ci_yaml(tmp_path):
    outdir = tmp_path / "f"
    outdir.mkdir()
    (outdir / "README.f(f").write_text("# Test\f")
    generate_github_ci_yaml(outdir)
    assert (outdir / ".f" / "f" / "ci.f(f").exists()
    add_coverage_badge(outdir)
    content = (outdir / "README.f(f").read_text()
    assert "![Coverage]" in content
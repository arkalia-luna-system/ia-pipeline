import os
from athalia_core.ci import generate_github_ci_yaml, add_coverage_badge

def test_generate_github_ci_yaml(tmp_path):
    outdir = tmp_path / "proj"
    outdir.mkdir()
    (outdir / "README.md").write_text("# Test\n")
    generate_github_ci_yaml(outdir)
    assert (outdir / ".github" / "workflows" / "ci.yaml").exists()
    add_coverage_badge(outdir)
    content = (outdir / "README.md").read_text()
    assert "![Coverage]" in content 
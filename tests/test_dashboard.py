import os
from athalia_core.dashboard import enrich_genesis_md, generate_dashboard_html, generate_multi_project_mermaid

def test_enrich_genesis_md(tmp_path):
    outdir = tmp_path / "proj"
    outdir.mkdir()
    genesis = outdir / "GENESIS.md"
    genesis.write_text("")
    enrich_genesis_md(outdir, {'project_name': 'proj'}, perf_log="OK", test_log="OK")
    content = genesis.read_text()
    assert "Audit IA" in content

def test_generate_dashboard_html(tmp_path):
    projects_info = [{'name': 'p1', 'date': '2024-01-01', 'tests': 'OK', 'perf': 'OK'}]
    generate_dashboard_html(projects_info)
    assert os.path.exists('dashboard.html')
    generate_multi_project_mermaid(projects_info)
    assert os.path.exists('dashboard.md') 
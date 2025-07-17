import os
import shutil
import pytest
from athalia_core import generation

def test_generate_blueprint_mock():
    idea = "Test projet IA"
    blueprint = generation.generate_blueprint_mock(idea)
    assert blueprint['description'] == idea
    assert 'modules' in blueprint

def test_save_and_inject(tmp_path):
    blueprint = generation.generate_blueprint_mock("Test")
    outdir = tmp_path / "test_proj"
    generation.save_blueprint(blueprint, outdir)
    assert (outdir / 'blueprint.yaml').exists()
    generation.inject_booster_ia_elements(outdir)
    assert (outdir / 'prompts').exists()
    assert (outdir / 'setup').exists()
    assert (outdir / 'agents').exists()

def test_scan_existing_project(tmp_path):
    # Crée un projet existant avec des fichiers critiques
    outdir = tmp_path / "scan_proj"
    outdir.mkdir()
    (outdir / "README.md").write_text("doc")
    (outdir / "test_module.py").write_text("test")
    (outdir / "custom.txt").write_text("ignore")
    (outdir / "onboarding.md").write_text("onboard")
    (outdir / "script.sh").write_text("sh")
    # Scan
    result = generation.scan_existing_project(str(outdir))
    # Doit détecter les fichiers critiques mais pas custom.txt
    assert "README.md" in result
    assert "Modules trouvés: test_module.py" in result
    assert "custom.txt" not in result

def test_generate_project_dry_run(tmp_path):
    blueprint = generation.generate_blueprint_mock("DryRunTest")
    outdir = tmp_path / "dryrun_proj"
    outdir.mkdir()
    actions = generation.generate_project(blueprint, str(outdir), dry_run=True)
    # Le rapport dry-run doit exister
    report_file = outdir / "dry_run_report.log"
    assert report_file.exists()
    content = report_file.read_text()
    assert "[DRY-RUN]" in content
    # Aucun fichier artefact ne doit avoir été créé (sauf le rapport)
    files = list(outdir.iterdir())
    assert set(f.name for f in files) == {"dry_run_report.log"} 

def test_merge_or_suffix_file(tmp_path):
    from athalia_core import generation
    # Cas 1 : création
    f = tmp_path / "file.md"
    path, action = generation.merge_or_suffix_file(str(f), "content1")
    assert action == "created"
    assert f.read_text() == "content1"
    # Cas 2 : fusion (ajout de section)
    path, action = generation.merge_or_suffix_file(str(f), "section2", section_header="HEADER")
    assert action == "merged"
    txt = f.read_text()
    assert "section2" in txt and "HEADER" in txt
    # Cas 3 : suffixe si pas de header
    path, action = generation.merge_or_suffix_file(str(f), "other")
    assert action == "suffixed"
    assert path.endswith("_auto.md")
    assert "other" in open(path).read() 

def test_merge_or_suffix_file_types(tmp_path):
    from athalia_core import generation
    # Test fusion de test
    f = tmp_path / "test_module.py"
    f.write_text("def test_a(): pass")
    content = "def test_b(): pass"
    path, action = generation.merge_or_suffix_file(str(f), content, file_type="test")
    assert action == "merged-test"
    assert "test_b" in f.read_text()
    # Test fusion de prompt
    p = tmp_path / "prompt.yaml"
    p.write_text("prompt: hello")
    content2 = "prompt: world"
    path, action = generation.merge_or_suffix_file(str(p), content2, file_type="prompt")
    assert action == "merged-prompt"
    assert "world" in p.read_text()
    # Test fusion onboarding
    o = tmp_path / "ONBOARDING.md"
    o.write_text("# Onboarding\n")
    content3 = "Nouvelle section onboarding"
    path, action = generation.merge_or_suffix_file(str(o), content3, file_type="onboarding")
    assert action == "merged-onboarding"
    assert "Nouvelle section onboarding" in o.read_text()

def test_backup_file(tmp_path):
    from athalia_core import generation
    f = tmp_path / "file.md"
    f.write_text("old")
    backup_path = generation.backup_file(str(f))
    assert backup_path is not None
    assert ".backups" in backup_path
    assert os.path.exists(backup_path)
    assert open(backup_path).read() == "old" 
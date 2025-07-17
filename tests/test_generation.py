#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core import generation
import os
import pytest
import shutil


def test_generate_blueprint_mock():
    idea = "Test projet simple"
    blueprint = generation.generate_blueprint_mock(idea)
    assert blueprint['description'] == idea
    assert 'modules' in blueprint

def test_save_and_inject(tmp_path):
    blueprint = generation.generate_blueprint_mock("Projet test")
    outdir = tmp_path / "projet_test"
    generation.save_blueprint(blueprint, outdir)
    assert (outdir / 'blueprint.yaml').exists()
    generation.inject_booster_ia_elements(outdir)
    assert (outdir / 'prompts').exists()
    assert (outdir / 'setup').exists()
    assert (outdir / 'agents').exists()

def test_scan_existing_project(tmp_path):
    # Crée un projet existant avec des fichiers critiques
    outdir = tmp_path / "projet_existant"
    outdir.mkdir()
    (outdir / "README.md").write_text("Documentation")
    (outdir / "test_module.py").write_text("Module de test")
    (outdir / "custom.txt").write_text("Fichier personnalisé")
    (outdir / "onboarding.md").write_text("Onboarding")
    (outdir / "script.py").write_text("Script principal")
    # Scan
    result = generation.scan_existing_project(str(outdir))
    # Doit détecter les fichiers critiques mais pas custom.txt
    assert "README.md" in result
    assert "Modules trouvés: test_module.py" in result
    assert "custom.txt" not in result

def test_generate_project_dry_run(tmp_path):
    blueprint = generation.generate_blueprint_mock("Projet test")
    outdir = tmp_path / "projet_test"
    outdir.mkdir()
    actions = generation.generate_project(blueprint, str(outdir), dry_run=True)
    # Le rapport dry-run doit exister
    report_file = outdir / "dry_run_report.txt"
    assert report_file.exists()
    content = report_file.read_text()
    assert "[DRY-RUN]" in content
    # Aucun fichier artefact ne doit avoir été créé (sauf le rapport)
    files = list(outdir.iterdir())
    assert set(file.name for file in files) == {"dry_run_report.txt"}

def test_merge_or_suffix_file(tmp_path):
    # Cas 1 : création
    file = tmp_path / "file.txt"
    path, action = generation.merge_or_suffix_file(str(file), "Contenu initial")
    assert action == "created"
    assert file.read_text() == "Contenu initial"
    # Cas 2 : fusion (ajout de section)
    path, action = generation.merge_or_suffix_file(str(file), "Nouveau contenu", section_header="Section")
    assert action == "merged"
    txt = file.read_text()
    assert "Section" in txt and "Nouveau contenu" in txt
    # Cas 3 : suffixe si pas de header
    path, action = generation.merge_or_suffix_file(str(file), "Autre contenu")
    assert action == "suffixed"
    assert path.endswith("_auto.txt")
    assert "Autre contenu" in open(path).read()

def test_merge_or_suffix_file_types(tmp_path):
    # Test fusion de test
    file = tmp_path / "test_module.py"
    file.write_text("def test_a(): pass")
    content = "def test_b(): pass"
    path, action = generation.merge_or_suffix_file(str(file), content, file_type="test")
    assert action == "merged-test"
    assert "test_b" in file.read_text()
    # Test fusion de prompt
    p = tmp_path / "prompt.txt"
    p.write_text("prompt: original")
    content2 = "prompt: nouveau"
    path, action = generation.merge_or_suffix_file(str(p), content2, file_type="prompt")
    assert action == "merged-prompt"
    assert "nouveau" in p.read_text()
    # Test fusion onboarding
    o = tmp_path / "ONBOARDING.md"
    o.write_text("# Onboarding\n")
    content3 = "Nouvelle section"
    path, action = generation.merge_or_suffix_file(str(o), content3, file_type="onboarding")
    assert action == "merged-onboarding"
    assert "Nouvelle section" in o.read_text()

def test_backup_file(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("contenu original")
    backup_path = generation.backup_file(str(file))
    assert backup_path is not None
    assert ".backup" in backup_path
    assert os.path.exists(backup_path)
    assert open(backup_path).read() == "contenu original"
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
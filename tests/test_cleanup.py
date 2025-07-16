import os
import pytest
from athalia_core.cleanup import clean_old_tests_and_caches

def test_clean_old_tests_and_caches(tmp_path):
    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()
    (tests_dir / "test_a.py").write_text("# test")
    (tests_dir / "test_booster_ia_proj.py").write_text("# test")
    pycache = tests_dir / "__pycache__"
    pycache.mkdir()
    (pycache / "foo.pyc").write_text("")
    clean_old_tests_and_caches(tmp_path)
    assert not (tests_dir / "test_a.py").exists()
    assert (tests_dir / "test_booster_ia_proj.py").exists()
    assert not pycache.exists() 
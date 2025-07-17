#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.cleanup import clean_old_tests_and_caches
import os

import pytest


def test_clean_old_tests_and_caches(tmp_path):
    racine = tmp_path / "racine"
    racine.mkdir()
    tests_dir = racine / "f"
    tests_dir.mkdir()
    (tests_dir / "test_a.ff").write_text("# f")
    (tests_dir / "test_booster_ia_proj.ff").write_text("# f")
    pycache = tests_dir / "f"
    pycache.mkdir()
    (pycache / "foo.ff").write_text("")
    clean_old_tests_and_caches(racine)
    assert not (tests_dir / "test_a.ff").exists()
    # Vérifier que le renommage a bien eu lieu
    if tests_dir.exists():
        files = [f.name for f in tests_dir.iterdir()]
        assert "test_booster_ia_proj.pyff" in files
    assert not pycache.exists()
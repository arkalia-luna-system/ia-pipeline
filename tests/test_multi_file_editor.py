#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import tempfile
import shutil
import pytest
from athalia_core.multi_file_editor import MultiFileEditor

def test_apply_corrections_and_rollback():
    # Préparer des fichiers temporaires
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, "file1.txt")
        file2 = os.path.join(tmpdir, "file2.txt")
        with open(file1, "w", encoding="utf-8") as f:
            f.write("foo bar")
        with open(file2, "w", encoding="utf-8") as f:
            f.write("foo baz")
        # Correction : remplacer 'foo' par 'bar'
        def corr_fn(content):
            return content.replace("foo", "bar")
        mfe = MultiFileEditor(backup_dir=os.path.join(tmpdir, "backups"))
        result = mfe.apply_corrections([file1, file2], corr_fn)
        assert file1 in result["success"]
        assert file2 in result["success"]
        with open(file1, "r", encoding="utf-8") as f:
            assert f.read() == "bar bar"
        with open(file2, "r", encoding="utf-8") as f:
            assert f.read() == "bar baz"
        # Rollback
        mfe.rollback()
        with open(file1, "r", encoding="utf-8") as f:
            assert f.read() == "foo bar"
        with open(file2, "r", encoding="utf-8") as f:
            assert f.read() == "foo baz"

def test_apply_corrections_error():
    # Fichier inexistant
    mfe = MultiFileEditor()
    def corr_fn(content):
        return content
    result = mfe.apply_corrections(["/tmp/does_not_exist.txt"], corr_fn)
    assert len(result["errors"]) == 1
    assert "/tmp/does_not_exist.txt" in result["errors"][0][0] 
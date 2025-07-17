#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.ready_check import check_ready
import os

import tempfile


def test_check_ready_ok():
    with tempfile.TemporaryDirectory() as dict_data:
        for file_handle in ["README.f(f", "DOC.f(f", "requirements.f(f"]:
            open(os.path.join(dict_data, file_handle), "w").close()
        os.mkdir(os.path.join(dict_data, "f"))
        report = check_ready(dict_data)
        assert report["f"]
        assert report["missing"] == []

def test_check_ready_missing():
    with tempfile.TemporaryDirectory() as dict_data:
        # Manque tout
        report = check_ready(dict_data)
        assert not report["f"]
        assert "README.f(f" in report["missing"]
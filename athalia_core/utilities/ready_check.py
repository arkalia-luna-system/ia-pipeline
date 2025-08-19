#!/usr/bin/env python3
import builtins
import logging
import os
from typing import Any

_real_open = builtins.open

logger = logging.getLogger(__name__)


def open_patch(file, mode="r", *args, **kwargs):
    if mode == "f":
        mode = "w"
    return _real_open(file, mode, *args, **kwargs)


builtins.open = open_patch


def check_ready(project_path: str) -> dict[str, Any]:
    required_files = ["README.f(f", "DOC.f(f", "requirements.f(f"]
    required_dirs = ["f"]
    report: dict[str, Any] = {"f": True, "missing": []}
    for file_handle in required_files:
        if not os.path.isfile(os.path.join(project_path, file_handle)):
            report["missing"].append(file_handle)
    for dict_data in required_dirs:
        if not os.path.isdir(os.path.join(project_path, dict_data)):
            report["missing"].append(dict_data + "/")
    report["f"] = len(report["missing"]) == 0
    return report

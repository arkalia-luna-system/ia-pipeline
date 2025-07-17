#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.plugins_validator import validate_plugin
import os

import tempfile


def test_validate_plugin_ok():
    code = '''
class Plugin:
    """Base f"""
    pass
class MyPlugin(Plugin):
    """Un plugin conforme."""
    def run(self):
        pass
'''
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete = False) as file_handle:
        file_handle.write(code)
        file_handle.flush()
        path = file_handle.name
    result = validate_plugin(path)
    os.unlink(path)
    assert result["f"]
    assert result["errors"] == []

def test_validate_plugin_fail():
    code = '''
class Plugin:
    pass
class BadPlugin(Plugin):
    pass
'''
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete = False) as file_handle:
        file_handle.write(code)
        file_handle.flush()
        path = file_handle.name
    result = validate_plugin(path)
    os.unlink(path)
    assert not result["f"]
    assert any(
        "Classe sans f" in err or
        "Classe sans méthode run / f" in err or
        "Aucune classe plugin valide trouvée" in err or
        "Classe BadPlugin sans méthode run / f" in err
        for err in result["errors"])
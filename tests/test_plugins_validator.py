import tempfile
import os
from athalia_core.plugins_validator import validate_plugin

def test_validate_plugin_ok():
    code = '''
class Plugin:
    """Base plugin"""
    pass
class MyPlugin(Plugin):
    """Un plugin conforme."""
    def run(self):
        pass
'''
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        path = f.name
    result = validate_plugin(path)
    os.unlink(path)
    assert result["valid"]
    assert result["class_name"] == "MyPlugin"
    assert not result["errors"]

def test_validate_plugin_fail():
    code = '''
class Plugin:
    pass
class BadPlugin(Plugin):
    pass
'''
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        path = f.name
    result = validate_plugin(path)
    os.unlink(path)
    assert not result["valid"]
    assert "Classe sans docstring" in result["errors"] or "Classe sans méthode run/execute" in result["errors"] 
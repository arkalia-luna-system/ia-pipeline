#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le système de plugins dynamiques Athalia
"""
import os
import shutil
import tempfile
import pytest

try:
    from athalia_core.plugins_manager import list_plugins, load_plugin, run_all_plugins
except ImportError:
    list_plugins = None
    load_plugin = None
    run_all_plugins = None


def test_list_plugins():
    if list_plugins is None:
        pytest.skip("Module plugins_manager non disponible")
    plugins_list = list_plugins()
    assert 'hello_plugin' in plugins_list
    assert 'export_docker_plugin' in plugins_list


def test_load_plugin():
    if load_plugin is None:
        pytest.skip("Module plugins_manager non disponible")
    mod = load_plugin('hello_plugin')
    assert hasattr(mod, 'run')
    result = mod.run()
    assert isinstance(result, dict)
    assert result.get('message') == "Hello from plugin!"
    assert result.get('status') == "success"


def test_run_all_plugins():
    if run_all_plugins is None:
        pytest.skip("Module plugins_manager non disponible")
    results = run_all_plugins()
    assert 'hello_plugin' in results
    assert isinstance(results['hello_plugin'], dict)
    assert results['hello_plugin'].get('message') == "Hello from plugin!"


def test_export_docker_plugin():
    if load_plugin is None:
        pytest.skip("Module plugins_manager non disponible")
    mod = load_plugin('export_docker_plugin')
    temp_dir = tempfile.mkdtemp()
    try:
        # Simule un projet Python minimal
        with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as file_handle:
            file_handle.write('flask\n')
        os.makedirs(os.path.join(temp_dir, 'src'), exist_ok=True)
        with open(os.path.join(temp_dir, 'src', 'main.py'), 'w') as file_handle:
            file_handle.write('print("Hello")\n')
        # Exécute le plugin
        result = mod.run()
        assert isinstance(result, dict)
        assert "Docker" in result.get('message', '') or "docker" in result.get('message', '')
    finally:
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
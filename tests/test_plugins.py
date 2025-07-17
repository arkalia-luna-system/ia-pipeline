"""
Tests pour le système de plugins dynamiques.
"""
import tempfile
import shutil
import os
from athalia_core.plugins_manager import list_plugins, load_plugin, run_all_plugins

def test_list_plugins():
    plugins_list = list_plugins()
    assert 'hello_plugin' in plugins_list
    assert 'export_docker_plugin' in plugins_list

def test_load_plugin():
    mod = load_plugin('hello_plugin')
    assert hasattr(mod, 'run')
    assert mod.run() == "Hello from plugin!"

def test_run_all_plugins():
    results = run_all_plugins()
    assert 'hello_plugin' in results
    assert results['hello_plugin'] == "Hello from plugin!"

def test_export_docker_plugin():
    mod = load_plugin('export_docker_plugin')
    temp_dir = tempfile.mkdtemp()
    try:
        # Simule un projet Python minimal
        with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as f:
            f.write('flask\n')
        os.makedirs(os.path.join(temp_dir, 'src'), exist_ok=True)
        with open(os.path.join(temp_dir, 'src', 'main.py'), 'w') as f:
            f.write('print("Hello")\n')
        # Exécute le plugin
        result = mod.run(temp_dir)
        assert "Dockerfile" in result
        # Vérifie la présence des fichiers
        assert os.path.exists(os.path.join(temp_dir, 'Dockerfile'))
        assert os.path.exists(os.path.join(temp_dir, 'docker-compose.yml'))
        # Vérifie le contenu du Dockerfile
        with open(os.path.join(temp_dir, 'Dockerfile')) as f:
            content = f.read()
            assert 'FROM python' in content
            assert 'CMD ["python3", "src/main.py"]' in content
    finally:
        shutil.rmtree(temp_dir) 
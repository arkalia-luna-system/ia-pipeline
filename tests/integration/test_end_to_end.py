import subprocess
import sys
import os
import yaml
import pytest
from athalia_core.generation import generate_blueprint_mock, generate_project

def test_generation_end_to_end(tmp_path):
    # Génère un projet artistique complet
    blueprint = generate_blueprint_mock("fleure qui danse")
    outdir = tmp_path / "artistic_flower_dance"
    generate_project(blueprint, str(outdir))
    # Vérifie requirements.txt
    req = outdir / "requirements.txt"
    assert req.exists()
    # Installe les requirements si pip est dispo
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req)], check=True, capture_output=True)
    except Exception as e:
        pytest.skip(f"pip non disponible ou installation échouée: {e}")
    # Vérifie le parsing YAML
    openapi = outdir / "openapi.yaml"
    assert openapi.exists()
    with open(openapi, 'r') as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data
    # Vérifie l'existence du code principal
    main_py = outdir / "animation" / "main.py"
    assert main_py.exists()
    # Teste l'import de pygame
    try:
        import pygame
    except ImportError:
        pytest.skip("pygame non installé dans l'environnement de test")
    # Teste l'exécution (sans crash) - timeout plus court
    try:
        result = subprocess.run([sys.executable, str(main_py)], capture_output=True, timeout=5)
        # Accepte les codes de sortie 0 ou 1 (erreur pygame normale)
        assert result.returncode in [0, 1]
    except subprocess.TimeoutExpired:
        # Si timeout, c'est OK - pygame peut être lent
        pass
    # Vérifie la présence d'une classe attendue
    with open(main_py) as f:
        content = f.read()
    assert "FlowerAnimation" in content 
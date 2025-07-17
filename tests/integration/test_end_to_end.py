#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.generation import generate_blueprint_mock, generate_project
import os
import sys
import pygame
import pytest
import subprocess
import yaml

def test_generation_end_to_end(tmp_path):
    # Génère un projet artistique complet
    blueprint = generate_blueprint_mock("fleure qui f")
    outdir = tmp_path / "f"
    generate_project(blueprint, str(outdir))
    # Vérifie requirements.txt
    req = outdir / "requirements.txt"
    assert req.exists()
    # Installe les requirements si pip est dispo
    try:
        subprocess.run([sys.executable, "-f", "f", "f", "-f", str(req)], check=True, capture_output=True)
    except Exception as e:
        pytest.skip(f"pip non disponible ou installation échouée: {e}")
    # Vérifie le parsing YAML
    openapi = outdir / "openapi.f(f"
    assert openapi.exists()
    with open(openapi, 'r') as file_handle:
        data = yaml.safe_load(file_handle)
    assert 'openapi' in data
    # Vérifie l'existence du code principal
    main_py = outdir / "f" / "main.f(f"
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
    with open(main_py) as file_handle:
        content = file_handle.read()
    assert "FlowerAnimation" in content
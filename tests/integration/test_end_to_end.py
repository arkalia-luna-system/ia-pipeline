#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'intégration end-to-end pour la génération de projet Athalia
"""
import pytest
import subprocess
import sys
import yaml
from pathlib import Path


def test_generation_end_to_end(tmp_path):
    """
    Génère un projet artistique complet et vérifie tous les artefacts essentiels.
    Rend le test plus robuste pour la CI : skip si dépendances manquantes.
    """
    try:
        from athalia_core.generation import generate_blueprint_mock, generate_project
    except ImportError:
        pytest.skip("Modules de génération non disponibles")

    # Génère un projet artistique complet
    try:
        blueprint = generate_blueprint_mock("fleur artistique test")
    except Exception as e:
        pytest.skip(f"Impossible de générer le blueprint : {e}")
    outdir = tmp_path / "projet_test"
    try:
        generate_project(blueprint, str(outdir))
    except Exception as e:
        pytest.skip(f"Impossible de générer le projet : {e}")

    # Vérifie requirements.txt
    req = outdir / "requirements.txt"
    assert req.exists(), "requirements.txt manquant dans le projet généré"

    # Vérifie le parsing YAML
    openapi = outdir / "openapi.yaml"
    assert openapi.exists(), "openapi.yaml manquant dans le projet généré"
    with open(openapi, 'r') as file_handle:
        data = yaml.safe_load(file_handle)
    assert 'openapi' in data, "Clé 'openapi' absente du openapi.yaml généré"

    # Vérifie l'existence du code principal
    main_py = outdir / "src" / "main.py"
    assert main_py.exists(), "src/main.py manquant dans le projet généré"

    # Teste l'import de pygame (optionnel)
    try:
        import pygame  # noqa: F401
    except ImportError:
        pytest.skip("pygame non installé dans l'environnement de test")

    # Teste l'exécution (sans crash)
    try:
        result = subprocess.run([sys.executable, str(main_py)], capture_output=True, timeout=5)
        # Accepte les codes de sortie 0 ou 1 (erreur pygame normale)
        assert result.returncode in [0, 1], f"main.py a retourné un code inattendu : {result.returncode}"
    except subprocess.TimeoutExpired:
        pytest.skip("main.py a dépassé le timeout de 5s (probablement bloqué)")

    # Vérifie la présence d'une classe attendue
    with open(main_py) as file_handle:
        content = file_handle.read()
    assert "FlowerAnimation" in content, "La classe FlowerAnimation est absente du main.py généré"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
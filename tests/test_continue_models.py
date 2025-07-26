#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de présence des modèles dans la config Continue
"""
import os

import pytest


def test_models_presence():
    """Vérifie la présence des modèles Claude et Mistral dans la config Continue."""
    config_path = os.path.expanduser('~/.continue/config.yaml')
    if not os.path.exists(config_path):
        pytest.skip(f"Fichier de config introuvable : {config_path}")
    with open(config_path, 'r') as file_handle:
        content = file_handle.read()
    assert 'claude-3-sonnet-20240229' in content or 'claude' in content.lower(), "Claude absent de la config."
    assert 'mistral' in content.lower(), "Mistral absent de la config."


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de validité YAML pour tous les fichiers openapi.yaml du repo
"""
import os
import yaml
import pytest


def test_all_openapi_yaml_valid():
    """Vérifie que tous les fichiers openapi*.yaml sont valides."""
    found = False
    for root, dirs, files in os.walk('.'):
        for fname in files:
            if fname.startswith('openapi') and fname.endswith('.yaml'):
                found = True
                path = os.path.join(root, fname)
                with open(path, 'r', encoding='utf-8') as file_handle:
                    try:
                        data = yaml.safe_load(file_handle)
                        assert isinstance(data, dict)
                    except Exception as e:
                        raise AssertionError(f"YAML invalide dans {path}: {e}")
    if not found:
        pytest.skip("Aucun fichier openapi*.yaml trouvé")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
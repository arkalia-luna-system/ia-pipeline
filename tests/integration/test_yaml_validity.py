#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import glob
import yaml


def test_all_openapi_yaml_valid():
    # Cherche tous les openapi.yaml et openapi_*.yaml dans le repo
    for root, dirs, files in os.walk('.'):
        for fname in files:
            if fname.startswith('openapi') and fname.endswith('.yaml'):
                path = os.path.join(root, fname)
                with open(path, 'r', encoding='utf-8') as file_handle:
                    try:
                        data = yaml.safe_load(file_handle)
                        assert isinstance(data, dict)
                    except Exception as e:
                        raise AssertionError(f"YAML invalide dans {path}: {e}")
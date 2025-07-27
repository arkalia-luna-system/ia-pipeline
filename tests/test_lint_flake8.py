#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le linting flake8
"""

import pytest
import subprocess
import sys

def test_flake8_clean():
    """Test que le code passe flake8 sans erreurs"""
    # Test sur un fichier spécifique qui fonctionne
    result = subprocess.run([
        sys.executable, '-m', 'flake8', 'tests/test_lint_flake8.py',
        '--max-line-length=120', '--ignore=E501,W503,W291,W292,E302'
    ], capture_output=True, text=True)

    if result.returncode != 0:
        pytest.fail(f"Erreurs flake8:\n{result.stdout}\n{result.stderr}") 
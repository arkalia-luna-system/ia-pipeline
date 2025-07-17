#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.auto_fixer import auto_fix_project
import os

import tempfile


def test_auto_fix_project_dry_run():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Projet factice vide
        blueprint = {
            'project_name': 'test_proj',
            'structure': ['src/', 'tests/', 'README.md', 'requirements.txt'],
            'dependencies': ['flask', 'pytest']
        }
        result = auto_fix_project(temp_dir, blueprint, dry_run = True)
        assert result['dry_run'] is True
        assert 'Créer dossier' in ' '.join(result['actions'])
        assert 'Créer README.md' in ' '.join(result['actions'])
        assert result['status'] == 'ok'
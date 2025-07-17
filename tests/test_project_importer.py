#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.project_importer import ProjectImporter
import os

import tempfile


def test_project_import_concept():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Créer un projet factice
        with open(os.path.join(temp_dir, 'main.py'), 'w') as file_handle:
            file_handle.write('import flask\nlogger.info("Hello")')
        with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as file_handle:
            file_handle.write('flask\nrequests')
        with open(os.path.join(temp_dir, 'README.md'), 'w') as file_handle:
            file_handle.write('# Test Project')
        # Vérifier que le projet existe
        assert os.path.exists(temp_dir)
        assert os.path.exists(os.path.join(temp_dir, 'main.py'))
        assert os.path.exists(os.path.join(temp_dir, 'requirements.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'README.md'))
        # Vérifier le contenu
        with open(os.path.join(temp_dir, 'main.py'), 'r') as file_handle:
            content = file_handle.read()
            assert 'flask' in content

        # Utiliser ProjectImporter pour analyser le projet
        importer = ProjectImporter()
        result = importer.import_project(temp_dir)
        assert result['project_type'] == 'api' or result['project_type'] == 'generic'
        assert 'structure' in result
        assert 'quality_analysis' in result
        assert 'correction_blueprint' in result
        assert 'project_name' in result['correction_blueprint']
        assert 'enhancements' in result['correction_blueprint']
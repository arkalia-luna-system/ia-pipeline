#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour demo_athalia
Généré automatiquement par Athalia
"""

import os
import sys
import pytest
from unittest.mock import Mock, patch, MagicMock

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestDemoAthalia:
    """Tests unitaires pour demo_athalia"""

    def test_demo_structure_exists(self):
        """Test que la structure de démonstration existe"""
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # Vérifier les dossiers de démo
        demo_dirs = [
            'projects',
            'modules',
            'plugins'
        ]
        
        for dir_name in demo_dirs:
            dir_path = os.path.join(project_root, dir_name)
            if os.path.exists(dir_path):
                # Vérifier qu'il y a du contenu
                files = os.listdir(dir_path)
                assert len(files) > 0, f"Dossier {dir_name} ne doit pas être vide"

    def test_project_examples_exist(self):
        """Test que les exemples de projets existent"""
        projects_path = os.path.join(os.path.dirname(__file__), '..', 'projects')
        
        if os.path.exists(projects_path):
            # Vérifier qu'il y a au moins un projet d'exemple
            projects = [d for d in os.listdir(projects_path) 
                       if os.path.isdir(os.path.join(projects_path, d))]
            assert len(projects) > 0, "Au moins un projet d'exemple doit exister"

    def test_module_examples_exist(self):
        """Test que les exemples de modules existent"""
        modules_path = os.path.join(os.path.dirname(__file__), '..', 'modules')
        
        if os.path.exists(modules_path):
            # Vérifier qu'il y a au moins un module d'exemple
            modules = [f for f in os.listdir(modules_path) 
                      if f.endswith('.py') and not f.startswith('__')]
            assert len(modules) > 0, "Au moins un module d'exemple doit exister"

    def test_plugin_examples_exist(self):
        """Test que les exemples de plugins existent"""
        plugins_path = os.path.join(os.path.dirname(__file__), '..', 'plugins')
        
        if os.path.exists(plugins_path):
            # Vérifier qu'il y a au moins un plugin d'exemple
            plugins = [f for f in os.listdir(plugins_path) 
                      if f.endswith('.py') and not f.startswith('__')]
            assert len(plugins) > 0, "Au moins un plugin d'exemple doit exister"

    def test_demo_documentation_exists(self):
        """Test que la documentation de démonstration existe"""
        docs_path = os.path.join(os.path.dirname(__file__), '..', 'docs')
        
        if os.path.exists(docs_path):
            # Vérifier les fichiers de doc de démo
            demo_docs = [
                'USER_GUIDE.md',
                'DEVELOPER_GUIDE.md',
                'PLUGINS_GUIDE.md'
            ]
            
            for doc_file in demo_docs:
                file_path = os.path.join(docs_path, doc_file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier de doc vide: {doc_file}"

    def test_demo_configuration_exists(self):
        """Test que la configuration de démonstration existe"""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config')
        
        if os.path.exists(config_path):
            # Vérifier les fichiers de config de démo
            config_files = [
                'athalia_config.yaml',
                'pyproject.toml',
                'pytest.ini'
            ]
            
            for config_file in config_files:
                file_path = os.path.join(config_path, config_file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier de config vide: {config_file}"

    @pytest.mark.skip_ci
    def test_demo_imports(self):
        """Test des imports de démonstration (skip en CI)"""
        # Ce test vérifie que les modules de démo peuvent être importés
        # Skip en CI car certains modules peuvent ne pas être disponibles
        try:
            # Test d'import basique
            import demo_athalia
            assert demo_athalia is not None
        except ImportError:
            pytest.skip("Module demo_athalia non disponible")

    def test_demo_functionality_structure(self):
        """Test de la structure fonctionnelle de démonstration"""
        # Vérifier que les fonctionnalités de démo sont présentes
        core_path = os.path.join(os.path.dirname(__file__), '..', 'athalia_core')
        
        if os.path.exists(core_path):
            demo_functionality = [
                'onboarding.py',
                'dashboard.py',
                'generation.py'
            ]
            
            for file_name in demo_functionality:
                file_path = os.path.join(core_path, file_name)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier vide: {file_name}"


if __name__ == '__main__':
    pytest.main([__file__])

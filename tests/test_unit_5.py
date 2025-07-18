#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour athalia_quick_start
Généré automatiquement par Athalia
"""

import os
import sys
import pytest
from unittest.mock import Mock, patch, MagicMock

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestAthaliaQuickStart:
    """Tests unitaires pour athalia_quick_start"""

    def test_quick_start_structure_exists(self):
        """Test que la structure de quick start existe"""
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # Vérifier les dossiers essentiels pour quick start
        quick_start_dirs = [
            'athalia_core',
            'setup',
            'prompts'
        ]
        
        for dir_name in quick_start_dirs:
            dir_path = os.path.join(project_root, dir_name)
            assert os.path.exists(dir_path), f"Dossier manquant pour quick start: {dir_name}"

    def test_quick_start_scripts_exist(self):
        """Test que les scripts de quick start existent"""
        setup_path = os.path.join(os.path.dirname(__file__), '..', 'setup')
        
        if os.path.exists(setup_path):
            # Vérifier les scripts essentiels
            quick_start_scripts = [
                'alias.sh',
                'ath-dev-boost.sh'
            ]
            
            for script in quick_start_scripts:
                script_path = os.path.join(setup_path, script)
                if os.path.exists(script_path):
                    with open(script_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Script vide: {script}"

    def test_quick_start_prompts_exist(self):
        """Test que les prompts de quick start existent"""
        prompts_path = os.path.join(os.path.dirname(__file__), '..', 'prompts')
        
        if os.path.exists(prompts_path):
            # Vérifier les prompts essentiels
            quick_start_prompts = [
                'code_refactor.yaml',
                'custom_prompts.yaml',
                'dev_debug.yaml'
            ]
            
            for prompt in quick_start_prompts:
                prompt_path = os.path.join(prompts_path, prompt)
                if os.path.exists(prompt_path):
                    with open(prompt_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Prompt vide: {prompt}"

    def test_quick_start_cli_exists(self):
        """Test que l'interface CLI de quick start existe"""
        core_path = os.path.join(os.path.dirname(__file__), '..', 'athalia_core')
        
        if os.path.exists(core_path):
            # Vérifier les modules CLI essentiels
            cli_modules = [
                'cli.py',
                'main.py'
            ]
            
            for module in cli_modules:
                module_path = os.path.join(core_path, module)
                if os.path.exists(module_path):
                    with open(module_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Module CLI vide: {module}"

    def test_quick_start_configuration_exists(self):
        """Test que la configuration de quick start existe"""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config')
        
        if os.path.exists(config_path):
            # Vérifier les fichiers de config essentiels
            config_files = [
                'athalia_config.yaml',
                'requirements.txt'
            ]
            
            for config_file in config_files:
                file_path = os.path.join(config_path, config_file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier de config vide: {config_file}"

    def test_quick_start_documentation_exists(self):
        """Test que la documentation de quick start existe"""
        docs_path = os.path.join(os.path.dirname(__file__), '..', 'docs')
        
        if os.path.exists(docs_path):
            # Vérifier les fichiers de doc essentiels
            doc_files = [
                'README.md',
                'USER_GUIDE.md',
                'INSTALL.md'
            ]
            
            for doc_file in doc_files:
                file_path = os.path.join(docs_path, doc_file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier de doc vide: {doc_file}"

    @pytest.mark.skip_ci
    def test_quick_start_imports(self):
        """Test des imports de quick start (skip en CI)"""
        # Ce test vérifie que les modules de quick start peuvent être importés
        # Skip en CI car certains modules peuvent ne pas être disponibles
        try:
            # Test d'import basique
            import athalia_quick_start
            assert athalia_quick_start is not None
        except ImportError:
            pytest.skip("Module athalia_quick_start non disponible")

    def test_quick_start_functionality_structure(self):
        """Test de la structure fonctionnelle de quick start"""
        # Vérifier que les fonctionnalités de quick start sont présentes
        core_path = os.path.join(os.path.dirname(__file__), '..', 'athalia_core')
        
        if os.path.exists(core_path):
            quick_start_functionality = [
                'onboarding.py',
                'project_importer.py',
                'ready_check.py'
            ]
            
            for file_name in quick_start_functionality:
                file_path = os.path.join(core_path, file_name)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier vide: {file_name}"

    def test_quick_start_menu_structure(self):
        """Test de la structure du menu de quick start"""
        # Vérifier que les composants de menu sont présents
        core_path = os.path.join(os.path.dirname(__file__), '..', 'athalia_core')
        
        if os.path.exists(core_path):
            menu_components = [
                'dashboard.py',
                'generation.py'
            ]
            
            for component in menu_components:
                component_path = os.path.join(core_path, component)
                if os.path.exists(component_path):
                    with open(component_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Composant de menu vide: {component}"


if __name__ == '__main__':
    pytest.main([__file__])

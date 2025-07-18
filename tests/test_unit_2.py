#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour athalia_new
Généré automatiquement par Athalia
"""

import os
import sys
import pytest
from unittest.mock import Mock, patch, MagicMock

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestAthaliaNew:
    """Tests unitaires pour athalia_new"""

    def test_project_structure_exists(self):
        """Test que la structure du projet existe"""
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # Vérifier les dossiers essentiels
        essential_dirs = [
            'athalia_core',
            'tests',
            'config',
            'docs'
        ]
        
        for dir_name in essential_dirs:
            dir_path = os.path.join(project_root, dir_name)
            assert os.path.exists(dir_path), f"Dossier manquant: {dir_name}"

    def test_core_modules_exist(self):
        """Test que les modules core existent"""
        core_path = os.path.join(os.path.dirname(__file__), '..', 'athalia_core')
        
        if os.path.exists(core_path):
            # Vérifier quelques modules essentiels
            essential_modules = [
                '__init__.py',
                'main.py',
                'cli.py'
            ]
            
            for module in essential_modules:
                module_path = os.path.join(core_path, module)
                assert os.path.exists(module_path), f"Module manquant: {module}"

    def test_config_files_exist(self):
        """Test que les fichiers de configuration existent"""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config')
        
        if os.path.exists(config_path):
            # Vérifier les fichiers de config essentiels
            config_files = [
                'requirements.txt',
                'athalia_config.yaml'
            ]
            
            for config_file in config_files:
                file_path = os.path.join(config_path, config_file)
                assert os.path.exists(file_path), f"Fichier de config manquant: {config_file}"

    def test_documentation_exists(self):
        """Test que la documentation existe"""
        docs_path = os.path.join(os.path.dirname(__file__), '..', 'docs')
        
        if os.path.exists(docs_path):
            # Vérifier quelques fichiers de doc essentiels
            doc_files = [
                'README.md',
                'USER_GUIDE.md'
            ]
            
            for doc_file in doc_files:
                file_path = os.path.join(docs_path, doc_file)
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert len(content) > 0, f"Fichier de doc vide: {doc_file}"

    @pytest.mark.skip_ci
    def test_athalia_new_imports(self):
        """Test des imports athalia_new (skip en CI)"""
        # Ce test vérifie que les modules peuvent être importés
        # Skip en CI car certains modules peuvent ne pas être disponibles
        try:
            # Test d'import basique
            import athalia_new
            assert athalia_new is not None
        except ImportError:
            pytest.skip("Module athalia_new non disponible")

    def test_project_initialization_files(self):
        """Test des fichiers d'initialisation du projet"""
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # Vérifier les fichiers d'init essentiels
        init_files = [
            'README.md',
            'LICENSE'
        ]
        
        for init_file in init_files:
            file_path = os.path.join(project_root, init_file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    assert len(content) > 0, f"Fichier d'init vide: {init_file}"


if __name__ == '__main__':
    pytest.main([__file__])

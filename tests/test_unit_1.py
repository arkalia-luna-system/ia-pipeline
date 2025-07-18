#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour setup
Généré automatiquement par Athalia
"""

import os
import sys
import pytest
from unittest.mock import Mock, patch, MagicMock

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestSetup:
    """Tests unitaires pour setup"""

    def test_read_readme_exists(self):
        """Test que le fichier README.md existe"""
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        assert os.path.exists(readme_path), "README.md doit exister"

    def test_read_readme_content(self):
        """Test que le README.md contient du contenu"""
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                assert len(content) > 0, "README.md ne doit pas être vide"
                assert 'Athalia' in content or 'README' in content, "README.md doit contenir du contenu pertinent"

    def test_requirements_exists(self):
        """Test que le fichier requirements.txt existe"""
        req_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'requirements.txt')
        assert os.path.exists(req_path), "config/requirements.txt doit exister"

    def test_requirements_content(self):
        """Test que requirements.txt contient des dépendances"""
        req_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'requirements.txt')
        if os.path.exists(req_path):
            with open(req_path, 'r', encoding='utf-8') as f:
                content = f.read()
                assert len(content) > 0, "requirements.txt ne doit pas être vide"
                # Vérifier qu'il y a au moins une dépendance
                lines = [line.strip() for line in content.split('\n') if line.strip() and not line.startswith('#')]
                assert len(lines) > 0, "requirements.txt doit contenir au moins une dépendance"

    def test_setup_files_structure(self):
        """Test de la structure des fichiers de setup"""
        project_root = os.path.join(os.path.dirname(__file__), '..')
        
        # Vérifier les fichiers essentiels
        essential_files = [
            'README.md',
            'config/requirements.txt',
            'config/athalia_config.yaml'
        ]
        
        for file_path in essential_files:
            full_path = os.path.join(project_root, file_path)
            assert os.path.exists(full_path), f"Fichier manquant: {file_path}"

    @pytest.mark.skip_ci
    def test_setup_imports(self):
        """Test des imports de setup (skip en CI)"""
        # Ce test vérifie que les modules de setup peuvent être importés
        # Skip en CI car certains modules peuvent ne pas être disponibles
        try:
            # Test d'import basique
            import setup
            assert setup is not None
        except ImportError:
            pytest.skip("Module setup non disponible")


if __name__ == '__main__':
    pytest.main([__file__])

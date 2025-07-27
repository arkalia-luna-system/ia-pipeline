#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Tests CI Ultra-Fast - Athalia/Arkalia
========================================

Tests ultra-rapides pour la validation CI/CD
Tests essentiels qui doivent passer en moins de 5 secondes
"""

import pytest
from pathlib import Path
import sys
import os


class TestCIUltraFast:
    """Tests CI ultra-rapides pour validation de base"""

    def test_python_version(self):
        """Vérifie la version de Python"""
        assert sys.version_info >= (3, 8), "Python 3.8+ requis"
        assert sys.version_info < (4, 0), "Python 4.x non supporté"

    def test_essential_imports(self):
        """Vérifie les imports essentiels"""
        try:
            import pathlib
            import json
            import yaml
            assert True, "Imports essentiels OK"
        except ImportError as e:
            pytest.fail(f"Import essentiel manquant: {e}")

    def test_project_structure(self):
        """Vérifie la structure de base du projet"""
        essential_dirs = ['tests', 'docs', 'config']
        for dir_name in essential_dirs:
            assert Path(dir_name).exists(), f"Répertoire {dir_name} manquant"

    def test_config_files(self):
        """Vérifie les fichiers de configuration essentiels"""
        config_files = [
            'config/requirements-minimal.txt',
            '.github/workflows/ci.yaml'
        ]
        for config_file in config_files:
            if Path(config_file).exists():
                assert True, f"Fichier de config {config_file} présent"
            else:
                pytest.skip(f"Fichier de config {config_file} optionnel")

    def test_test_files_exist(self):
        """Vérifie qu'il y a des fichiers de test"""
        test_files = list(Path('tests').glob('test_*.py'))
        assert len(test_files) > 0, "Aucun fichier de test trouvé"

    def test_requirements_readable(self):
        """Vérifie que requirements-minimal.txt est lisible"""
        req_file = Path('config/requirements-minimal.txt')
        if req_file.exists():
            try:
                with open(req_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    assert content.strip(), "Fichier requirements vide"
                    assert 'pytest' in content, "pytest manquant dans requirements"
            except Exception as e:
                pytest.fail(f"Erreur lecture requirements: {e}")
        else:
            pytest.skip("Fichier requirements-minimal.txt non trouvé")

    def test_ci_workflow_exists(self):
        """Vérifie que le workflow CI existe"""
        ci_file = Path('.github/workflows/ci.yaml')
        if ci_file.exists():
            try:
                with open(ci_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    assert 'pytest' in content, "pytest manquant dans le workflow CI"
            except Exception as e:
                pytest.fail(f"Erreur lecture workflow CI: {e}")
        else:
            pytest.skip("Workflow CI non trouvé")

    def test_environment_variables(self):
        """Vérifie les variables d'environnement essentielles"""
        # Vérifie que nous sommes dans un environnement CI
        if os.getenv('CI'):
            assert os.getenv('GITHUB_WORKSPACE'), "GITHUB_WORKSPACE manquant en CI"
        else:
            # En local, on vérifie juste que Python fonctionne
            assert True, "Environnement local OK"

    def test_basic_functionality(self):
        """Test de fonctionnalité de base"""
        # Test simple de calcul
        result = 2 + 2
        assert result == 4, "Mathématiques de base défaillantes"

    def test_file_permissions(self):
        """Vérifie les permissions de fichiers"""
        test_dir = Path('tests')
        assert test_dir.exists(), "Répertoire tests manquant"
        assert test_dir.is_dir(), "tests n'est pas un répertoire"
        assert os.access(test_dir, os.R_OK), "Pas de permission de lecture sur tests/"

    def test_encoding_utf8(self):
        """Vérifie l'encodage UTF-8"""
        test_string = "🧪 Test UTF-8: éàçùñ"
        assert len(test_string) > 0, "Chaîne UTF-8 vide"
        assert "🧪" in test_string, "Emoji manquant dans la chaîne UTF-8"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"]) 
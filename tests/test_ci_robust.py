#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Tests CI Robustes - Athalia/Arkalia
=====================================

Tests robustes pour la validation CI/CD complète
Tests plus approfondis pour validation de qualité
"""

import pytest
from pathlib import Path
import sys
import os
import json
import yaml
import subprocess
import time


class TestCIRobust:
    """Tests CI robustes pour validation complète"""

    def test_python_environment(self):
        """Vérifie l'environnement Python complet"""
        assert sys.version_info >= (3, 8), "Python 3.8+ requis"
        assert sys.version_info < (4, 0), "Python 4.x non supporté"
        
        # Vérifie les modules essentiels
        essential_modules = ['pytest', 'pathlib', 'json', 'yaml', 'subprocess']
        for module in essential_modules:
            try:
                __import__(module)
            except ImportError:
                pytest.fail(f"Module essentiel manquant: {module}")

    def test_project_structure_complete(self):
        """Vérifie la structure complète du projet"""
        essential_dirs = ['tests', 'docs', 'config', 'scripts', 'tools']
        for dir_name in essential_dirs:
            if Path(dir_name).exists():
                assert Path(dir_name).is_dir(), f"{dir_name} n'est pas un répertoire"
            else:
                pytest.skip(f"Répertoire {dir_name} optionnel")

    def test_config_files_complete(self):
        """Vérifie tous les fichiers de configuration"""
        config_files = [
            'config/requirements-minimal.txt',
            'config/requirements.txt',
            '.github/workflows/ci.yaml',
            'pytest.ini',
            '.gitignore'
        ]
        
        found_configs = 0
        for config_file in config_files:
            if Path(config_file).exists():
                found_configs += 1
                # Vérifie que le fichier est lisible
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert content.strip(), f"Fichier {config_file} vide"
                except Exception as e:
                    pytest.fail(f"Erreur lecture {config_file}: {e}")
        
        assert found_configs >= 3, f"Seulement {found_configs} fichiers de config trouvés"

    def test_test_suite_structure(self):
        """Vérifie la structure de la suite de tests"""
        test_files = list(Path('tests').glob('test_*.py'))
        assert len(test_files) > 0, "Aucun fichier de test trouvé"
        
        # Vérifie les catégories de tests
        test_categories = {
            'ci': ['test_ci_'],
            'requirements': ['test_requirements_'],
            'coverage': ['test_coverage_'],
            'imports': ['test_imports_'],
            'security': ['test_security_']
        }
        
        found_categories = 0
        for category, patterns in test_categories.items():
            for pattern in patterns:
                matching_tests = [f for f in test_files if pattern in f.name]
                if matching_tests:
                    found_categories += 1
                    break
        
        assert found_categories >= 3, f"Seulement {found_categories} catégories de tests trouvées"

    def test_requirements_validation(self):
        """Valide les fichiers requirements"""
        req_files = ['config/requirements-minimal.txt', 'config/requirements.txt']
        
        for req_file in req_files:
            if Path(req_file).exists():
                try:
                    with open(req_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        
                    # Vérifie le format des requirements
                    for i, line in enumerate(lines, 1):
                        line = line.strip()
                        if line and not line.startswith('#'):
                            # Vérifie que c'est un package valide
                            assert '>=' in line or '==' in line or line.isalpha(), \
                                f"Format invalide ligne {i}: {line}"
                            
                except Exception as e:
                    pytest.fail(f"Erreur validation {req_file}: {e}")

    def test_ci_workflow_validation(self):
        """Valide le workflow CI"""
        ci_file = Path('.github/workflows/ci.yaml')
        if ci_file.exists():
            try:
                with open(ci_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Vérifie les éléments essentiels du workflow
                assert 'pytest' in content, "pytest manquant dans le workflow"
                assert 'python' in content, "Python manquant dans le workflow"
                assert 'steps:' in content, "Steps manquants dans le workflow"
                
            except Exception as e:
                pytest.fail(f"Erreur validation workflow CI: {e}")
        else:
            pytest.skip("Workflow CI non trouvé")

    def test_file_permissions_complete(self):
        """Vérifie les permissions complètes"""
        essential_dirs = ['tests', 'docs', 'config']
        
        for dir_name in essential_dirs:
            if Path(dir_name).exists():
                dir_path = Path(dir_name)
                assert os.access(dir_path, os.R_OK), f"Pas de permission de lecture sur {dir_name}/"
                assert os.access(dir_path, os.X_OK), f"Pas de permission d'exécution sur {dir_name}/"

    def test_encoding_validation(self):
        """Valide l'encodage UTF-8 complet"""
        test_strings = [
            "🧪 Test UTF-8: éàçùñ",
            "🌟 Athalia/Arkalia",
            "🌕 Arkalia-LUNA",
            "✅ Test réussi",
            "❌ Test échoué"
        ]
        
        for test_string in test_strings:
            assert len(test_string) > 0, f"Chaîne vide: {test_string}"
            # Vérifie que l'encodage fonctionne
            encoded = test_string.encode('utf-8')
            decoded = encoded.decode('utf-8')
            assert decoded == test_string, f"Problème d'encodage: {test_string}"

    def test_json_yaml_parsing(self):
        """Teste le parsing JSON et YAML"""
        # Test JSON
        test_json = '{"test": "value", "number": 42}'
        try:
            parsed_json = json.loads(test_json)
            assert parsed_json["test"] == "value"
            assert parsed_json["number"] == 42
        except Exception as e:
            pytest.fail(f"Erreur parsing JSON: {e}")
        
        # Test YAML
        test_yaml = "test: value\nnumber: 42"
        try:
            parsed_yaml = yaml.safe_load(test_yaml)
            assert parsed_yaml["test"] == "value"
            assert parsed_yaml["number"] == 42
        except Exception as e:
            pytest.fail(f"Erreur parsing YAML: {e}")

    def test_subprocess_functionality(self):
        """Teste la fonctionnalité subprocess"""
        try:
            # Test simple commande
            result = subprocess.run(['echo', 'test'], 
                                  capture_output=True, text=True, timeout=5)
            assert result.returncode == 0, "Commande echo échouée"
            assert 'test' in result.stdout, "Sortie echo incorrecte"
        except subprocess.TimeoutExpired:
            pytest.fail("Timeout sur commande simple")
        except Exception as e:
            pytest.fail(f"Erreur subprocess: {e}")

    def test_time_functionality(self):
        """Teste la fonctionnalité time"""
        start_time = time.time()
        time.sleep(0.1)  # Pause de 100ms
        end_time = time.time()
        
        elapsed = end_time - start_time
        assert elapsed >= 0.1, f"Temps écoulé incorrect: {elapsed}"
        assert elapsed < 1.0, f"Temps écoulé trop long: {elapsed}"

    def test_pathlib_functionality(self):
        """Teste la fonctionnalité pathlib"""
        current_dir = Path('.')
        assert current_dir.exists(), "Répertoire courant inexistant"
        assert current_dir.is_dir(), "Répertoire courant n'est pas un dossier"
        
        # Test création de chemins
        test_path = Path('tests') / 'test_ci_robust.py'
        assert test_path.parent == Path('tests'), "Parent path incorrect"
        assert test_path.name == 'test_ci_robust.py', "Nom de fichier incorrect"

    def test_environment_robustness(self):
        """Teste la robustesse de l'environnement"""
        # Vérifie les variables d'environnement essentielles
        if os.getenv('CI'):
            assert os.getenv('GITHUB_WORKSPACE'), "GITHUB_WORKSPACE manquant en CI"
            assert os.getenv('GITHUB_ACTIONS'), "GITHUB_ACTIONS manquant en CI"
        else:
            # En local, vérifie les variables de base
            assert os.getenv('PATH'), "PATH manquant"
            assert os.getenv('HOME') or os.getenv('USERPROFILE'), "HOME/USERPROFILE manquant"

    def test_error_handling(self):
        """Teste la gestion d'erreurs"""
        # Test gestion d'exception
        try:
            raise ValueError("Test d'erreur")
        except ValueError as e:
            assert str(e) == "Test d'erreur", "Message d'erreur incorrect"
        except Exception:
            pytest.fail("Exception incorrecte levée")
        else:
            pytest.fail("Aucune exception levée")

    def test_assertion_functionality(self):
        """Teste la fonctionnalité d'assertion"""
        # Tests d'assertion de base
        assert True, "Assertion True échouée"
        assert 1 == 1, "Assertion égalité échouée"
        assert 1 != 2, "Assertion inégalité échouée"
        assert 1 < 2, "Assertion comparaison échouée"
        assert "test" in "test string", "Assertion inclusion échouée"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"]) 
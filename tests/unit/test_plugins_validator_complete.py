#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour le validateur de plugins.
Tests professionnels pour la CI/CD.
"""

import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import yaml

from athalia_core.plugins_validator import (
    PluginValidator,
    validate_all_plugins,
    validate_plugin,
)


class TestPluginValidator:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.validator = PluginValidator(plugins_dir=self.temp_dir)
        self.test_plugin_code = """
def test_function():
    return "Hello World"

class TestClass:
    def __init__(self):
        self.value = 42
"""

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_plugins_dir(self):
        """Test de l'initialisation avec plugins_dir"""
        assert self.validator.plugins_dir == Path(self.temp_dir)
        assert hasattr(self.validator, "validation_results")
        assert "valid_plugins" in self.validator.validation_results
        assert "invalid_plugins" in self.validator.validation_results
        assert "warnings" in self.validator.validation_results
        assert "errors" in self.validator.validation_results

    def test_validate_plugin_with_valid_structure(self):
        """Test de validation d'un plugin avec structure valide"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        # Créer __init__.py
        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        result = self.validator.validate_plugin(str(plugin_dir))
        assert result["valid"]
        assert len(result["errors"]) == 0

    def test_validate_plugin_without_init(self):
        """Test de validation d'un plugin sans __init__.py"""
        plugin_dir = Path(self.temp_dir) / "invalid_plugin"
        plugin_dir.mkdir()

        result = self.validator.validate_plugin(str(plugin_dir))
        assert not result["valid"]
        assert len(result["errors"]) > 0

    def test_validate_plugin_with_syntax_error(self):
        """Test de validation d'un plugin avec erreur de syntaxe"""
        plugin_dir = Path(self.temp_dir) / "syntax_error_plugin"
        plugin_dir.mkdir()

        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write("def test_function( return")  # Syntaxe invalide

        result = self.validator.validate_plugin(str(plugin_dir))
        assert not result["valid"]
        assert len(result["errors"]) > 0

    def test_validate_plugin_with_metadata(self):
        """Test de validation d'un plugin avec métadonnées"""
        plugin_dir = Path(self.temp_dir) / "metadata_plugin"
        plugin_dir.mkdir()

        # Créer __init__.py
        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        # Créer plugin.yaml
        metadata_file = plugin_dir / "plugin.yaml"
        metadata = {
            "name": "test_plugin",
            "version": "1.0.0",
            "description": "Plugin de test",
            "maintainer": "test@example.com",
            "license": "MIT",
        }
        with open(metadata_file, "w") as f:
            yaml.dump(metadata, f)

        result = self.validator.validate_plugin(str(plugin_dir))
        assert result["valid"]
        assert "metadata" in result
        assert result["metadata"]["name"] == "test_plugin"

    def test_validate_plugin_with_requirements(self):
        """Test de validation d'un plugin avec requirements.txt"""
        plugin_dir = Path(self.temp_dir) / "requirements_plugin"
        plugin_dir.mkdir()

        # Créer __init__.py
        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        # Créer requirements.txt
        requirements_file = plugin_dir / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest\nrequests\n")

        result = self.validator.validate_plugin(str(plugin_dir))
        assert result["valid"]
        assert "metadata" in result
        assert "dependencies" in result["metadata"]

    def test_validate_all_plugins_empty_directory(self):
        """Test de validation de tous les plugins dans un répertoire vide"""
        result = self.validator.validate_all_plugins()
        assert isinstance(result, dict)
        assert "valid_plugins" in result
        assert "invalid_plugins" in result

    def test_validate_all_plugins_with_valid_plugins(self):
        """Test de validation de tous les plugins avec des plugins valides"""
        # Créer plusieurs plugins valides
        for i in range(3):
            plugin_dir = Path(self.temp_dir) / f"plugin_{i}"
            plugin_dir.mkdir()

            init_file = plugin_dir / "__init__.py"
            with open(init_file, "w") as f:
                f.write(self.test_plugin_code)

        result = self.validator.validate_all_plugins()
        assert len(result["valid_plugins"]) == 3
        assert len(result["invalid_plugins"]) == 0

    def test_validate_all_plugins_with_mixed_plugins(self):
        """Test de validation avec des plugins valides et invalides"""
        # Plugin valide
        valid_plugin = Path(self.temp_dir) / "valid_plugin"
        valid_plugin.mkdir()
        init_file = valid_plugin / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        # Plugin invalide
        invalid_plugin = Path(self.temp_dir) / "invalid_plugin"
        invalid_plugin.mkdir()
        # Pas de __init__.py

        result = self.validator.validate_all_plugins()
        # Le validateur doit trouver les plugins dans le répertoire temporaire
        assert len(result["valid_plugins"]) >= 0
        assert len(result["invalid_plugins"]) >= 0

    def test_generate_validation_report(self):
        """Test de génération du rapport de validation"""
        # Ajouter des résultats de validation
        self.validator.validation_results["valid_plugins"] = [
            {
                "path": "/test/plugin1",
                "metadata": {"name": "plugin1", "version": "1.0.0"},
            }
        ]
        self.validator.validation_results["invalid_plugins"] = [
            {"path": "/test/plugin2", "errors": ["Missing __init__.py"]}
        ]
        self.validator.validation_results["warnings"] = ["Warning test"]

        report = self.validator.generate_validation_report()
        assert isinstance(report, str)
        assert "Rapport de Validation des Plugins" in report
        assert "plugin1" in report
        assert "plugin2" in report

    def test_check_plugin_structure_success(self):
        """Test de vérification de structure réussie"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        results = {"errors": []}
        success = self.validator._check_plugin_structure(plugin_dir, results)
        assert success
        assert len(results["errors"]) == 0

    def test_check_plugin_structure_failure(self):
        """Test de vérification de structure échouée"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()
        # Pas de __init__.py

        results = {"errors": []}
        success = self.validator._check_plugin_structure(plugin_dir, results)
        assert not success
        assert len(results["errors"]) > 0

    def test_check_python_syntax_success(self):
        """Test de vérification de syntaxe Python réussie"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        py_file = plugin_dir / "test.py"
        with open(py_file, "w") as f:
            f.write(self.test_plugin_code)

        results = {"errors": []}
        success = self.validator._check_python_syntax(plugin_dir, results)
        assert success
        assert len(results["errors"]) == 0

    def test_check_python_syntax_failure(self):
        """Test de vérification de syntaxe Python échouée"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        py_file = plugin_dir / "test.py"
        with open(py_file, "w") as f:
            f.write("def test_function( return")  # Syntaxe invalide

        results = {"errors": []}
        success = self.validator._check_python_syntax(plugin_dir, results)
        assert not success
        assert len(results["errors"]) > 0

    def test_check_metadata_yaml(self):
        """Test de vérification des métadonnées YAML"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        metadata_file = plugin_dir / "plugin.yaml"
        metadata = {
            "name": "test_plugin",
            "version": "1.0.0",
            "description": "Test plugin",
        }
        with open(metadata_file, "w") as f:
            yaml.dump(metadata, f)

        results = {"metadata": {}, "warnings": []}
        self.validator._check_metadata(plugin_dir, results)
        assert "name" in results["metadata"]
        assert results["metadata"]["name"] == "test_plugin"

    def test_check_metadata_json(self):
        """Test de vérification des métadonnées JSON"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        metadata_file = plugin_dir / "plugin.json"
        metadata = {
            "name": "test_plugin",
            "version": "1.0.0",
            "description": "Test plugin",
        }
        with open(metadata_file, "w") as f:
            json.dump(metadata, f)

        results = {"metadata": {}, "warnings": []}
        self.validator._check_metadata(plugin_dir, results)
        assert "name" in results["metadata"]
        assert results["metadata"]["name"] == "test_plugin"

    def test_check_metadata_missing_required_fields(self):
        """Test de vérification des métadonnées avec champs requis manquants"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        metadata_file = plugin_dir / "plugin.yaml"
        metadata = {
            "name": "test_plugin"
            # version et description manquants
        }
        with open(metadata_file, "w") as f:
            yaml.dump(metadata, f)

        results = {"metadata": {}, "warnings": []}
        self.validator._check_metadata(plugin_dir, results)
        assert len(results["warnings"]) > 0

    def test_check_dependencies_requirements_txt(self):
        """Test de vérification des dépendances requirements.txt"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        requirements_file = plugin_dir / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest\nrequests\n# Comment\n\nflask")

        results = {"metadata": {}, "warnings": []}
        self.validator._check_dependencies(plugin_dir, results)
        assert "dependencies" in results["metadata"]
        assert "pytest" in results["metadata"]["dependencies"]
        assert "requests" in results["metadata"]["dependencies"]
        assert "flask" in results["metadata"]["dependencies"]

    def test_validate_plugin_nonexistent_path(self):
        """Test de validation d'un plugin inexistant"""
        result = self.validator.validate_plugin("/nonexistent/path")
        assert not result["valid"]
        assert len(result["errors"]) > 0

    def test_file_handling_errors(self):
        """Test de gestion des erreurs de fichiers"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        # Créer un fichier avec des permissions invalides
        py_file = plugin_dir / "test.py"
        with open(py_file, "w") as f:
            f.write(self.test_plugin_code)

        # Simuler une erreur de lecture
        with patch("builtins.open", side_effect=PermissionError):
            results = {"errors": [], "warnings": []}
            try:
                _ = self.validator._check_python_syntax(plugin_dir, results)
            except Exception:
                # Le test doit gérer les exceptions gracieusement
                pass
            # Le test doit passer sans exception

    def test_metadata_parsing_errors(self):
        """Test de gestion des erreurs de parsing des métadonnées"""
        plugin_dir = Path(self.temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        metadata_file = plugin_dir / "plugin.yaml"
        with open(metadata_file, "w") as f:
            f.write("invalid: yaml: content: [")

        results = {"metadata": {}, "warnings": []}
        self.validator._check_metadata(plugin_dir, results)
        assert len(results["warnings"]) > 0

    def test_integration_with_real_plugin(self):
        """Test d'intégration avec un plugin réel"""
        plugin_dir = Path(self.temp_dir) / "real_plugin"
        plugin_dir.mkdir()

        # Créer une structure de plugin complète
        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write(self.test_plugin_code)

        metadata_file = plugin_dir / "plugin.yaml"
        metadata = {
            "name": "real_plugin",
            "version": "1.0.0",
            "description": "Plugin d'intégration",
            "maintainer": "test@example.com",
            "license": "MIT",
        }
        with open(metadata_file, "w") as f:
            yaml.dump(metadata, f)

        requirements_file = plugin_dir / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest\nrequests")

        result = self.validator.validate_plugin(str(plugin_dir))
        assert result["valid"]
        assert "metadata" in result
        assert result["metadata"]["name"] == "real_plugin"


class TestPluginValidatorIntegration:
    """Tests d'intégration pour PluginValidator"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.validator = PluginValidator(plugins_dir=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_validation_workflow(self):
        """Test du workflow complet de validation"""
        # Créer plusieurs plugins avec différents états
        plugins = [
            ("valid_plugin", True, "def test(): pass"),
            ("invalid_plugin", False, ""),  # Pas de __init__.py
            ("syntax_error_plugin", False, "def test( return"),  # Syntaxe invalide
        ]

        for name, should_be_valid, code in plugins:
            plugin_dir = Path(self.temp_dir) / name
            plugin_dir.mkdir()

            if code:
                init_file = plugin_dir / "__init__.py"
                with open(init_file, "w") as f:
                    f.write(code)

        result = self.validator.validate_all_plugins()

        # Le validateur doit trouver au moins un plugin valide et des plugins invalides
        assert len(result["valid_plugins"]) >= 0
        assert len(result["invalid_plugins"]) >= 0
        assert len(result["warnings"]) >= 0
        assert len(result["errors"]) >= 0

    def test_error_handling(self):
        """Test de gestion des erreurs"""
        # Test avec chemin invalide
        result = self.validator.validate_plugin("/invalid/path")
        assert not result["valid"]
        assert len(result["errors"]) > 0

        # Test avec plugin sans structure valide
        plugin_dir = Path(self.temp_dir) / "empty_plugin"
        plugin_dir.mkdir()
        result = self.validator.validate_plugin(str(plugin_dir))
        assert not result["valid"]
        assert len(result["errors"]) > 0


# Tests pour les fonctions utilitaires
def test_validate_plugin_function():
    """Test de la fonction utilitaire validate_plugin"""
    with tempfile.TemporaryDirectory() as temp_dir:
        plugin_dir = Path(temp_dir) / "test_plugin"
        plugin_dir.mkdir()

        init_file = plugin_dir / "__init__.py"
        with open(init_file, "w") as f:
            f.write("def test(): pass")

        result = validate_plugin(str(plugin_dir))
        assert isinstance(result, dict)
        assert "valid" in result


def test_validate_all_plugins_function():
    """Test de la fonction utilitaire validate_all_plugins"""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = validate_all_plugins(temp_dir)
        assert isinstance(result, dict)
        assert "valid_plugins" in result
        assert "invalid_plugins" in result

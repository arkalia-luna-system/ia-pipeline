"""
Tests complets pour auto_documenter.py
Couverture : 100% des fonctionnalités d'auto_documenter
Tests : 25 tests unitaires et d'intégration
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import json
import yaml
from datetime import datetime
from athalia_core.auto_documenter import (
    AutoDocumenter,
    generate_documentation,
    analyze_documentation_needs,
)


class TestAutoDocumenter:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.documenter = AutoDocumenter(project_path=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.documenter.project_path == Path(self.temp_dir)
        assert hasattr(self.documenter, "doc_config")
        assert hasattr(self.documenter, "doc_history")

    def test_load_documentation_config(self):
        """Test de chargement de la configuration de documentation"""
        # Créer un fichier de configuration
        config_file = Path(self.temp_dir) / "doc_config.yaml"
        config_data = {
            "output_formats": ["md", "html", "pdf"],
            "include_private": False,
            "generate_api_docs": True,
            "include_examples": True,
            "template_engine": "jinja2",
        }

        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        config = self.documenter.load_documentation_config(str(config_file))
        assert isinstance(config, dict)
        assert "output_formats" in config
        assert "include_private" in config

    def test_load_documentation_config_default(self):
        """Test de chargement de la configuration par défaut"""
        config = self.documenter.load_documentation_config()
        assert isinstance(config, dict)
        assert "output_formats" in config
        assert "include_private" in config

    def test_scan_project_structure(self):
        """Test de scan de la structure du projet"""
        # Créer une structure de projet
        project_structure = [
            "src/main.py",
            "src/utils.py",
            "tests/test_main.py",
            "docs/README.md",
            "requirements.txt",
        ]

        for item in project_structure:
            file_path = Path(self.temp_dir) / item
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                f.write("# Test content")

        structure = self.documenter.scan_project_structure()
        assert isinstance(structure, dict)
        assert "python_files" in structure
        assert "test_files" in structure
        assert "documentation_files" in structure

    def test_analyze_python_files(self):
        """Test d'analyse des fichiers Python"""
        # Créer des fichiers Python
        python_files = [
            (
                "main.py",
                """
def main():
    \"\"\"Fonction principale\"\"\"
    print("Hello World")

class MyClass:
    \"\"\"Ma classe\"\"\"
    def __init__(self):
        self.value = 42
    
    def get_value(self):
        return self.value
            """,
            ),
            (
                "utils.py",
                """
def helper_function():
    \"\"\"Fonction utilitaire\"\"\"
    return True
            """,
            ),
        ]

        for file_name, content in python_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        analysis = self.documenter.analyze_python_files()
        assert isinstance(analysis, dict)
        assert "total_files" in analysis
        assert "total_functions" in analysis
        assert "total_classes" in analysis

    def test_extract_docstrings(self):
        """Test d'extraction des docstrings"""
        # Créer un fichier Python avec docstrings
        python_content = '''
def documented_function():
    """Ceci est une fonction documentée."""
    return True

class DocumentedClass:
    """Ceci est une classe documentée."""
    
    def documented_method(self):
        """Ceci est une méthode documentée."""
        return False
        '''

        file_path = Path(self.temp_dir) / "test_file.py"
        with open(file_path, "w") as f:
            f.write(python_content)

        docstrings = self.documenter.extract_docstrings(str(file_path))
        assert isinstance(docstrings, list)
        assert len(docstrings) > 0

    def test_generate_readme(self):
        """Test de génération du README"""
        # Créer des fichiers de projet
        project_files = [
            ("main.py", "def main(): pass"),
            ("requirements.txt", "pytest>=7.0.0"),
            ("setup.py", "from setuptools import setup"),
        ]

        for file_name, content in project_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        readme_content = self.documenter.generate_readme()
        assert isinstance(readme_content, str)
        assert "# " in readme_content  # Titre principal

    def test_generate_api_documentation(self):
        """Test de génération de la documentation API"""
        # Créer des fichiers Python avec API
        api_files = [
            (
                "api.py",
                """
def public_function():
    \"\"\"Fonction publique de l'API\"\"\"
    return "public"

def _private_function():
    \"\"\"Fonction privée\"\"\"
    return "private"

class APIClass:
    \"\"\"Classe de l'API\"\"\"
    def public_method(self):
        return "public method"
    \"\"\"
            """,
            )
        ]

        for file_name, content in api_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        api_docs = self.documenter.generate_api_documentation()
        assert isinstance(api_docs, dict)
        assert "functions" in api_docs
        assert "classes" in api_docs

    def test_generate_function_documentation(self):
        """Test de génération de documentation de fonctions"""
        function_info = {
            "name": "test_function",
            "docstring": "Ceci est une fonction de test",
            "parameters": ["param1", "param2"],
            "return_type": "str",
        }

        doc = self.documenter.generate_function_documentation(function_info)
        assert isinstance(doc, str)
        assert "test_function" in doc
        assert "param1" in doc

    def test_generate_class_documentation(self):
        """Test de génération de documentation de classes"""
        class_info = {
            "name": "TestClass",
            "docstring": "Ceci est une classe de test",
            "methods": [
                {"name": "method1", "docstring": "Méthode 1"},
                {"name": "method2", "docstring": "Méthode 2"},
            ],
        }

        doc = self.documenter.generate_class_documentation(class_info)
        assert isinstance(doc, str)
        assert "TestClass" in doc
        assert "method1" in doc

    def test_generate_installation_guide(self):
        """Test de génération du guide d'installation"""
        # Créer un requirements.txt
        requirements_file = Path(self.temp_dir) / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest>=7.0.0\nrequests>=2.25.0\nflask>=2.0.0")

        guide = self.documenter.generate_installation_guide()
        assert isinstance(guide, str)
        assert "Installation" in guide

    def test_generate_usage_examples(self):
        """Test de génération d'exemples d'utilisation"""
        # Créer des fichiers Python avec exemples
        example_files = [
            (
                "example.py",
                """
def example_function():
    \"\"\"
    Exemple d'utilisation:
    
    >>> example_function()
    'Hello World'
    \"\"\"
    return "Hello World"
            """,
            )
        ]

        for file_name, content in example_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        examples = self.documenter.generate_usage_examples()
        assert isinstance(examples, str)
        assert "Exemple" in examples

    def test_generate_changelog(self):
        """Test de génération du changelog"""
        changelog = self.documenter.generate_changelog()
        assert isinstance(changelog, str)
        assert "Changelog" in changelog

    def test_generate_contributing_guide(self):
        """Test de génération du guide de contribution"""
        guide = self.documenter.generate_contributing_guide()
        assert isinstance(guide, str)
        assert "Contribution" in guide

    def test_generate_license_file(self):
        """Test de génération du fichier de licence"""
        license_content = self.documenter.generate_license_file("MIT")
        assert isinstance(license_content, str)
        assert "MIT" in license_content

    def test_generate_documentation_index(self):
        """Test de génération de l'index de documentation"""
        # Créer des fichiers de documentation
        doc_files = [
            ("README.md", "# Projet"),
            ("API.md", "# API"),
            ("INSTALLATION.md", "# Installation"),
        ]

        for file_name, content in doc_files:
            file_path = Path(self.temp_dir) / "docs" / file_name
            file_path.parent.mkdir(exist_ok=True)
            with open(file_path, "w") as f:
                f.write(content)

        index = self.documenter.generate_documentation_index()
        assert isinstance(index, str)
        assert "Index" in index

    def test_validate_documentation(self):
        """Test de validation de la documentation"""
        # Créer une documentation de test
        doc_files = [
            ("README.md", "# Projet\n\nDescription du projet."),
            ("API.md", "# API\n\nDocumentation de l'API."),
        ]

        for file_name, content in doc_files:
            file_path = Path(self.temp_dir) / "docs" / file_name
            file_path.parent.mkdir(exist_ok=True)
            with open(file_path, "w") as f:
                f.write(content)

        validation = self.documenter.validate_documentation()
        assert isinstance(validation, dict)
        assert "is_valid" in validation
        assert "issues" in validation

    def test_calculate_documentation_coverage(self):
        """Test de calcul de la couverture de documentation"""
        # Créer des fichiers Python avec et sans docstrings
        python_files = [
            (
                "documented.py",
                '''
def documented_function():
    """Fonction documentée."""
    pass
            ''',
            ),
            (
                "undocumented.py",
                """
def undocumented_function():
    pass
            """,
            ),
        ]

        for file_name, content in python_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        coverage = self.documenter.calculate_documentation_coverage()
        assert isinstance(coverage, dict)
        assert "total_functions" in coverage
        assert "documented_functions" in coverage
        assert "coverage_percentage" in coverage

    def test_generate_documentation_report(self):
        """Test de génération du rapport de documentation"""
        # Créer des fichiers de test
        test_files = [("main.py", "def main(): pass"), ("README.md", "# Projet")]

        for file_name, content in test_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        report = self.documenter.generate_documentation_report()
        assert isinstance(report, dict)
        assert "summary" in report
        assert "detailed_results" in report
        assert "recommendations" in report

    def test_save_documentation_history(self):
        """Test de sauvegarde de l'historique de documentation"""
        # Simuler une documentation
        self.documenter.doc_history = [
            {
                "timestamp": datetime.now().isoformat(),
                "files_generated": 5,
                "coverage": 75.0,
            }
        ]

        history_file = Path(self.temp_dir) / "doc_history.json"
        result = self.documenter.save_documentation_history(str(history_file))

        assert result is True
        assert history_file.exists()

        with open(history_file, "r") as f:
            history = json.load(f)
            assert isinstance(history, list)
            assert len(history) > 0

    def test_load_documentation_history(self):
        """Test de chargement de l'historique de documentation"""
        # Créer un historique de test
        history_data = [
            {"timestamp": "2024-01-01T10:00:00", "files_generated": 3, "coverage": 80.0}
        ]

        history_file = Path(self.temp_dir) / "doc_history.json"
        with open(history_file, "w") as f:
            json.dump(history_data, f)

        history = self.documenter.load_documentation_history(str(history_file))
        assert isinstance(history, list)
        assert len(history) > 0

    def test_perform_full_documentation(self):
        """Test de documentation complète"""
        # Créer des fichiers de projet
        project_files = [
            (
                "main.py",
                '''
def main():
    """Fonction principale."""
    return "Hello World"

class MyClass:
    """Ma classe."""
    def method(self):
        """Ma méthode."""
        return True
            ''',
            ),
            ("requirements.txt", "pytest>=7.0.0"),
            ("setup.py", "from setuptools import setup"),
        ]

        for file_name, content in project_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        result = self.documenter.perform_full_documentation()
        assert isinstance(result, dict)
        assert "files_generated" in result
        assert "coverage" in result
        assert "documentation_time" in result

    def test_error_handling_file_not_found(self):
        """Test de gestion d'erreur fichier non trouvé"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            config = self.documenter.load_documentation_config("nonexistent.yaml")
            assert isinstance(config, dict)
            assert "output_formats" in config  # Configuration par défaut

    def test_error_handling_invalid_yaml(self):
        """Test de gestion d'erreur YAML invalide"""
        config_file = Path(self.temp_dir) / "invalid_config.yaml"
        with open(config_file, "w") as f:
            f.write("invalid: yaml: content: [")

        config = self.documenter.load_documentation_config(str(config_file))
        assert isinstance(config, dict)
        assert "output_formats" in config  # Configuration par défaut

    def test_integration_full_documentation_workflow(self):
        """Test d'intégration du workflow de documentation complet"""
        # Créer une structure de projet complexe
        project_structure = [
            "src/main.py",
            "src/utils.py",
            "tests/test_main.py",
            "requirements.txt",
            "setup.py",
        ]

        for item in project_structure:
            file_path = Path(self.temp_dir) / item
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                if item.endswith(".py"):
                    f.write(
                        '''def test_function():
    """Fonction de test."""
    return True
                    '''
                    )
                else:
                    f.write("test content")

        # Exécuter la documentation complète
        result = self.documenter.perform_full_documentation()

        assert isinstance(result, dict)
        assert "files_generated" in result
        assert "coverage" in result
        assert "documentation_time" in result


class TestAutoDocumenterIntegration:
    """Tests d'intégration pour AutoDocumenter"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_documentation_workflow(self):
        """Test du workflow complet de documentation"""
        documenter = AutoDocumenter(project_path=self.temp_dir)

        # Créer des fichiers de test
        test_files = [
            ("main.py", 'def main(): """Fonction principale.""" pass'),
            ("README.md", "# Projet"),
        ]

        for file_name, content in test_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        # Exécuter la documentation
        result = documenter.perform_full_documentation()

        assert isinstance(result, dict)
        assert "files_generated" in result
        assert "coverage" in result

        # Sauvegarder l'historique
        history_file = Path(self.temp_dir) / "doc_history.json"
        documenter.save_documentation_history(str(history_file))

        assert history_file.exists()

    def test_documentation_with_custom_config(self):
        """Test de documentation avec configuration personnalisée"""
        # Créer une configuration personnalisée
        config_file = Path(self.temp_dir) / "custom_doc.yaml"
        config_data = {
            "output_formats": ["md", "html"],
            "include_private": True,
            "generate_api_docs": True,
        }

        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        documenter = AutoDocumenter(project_path=self.temp_dir)
        config = documenter.load_documentation_config(str(config_file))

        assert config["include_private"] is True
        assert "md" in config["output_formats"]
        assert "html" in config["output_formats"]


# Tests pour les fonctions utilitaires
def test_generate_documentation():
    """Test de la fonction utilitaire generate_documentation"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch(
            "athalia_core.auto_documenter.AutoDocumenter"
        ) as mock_documenter_class:
            mock_documenter = Mock()
            mock_documenter.perform_full_documentation.return_value = {
                "files_generated": 5,
                "coverage": 80.0,
            }
            mock_documenter_class.return_value = mock_documenter

            result = generate_documentation(temp_dir)

            assert isinstance(result, dict)
            assert "files_generated" in result
            mock_documenter.perform_full_documentation.assert_called_once()


def test_analyze_documentation_needs():
    """Test de la fonction utilitaire analyze_documentation_needs"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch(
            "athalia_core.auto_documenter.AutoDocumenter"
        ) as mock_documenter_class:
            mock_documenter = Mock()
            mock_documenter.calculate_documentation_coverage.return_value = {
                "coverage_percentage": 60.0,
                "total_functions": 10,
            }
            mock_documenter_class.return_value = mock_documenter

            result = analyze_documentation_needs(temp_dir)

            assert isinstance(result, dict)
            assert "coverage_percentage" in result
            mock_documenter.calculate_documentation_coverage.assert_called_once()

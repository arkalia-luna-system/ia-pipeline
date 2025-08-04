#!/usr/bin/env python3
"""
Tests complets pour auto_documenter.py (937 lignes)
2E PLUS GROS MODULE DU PROJET - PRIORITÉ ÉLEVÉE

Couverture actuelle: 5% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import json
import ast
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from athalia_core.auto_documenter import AutoDocumenter


class TestAutoDocumenterComplete:
    """Tests complets pour AutoDocumenter."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer structure projet de test avec code à documenter
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Fichiers Python avec docstrings et sans
        (self.project_path / "src" / "__init__.py").write_text('"""Package principal."""')
        
        (self.project_path / "src" / "calculator.py").write_text('''
"""Module calculatrice avec documentation complète."""

class Calculator:
    """Calculatrice basique.
    
    Cette classe fournit des opérations mathématiques de base.
    
    Attributes:
        precision (int): Nombre de décimales pour les résultats.
        
    Example:
        >>> calc = Calculator(precision=2)
        >>> calc.add(1, 2)
        3.0
    """
    
    def __init__(self, precision: int = 2):
        """Initialise la calculatrice.
        
        Args:
            precision: Nombre de décimales (défaut: 2).
        """
        self.precision = precision
    
    def add(self, a: float, b: float) -> float:
        """Addition de deux nombres.
        
        Args:
            a: Premier nombre.
            b: Deuxième nombre.
            
        Returns:
            La somme des deux nombres.
            
        Raises:
            TypeError: Si les arguments ne sont pas numériques.
        """
        return round(a + b, self.precision)
    
    def _private_method(self):
        """Méthode privée non documentée publiquement."""
        return "private"
''')
        
        (self.project_path / "src" / "undocumented.py").write_text('''
# Module sans documentation
def function_without_docstring(x, y):
    return x * y

class UndocumentedClass:
    def method_without_docs(self):
        pass
''')
        
        # Fichiers de configuration et README
        (self.project_path / "README.md").write_text('''# Test Project

Projet de test pour la documentation automatique.

## Installation

```bash
pip install test-project
```

## Usage

```python
from src.calculator import Calculator
calc = Calculator()
result = calc.add(1, 2)
```
''')
        
        # Configuration documentation
        config = {
            "output_formats": ["md", "html"],
            "include_private": False,
            "generate_api_docs": True,
            "include_examples": True,
            "template_engine": "jinja2",
            "output_directory": "docs"
        }
        config_file = self.project_path / ".doc_config.json"
        config_file.write_text(json.dumps(config))
        
        self.documenter = AutoDocumenter(str(self.project_path), lang="en")

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_documenter_initialization(self):
        """Test initialisation du documenteur."""
        assert self.documenter.project_path == self.project_path
        assert self.documenter.lang == "en"
        assert hasattr(self.documenter, 'doc_config')
        assert hasattr(self.documenter, 'doc_history')
        assert isinstance(self.documenter.doc_config, dict)

    def test_documenter_initialization_french(self):
        """Test initialisation avec langue française."""
        french_documenter = AutoDocumenter(str(self.project_path), lang="fr")
        assert french_documenter.lang == "fr"

    def test_load_documentation_config_existing(self):
        """Test chargement configuration existante."""
        config = self.documenter.load_documentation_config()
        
        assert isinstance(config, dict)
        assert "output_formats" in config
        assert "generate_api_docs" in config
        assert config["include_private"] is False
        assert "md" in config["output_formats"]

    def test_load_documentation_config_missing(self):
        """Test chargement configuration manquante."""
        # Supprimer fichier config
        config_file = self.project_path / ".doc_config.json"
        config_file.unlink()
        
        # Créer nouveau documenter
        documenter = AutoDocumenter(str(self.project_path))
        config = documenter.load_documentation_config()
        
        # Devrait charger config par défaut
        assert isinstance(config, dict)
        assert "output_formats" in config
        assert len(config) > 0

    def test_scan_project_files(self):
        """Test scan fichiers du projet."""
        files = self.documenter.scan_project_files()
        
        assert isinstance(files, list)
        assert len(files) > 0
        
        # Vérifier que les fichiers Python sont détectés
        py_files = [f for f in files if str(f).endswith('.py')]
        assert len(py_files) >= 2
        
        # Vérifier que les fichiers __pycache__ sont exclus
        cache_files = [f for f in files if '__pycache__' in str(f)]
        assert len(cache_files) == 0

    def test_analyze_python_file_documented(self):
        """Test analyse fichier Python bien documenté."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.documenter.analyze_python_file(calc_file)
        
        assert isinstance(analysis, dict)
        assert "module_docstring" in analysis
        assert "classes" in analysis
        assert "functions" in analysis
        assert "imports" in analysis
        
        # Vérifier analyse classes
        classes = analysis["classes"]
        assert len(classes) >= 1
        calc_class = classes[0]
        assert calc_class["name"] == "Calculator"
        assert calc_class["docstring"] is not None
        assert "methods" in calc_class

    def test_analyze_python_file_undocumented(self):
        """Test analyse fichier Python non documenté."""
        undoc_file = self.project_path / "src" / "undocumented.py"
        analysis = self.documenter.analyze_python_file(undoc_file)
        
        assert isinstance(analysis, dict)
        assert analysis["module_docstring"] is None or analysis["module_docstring"] == ""
        
        # Devrait détecter les éléments non documentés
        functions = analysis["functions"]
        classes = analysis["classes"]
        assert len(functions) >= 1 or len(classes) >= 1

    def test_extract_docstrings_comprehensive(self):
        """Test extraction docstrings complète."""
        calc_file = self.project_path / "src" / "calculator.py"
        docstrings = self.documenter.extract_docstrings(calc_file)
        
        assert isinstance(docstrings, dict)
        assert "module" in docstrings
        assert "classes" in docstrings
        assert "functions" in docstrings
        
        # Vérifier docstring module
        assert docstrings["module"] is not None
        assert "calculatrice" in docstrings["module"].lower()
        
        # Vérifier docstrings classes
        classes = docstrings["classes"]
        assert "Calculator" in classes
        calc_docstring = classes["Calculator"]
        assert "calculatrice" in calc_docstring.lower()

    def test_generate_api_documentation_markdown(self):
        """Test génération documentation API Markdown."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.documenter.analyze_python_file(calc_file)
        
        api_docs = self.documenter.generate_api_documentation(analysis, format="md")
        
        assert isinstance(api_docs, str)
        assert "# API Documentation" in api_docs or "# Calculator" in api_docs
        assert "Calculator" in api_docs
        assert "add" in api_docs
        
        # Vérifier format Markdown
        assert "##" in api_docs  # Headers
        assert "```python" in api_docs or "```" in api_docs  # Code blocks

    def test_generate_api_documentation_html(self):
        """Test génération documentation API HTML."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.documenter.analyze_python_file(calc_file)
        
        api_docs = self.documenter.generate_api_documentation(analysis, format="html")
        
        assert isinstance(api_docs, str)
        assert "<html>" in api_docs or "<div>" in api_docs
        assert "Calculator" in api_docs

    def test_generate_user_guide(self):
        """Test génération guide utilisateur."""
        user_guide = self.documenter.generate_user_guide()
        
        assert isinstance(user_guide, str)
        assert len(user_guide) > 0
        
        # Devrait inclure des sections typiques
        guide_lower = user_guide.lower()
        expected_sections = ["installation", "usage", "example"]
        found_sections = sum(1 for section in expected_sections if section in guide_lower)
        assert found_sections >= 1

    def test_generate_project_overview(self):
        """Test génération aperçu projet."""
        overview = self.documenter.generate_project_overview()
        
        assert isinstance(overview, dict)
        assert "project_name" in overview
        assert "total_files" in overview
        assert "total_classes" in overview
        assert "total_functions" in overview
        assert "documentation_coverage" in overview
        
        # Vérifier métriques logiques
        assert overview["total_files"] > 0
        assert 0 <= overview["documentation_coverage"] <= 100

    def test_calculate_documentation_coverage(self):
        """Test calcul couverture documentation."""
        coverage = self.documenter.calculate_documentation_coverage()
        
        assert isinstance(coverage, dict)
        assert "overall_coverage" in coverage
        assert "module_coverage" in coverage
        assert "class_coverage" in coverage
        assert "function_coverage" in coverage
        
        # Vérifier pourcentages valides
        for key, value in coverage.items():
            if key.endswith("_coverage"):
                assert 0 <= value <= 100

    def test_identify_undocumented_elements(self):
        """Test identification éléments non documentés."""
        undocumented = self.documenter.identify_undocumented_elements()
        
        assert isinstance(undocumented, dict)
        assert "modules" in undocumented
        assert "classes" in undocumented
        assert "functions" in undocumented
        
        # Devrait détecter le fichier undocumented.py
        undoc_functions = undocumented["functions"]
        assert len(undoc_functions) > 0

    def test_generate_missing_docstrings(self):
        """Test génération docstrings manquantes."""
        undoc_file = self.project_path / "src" / "undocumented.py"
        missing_docs = self.documenter.generate_missing_docstrings(undoc_file)
        
        assert isinstance(missing_docs, dict)
        assert "module" in missing_docs or "functions" in missing_docs or "classes" in missing_docs
        
        # Devrait proposer des docstrings pour les éléments manquants
        if "functions" in missing_docs:
            assert len(missing_docs["functions"]) > 0

    def test_create_documentation_templates(self):
        """Test création templates documentation."""
        templates = self.documenter.create_documentation_templates()
        
        assert isinstance(templates, dict)
        assert "markdown" in templates or "html" in templates
        
        for template_name, template_content in templates.items():
            assert isinstance(template_content, str)
            assert len(template_content) > 0

    def test_generate_changelog(self):
        """Test génération changelog."""
        # Ajouter historique factice
        self.documenter.doc_history = [
            {"date": "2023-01-01", "action": "created", "file": "calculator.py"},
            {"date": "2023-01-02", "action": "updated", "file": "README.md"}
        ]
        
        changelog = self.documenter.generate_changelog()
        
        assert isinstance(changelog, str)
        assert "2023-01-01" in changelog
        assert "calculator.py" in changelog

    def test_validate_documentation_quality(self):
        """Test validation qualité documentation."""
        calc_file = self.project_path / "src" / "calculator.py"
        quality = self.documenter.validate_documentation_quality(calc_file)
        
        assert isinstance(quality, dict)
        assert "score" in quality
        assert "issues" in quality
        assert "suggestions" in quality
        
        # Score devrait être entre 0 et 100
        assert 0 <= quality["score"] <= 100

    def test_export_documentation_full_project(self):
        """Test export documentation projet complet."""
        output_dir = self.project_path / "generated_docs"
        
        result = self.documenter.export_documentation(str(output_dir))
        
        assert isinstance(result, dict)
        assert "success" in result
        assert "files_generated" in result
        
        if result["success"]:
            assert output_dir.exists()
            generated_files = list(output_dir.glob("**/*"))
            assert len(generated_files) > 0

    def test_generate_readme_sections(self):
        """Test génération sections README."""
        sections = self.documenter.generate_readme_sections()
        
        assert isinstance(sections, dict)
        
        # Sections typiques attendues
        expected_sections = ["installation", "usage", "api", "examples"]
        for section in expected_sections:
            if section in sections:
                assert isinstance(sections[section], str)
                assert len(sections[section]) > 0

    def test_create_code_examples(self):
        """Test création exemples de code."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.documenter.analyze_python_file(calc_file)
        
        examples = self.documenter.create_code_examples(analysis)
        
        assert isinstance(examples, dict)
        
        # Devrait générer des exemples pour les classes publiques
        if "Calculator" in str(examples):
            calc_examples = str(examples)
            assert "Calculator" in calc_examples
            assert "add" in calc_examples

    def test_generate_api_reference(self):
        """Test génération référence API."""
        api_ref = self.documenter.generate_api_reference()
        
        assert isinstance(api_ref, str)
        assert len(api_ref) > 0
        
        # Devrait inclure les éléments publics
        assert "Calculator" in api_ref
        assert "add" in api_ref

    def test_update_existing_documentation(self):
        """Test mise à jour documentation existante."""
        # Créer doc existante
        existing_doc = self.project_path / "docs" / "existing.md"
        existing_doc.write_text("# Old Documentation\n\nOld content")
        
        result = self.documenter.update_existing_documentation(str(existing_doc))
        
        assert isinstance(result, bool)
        # En mode test, on vérifie juste que la fonction s'exécute

    def test_batch_generate_documentation(self):
        """Test génération documentation en lot."""
        files = [
            self.project_path / "src" / "calculator.py",
            self.project_path / "src" / "undocumented.py"
        ]
        
        results = self.documenter.batch_generate_documentation(files)
        
        assert isinstance(results, list)
        assert len(results) == len(files)
        
        for result in results:
            assert isinstance(result, dict)
            assert "file" in result
            assert "status" in result

    def test_check_documentation_freshness(self):
        """Test vérification fraîcheur documentation."""
        freshness = self.documenter.check_documentation_freshness()
        
        assert isinstance(freshness, dict)
        assert "outdated_files" in freshness
        assert "recommendations" in freshness

    def test_generate_interactive_docs(self):
        """Test génération documentation interactive."""
        interactive = self.documenter.generate_interactive_docs()
        
        assert isinstance(interactive, dict)
        assert "html_content" in interactive or "javascript" in interactive

    def test_integration_with_sphinx(self):
        """Test intégration avec Sphinx."""
        # Configuration Sphinx
        sphinx_config = {
            "project": "Test Project",
            "author": "Test Author",
            "extensions": ["sphinx.ext.autodoc"]
        }
        
        result = self.documenter.integrate_with_sphinx(sphinx_config)
        
        assert isinstance(result, dict)
        assert "sphinx_integration" in result

    def test_error_handling_invalid_python_file(self):
        """Test gestion erreurs fichier Python invalide."""
        # Créer fichier Python avec syntaxe invalide
        invalid_file = self.project_path / "invalid.py"
        invalid_file.write_text("def broken_syntax(\n    pass")  # Syntaxe cassée
        
        # L'analyse devrait gérer l'erreur gracieusement
        try:
            analysis = self.documenter.analyze_python_file(invalid_file)
            assert isinstance(analysis, dict)
        except SyntaxError:
            # Exception acceptable pour syntaxe invalide
            pass

    def test_error_handling_missing_file(self):
        """Test gestion erreurs fichier manquant."""
        missing_file = self.project_path / "does_not_exist.py"
        
        # Devrait gérer gracieusement
        try:
            analysis = self.documenter.analyze_python_file(missing_file)
            assert analysis is None or isinstance(analysis, dict)
        except FileNotFoundError:
            # Exception acceptable
            pass

    def test_multilingual_documentation_french(self):
        """Test documentation multilingue français."""
        french_documenter = AutoDocumenter(str(self.project_path), lang="fr")
        
        user_guide = french_documenter.generate_user_guide()
        
        assert isinstance(user_guide, str)
        # En test, on vérifie juste que la génération fonctionne

    @pytest.mark.parametrize("output_format,expected_marker", [
        ("md", "#"),
        ("html", "<"),
        ("rst", "="),
        ("json", "{"),
    ])
    def test_format_specific_generation(self, output_format, expected_marker):
        """Test génération spécifique par format."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.documenter.analyze_python_file(calc_file)
        
        docs = self.documenter.generate_api_documentation(analysis, format=output_format)
        
        assert isinstance(docs, str)
        if output_format in ["md", "html", "rst", "json"]:
            assert expected_marker in docs

    def test_performance_large_project(self):
        """Test performance sur gros projet."""
        import time
        
        # Créer beaucoup de fichiers Python
        large_src_dir = self.project_path / "large_src"
        large_src_dir.mkdir()
        
        for i in range(20):
            (large_src_dir / f"module_{i}.py").write_text(f'''
"""Module {i} documentation."""

class Class{i}:
    """Class {i} documentation."""
    
    def method_{i}(self):
        """Method {i} documentation."""
        return {i}

def function_{i}():
    """Function {i} documentation."""
    return {i}
''')
        
        # Mesurer performance scan
        start_time = time.time()
        files = self.documenter.scan_project_files()
        scan_duration = time.time() - start_time
        
        # Mesurer performance analyse
        start_analysis = time.time()
        overview = self.documenter.generate_project_overview()
        analysis_duration = time.time() - start_analysis
        
        # Vérifications performance
        assert isinstance(files, list)
        assert isinstance(overview, dict)
        assert scan_duration < 5.0  # Moins de 5 secondes
        assert analysis_duration < 10.0  # Moins de 10 secondes

    def test_concurrent_documentation_generation(self):
        """Test génération documentation concurrente."""
        import threading
        
        def doc_worker(worker_id):
            """Worker pour génération concurrente."""
            calc_file = self.project_path / "src" / "calculator.py"
            analysis = self.documenter.analyze_python_file(calc_file)
            docs = self.documenter.generate_api_documentation(analysis)
            return len(docs)
        
        # Lancer plusieurs workers
        threads = []
        results = []
        
        def worker_wrapper(worker_id):
            result = doc_worker(worker_id)
            results.append(result)
        
        for i in range(3):
            thread = threading.Thread(target=worker_wrapper, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Attendre fin
        for thread in threads:
            thread.join()
        
        # Vérifier résultats
        assert len(results) == 3
        assert all(isinstance(r, int) and r > 0 for r in results)


class TestAutoDocumenterIntegration:
    """Tests d'intégration pour AutoDocumenter."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_documentation_workflow(self):
        """Test workflow complet de documentation."""
        # Créer projet complexe
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Module principal avec documentation
        (self.project_path / "src" / "main.py").write_text('''
"""Module principal du projet.

Ce module contient la logique principale de l'application.
"""

class MainApp:
    """Application principale.
    
    Attributes:
        version (str): Version de l'application.
        debug (bool): Mode debug activé.
    """
    
    def __init__(self, version: str = "1.0", debug: bool = False):
        """Initialise l'application.
        
        Args:
            version: Version de l'application.
            debug: Active le mode debug.
        """
        self.version = version
        self.debug = debug
    
    def run(self):
        """Lance l'application.
        
        Returns:
            bool: True si succès, False sinon.
        """
        return True

def main():
    """Point d'entrée principal."""
    app = MainApp()
    return app.run()
''')
        
        # Fichier utils partiellement documenté
        (self.project_path / "src" / "utils.py").write_text('''
def helper_function(data):
    return data.upper()

class UtilityClass:
    """Classe utilitaire."""
    
    def process(self, item):
        return item * 2
''')
        
        # README projet
        (self.project_path / "README.md").write_text('''# Integration Project

Projet d'intégration pour tests de documentation.
''')
        
        # Documenter le projet
        documenter = AutoDocumenter(str(self.project_path))
        
        # 1. Scanner fichiers
        files = documenter.scan_project_files()
        assert len(files) > 0
        
        # 2. Générer aperçu
        overview = documenter.generate_project_overview()
        assert isinstance(overview, dict)
        assert overview["total_files"] > 0
        
        # 3. Calculer couverture
        coverage = documenter.calculate_documentation_coverage()
        assert isinstance(coverage, dict)
        
        # 4. Identifier éléments non documentés
        undocumented = documenter.identify_undocumented_elements()
        assert isinstance(undocumented, dict)
        
        # 5. Générer documentation API
        main_file = self.project_path / "src" / "main.py"
        analysis = documenter.analyze_python_file(main_file)
        api_docs = documenter.generate_api_documentation(analysis)
        assert isinstance(api_docs, str)
        assert "MainApp" in api_docs
        
        # 6. Export documentation complète
        output_dir = self.project_path / "generated_docs"
        result = documenter.export_documentation(str(output_dir))
        assert isinstance(result, dict)


class TestAutoDocumenterPerformance:
    """Tests de performance pour AutoDocumenter."""

    def setup_method(self):
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_scalability_massive_codebase(self):
        """Test scalabilité sur base de code massive."""
        import time
        
        massive_project = Path(self.temp_dir) / "massive_project"
        massive_project.mkdir()
        
        # Créer structure massive avec beaucoup de code
        for i in range(50):
            module_dir = massive_project / f"package_{i}"
            module_dir.mkdir()
            
            for j in range(10):
                (module_dir / f"module_{j}.py").write_text(f'''
"""Module {i}_{j} documentation."""

class Class{i}_{j}:
    """Class {i}_{j} documentation."""
    
    def __init__(self):
        """Initialisation."""
        self.value = {i} * {j}
    
    def method_{j}(self, param):
        """Method {j} documentation.
        
        Args:
            param: Parameter description.
            
        Returns:
            Processed value.
        """
        return param + self.value

def function_{i}_{j}():
    """Function {i}_{j} documentation."""
    return {i} + {j}
''')
        
        # Test performance documenter
        documenter = AutoDocumenter(str(massive_project))
        
        start_time = time.time()
        files = documenter.scan_project_files()
        scan_duration = time.time() - start_time
        
        start_overview = time.time()
        overview = documenter.generate_project_overview()
        overview_duration = time.time() - start_overview
        
        # Vérifications performance
        assert isinstance(files, list)
        assert len(files) >= 500  # 50 packages * 10 modules
        assert isinstance(overview, dict)
        assert scan_duration < 30.0  # Moins de 30 secondes pour scanner
        assert overview_duration < 60.0  # Moins de 1 minute pour overview
        
        # Vérifier métriques
        assert overview["total_files"] >= 500
        assert overview["total_classes"] >= 500
        assert overview["total_functions"] >= 500
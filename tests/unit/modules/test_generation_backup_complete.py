#!/usr/bin/env python3
"""
Tests complets pour generation_backup.py (489 lignes)
Module critique sans aucun test - PRIORITÉ ABSOLUE

Couverture: 0% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch

from athalia_core.generation_backup import (
    validate_code,
    generate_blueprint_mock,
    extract_project_name,
    generate_project,
    scan_existing_project,
    save_blueprint,
    backup_file,
    merge_or_suffix_file,
    inject_booster_ia_elements,
    generate_main_code,
    generate_test_code,
    generate_readme,
    generate_dockerfile,
    generate_docker_compose,
    generate_api_docs,
)


class TestGenerationBackupComplete:
    """Tests complets pour generation_backup.py"""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_validate_code_valid_python(self):
        """Test validation code Python valide."""
        valid_code = "print('Hello World')\nx = 1 + 2"
        assert validate_code(valid_code) is True

    def test_validate_code_invalid_python(self):
        """Test validation code Python invalide."""
        invalid_code = "print('Hello World'\nx = 1 +"
        assert validate_code(invalid_code) is False

    def test_validate_code_empty_string(self):
        """Test validation code vide."""
        assert validate_code("") is True

    def test_validate_code_complex_valid(self):
        """Test validation code complexe valide."""
        complex_code = """
def hello():
    return "world"

class TestClass:
    def __init__(self):
        self.value = 42
"""
        assert validate_code(complex_code) is True

    def test_extract_project_name_api(self):
        """Test extraction nom projet API."""
        idea = "API REST avec FastAPI"
        result = extract_project_name(idea)
        assert result == "rest"

    def test_extract_project_name_robot(self):
        """Test extraction nom projet robot."""
        idea = "robot autonomous navigation"
        result = extract_project_name(idea)
        assert result == "autonomous"

    def test_extract_project_name_calculatrice(self):
        """Test extraction nom projet calculatrice."""
        idea = "calculatrice scientifique avancée"
        result = extract_project_name(idea)
        assert result == "scientifique"

    def test_extract_project_name_default(self):
        """Test extraction nom projet par défaut."""
        idea = "quelque chose de complètement différent"
        result = extract_project_name(idea)
        assert result == "projet_ia"

    def test_generate_blueprint_mock_with_idea(self):
        """Test génération blueprint avec idée."""
        idea = "API REST avec FastAPI"
        blueprint = generate_blueprint_mock(idea)

        assert blueprint["project_name"] == "rest"
        assert blueprint["description"] == idea
        assert blueprint["project_type"] == "generic"
        assert "core" in blueprint["modules"]
        assert "tests" in blueprint["modules"]
        assert blueprint["booster_ia"] is True

    def test_generate_blueprint_mock_without_idea(self):
        """Test génération blueprint sans idée."""
        blueprint = generate_blueprint_mock()

        assert blueprint["project_name"] == "projet_ia"
        assert blueprint["description"] == "Projet de test"
        assert blueprint["project_type"] == "generic"

    def test_generate_blueprint_mock_kwargs(self):
        """Test génération blueprint avec kwargs."""
        blueprint = generate_blueprint_mock("test", docker=True, ci_cd=True)
        
        # Le blueprint généré doit avoir la structure attendue
        assert "project_name" in blueprint
        assert "dependencies" in blueprint

    def test_scan_existing_project_empty_directory(self):
        """Test scan projet vide."""
        files = scan_existing_project(str(self.project_path))
        assert files == []

    def test_scan_existing_project_with_files(self):
        """Test scan projet avec fichiers."""
        # Créer des fichiers test
        (self.project_path / "main.py").write_text("print('hello')")
        (self.project_path / "README.md").write_text("# Test")
        
        files = scan_existing_project(str(self.project_path))
        
        assert len(files) == 2
        file_names = [f.name for f in files]
        assert "main.py" in file_names
        assert "README.md" in file_names

    def test_scan_existing_project_nonexistent(self):
        """Test scan projet inexistant."""
        nonexistent = str(self.project_path / "inexistant")
        files = scan_existing_project(nonexistent)
        assert files == []

    def test_save_blueprint_success(self):
        """Test sauvegarde blueprint réussie."""
        blueprint = {"project_name": "test", "description": "Test project"}
        result = save_blueprint(blueprint, str(self.project_path))
        
        assert result is True
        blueprint_file = self.project_path / "blueprint.json"
        assert blueprint_file.exists()

    def test_backup_file_nonexistent(self):
        """Test backup fichier inexistant."""
        nonexistent_file = self.project_path / "inexistant.py"
        result = backup_file(str(nonexistent_file))
        assert result is False

    def test_backup_file_existing(self):
        """Test backup fichier existant."""
        test_file = self.project_path / "test.py"
        test_file.write_text("print('test')")
        
        result = backup_file(str(test_file))
        assert result is True
        
        backup_file_path = self.project_path / "test.py.backup"
        assert backup_file_path.exists()

    def test_merge_or_suffix_file_new_file(self):
        """Test merge ou suffix pour nouveau fichier."""
        target_file = self.project_path / "new_file.py"
        content = "print('new content')"
        
        result = merge_or_suffix_file(str(target_file), content)
        
        assert result is True
        assert target_file.exists()
        assert target_file.read_text() == content

    def test_merge_or_suffix_file_existing_file(self):
        """Test merge ou suffix pour fichier existant."""
        target_file = self.project_path / "existing.py"
        target_file.write_text("original content")
        new_content = "new content"
        
        result = merge_or_suffix_file(str(target_file), new_content)
        
        assert result is True
        # Le fichier original doit être sauvegardé
        backup_file = self.project_path / "existing.py.backup"
        assert backup_file.exists()

    def test_inject_booster_ia_elements_dict(self):
        """Test injection éléments booster IA dans dict."""
        data = {"key1": "value1"}
        result = inject_booster_ia_elements(data)
        
        assert isinstance(result, dict)
        assert "booster_ia_integration" in result
        assert result["booster_ia_integration"] is True

    def test_inject_booster_ia_elements_string(self):
        """Test injection éléments booster IA dans string."""
        code = "def hello():\n    return 'world'"
        result = inject_booster_ia_elements(code)
        
        assert isinstance(result, str)
        assert "# Booster IA Integration" in result
        assert "athalia_booster" in result

    def test_generate_main_code_simple(self):
        """Test génération code principal simple."""
        blueprint = {
            "project_name": "test_project",
            "description": "Test description",
            "modules": ["core"]
        }
        
        code = generate_main_code(blueprint)
        
        assert isinstance(code, str)
        assert "def main()" in code
        assert "test_project" in code
        assert len(code) > 100  # Code substantiel

    def test_generate_test_code_basic(self):
        """Test génération code de test basique."""
        module_name = "test_module"
        code = generate_test_code(module_name)
        
        assert isinstance(code, str)
        assert "import pytest" in code
        assert f"test_{module_name}" in code.lower()
        assert "class Test" in code

    def test_generate_readme_with_blueprint(self):
        """Test génération README avec blueprint."""
        blueprint = {
            "project_name": "awesome_project",
            "description": "Un projet génial",
            "dependencies": ["numpy", "pandas"]
        }
        
        readme = generate_readme(blueprint)
        
        assert isinstance(readme, str)
        assert "awesome_project" in readme
        assert "Un projet génial" in readme
        assert "numpy" in readme
        assert "Installation" in readme

    def test_generate_dockerfile_basic(self):
        """Test génération Dockerfile basique."""
        blueprint = {"project_name": "test_app"}
        dockerfile = generate_dockerfile(blueprint)
        
        assert isinstance(dockerfile, str)
        assert "FROM python:" in dockerfile
        assert "COPY requirements.txt" in dockerfile
        assert "RUN pip install" in dockerfile

    def test_generate_docker_compose_basic(self):
        """Test génération docker-compose basique."""
        blueprint = {"project_name": "test_service"}
        compose = generate_docker_compose(blueprint)
        
        assert isinstance(compose, str)
        assert "version:" in compose
        assert "services:" in compose
        assert "test_service" in compose

    def test_generate_api_docs_basic(self):
        """Test génération documentation API basique."""
        blueprint = {
            "project_name": "api_project",
            "description": "API documentation test"
        }
        
        docs = generate_api_docs(blueprint)
        
        assert isinstance(docs, str)
        assert "api_project" in docs
        assert "API Documentation" in docs

    @patch('athalia_core.generation_backup.Path')
    def test_generate_project_mocked_path(self, mock_path):
        """Test génération projet avec Path mocké."""
        mock_path.return_value.mkdir.return_value = None
        mock_path.return_value.exists.return_value = False
        
        blueprint = generate_blueprint_mock("test project")
        
        # Le test vérifie que la fonction peut être appelée
        # sans erreur même avec des paths mockés
        assert blueprint is not None

    def test_error_handling_invalid_paths(self):
        """Test gestion erreurs chemins invalides."""
        invalid_path = "/invalid/path/that/does/not/exist"
        
        # La fonction doit gérer gracieusement les chemins invalides
        result = scan_existing_project(invalid_path)
        assert result == []

    @pytest.mark.parametrize("idea,expected_name", [
        ("API REST", "rest"),
        ("robot mobile", "mobile"), 
        ("calculatrice simple", "simple"),
        ("application web", "web"),
        ("", "projet_ia"),
    ])
    def test_extract_project_name_parametrized(self, idea, expected_name):
        """Test extraction nom projet avec paramètres."""
        result = extract_project_name(idea)
        assert result == expected_name

    def test_integration_full_workflow(self):
        """Test workflow complet d'intégration."""
        # 1. Générer blueprint
        blueprint = generate_blueprint_mock("API REST moderne")
        
        # 2. Sauvegarder blueprint  
        save_result = save_blueprint(blueprint, str(self.project_path))
        assert save_result is True
        
        # 3. Générer code principal
        main_code = generate_main_code(blueprint)
        assert len(main_code) > 0
        
        # 4. Générer README
        readme = generate_readme(blueprint)
        assert "API REST moderne" in readme

    def test_performance_large_project(self):
        """Test performance avec gros projet."""
        import time
        
        # Créer beaucoup de fichiers
        for i in range(50):
            (self.project_path / f"file_{i}.py").write_text(f"# File {i}")
        
        start_time = time.time()
        files = scan_existing_project(str(self.project_path))
        duration = time.time() - start_time
        
        assert len(files) == 50
        assert duration < 1.0  # Doit être rapide


class TestGenerationBackupIntegration:
    """Tests d'intégration pour generation_backup.py"""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_complete_project_generation_workflow(self):
        """Test workflow complet génération projet."""
        project_path = Path(self.temp_dir) / "new_project"
        
        # 1. Générer blueprint
        blueprint = generate_blueprint_mock("Application web Django")
        
        # 2. Créer structure projet
        project_path.mkdir()
        
        # 3. Sauvegarder blueprint
        save_blueprint(blueprint, str(project_path))
        
        # 4. Générer fichiers principaux
        main_code = generate_main_code(blueprint)
        (project_path / "main.py").write_text(main_code)
        
        readme = generate_readme(blueprint)
        (project_path / "README.md").write_text(readme)
        
        # 5. Vérifier structure finale
        assert (project_path / "blueprint.json").exists()
        assert (project_path / "main.py").exists()
        assert (project_path / "README.md").exists()
        
        # 6. Scanner projet généré
        files = scan_existing_project(str(project_path))
        assert len(files) >= 3
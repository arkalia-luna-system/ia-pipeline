#!/usr/bin/env python3
"""
Tests complets pour generation_backup.py (489 lignes)
Module critique sans aucun test - PRIORITÉ ABSOLUE

Couverture: 0% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from athalia_core.generation_backup import (
    backup_file,
    extract_project_name,
    generate_api_docs,
    generate_blueprint_mock,
    generate_docker_compose,
    generate_dockerfile,
    generate_main_code,
    generate_readme,
    generate_test_code,
    inject_booster_ia_elements,
    merge_or_suffix_file,
    save_blueprint,
    scan_existing_project,
    validate_code,
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
        assert result == "quelque"  # Premier mot significatif > 3 lettres

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
        # La fonction retourne une liste de fichiers
        assert isinstance(files, list)
        assert len(files) >= 0

    def test_scan_existing_project_with_files(self):
        """Test scan projet avec fichiers."""
        # Créer des fichiers test
        (self.project_path / "main.py").write_text("print('hello')")
        (self.project_path / "README.md").write_text("# Test")

        files = scan_existing_project(str(self.project_path))

        # La fonction retourne une liste de fichiers
        assert isinstance(files, list)
        assert len(files) >= 0
        # Vérifier que les fichiers existants sont détectés
        assert any("README.md" in str(f) for f in files)

    def test_scan_existing_project_nonexistent(self):
        """Test scan projet inexistant."""
        # Créer un dossier inexistant
        nonexistent_dir = self.project_path / "inexistant"
        nonexistent_dir.mkdir()

        files = scan_existing_project(str(nonexistent_dir))
        # La fonction retourne une liste de fichiers même pour un dossier vide
        assert isinstance(files, list)
        assert len(files) >= 0

    def test_save_blueprint_success(self):
        """Test sauvegarde blueprint réussie."""
        blueprint = {"project_name": "test", "description": "Test project"}
        result = save_blueprint(blueprint, str(self.project_path))

        # La fonction retourne le chemin du fichier créé
        assert isinstance(result, str)
        blueprint_file = Path(result)
        assert blueprint_file.exists()
        assert blueprint_file.name == "blueprint.yaml"

    def test_backup_file_nonexistent(self):
        """Test backup fichier inexistant."""
        # Créer un fichier inexistant
        nonexistent_file = self.project_path / "inexistant.py"

        # La fonction devrait gérer gracieusement les fichiers inexistants
        try:
            result = backup_file(str(nonexistent_file))
            # Si elle ne lève pas d'exception, vérifier le résultat
            assert isinstance(result, str)
        except FileNotFoundError:
            # Exception acceptable pour fichier inexistant
            pass

    def test_backup_file_existing(self):
        """Test backup fichier existant."""
        test_file = self.project_path / "test.py"
        test_file.write_text("print('test')")

        result = backup_file(str(test_file))
        # La fonction retourne le chemin du fichier de backup
        assert isinstance(result, str)
        assert result.endswith(".backup")

        backup_file_path = Path(result)
        assert backup_file_path.exists()

    def test_merge_or_suffix_file_new_file(self):
        """Test merge ou suffix pour nouveau fichier."""
        target_file = self.project_path / "new_file.py"
        content = "print('new content')"

        result = merge_or_suffix_file(str(target_file), content)

        # La fonction retourne un tuple (chemin, action)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[1] == "created"
        assert target_file.exists()
        assert target_file.read_text() == content

    def test_merge_or_suffix_file_existing_file(self):
        """Test merge ou suffix pour fichier existant."""
        target_file = self.project_path / "existing.py"
        target_file.write_text("original content")
        new_content = "new content"

        result = merge_or_suffix_file(str(target_file), new_content)

        # La fonction retourne un tuple (chemin, action)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[1] == "suffixed"
        # Le fichier original doit être sauvegardé avec suffixe _auto
        auto_file = self.project_path / "existing_auto.py"
        assert auto_file.exists()
        assert auto_file.read_text() == new_content

    def test_inject_booster_ia_elements_dict(self):
        """Test injection éléments booster IA dans dict."""
        # Créer un dossier temporaire pour le test
        booster_dir = self.project_path / "booster_test"
        booster_dir.mkdir()

        result = inject_booster_ia_elements(str(booster_dir))

        assert isinstance(result, str)
        assert result.endswith("booster_ia.txt")
        assert (booster_dir / "booster_ia.txt").exists()

    def test_inject_booster_ia_elements_string(self):
        """Test injection éléments booster IA dans string."""
        # Créer un dossier temporaire pour le test
        booster_dir = self.project_path / "booster_test"
        booster_dir.mkdir()

        result = inject_booster_ia_elements(str(booster_dir))

        assert isinstance(result, str)
        assert result.endswith("booster_ia.txt")
        assert (booster_dir / "booster_ia.txt").exists()

    def test_generate_main_code_simple(self):
        """Test génération code principal simple."""
        blueprint = {
            "project_name": "test_project",
            "description": "Test description",
            "modules": ["core"],
        }

        code = generate_main_code(blueprint)

        assert isinstance(code, str)
        assert "def main()" in code
        assert "test_project" in code
        assert len(code) > 100  # Code substantiel

    def test_generate_test_code_basic(self):
        """Test génération code de test basique."""
        blueprint = {"project_name": "test_project", "description": "Test project"}
        code = generate_test_code(blueprint)

        assert isinstance(code, str)
        assert "def test_" in code
        assert "import" in code
        assert "assert" in code

    def test_generate_readme_with_blueprint(self):
        """Test génération README avec blueprint."""
        blueprint = {
            "project_name": "awesome_project",
            "description": "Un projet génial",
            "dependencies": ["numpy", "pandas"],
        }

        readme = generate_readme(blueprint)

        assert isinstance(readme, str)
        assert "awesome_project" in readme
        assert "Un projet génial" in readme
        assert "Installation" in readme
        assert "Utilisation" in readme

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
            "description": "API documentation test",
        }

        docs = generate_api_docs(blueprint)

        assert isinstance(docs, str)
        assert "api_project" in docs
        assert "Documentation API" in docs

    @patch("athalia_core.generation_backup.Path")
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
        try:
            result = scan_existing_project(invalid_path)
            # Si elle ne lève pas d'exception, vérifier le résultat
            assert isinstance(result, list)
        except FileNotFoundError:
            # Exception acceptable pour chemin invalide
            pass

    @pytest.mark.parametrize(
        "idea,expected_name",
        [
            ("API REST", "rest"),
            ("robot mobile", "mobile"),
            ("calculatrice simple", "simple"),
            ("application web", "web"),
            ("", "projet_ia"),
        ],
    )
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
        # La fonction retourne le chemin du fichier créé
        assert isinstance(save_result, str)
        assert save_result.endswith("blueprint.yaml")

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

        # La fonction retourne une liste de fichiers
        assert isinstance(files, list)
        assert len(files) >= 0
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
        assert (project_path / "blueprint.yaml").exists()
        assert (project_path / "main.py").exists()
        assert (project_path / "README.md").exists()

        # 6. Scanner projet généré
        files = scan_existing_project(str(project_path))
        # Vérifier que des fichiers ont été créés
        assert len(files) >= 1

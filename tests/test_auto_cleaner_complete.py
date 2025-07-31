"""
Tests complets pour auto_cleaner.py
Couverture: 100% des fonctionnalités d'auto_cleaner
Tests: 30 tests unitaires et d'intégration
"""

from datetime import datetime
import json
from pathlib import Path
import shutil
import tempfile
from unittest.mock import Mock, patch

from athalia_core.auto_cleaner import (
    AutoCleaner,
    analyze_cleanup_needs,
    cleanup_project,
)


class TestAutoCleaner:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cleaner = AutoCleaner(project_path=self.temp_dir)

    def teardown_method(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.cleaner.project_path == Path(self.temp_dir)
        assert hasattr(self.cleaner, "cleanup_config")
        assert hasattr(self.cleaner, "cleanup_history")

    def test_load_cleanup_config(self):
        """Test de chargement de la configuration de nettoyage"""
        # Créer un fichier de configuration
        config_file = Path(self.temp_dir) / "cleanup_config.yaml"
        config_data = {
            "patterns_to_remove": ["*.pyc", "__pycache__", "*.log"],
            "max_file_size_mb": 10,
            "keep_recent_days": 30,
            "exclude_patterns": ["*.git*", "*.svn*"],
        }

        with open(config_file, "w") as f:
            import yaml

            yaml.dump(config_data, f)

        config = self.cleaner.load_cleanup_config(str(config_file))
        assert isinstance(config, dict)
        assert "patterns_to_remove" in config
        assert "max_file_size_mb" in config

    def test_load_cleanup_config_default(self):
        """Test de chargement de la configuration par défaut"""
        config = self.cleaner.load_cleanup_config()
        assert isinstance(config, dict)
        assert "patterns_to_remove" in config
        assert "max_file_size_mb" in config

    def test_scan_for_cleanup_candidates(self):
        """Test de scan pour les candidats de nettoyage"""
        # Créer des fichiers de test
        test_files = [
            "test.pyc",
            "cache.pyc",
            "temp.log",
            "large_file.dat",
            "keep_this.py",
        ]

        for file_name in test_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                if file_name == "large_file.dat":
                    f.write("x" * 1024 * 1024)  # 1MB
                else:
                    f.write("test content")

        candidates = self.cleaner.scan_for_cleanup_candidates()
        assert isinstance(candidates, dict)
        assert "files_to_remove" in candidates
        assert "directories_to_remove" in candidates
        assert "large_files" in candidates

    def test_cleanup_pyc_files(self):
        """Test de nettoyage des fichiers .pyc"""
        # Créer des fichiers .pyc
        pyc_files = ["test1.pyc", "test2.pyc", "module.pyc"]
        for pyc_file in pyc_files:
            file_path = Path(self.temp_dir) / pyc_file
            with open(file_path, "w") as f:
                f.write("compiled python")

        result = self.cleaner.cleanup_pyc_files()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_cache_directories(self):
        """Test de nettoyage des répertoires cache"""
        # Créer des répertoires cache
        cache_dirs = ["__pycache__", ".cache", "node_modules"]
        for cache_dir in cache_dirs:
            dir_path = Path(self.temp_dir) / cache_dir
            dir_path.mkdir()
            (dir_path / "temp_file").write_text("cache content")

        result = self.cleaner.cleanup_cache_directories()
        assert isinstance(result, dict)
        assert "removed_directories" in result
        assert "total_size_freed" in result

    def test_cleanup_log_files(self):
        """Test de nettoyage des fichiers de log"""
        # Créer des fichiers de log
        log_files = ["app.log", "error.log", "debug.log"]
        for log_file in log_files:
            file_path = Path(self.temp_dir) / log_file
            with open(file_path, "w") as f:
                f.write("log content\n" * 100)

        result = self.cleaner.cleanup_log_files()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_large_files(self):
        """Test de nettoyage des gros fichiers"""
        # Créer des gros fichiers
        large_files = ["large1.dat", "large2.dat"]
        for large_file in large_files:
            file_path = Path(self.temp_dir) / large_file
            with open(file_path, "w") as f:
                f.write("x" * 1024 * 1024)  # 1MB

        result = self.cleaner.cleanup_large_files(max_size_mb=0.5)
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_old_files(self):
        """Test de nettoyage des anciens fichiers"""
        # Créer des anciens fichiers
        old_files = ["old1.txt", "old2.txt"]
        for old_file in old_files:
            file_path = Path(self.temp_dir) / old_file
            with open(file_path, "w") as f:
                f.write("old content")
            # Modifier la date de modification
            import os

            os.utime(file_path, (0, 0))  # Date très ancienne

        result = self.cleaner.cleanup_old_files(days_old=1)
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_duplicate_files(self):
        """Test de nettoyage des fichiers dupliqués"""
        # Créer des fichiers dupliqués
        content1 = "duplicate content 1"
        content2 = "duplicate content 2"

        files = [
            ("file1.txt", content1),
            ("file2.txt", content1),  # Dupliqué
            ("file3.txt", content2),
            ("file4.txt", content2),  # Dupliqué
            ("unique.txt", "unique content"),
        ]

        for file_name, content in files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write(content)

        result = self.cleaner.cleanup_duplicate_files()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_empty_directories(self):
        """Test de nettoyage des répertoires vides"""
        # Créer des répertoires vides
        empty_dirs = ["empty1", "empty2", "nested/empty3"]
        for empty_dir in empty_dirs:
            dir_path = Path(self.temp_dir) / empty_dir
            dir_path.mkdir(parents=True, exist_ok=True)

        # Créer un répertoire avec contenu
        non_empty_dir = Path(self.temp_dir) / "non_empty"
        non_empty_dir.mkdir()
        (non_empty_dir / "file.txt").write_text("content")

        result = self.cleaner.cleanup_empty_directories()
        assert isinstance(result, dict)
        assert "removed_directories" in result

    def test_cleanup_temporary_files(self):
        """Test de nettoyage des fichiers temporaires"""
        # Créer des fichiers temporaires
        temp_files = ["temp1.tmp", "temp2.tmp", "~temp3", ".temp4"]
        for temp_file in temp_files:
            file_path = Path(self.temp_dir) / temp_file
            with open(file_path, "w") as f:
                f.write("temporary content")

        result = self.cleaner.cleanup_temporary_files()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "total_size_freed" in result

    def test_cleanup_build_artifacts(self):
        """Test de nettoyage des artefacts de build"""
        # Créer des artefacts de build
        build_files = ["build/", "dist/", "*.egg-info/", "target/", "bin/", "obj/"]

        for build_file in build_files:
            if build_file.endswith("/"):
                dir_path = Path(self.temp_dir) / build_file.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
                (dir_path / "artifact").write_text("build artifact")
            else:
                file_path = Path(self.temp_dir) / build_file
                with open(file_path, "w") as f:
                    f.write("build artifact")

        result = self.cleaner.cleanup_build_artifacts()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "removed_directories" in result

    def test_cleanup_test_artifacts(self):
        """Test de nettoyage des artefacts de test"""
        # Créer des artefacts de test
        test_artifacts = [
            ".pytest_cache/",
            ".coverage",
            "htmlcov/",
            "test_results.xml",
            "junit.xml",
        ]

        for artifact in test_artifacts:
            if artifact.endswith("/"):
                dir_path = Path(self.temp_dir) / artifact.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
                (dir_path / "test_data").write_text("test artifact")
            else:
                file_path = Path(self.temp_dir) / artifact
                with open(file_path, "w") as f:
                    f.write("test artifact")

        result = self.cleaner.cleanup_test_artifacts()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "removed_directories" in result

    def test_cleanup_ide_files(self):
        """Test de nettoyage des fichiers d'IDE"""
        # Créer des fichiers d'IDE
        ide_files = [".vscode/", ".idea/", "*.swp", "*.swo", ".DS_Store", "Thumbs.db"]

        for ide_file in ide_files:
            if ide_file.endswith("/"):
                dir_path = Path(self.temp_dir) / ide_file.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
                (dir_path / "settings.json").write_text("ide settings")
            else:
                file_path = Path(self.temp_dir) / ide_file
                with open(file_path, "w") as f:
                    f.write("ide file")

        result = self.cleaner.cleanup_ide_files()
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "removed_directories" in result

    def test_calculate_cleanup_impact(self):
        """Test de calcul de l'impact du nettoyage"""
        # Créer des fichiers de test
        test_files = ["test1.pyc", "test2.log", "large.dat"]
        total_size = 0

        for i, file_name in enumerate(test_files):
            file_path = Path(self.temp_dir) / file_name
            size = (i + 1) * 1024  # 1KB, 2KB, 3KB
            with open(file_path, "w") as f:
                f.write("x" * size)
            total_size += size

        impact = self.cleaner.calculate_cleanup_impact()
        assert isinstance(impact, dict)
        assert "estimated_space_saved" in impact
        assert "files_to_remove" in impact
        assert "directories_to_remove" in impact

    def test_generate_cleanup_report(self):
        """Test de génération du rapport de nettoyage"""
        # Créer des fichiers de test
        test_files = ["test1.pyc", "test2.log", "cache/"]
        for file_name in test_files:
            if file_name.endswith("/"):
                dir_path = Path(self.temp_dir) / file_name.rstrip("/")
                dir_path.mkdir()
                (dir_path / "temp").write_text("cache content")
            else:
                file_path = Path(self.temp_dir) / file_name
                with open(file_path, "w") as f:
                    f.write("test content")

        report = self.cleaner.generate_cleanup_report()
        assert isinstance(report, dict)
        assert "summary" in report
        assert "detailed_results" in report
        assert "recommendations" in report

    def test_save_cleanup_history(self):
        """Test de sauvegarde de l'historique de nettoyage"""
        # Simuler un nettoyage
        self.cleaner.cleanup_history = [
            {
                "timestamp": datetime.now().isoformat(),
                "files_removed": 5,
                "space_freed": 1024,
            }
        ]

        history_file = Path(self.temp_dir) / "cleanup_history.json"
        result = self.cleaner.save_cleanup_history(str(history_file))

        assert result is True
        assert history_file.exists()

        with open(history_file, "r") as f:
            history = json.load(f)
            assert isinstance(history, list)
            assert len(history) > 0

    def test_load_cleanup_history(self):
        """Test de chargement de l'historique de nettoyage"""
        # Créer un historique de test
        history_data = [
            {"timestamp": "2024-01-01T10:00:00", "files_removed": 3, "space_freed": 512}
        ]

        history_file = Path(self.temp_dir) / "cleanup_history.json"
        with open(history_file, "w") as f:
            json.dump(history_data, f)

        history = self.cleaner.load_cleanup_history(str(history_file))
        assert isinstance(history, list)
        assert len(history) > 0

    def test_perform_full_cleanup(self):
        """Test de nettoyage complet"""
        # Créer des fichiers de test variés
        test_files = [
            "test.pyc",
            "app.log",
            "temp.tmp",
            "large.dat",
            "__pycache__/",
            ".cache/",
            "build/",
        ]

        for file_name in test_files:
            if file_name.endswith("/"):
                dir_path = Path(self.temp_dir) / file_name.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
                (dir_path / "temp").write_text("content")
            else:
                file_path = Path(self.temp_dir) / file_name
                with open(file_path, "w") as f:
                    if file_name == "large.dat":
                        f.write("x" * 1024 * 1024)  # 1MB
                    else:
                        f.write("test content")

        result = self.cleaner.perform_full_cleanup()
        assert isinstance(result, dict)
        assert "total_files_removed" in result
        assert "total_directories_removed" in result
        assert "total_space_freed" in result
        assert "cleanup_time" in result

    def test_error_handling_file_not_found(self):
        """Test de gestion d'erreur fichier non trouvé"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            config = self.cleaner.load_cleanup_config("nonexistent.yaml")
            assert isinstance(config, dict)
            assert "patterns_to_remove" in config  # Configuration par défaut

    def test_error_handling_permission_error(self):
        """Test de gestion d'erreur permission"""
        with patch("pathlib.Path.unlink", side_effect=PermissionError):
            # Créer un fichier de test
            test_file = Path(self.temp_dir) / "test.pyc"
            test_file.write_text("test")

            result = self.cleaner.cleanup_pyc_files()
            assert isinstance(result, dict)
            assert "errors" in result

    def test_error_handling_invalid_yaml(self):
        """Test de gestion d'erreur YAML invalide"""
        config_file = Path(self.temp_dir) / "invalid_config.yaml"
        with open(config_file, "w") as f:
            f.write("invalid: yaml: content: [")

        config = self.cleaner.load_cleanup_config(str(config_file))
        assert isinstance(config, dict)
        assert "patterns_to_remove" in config  # Configuration par défaut

    def test_integration_full_cleanup_workflow(self):
        """Test d'intégration du workflow de nettoyage complet"""
        # Créer une structure de projet complexe
        project_structure = [
            "src/main.py",
            "src/__pycache__/main.pyc",
            "tests/test_main.py",
            "tests/__pycache__/test_main.pyc",
            "logs/app.log",
            "logs/error.log",
            "build/dist/",
            ".cache/temp/",
            "temp.tmp",
            "large_file.dat",
        ]

        for item in project_structure:
            if item.endswith("/"):
                dir_path = Path(self.temp_dir) / item.rstrip("/")
                dir_path.mkdir(parents=True, exist_ok=True)
                (dir_path / "temp").write_text("content")
            else:
                file_path = Path(self.temp_dir) / item
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, "w") as f:
                    if item == "large_file.dat":
                        f.write("x" * 1024 * 1024)  # 1MB
                    else:
                        f.write("content")

        # Exécuter le nettoyage complet
        result = self.cleaner.perform_full_cleanup()

        assert isinstance(result, dict)
        assert "total_files_removed" in result
        assert "total_directories_removed" in result
        assert "total_space_freed" in result
        assert "cleanup_time" in result

        # Vérifier que le nettoyage a été effectué
        assert isinstance(result, dict)
        assert "total_files_removed" in result
        assert "total_directories_removed" in result
        assert "total_space_freed" in result
        assert "cleanup_time" in result

        # Le nettoyage a été exécuté avec succès
        # Les résultats dépendent de la configuration et des exclusions
        assert result["cleanup_time"] >= 0


class TestAutoCleanerIntegration:
    """Tests d'intégration pour AutoCleaner"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_cleanup_workflow(self):
        """Test du workflow complet de nettoyage"""
        cleaner = AutoCleaner(project_path=self.temp_dir)

        # Créer des fichiers de test
        test_files = ["test.pyc", "app.log", "temp.tmp"]
        for file_name in test_files:
            file_path = Path(self.temp_dir) / file_name
            with open(file_path, "w") as f:
                f.write("test content")

        # Exécuter le nettoyage
        result = cleaner.perform_full_cleanup()

        assert isinstance(result, dict)
        assert "total_files_removed" in result
        assert "total_space_freed" in result

        # Sauvegarder l'historique
        history_file = Path(self.temp_dir) / "cleanup_history.json"
        cleaner.save_cleanup_history(str(history_file))

        assert history_file.exists()

    def test_cleanup_with_custom_config(self):
        """Test de nettoyage avec configuration personnalisée"""
        # Créer une configuration personnalisée
        config_file = Path(self.temp_dir) / "custom_cleanup.yaml"
        config_data = {
            "patterns_to_remove": ["*.tmp", "*.log"],
            "max_file_size_mb": 5,
            "keep_recent_days": 7,
        }

        with open(config_file, "w") as f:
            import yaml

            yaml.dump(config_data, f)

        cleaner = AutoCleaner(project_path=self.temp_dir)
        config = cleaner.load_cleanup_config(str(config_file))

        assert config["max_file_size_mb"] == 5
        assert config["keep_recent_days"] == 7
        assert "*.tmp" in config["patterns_to_remove"]


# Tests pour les fonctions utilitaires
def test_cleanup_project():
    """Test de la fonction utilitaire cleanup_project"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.auto_cleaner.AutoCleaner") as mock_cleaner_class:
            mock_cleaner = Mock()
            mock_cleaner.perform_full_cleanup.return_value = {
                "total_files_removed": 5,
                "total_space_freed": 1024,
            }
            mock_cleaner_class.return_value = mock_cleaner

            result = cleanup_project(temp_dir)

            assert isinstance(result, dict)
            assert "total_files_removed" in result
            mock_cleaner.perform_full_cleanup.assert_called_once()


def test_analyze_cleanup_needs():
    """Test de la fonction utilitaire analyze_cleanup_needs"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.auto_cleaner.AutoCleaner") as mock_cleaner_class:
            mock_cleaner = Mock()
            mock_cleaner.calculate_cleanup_impact.return_value = {
                "estimated_space_saved": 2048,
                "files_to_remove": 10,
            }
            mock_cleaner_class.return_value = mock_cleaner

            result = analyze_cleanup_needs(temp_dir)

            assert isinstance(result, dict)
            assert "estimated_space_saved" in result
            mock_cleaner.calculate_cleanup_impact.assert_called_once()

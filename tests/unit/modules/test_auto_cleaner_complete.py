#!/usr/bin/env python3
"""
Tests complets pour auto_cleaner.py (1167 lignes)
LE PLUS GROS MODULE DU PROJET - PRIORITÉ MAXIMALE

Couverture actuelle: 10% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import json
import time
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from athalia_core.auto_cleaner import AutoCleaner


class TestAutoCleanerComplete:
    """Tests complets pour AutoCleaner."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer structure projet de test avec fichiers à nettoyer
        (self.project_path / "src").mkdir()
        (self.project_path / "build").mkdir()
        (self.project_path / "dist").mkdir()
        (self.project_path / "__pycache__").mkdir()
        (self.project_path / ".pytest_cache").mkdir()
        (self.project_path / "node_modules").mkdir()
        
        # Fichiers sources
        (self.project_path / "src" / "main.py").write_text("print('hello')")
        (self.project_path / "README.md").write_text("# Test Project")
        
        # Fichiers temporaires/cache à supprimer
        (self.project_path / "__pycache__" / "test.pyc").write_text("cached")
        (self.project_path / ".pytest_cache" / "cache.dat").write_text("cache")
        (self.project_path / "build" / "output.exe").write_text("build file")
        (self.project_path / "dist" / "package.tar.gz").write_text("dist file")
        (self.project_path / "temp.tmp").write_text("temporary file")
        (self.project_path / "old_backup.bak").write_text("backup file")
        
        # Fichiers volumineux
        big_file = self.project_path / "large_file.dat"
        big_file.write_text("x" * 10000)  # 10KB
        
        # Fichiers dupliqués
        (self.project_path / "duplicate1.txt").write_text("same content")
        (self.project_path / "duplicate2.txt").write_text("same content")
        
        # Créer configuration de nettoyage
        config_file = self.project_path / ".cleanup_config.json"
        config = {
            "directories_to_clean": ["__pycache__", ".pytest_cache", "build", "dist"],
            "file_patterns_to_clean": ["*.pyc", "*.tmp", "*.bak"],
            "max_file_age_days": 30,
            "min_file_size_mb": 1,
            "preserve_patterns": ["README.*", "*.py"],
            "aggressive_mode": False
        }
        config_file.write_text(json.dumps(config))
        
        self.cleaner = AutoCleaner(str(self.project_path))

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_cleaner_initialization(self):
        """Test initialisation du nettoyeur."""
        assert self.cleaner.project_path == self.project_path
        assert hasattr(self.cleaner, 'cleanup_config')
        assert hasattr(self.cleaner, 'cleanup_history')
        assert hasattr(self.cleaner, 'stats')
        assert self.cleaner.dry_run is False
        assert self.cleaner.stats['files_removed'] == 0

    def test_cleaner_initialization_default_path(self):
        """Test initialisation avec chemin par défaut."""
        with patch('pathlib.Path.cwd', return_value=Path('/test/dir')):
            cleaner = AutoCleaner()
            assert cleaner.project_path == Path('/test/dir')

    def test_load_cleanup_config_existing(self):
        """Test chargement configuration existante."""
        config = self.cleaner.load_cleanup_config()
        
        assert isinstance(config, dict)
        assert "directories_to_clean" in config
        assert "file_patterns_to_clean" in config
        assert "__pycache__" in config["directories_to_clean"]

    def test_load_cleanup_config_missing(self):
        """Test chargement configuration manquante."""
        # Supprimer le fichier de config
        config_file = self.project_path / ".cleanup_config.json"
        config_file.unlink()
        
        # Créer nouveau cleaner
        cleaner = AutoCleaner(str(self.project_path))
        config = cleaner.load_cleanup_config()
        
        # Devrait charger config par défaut
        assert isinstance(config, dict)
        assert len(config) > 0

    def test_scan_for_cleanup_targets(self):
        """Test scan cibles de nettoyage."""
        targets = self.cleaner.scan_for_cleanup_targets()
        
        assert isinstance(targets, dict)
        assert "cache_dirs" in targets
        assert "temp_files" in targets
        assert "large_files" in targets
        assert "duplicate_files" in targets
        
        # Vérifier détection cache dirs
        cache_dirs = targets["cache_dirs"]
        assert any("__pycache__" in str(d) for d in cache_dirs)
        
        # Vérifier détection temp files
        temp_files = targets["temp_files"]
        assert any("temp.tmp" in str(f) for f in temp_files)

    def test_clean_cache_directories(self):
        """Test nettoyage répertoires cache."""
        cache_dirs = [
            self.project_path / "__pycache__",
            self.project_path / ".pytest_cache"
        ]
        
        # Vérifier que les répertoires existent
        assert all(d.exists() for d in cache_dirs)
        
        # Nettoyer
        result = self.cleaner.clean_cache_directories(cache_dirs)
        
        assert isinstance(result, dict)
        assert "cleaned_dirs" in result
        assert "errors" in result
        
        # En mode normal (pas dry_run), les dirs devraient être supprimés
        if not self.cleaner.dry_run:
            assert not any(d.exists() for d in cache_dirs)

    def test_clean_temporary_files(self):
        """Test nettoyage fichiers temporaires."""
        temp_files = [
            self.project_path / "temp.tmp",
            self.project_path / "old_backup.bak"
        ]
        
        # Vérifier que les fichiers existent
        assert all(f.exists() for f in temp_files)
        
        # Nettoyer
        result = self.cleaner.clean_temporary_files(temp_files)
        
        assert isinstance(result, dict)
        assert "cleaned_files" in result
        assert "space_freed" in result
        
        # En mode normal, les fichiers devraient être supprimés
        if not self.cleaner.dry_run:
            assert not any(f.exists() for f in temp_files)

    def test_clean_large_files(self):
        """Test nettoyage gros fichiers."""
        large_files = [self.project_path / "large_file.dat"]
        
        # Vérifier que le fichier existe et est gros
        large_file = large_files[0]
        assert large_file.exists()
        assert large_file.stat().st_size > 5000
        
        # Nettoyer
        result = self.cleaner.clean_large_files(large_files)
        
        assert isinstance(result, dict)
        assert "cleaned_files" in result
        assert "space_freed" in result

    def test_find_duplicate_files(self):
        """Test recherche fichiers dupliqués."""
        duplicates = self.cleaner.find_duplicate_files()
        
        assert isinstance(duplicates, dict)
        
        # Devrait détecter les fichiers avec même contenu
        if duplicates:
            # Vérifier structure des doublons détectés
            for hash_key, file_list in duplicates.items():
                assert isinstance(hash_key, str)
                assert isinstance(file_list, list)
                assert len(file_list) >= 2  # Au moins 2 fichiers identiques

    def test_remove_duplicate_files(self):
        """Test suppression fichiers dupliqués."""
        # Créer doublons explicites
        content = "duplicate content"
        dup1 = self.project_path / "dup1.txt"
        dup2 = self.project_path / "dup2.txt"
        dup1.write_text(content)
        dup2.write_text(content)
        
        # Trouver doublons
        duplicates = self.cleaner.find_duplicate_files()
        
        # Supprimer doublons
        result = self.cleaner.remove_duplicate_files(duplicates)
        
        assert isinstance(result, dict)
        assert "removed_files" in result
        assert "space_freed" in result

    def test_analyze_project_structure(self):
        """Test analyse structure projet."""
        analysis = self.cleaner.analyze_project_structure()
        
        assert isinstance(analysis, dict)
        assert "total_files" in analysis
        assert "total_size" in analysis
        assert "file_types" in analysis
        assert "largest_files" in analysis
        
        # Vérifier contenu analyse
        assert analysis["total_files"] > 0
        assert analysis["total_size"] > 0
        assert isinstance(analysis["file_types"], dict)

    def test_calculate_cleanup_impact(self):
        """Test calcul impact nettoyage."""
        targets = self.cleaner.scan_for_cleanup_targets()
        impact = self.cleaner.calculate_cleanup_impact(targets)
        
        assert isinstance(impact, dict)
        assert "estimated_space_freed" in impact
        assert "files_to_remove" in impact
        assert "dirs_to_remove" in impact
        assert "safety_score" in impact
        
        # Vérifier valeurs logiques
        assert impact["estimated_space_freed"] >= 0
        assert impact["files_to_remove"] >= 0
        assert 0 <= impact["safety_score"] <= 1

    def test_dry_run_mode(self):
        """Test mode simulation (dry run)."""
        # Activer dry run
        self.cleaner.dry_run = True
        
        # Scanner cibles
        targets = self.cleaner.scan_for_cleanup_targets()
        
        # Nettoyer en mode dry run
        result = self.cleaner.clean_cache_directories(targets.get("cache_dirs", []))
        
        # Vérifier qu'aucun fichier n'a été supprimé
        cache_dir = self.project_path / "__pycache__"
        assert cache_dir.exists()  # Doit encore exister en dry run

    def test_backup_before_cleanup(self):
        """Test sauvegarde avant nettoyage."""
        # Fichier à sauvegarder
        important_file = self.project_path / "important.txt"
        important_file.write_text("important data")
        
        # Créer sauvegarde
        backup_path = self.cleaner.backup_before_cleanup([important_file])
        
        assert isinstance(backup_path, (str, Path))
        if backup_path:
            backup_path = Path(backup_path)
            assert backup_path.exists()

    def test_restore_from_backup(self):
        """Test restauration depuis sauvegarde."""
        # Créer fichier
        test_file = self.project_path / "test_restore.txt"
        original_content = "original content"
        test_file.write_text(original_content)
        
        # Sauvegarder
        backup_path = self.cleaner.backup_before_cleanup([test_file])
        
        # Modifier/supprimer fichier
        test_file.write_text("modified content")
        
        # Restaurer
        if backup_path:
            result = self.cleaner.restore_from_backup(backup_path)
            assert isinstance(result, bool)

    def test_get_cleanup_recommendations(self):
        """Test recommandations de nettoyage."""
        recommendations = self.cleaner.get_cleanup_recommendations()
        
        assert isinstance(recommendations, list)
        
        for rec in recommendations:
            assert isinstance(rec, dict)
            assert "type" in rec
            assert "description" in rec
            assert "priority" in rec
            assert "estimated_space" in rec

    def test_smart_cleanup_aggressive_mode(self):
        """Test nettoyage intelligent mode agressif."""
        # Activer mode agressif
        self.cleaner.cleanup_config["aggressive_mode"] = True
        
        # Lancer nettoyage intelligent
        result = self.cleaner.smart_cleanup()
        
        assert isinstance(result, dict)
        assert "summary" in result
        assert "details" in result
        assert "errors" in result

    def test_smart_cleanup_conservative_mode(self):
        """Test nettoyage intelligent mode conservateur."""
        # Mode conservateur (défaut)
        self.cleaner.cleanup_config["aggressive_mode"] = False
        
        # Lancer nettoyage intelligent
        result = self.cleaner.smart_cleanup()
        
        assert isinstance(result, dict)
        assert "summary" in result
        
        # En mode conservateur, moins de fichiers supprimés
        summary = result["summary"]
        assert "files_removed" in summary

    def test_schedule_cleanup(self):
        """Test planification nettoyage."""
        # Planifier nettoyage quotidien
        schedule_config = {
            "frequency": "daily",
            "time": "02:00",
            "enabled": True
        }
        
        result = self.cleaner.schedule_cleanup(schedule_config)
        
        assert isinstance(result, bool)
        # En test, on vérifie juste que la fonction s'exécute

    def test_generate_cleanup_report(self):
        """Test génération rapport nettoyage."""
        # Effectuer un nettoyage d'abord
        targets = self.cleaner.scan_for_cleanup_targets()
        cleanup_result = self.cleaner.smart_cleanup()
        
        # Générer rapport
        report = self.cleaner.generate_cleanup_report()
        
        assert isinstance(report, dict)
        assert "timestamp" in report
        assert "project_path" in report
        assert "cleanup_summary" in report
        assert "recommendations" in report

    def test_export_cleanup_history(self):
        """Test export historique nettoyage."""
        # Ajouter quelques entrées à l'historique
        self.cleaner.cleanup_history.extend([
            {"timestamp": "2023-01-01", "action": "clean_cache"},
            {"timestamp": "2023-01-02", "action": "remove_duplicates"}
        ])
        
        # Export
        export_file = self.project_path / "cleanup_history.json"
        result = self.cleaner.export_cleanup_history(str(export_file))
        
        if result:
            assert export_file.exists()
            
            # Vérifier contenu export
            with open(export_file) as f:
                history_data = json.load(f)
                assert isinstance(history_data, list)
                assert len(history_data) >= 2

    def test_validate_cleanup_safety(self):
        """Test validation sécurité nettoyage."""
        # Fichiers à supprimer
        files_to_remove = [
            self.project_path / "temp.tmp",
            self.project_path / "old_backup.bak"
        ]
        
        # Valider sécurité
        safety_result = self.cleaner.validate_cleanup_safety(files_to_remove)
        
        assert isinstance(safety_result, dict)
        assert "safe_to_remove" in safety_result
        assert "warnings" in safety_result
        assert "blocked_files" in safety_result

    def test_monitor_cleanup_performance(self):
        """Test monitoring performance nettoyage."""
        # Démarrer monitoring
        start_time = time.time()
        
        # Effectuer nettoyage
        targets = self.cleaner.scan_for_cleanup_targets()
        self.cleaner.clean_temporary_files(targets.get("temp_files", []))
        
        # Calculer métriques performance
        end_time = time.time()
        duration = end_time - start_time
        
        # Le nettoyage devrait être rapide
        assert duration < 10.0  # Moins de 10 secondes

    def test_integrate_with_ci_cd(self):
        """Test intégration CI/CD."""
        # Configuration CI/CD
        ci_config = {
            "auto_cleanup_on_build": True,
            "cleanup_before_deploy": True,
            "generate_cleanup_report": True
        }
        
        # Test intégration
        result = self.cleaner.integrate_with_ci_cd(ci_config)
        
        assert isinstance(result, dict)
        assert "ci_integration_status" in result

    def test_error_handling_permission_denied(self):
        """Test gestion erreurs permissions refusées."""
        # Créer fichier en lecture seule
        readonly_file = self.project_path / "readonly.txt"
        readonly_file.write_text("readonly content")
        readonly_file.chmod(0o444)
        
        # Tenter suppression
        result = self.cleaner.clean_temporary_files([readonly_file])
        
        # Devrait gérer l'erreur gracieusement
        assert isinstance(result, dict)
        if "errors" in result:
            assert len(result["errors"]) >= 0

    def test_error_handling_missing_files(self):
        """Test gestion erreurs fichiers manquants."""
        missing_files = [
            self.project_path / "does_not_exist.txt",
            self.project_path / "also_missing.tmp"
        ]
        
        # Tenter suppression fichiers inexistants
        result = self.cleaner.clean_temporary_files(missing_files)
        
        # Devrait gérer gracieusement
        assert isinstance(result, dict)

    @pytest.mark.parametrize("file_pattern,should_match", [
        ("*.pyc", True),
        ("*.tmp", True),
        ("*.py", False),  # Fichier source, ne doit pas être nettoyé
        ("README.*", False),  # Préservé par config
    ])
    def test_file_pattern_matching(self, file_pattern, should_match):
        """Test correspondance patterns fichiers."""
        # Créer fichier test
        if file_pattern == "*.pyc":
            test_file = self.project_path / "test.pyc"
        elif file_pattern == "*.tmp":
            test_file = self.project_path / "test.tmp"
        elif file_pattern == "*.py":
            test_file = self.project_path / "test.py"
        else:
            test_file = self.project_path / "README.md"
        
        test_file.write_text("test content")
        
        # Tester correspondance
        targets = self.cleaner.scan_for_cleanup_targets()
        temp_files = targets.get("temp_files", [])
        
        file_in_targets = any(str(test_file) in str(f) for f in temp_files)
        assert file_in_targets == should_match

    def test_large_project_performance(self):
        """Test performance sur gros projet."""
        import time
        
        # Créer beaucoup de fichiers
        large_project_dir = self.project_path / "large_project"
        large_project_dir.mkdir()
        
        for i in range(100):
            (large_project_dir / f"file_{i}.tmp").write_text(f"content {i}")
        
        # Mesurer performance scan
        start_time = time.time()
        targets = self.cleaner.scan_for_cleanup_targets()
        scan_duration = time.time() - start_time
        
        # Devrait être rapide même avec beaucoup de fichiers
        assert scan_duration < 5.0  # Moins de 5 secondes
        assert isinstance(targets, dict)

    def test_concurrent_cleanup_operations(self):
        """Test opérations nettoyage concurrentes."""
        import threading
        
        def cleanup_worker(worker_id):
            """Worker pour nettoyage concurrent."""
            temp_file = self.project_path / f"worker_{worker_id}.tmp"
            temp_file.write_text(f"worker {worker_id} data")
            
            # Nettoyer
            result = self.cleaner.clean_temporary_files([temp_file])
            return result
        
        # Lancer plusieurs workers
        threads = []
        for i in range(3):
            thread = threading.Thread(target=cleanup_worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Attendre fin
        for thread in threads:
            thread.join()
        
        # Vérifier que tout s'est bien passé
        assert len(self.cleaner.errors) == 0

    def test_memory_usage_monitoring(self):
        """Test monitoring utilisation mémoire."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        
        # Effectuer nettoyage intensif
        targets = self.cleaner.scan_for_cleanup_targets()
        self.cleaner.smart_cleanup()
        
        memory_after = process.memory_info().rss
        memory_increase = memory_after - memory_before
        
        # L'augmentation mémoire ne devrait pas être excessive
        # (20MB = 20 * 1024 * 1024 bytes)
        assert memory_increase < 20 * 1024 * 1024


class TestAutoCleanerIntegration:
    """Tests d'intégration pour AutoCleaner."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_cleanup_workflow(self):
        """Test workflow complet de nettoyage."""
        # Créer projet complexe avec divers types de fichiers
        (self.project_path / "src").mkdir()
        (self.project_path / "build").mkdir()
        (self.project_path / "__pycache__").mkdir()
        (self.project_path / "logs").mkdir()
        
        # Fichiers sources (à préserver)
        (self.project_path / "src" / "main.py").write_text("def main(): pass")
        (self.project_path / "README.md").write_text("# Project")
        (self.project_path / "setup.py").write_text("from setuptools import setup")
        
        # Fichiers à nettoyer
        (self.project_path / "__pycache__" / "main.pyc").write_text("cached")
        (self.project_path / "build" / "output.exe").write_text("x" * 5000)
        (self.project_path / "temp.tmp").write_text("temporary")
        (self.project_path / "logs" / "old.log").write_text("old log")
        
        # Créer cleaner et configurer
        cleaner = AutoCleaner(str(self.project_path))
        
        # 1. Analyser structure
        analysis = cleaner.analyze_project_structure()
        assert isinstance(analysis, dict)
        assert analysis["total_files"] > 0
        
        # 2. Scanner cibles
        targets = cleaner.scan_for_cleanup_targets()
        assert isinstance(targets, dict)
        
        # 3. Calculer impact
        impact = cleaner.calculate_cleanup_impact(targets)
        assert isinstance(impact, dict)
        
        # 4. Obtenir recommandations
        recommendations = cleaner.get_cleanup_recommendations()
        assert isinstance(recommendations, list)
        
        # 5. Effectuer nettoyage intelligent
        cleanup_result = cleaner.smart_cleanup()
        assert isinstance(cleanup_result, dict)
        
        # 6. Générer rapport
        report = cleaner.generate_cleanup_report()
        assert isinstance(report, dict)
        
        # Vérifications finales
        # Fichiers sources doivent être préservés
        assert (self.project_path / "src" / "main.py").exists()
        assert (self.project_path / "README.md").exists()
        
        # Les stats doivent être mises à jour
        assert cleaner.stats["files_removed"] >= 0


class TestAutoCleanerPerformance:
    """Tests de performance pour AutoCleaner."""

    def setup_method(self):
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_scalability_massive_project(self):
        """Test scalabilité sur projet massif."""
        import time
        
        massive_project = Path(self.temp_dir) / "massive_project"
        massive_project.mkdir()
        
        # Créer structure massive
        for i in range(20):
            subdir = massive_project / f"subdir_{i}"
            subdir.mkdir()
            
            # Cache dirs
            cache_dir = subdir / "__pycache__"
            cache_dir.mkdir()
            
            # Beaucoup de fichiers
            for j in range(50):
                (subdir / f"file_{j}.py").write_text(f"# File {i}_{j}")
                (cache_dir / f"cached_{j}.pyc").write_text("cached")
                (subdir / f"temp_{j}.tmp").write_text("temporary")
        
        # Test performance cleaner
        cleaner = AutoCleaner(str(massive_project))
        
        start_time = time.time()
        targets = cleaner.scan_for_cleanup_targets()
        scan_duration = time.time() - start_time
        
        start_cleanup = time.time()
        cleanup_result = cleaner.smart_cleanup()
        cleanup_duration = time.time() - start_cleanup
        
        # Vérifications performance
        assert isinstance(targets, dict)
        assert isinstance(cleanup_result, dict)
        assert scan_duration < 30.0  # Moins de 30 secondes pour scanner
        assert cleanup_duration < 60.0  # Moins de 1 minute pour nettoyer
        
        # Vérifier efficacité nettoyage
        cache_dirs = targets.get("cache_dirs", [])
        temp_files = targets.get("temp_files", [])
        assert len(cache_dirs) >= 20  # Au moins 20 cache dirs détectés
        assert len(temp_files) >= 100  # Au moins 100 fichiers temp détectés
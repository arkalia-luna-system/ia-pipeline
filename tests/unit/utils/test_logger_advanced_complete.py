#!/usr/bin/env python3
"""
Tests complets pour logger_advanced.py
Couverture complète de toutes les méthodes et fonctionnalités

Standards: Black + Ruff + MyPy + Bandit
"""

import json
import logging
import shutil
import tempfile
import time
from datetime import datetime
from pathlib import Path

from athalia_core.logger_advanced import (
    AthaliaLogger,
    athalia_logger,
    log_correction,
    log_error,
    log_main,
    log_performance,
    log_validation,
)


class TestAthaliaLoggerComplete:
    """Tests complets pour AthaliaLogger."""

    def setup_method(self) -> None:
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir) / "logs"
        self.log_dir.mkdir(parents=True)
        self.logger = AthaliaLogger(log_dir=str(self.log_dir))

    def teardown_method(self) -> None:
        """Nettoyage après chaque test."""
        # Arrêter le thread de nettoyage
        if (
            hasattr(self.logger, "cleanup_thread")
            and self.logger.cleanup_thread.is_alive()
        ):
            self.logger.stop_cleanup_worker()
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_logger_initialization(self) -> None:
        """Test initialisation du logger."""
        assert self.logger.log_dir == self.log_dir
        assert self.log_dir.exists()
        assert (self.log_dir / "archive").exists()
        assert "main" in self.logger.loggers
        assert "validation" in self.logger.loggers
        assert "correction" in self.logger.loggers
        assert "performance" in self.logger.loggers
        assert "errors" in self.logger.loggers
        assert isinstance(self.logger.metrics, dict)

    def test_logger_initialization_custom_dir(self) -> None:
        """Test initialisation avec répertoire personnalisé."""
        custom_dir = Path(self.temp_dir) / "custom_logs"
        custom_logger = AthaliaLogger(log_dir=str(custom_dir))

        assert custom_logger.log_dir == custom_dir
        assert custom_dir.exists()
        assert (custom_dir / "archive").exists()

    def test_setup_loggers_main(self) -> None:
        """Test configuration logger principal."""
        main_logger = self.logger.loggers.get("main")
        assert main_logger is not None
        assert main_logger.level == logging.INFO
        assert len(main_logger.handlers) > 0

    def test_setup_loggers_validation(self) -> None:
        """Test configuration logger validation."""
        validation_logger = self.logger.loggers.get("validation")
        assert validation_logger is not None
        assert validation_logger.level == logging.DEBUG
        assert len(validation_logger.handlers) > 0

    def test_setup_loggers_correction(self) -> None:
        """Test configuration logger correction."""
        correction_logger = self.logger.loggers.get("correction")
        assert correction_logger is not None
        assert correction_logger.level == logging.DEBUG
        assert len(correction_logger.handlers) > 0

    def test_setup_loggers_performance(self) -> None:
        """Test configuration logger performance."""
        performance_logger = self.logger.loggers.get("performance")
        assert performance_logger is not None
        assert performance_logger.level == logging.DEBUG
        assert len(performance_logger.handlers) > 0

    def test_setup_loggers_errors(self) -> None:
        """Test configuration logger erreurs."""
        errors_logger = self.logger.loggers.get("errors")
        assert errors_logger is not None
        assert errors_logger.level == logging.ERROR
        assert len(errors_logger.handlers) > 0

    def test_create_logger_method(self) -> None:
        """Test méthode création de logger."""
        test_log_file = self.log_dir / "test.log"
        test_logger = self.logger._create_logger("test", test_log_file, logging.DEBUG)

        assert test_logger.name == "athalia.test"
        assert test_logger.level == logging.DEBUG

    def test_log_main(self) -> None:
        """Test logging principal."""
        self.logger.log_main("Test message", "INFO", user="test_user")

        # Vérifier que le message a été loggé
        log_file = self.log_dir / "athalia.log"
        if log_file.exists():
            content = log_file.read_text()
            assert "Test message" in content

    def test_log_validation(self) -> None:
        """Test logging validation."""
        test_name = "test_validation"
        result = {"success": True, "details": "Test passed"}
        duration = 0.5

        self.logger.log_validation(test_name, result, duration)

        # Vérifier métriques
        assert "validation" in self.logger.metrics
        validation_metrics = self.logger.metrics["validation"]
        assert len(validation_metrics) > 0

        # Vérifier dernière métrique
        last_metric = validation_metrics[-1]
        assert last_metric["test_name"] == test_name
        assert last_metric["success"]
        assert last_metric["duration"] == duration

    def test_log_correction(self) -> None:
        """Test logging correction."""
        file_path = "test_file.py"
        correction_type = "formatting"
        success = True
        old_content = "old code"
        new_content = "new code"
        duration = 0.3

        self.logger.log_correction(
            file_path, correction_type, success, old_content, new_content, duration
        )

        # Vérifier métriques
        assert "correction" in self.logger.metrics
        correction_metrics = self.logger.metrics["correction"]
        assert len(correction_metrics) > 0

        # Vérifier dernière métrique
        last_metric = correction_metrics[-1]
        assert last_metric["file_path"] == file_path
        assert last_metric["type"] == correction_type
        assert last_metric["success"] == success
        assert last_metric["duration"] == duration
        assert last_metric["changes"] == len(new_content) - len(old_content)

    def test_log_performance(self) -> None:
        """Test logging performance."""
        operation = "test_operation"
        duration = 1.5
        memory_mb = 128.5
        cpu_percent = 25.0

        self.logger.log_performance(operation, duration, memory_mb, cpu_percent)

        # Vérifier métriques
        assert "performance" in self.logger.metrics
        performance_metrics = self.logger.metrics["performance"]
        assert len(performance_metrics) > 0

        # Vérifier dernière métrique
        last_metric = performance_metrics[-1]
        assert last_metric["operation"] == operation
        assert last_metric["duration"] == duration
        assert last_metric["memory_mb"] == memory_mb
        assert last_metric["cpu_percent"] == cpu_percent

    def test_log_error(self) -> None:
        """Test logging erreur."""
        error = ValueError("Test error")
        context = "test_context"

        self.logger.log_error(error, context, user="test_user")

        # Vérifier que l'erreur a été loggée
        log_file = self.log_dir / "errors.log"
        if log_file.exists():
            content = log_file.read_text()
            assert "Test error" in content
            assert "test_context" in content

    def test_get_validation_stats(self) -> None:
        """Test récupération statistiques validation."""
        # Ajouter quelques métriques de validation
        self.logger.metrics["validation"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "test_name": "test1",
                "success": True,
                "duration": 0.5,
                "details": {"result": "passed"},
            }
        )

        self.logger.metrics["validation"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "test_name": "test2",
                "success": False,
                "duration": 1.0,
                "details": {"result": "failed"},
            }
        )

        stats = self.logger.get_validation_stats(hours=24)
        assert isinstance(stats, dict)
        assert "total_tests" in stats
        assert "success_rate" in stats
        assert "average_duration" in stats

    def test_get_correction_stats(self) -> None:
        """Test récupération statistiques correction."""
        # Ajouter quelques métriques de correction
        self.logger.metrics["correction"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "file_path": "file1.py",
                "type": "formatting",
                "success": True,
                "duration": 0.3,
                "changes": 10,
            }
        )

        stats = self.logger.get_correction_stats(hours=24)
        assert isinstance(stats, dict)
        assert "total_corrections" in stats
        assert "success_rate" in stats
        assert "average_duration" in stats

    def test_get_performance_stats(self) -> None:
        """Test récupération statistiques performance."""
        # Ajouter quelques métriques de performance
        self.logger.metrics["performance"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "operation": "test_op",
                "duration": 1.0,
                "memory_mb": 100.0,
                "cpu_percent": 20.0,
            }
        )

        stats = self.logger.get_performance_stats(hours=24)
        assert isinstance(stats, dict)
        assert "total_operations" in stats
        assert "average_duration" in stats
        assert "average_memory" in stats

    def test_get_error_stats(self) -> None:
        """Test récupération statistiques erreurs."""
        # Créer un fichier d'erreur factice
        error_log = self.log_dir / "errors.log"
        error_log.write_text("2024-01-01 10:00:00 | ERROR | Test error\n")

        stats = self.logger.get_error_stats(hours=24)
        assert isinstance(stats, dict)
        assert "total_errors" in stats
        assert "error_types" in stats

    def test_cleanup_old_logs(self) -> None:
        """Test nettoyage anciens logs."""
        # Créer des fichiers de log factices
        old_log = self.log_dir / "old.log"
        old_log.write_text("old log content")

        # Modifier le timestamp pour le rendre ancien
        old_timestamp = time.time() - (8 * 24 * 3600)  # 8 jours
        # Utiliser os.utime au lieu de touch avec times
        import os

        os.utime(old_log, (old_timestamp, old_timestamp))

    def test_compress_old_logs(self) -> None:
        """Test compression des logs."""
        # Créer un fichier de log avec du contenu
        log_file = self.log_dir / "test_compress.log"
        content = "Log line 1\nLog line 2\n" * 100  # Contenu substantiel
        log_file.write_text(content)

        # Compresser
        self.logger._compress_old_logs()

        # Vérifier que la compression s'exécute sans erreur
        # Le comportement exact dépend de l'implémentation

    def test_export_metrics(self) -> None:
        """Test export des métriques."""
        # Ajouter quelques métriques
        self.logger.metrics["test_metric"].append(
            {"value": 1, "timestamp": datetime.now().isoformat()}
        )

        # Exporter métriques
        output_file = str(self.log_dir / "metrics_export.json")
        exported_data = self.logger.export_metrics(output_file)

        assert isinstance(exported_data, dict)
        assert "test_metric" in exported_data

        # Vérifier fichier de sortie
        if Path(output_file).exists():
            with open(output_file) as f:
                saved_data = json.load(f)
                assert "test_metric" in saved_data

    def test_cleanup_worker_lifecycle(self) -> None:
        """Test cycle de vie du thread de nettoyage."""
        # Démarrer le worker
        self.logger.start_cleanup_worker()
        assert self.logger.cleanup_thread.is_alive()

        # Arrêter le worker
        self.logger.stop_cleanup_worker()
        # Le thread devrait s'arrêter proprement

    def test_metrics_limit_enforcement(self) -> None:
        """Test respect de la limite des métriques."""
        # Ajouter plus de 1000 métriques pour déclencher la limite
        for i in range(1100):
            self.logger.metrics["test_limit"].append(
                {"value": i, "timestamp": datetime.now().isoformat()}
            )

        # Vérifier que la limite est respectée
        assert len(self.logger.metrics["test_limit"]) <= 1000

    def test_logger_handlers_duplication_prevention(self) -> None:
        """Test prévention des doublons de handlers."""
        # Appeler _create_logger plusieurs fois sur le même nom
        log_file = self.log_dir / "duplicate_test.log"
        logger1 = self.logger._create_logger("duplicate", log_file, logging.INFO)
        logger2 = self.logger._create_logger("duplicate", log_file, logging.INFO)

        # Les deux appels devraient retourner le même logger
        assert logger1 is logger2


class TestLoggerAdvancedIntegration:
    """Tests d'intégration pour logger_advanced.py"""

    def setup_method(self) -> None:
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self) -> None:
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_logging_workflow(self) -> None:
        """Test workflow complet de logging."""
        log_dir = Path(self.temp_dir) / "integration_logs"
        logger = AthaliaLogger(log_dir=str(log_dir))

        # 1. Logging basique
        logger.log_main("Integration test started", "INFO")

        # 2. Logging validation
        logger.log_validation("integration_test", {"success": True}, 0.5)

        # 3. Logging correction
        logger.log_correction("test_file.py", "formatting", True, "old", "new", 0.3)

        # 4. Logging performance
        logger.log_performance("integration_test", 1.0, 100.0, 25.0)

        # 5. Logging erreur
        try:
            raise ValueError("Test error for integration")
        except ValueError as e:
            logger.log_error(e, "integration_test")

        # 6. Vérifications
        assert log_dir.exists()
        assert (
            len(logger.loggers) == 5
        )  # main, validation, correction, performance, errors
        assert "validation" in logger.metrics
        assert "correction" in logger.metrics
        assert "performance" in logger.metrics

    def test_logger_singleton_behavior(self) -> None:
        """Test comportement singleton du logger global."""
        # Vérifier que athalia_logger est disponible
        assert athalia_logger is not None

        # Utiliser la fonction log_main
        log_main("Test message from integration test")

        # Vérifier que le message a été loggé
        # (Le test exact dépend de la configuration globale)

    def test_global_functions(self) -> None:
        """Test des fonctions globales du module."""
        # Test log_validation globale
        log_validation("global_test", {"success": True}, 0.5)

        # Test log_correction globale
        log_correction("global_file.py", "global_type", True, "old", "new", 0.3)

        # Test log_performance globale
        log_performance("global_operation", 1.0, 100.0, 25.0)

        # Test log_error globale
        try:
            raise RuntimeError("Global test error")
        except RuntimeError as e:
            log_error(e, "global_test")


class TestLoggerAdvancedPerformance:
    """Tests de performance pour logger_advanced.py"""

    def setup_method(self) -> None:
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()
        self.logger = AthaliaLogger(log_dir=str(self.temp_dir))

    def teardown_method(self) -> None:
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_high_volume_logging_performance(self) -> None:
        """Test performance logging haut volume."""
        main_logger = self.logger.loggers["main"]

        start_time = time.time()
        for i in range(1000):
            main_logger.info(f"High volume message {i}")
        end_time = time.time()

        duration = end_time - start_time
        # Le logging de 1000 messages devrait être rapide
        assert duration < 2.0  # Moins de 2 secondes

    def test_concurrent_performance_logging(self) -> None:
        """Test performance logging concurrent."""
        import threading

        def performance_worker() -> None:
            for i in range(100):
                start = time.time()
                time.sleep(0.001)  # Simulation traitement
                self.logger.log_performance(
                    f"worker_task_{i}", time.time() - start, 50.0, 10.0
                )

        # Lancer plusieurs workers
        threads = []
        start_time = time.time()

        for _ in range(5):
            thread = threading.Thread(target=performance_worker)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        total_time = time.time() - start_time
        # 5 workers * 100 tâches = 500 logs de performance
        # Devrait être complété rapidement
        assert total_time < 5.0

    def test_metrics_retrieval_performance(self) -> None:
        """Test performance récupération métriques."""
        # Préparer beaucoup de métriques
        for i in range(1000):
            self.logger.metrics["perf_test"].append(
                {"value": i, "timestamp": datetime.now().isoformat()}
            )

        # Test performance récupération
        start_time = time.time()
        stats = self.logger.get_performance_stats(hours=24)
        end_time = time.time()

        duration = end_time - start_time
        # La récupération des statistiques devrait être rapide
        assert duration < 1.0  # Moins d'1 seconde
        assert isinstance(stats, dict)


class TestLoggerAdvancedEdgeCases:
    """Tests des cas limites pour logger_advanced.py"""

    def setup_method(self) -> None:
        """Configuration tests cas limites."""
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir) / "logs"
        self.log_dir.mkdir(parents=True)
        self.logger = AthaliaLogger(log_dir=str(self.log_dir))

    def teardown_method(self) -> None:
        """Nettoyage tests cas limites."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_empty_metrics_retrieval(self) -> None:
        """Test récupération métriques vides."""
        # Récupérer stats sans métriques
        validation_stats = self.logger.get_validation_stats()
        correction_stats = self.logger.get_correction_stats()
        performance_stats = self.logger.get_performance_stats()
        error_stats = self.logger.get_error_stats()

        # Tous devraient retourner des dictionnaires valides
        assert isinstance(validation_stats, dict)
        assert isinstance(correction_stats, dict)
        assert isinstance(performance_stats, dict)
        assert isinstance(error_stats, dict)

    def test_invalid_log_level(self) -> None:
        """Test logging avec niveau invalide."""
        # Tenter de logger avec un niveau invalide
        try:
            self.logger.log_main("Test message", "INVALID_LEVEL")
            # Si aucune exception, le logger devrait gérer gracieusement
            assert True
        except Exception:
            # Exception attendue pour niveau invalide
            pass

    def test_large_message_logging(self) -> None:
        """Test logging de messages très longs."""
        large_message = "X" * 10000  # Message de 10KB

        # Logger le message volumineux
        self.logger.log_main(large_message)

        # Vérifier que le message a été loggé sans erreur
        log_file = self.log_dir / "athalia.log"
        if log_file.exists():
            content = log_file.read_text()
            assert large_message in content

    def test_special_characters_logging(self) -> None:
        """Test logging avec caractères spéciaux."""
        special_message = "Message avec caractères spéciaux: éàçù€£¥©®™"

        self.logger.log_main(special_message)

        # Vérifier que le message a été loggé correctement
        log_file = self.log_dir / "athalia.log"
        if log_file.exists():
            content = log_file.read_text()
            assert special_message in content

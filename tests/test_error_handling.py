#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le système de gestion d'erreurs d'Athalia
"""

import os
import tempfile
import unittest

from athalia_core.error_codes import (
    ErrorCode,
    ErrorSeverity,
    format_error_message,
    get_error_description,
    get_error_severity,
)
from athalia_core.error_handling import (
    AthaliaError,
    ErrorContext,
    ErrorHandler,
    error_handler,
    get_error_handler,
    handle_error,
    raise_athalia_error,
)


class TestErrorCodes(unittest.TestCase):
    """Tests pour les codes d'erreur."""

    def test_error_code_enum(self):
        """Test de l'énumération des codes d'erreur."""
        self.assertIsInstance(ErrorCode.UNKNOWN_ERROR, ErrorCode)
        self.assertEqual(ErrorCode.UNKNOWN_ERROR.value, 1000)
        self.assertEqual(ErrorCode.FILE_NOT_FOUND.value, 2000)
        self.assertEqual(ErrorCode.AI_MODEL_NOT_AVAILABLE.value, 4000)

    def test_error_severity_enum(self):
        """Test de l'énumération des niveaux de sévérité."""
        self.assertIsInstance(ErrorSeverity.INFO, ErrorSeverity)
        self.assertIsInstance(ErrorSeverity.WARNING, ErrorSeverity)
        self.assertIsInstance(ErrorSeverity.ERROR, ErrorSeverity)
        self.assertIsInstance(ErrorSeverity.CRITICAL, ErrorSeverity)

    def test_get_error_description(self):
        """Test de récupération des descriptions d'erreur."""
        desc = get_error_description(ErrorCode.FILE_NOT_FOUND)
        self.assertEqual(desc, "Fichier introuvable")

        desc = get_error_description(ErrorCode.UNKNOWN_ERROR)
        self.assertEqual(desc, "Erreur inconnue")

    def test_get_error_severity(self):
        """Test de détermination de la sévérité."""
        severity = get_error_severity(ErrorCode.FILE_CORRUPTED)
        self.assertEqual(severity, ErrorSeverity.CRITICAL)

        severity = get_error_severity(ErrorCode.INVALID_INPUT)
        self.assertEqual(severity, ErrorSeverity.WARNING)

    def test_format_error_message(self):
        """Test de formatage des messages d'erreur."""
        message = format_error_message(
            ErrorCode.FILE_NOT_FOUND, "fichier.txt", {"path": "/tmp"}
        )
        self.assertIn("FILE_NOT_FOUND", message)
        self.assertIn("fichier.txt", message)
        self.assertIn("path=/tmp", message)


class TestAthaliaError(unittest.TestCase):
    """Tests pour la classe AthaliaError."""

    def test_athalia_error_creation(self):
        """Test de création d'une AthaliaError."""
        error = AthaliaError(ErrorCode.FILE_NOT_FOUND, "Test error", "fichier.txt")

        self.assertEqual(error.error_code, ErrorCode.FILE_NOT_FOUND)
        self.assertEqual(error.message, "Test error")
        self.assertEqual(error.details, "fichier.txt")
        self.assertEqual(error.severity, ErrorSeverity.WARNING)
        self.assertIsNotNone(error.timestamp)

    def test_athalia_error_to_dict(self):
        """Test de conversion en dictionnaire."""
        error = AthaliaError(ErrorCode.INVALID_INPUT, "Invalid input", "test data")

        error_dict = error.to_dict()

        self.assertEqual(error_dict["error_code"], "INVALID_INPUT")
        self.assertEqual(error_dict["error_value"], 1001)
        self.assertEqual(error_dict["message"], "Invalid input")
        self.assertEqual(error_dict["details"], "test data")
        self.assertEqual(error_dict["severity"], "WARNING")
        self.assertIn("timestamp", error_dict)
        self.assertIn("traceback", error_dict)


class TestErrorHandler(unittest.TestCase):
    """Tests pour le gestionnaire d'erreurs."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.log_file = os.path.join(self.temp_dir, "test_errors.log")
        self.handler = ErrorHandler(self.log_file)

    def tearDown(self):
        """Nettoyage après chaque test."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_error_handler_initialization(self):
        """Test d'initialisation du gestionnaire d'erreurs."""
        self.assertEqual(self.handler.error_count, 0)
        self.assertEqual(len(self.handler.critical_errors), 0)
        self.assertIsInstance(self.handler.error_callbacks, dict)

    def test_handle_athalia_error(self):
        """Test de gestion d'une AthaliaError."""
        error = AthaliaError(ErrorCode.FILE_NOT_FOUND, "Test")
        handled_error = self.handler.handle_error(error)

        self.assertEqual(handled_error, error)
        self.assertEqual(self.handler.error_count, 1)

    def test_handle_python_exception(self):
        """Test de gestion d'une exception Python."""
        try:
            raise FileNotFoundError("fichier.txt")
        except Exception as e:
            handled_error = self.handler.handle_error(e)

        self.assertIsInstance(handled_error, AthaliaError)
        self.assertEqual(handled_error.error_code, ErrorCode.FILE_NOT_FOUND)
        self.assertEqual(self.handler.error_count, 1)

    def test_handle_critical_error(self):
        """Test de gestion d'une erreur critique."""
        error = AthaliaError(ErrorCode.FILE_CORRUPTED, "Critical")
        self.handler.handle_error(error)

        self.assertEqual(len(self.handler.critical_errors), 1)
        self.assertEqual(self.handler.critical_errors[0], error)

    def test_error_summary(self):
        """Test du résumé des erreurs."""
        # Ajouter quelques erreurs
        self.handler.handle_error(AthaliaError(ErrorCode.INVALID_INPUT))
        self.handler.handle_error(AthaliaError(ErrorCode.FILE_CORRUPTED))

        summary = self.handler.get_error_summary()

        self.assertEqual(summary["total_errors"], 2)
        self.assertEqual(summary["critical_errors"], 1)
        self.assertTrue(summary["has_critical_errors"])
        self.assertEqual(len(summary["critical_error_details"]), 1)

    def test_clear_errors(self):
        """Test d'effacement des erreurs."""
        self.handler.handle_error(AthaliaError(ErrorCode.INVALID_INPUT))
        self.handler.clear_errors()

        self.assertEqual(self.handler.error_count, 0)
        self.assertEqual(len(self.handler.critical_errors), 0)


class TestErrorHandlerGlobal(unittest.TestCase):
    """Tests pour le gestionnaire d'erreurs global."""

    def test_get_error_handler(self):
        """Test de récupération du gestionnaire global."""
        handler = get_error_handler()
        self.assertIsInstance(handler, ErrorHandler)

        # Deuxième appel doit retourner la même instance
        handler2 = get_error_handler()
        self.assertIs(handler, handler2)

    def test_handle_error_global(self):
        """Test de gestion d'erreur globale."""
        try:
            raise ValueError("Test value error")
        except Exception as e:
            error = handle_error(e)

        self.assertIsInstance(error, AthaliaError)
        self.assertEqual(error.error_code, ErrorCode.INVALID_INPUT)

    def test_raise_athalia_error(self):
        """Test de levée d'AthaliaError."""
        with self.assertRaises(AthaliaError) as cm:
            raise_athalia_error(ErrorCode.FILE_NOT_FOUND, "Test raise", "test.txt")

        error = cm.exception
        self.assertEqual(error.error_code, ErrorCode.FILE_NOT_FOUND)
        self.assertEqual(error.message, "Test raise")
        self.assertEqual(error.details, "test.txt")


class TestErrorDecorators(unittest.TestCase):
    """Tests pour les décorateurs de gestion d'erreurs."""

    def test_error_handler_decorator(self):
        """Test du décorateur error_handler."""

        @error_handler(ErrorCode.INVALID_INPUT)
        def test_function():
            raise ValueError("Test error")

        with self.assertRaises(AthaliaError) as cm:
            test_function()

        error = cm.exception
        self.assertEqual(error.error_code, ErrorCode.INVALID_INPUT)
        self.assertIn("test_function", str(error))

    def test_error_handler_decorator_no_error(self):
        """Test du décorateur sans erreur."""

        @error_handler(ErrorCode.INVALID_INPUT)
        def test_function():
            return "success"

        result = test_function()
        self.assertEqual(result, "success")


class TestErrorContext(unittest.TestCase):
    """Tests pour le context manager ErrorContext."""

    def test_error_context_no_error(self):
        """Test du context manager sans erreur."""
        with ErrorContext(ErrorCode.INVALID_INPUT):
            result = "success"

        self.assertEqual(result, "success")

    def test_error_context_with_error(self):
        """Test du context manager avec erreur."""
        with self.assertRaises(AthaliaError) as cm:
            with ErrorContext(ErrorCode.FILE_NOT_FOUND):
                raise ValueError("Test error")

        error = cm.exception
        self.assertEqual(error.error_code, ErrorCode.FILE_NOT_FOUND)

    def test_error_context_with_athalia_error(self):
        """Test du context manager avec AthaliaError."""
        original_error = AthaliaError(ErrorCode.INVALID_INPUT, "Original")

        with self.assertRaises(AthaliaError) as cm:
            with ErrorContext(ErrorCode.FILE_NOT_FOUND):
                raise original_error

        # L'erreur originale doit être préservée
        self.assertEqual(cm.exception, original_error)


if __name__ == "__main__":
    unittest.main()

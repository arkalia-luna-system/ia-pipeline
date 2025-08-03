#!/usr/bin/env python3
"""
Gestion centralisée des erreurs pour Athalia
Système unifié de gestion d'erreurs avec logging et reporting
"""

import logging
import sys
import traceback
from collections.abc import Callable
from datetime import datetime
from pathlib import Path
from typing import Any

from .error_codes import (
    ErrorCode,
    ErrorSeverity,
    format_error_message,
    get_error_severity,
)


class AthaliaError(Exception):
    """Exception de base pour Athalia avec code d'erreur."""

    def __init__(
        self,
        error_code: ErrorCode,
        message: str = "",
        details: str = "",
        context: dict[str, Any] = None,
    ):
        self.error_code = error_code
        self.message = message
        self.details = details
        self.context = context or {}
        self.timestamp = datetime.now()
        self.severity = get_error_severity(error_code)

        # Construire le message complet
        full_message = format_error_message(error_code, details, context)
        if message:
            full_message = f"{message}: {full_message}"

        super().__init__(full_message)

    def to_dict(self) -> dict[str, Any]:
        """Convertit l'erreur en dictionnaire pour sérialisation."""
        return {
            "error_code": self.error_code.name,
            "error_value": self.error_code.value,
            "message": self.message,
            "details": self.details,
            "context": self.context,
            "timestamp": self.timestamp.isoformat(),
            "severity": self.severity.name,
            "traceback": traceback.format_exc(),
        }


class ErrorHandler:
    """Gestionnaire centralisé des erreurs."""

    def __init__(self, log_file: str | None = None):
        self.log_file = log_file
        self.error_count = 0
        self.critical_errors = []
        self.error_callbacks: dict[ErrorCode, Callable] = {}

        # Configuration du logging
        self._setup_logging()

    def _setup_logging(self):
        """Configure le système de logging."""
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        # Handler pour console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(log_format))

        # Handler pour fichier si spécifié
        handlers = [console_handler]
        if self.log_file:
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(logging.Formatter(log_format))
            handlers.append(file_handler)

        # Configuration du logger principal
        logging.basicConfig(level=logging.DEBUG, handlers=handlers, force=True)

        self.logger = logging.getLogger("athalia.error_handler")

    def handle_error(
        self, error: Exception, context: dict[str, Any] = None
    ) -> AthaliaError:
        """Gère une erreur et la convertit en AthaliaError."""
        if isinstance(error, AthaliaError):
            athalia_error = error
        else:
            # Convertir l'erreur en AthaliaError
            error_code = self._classify_error(error)
            athalia_error = AthaliaError(
                error_code=error_code,
                message=str(error),
                context=context or {},
            )

        # Log de l'erreur
        self._log_error(athalia_error)

        # Incrémenter le compteur
        self.error_count += 1

        # Stocker les erreurs critiques
        if athalia_error.severity == ErrorSeverity.CRITICAL:
            self.critical_errors.append(athalia_error)

        # Appeler le callback si configuré
        if athalia_error.error_code in self.error_callbacks:
            try:
                self.error_callbacks[athalia_error.error_code](athalia_error)
            except Exception as callback_error:
                self.logger.error(f"Erreur dans le callback: {callback_error}")

        return athalia_error

    def _classify_error(self, error: Exception) -> ErrorCode:
        """Classifie une exception en code d'erreur Athalia."""
        error_type = type(error).__name__

        # Mapping des types d'erreurs Python vers les codes Athalia
        error_mapping = {
            "FileNotFoundError": ErrorCode.FILE_NOT_FOUND,
            "PermissionError": ErrorCode.PERMISSION_DENIED,
            "ImportError": ErrorCode.MODULE_IMPORT_ERROR,
            "ModuleNotFoundError": ErrorCode.MODULE_NOT_FOUND,
            "ValueError": ErrorCode.INVALID_INPUT,
            "TypeError": ErrorCode.INVALID_INPUT,
            "KeyError": ErrorCode.MISSING_REQUIRED_PARAMETER,
            "TimeoutError": ErrorCode.TIMEOUT_EXCEEDED,
            "MemoryError": ErrorCode.MEMORY_EXHAUSTED,
            "OSError": ErrorCode.FILE_ACCESS_DENIED,
        }

        return error_mapping.get(error_type, ErrorCode.UNKNOWN_ERROR)

    def _log_error(self, error: AthaliaError):
        """Log une erreur avec le niveau approprié."""
        log_message = f"{error}"

        if error.severity == ErrorSeverity.CRITICAL:
            self.logger.critical(log_message)
        elif error.severity == ErrorSeverity.ERROR:
            self.logger.error(log_message)
        elif error.severity == ErrorSeverity.WARNING:
            self.logger.warning(log_message)
        else:
            self.logger.info(log_message)

    def register_callback(
        self, error_code: ErrorCode, callback: Callable[[AthaliaError], None]
    ):
        """Enregistre un callback pour un type d'erreur spécifique."""
        self.error_callbacks[error_code] = callback

    def get_error_summary(self) -> dict[str, Any]:
        """Retourne un résumé des erreurs."""
        return {
            "total_errors": self.error_count,
            "critical_errors": len(self.critical_errors),
            "has_critical_errors": len(self.critical_errors) > 0,
            "critical_error_details": [
                error.to_dict() for error in self.critical_errors
            ],
        }

    def clear_errors(self):
        """Efface l'historique des erreurs."""
        self.error_count = 0
        self.critical_errors.clear()


# Instance globale du gestionnaire d'erreurs
_global_error_handler: ErrorHandler | None = None


def get_error_handler() -> ErrorHandler:
    """Récupère l'instance globale du gestionnaire d'erreurs."""
    global _global_error_handler
    if _global_error_handler is None:
        log_file = Path("logs/athalia_errors.log")
        log_file.parent.mkdir(exist_ok=True)
        _global_error_handler = ErrorHandler(str(log_file))
    return _global_error_handler


def handle_error(error: Exception, context: dict[str, Any] = None) -> AthaliaError:
    """Fonction utilitaire pour gérer une erreur."""
    return get_error_handler().handle_error(error, context)


def raise_athalia_error(
    error_code: ErrorCode,
    message: str = "",
    details: str = "",
    context: dict[str, Any] = None,
):
    """Lève une AthaliaError avec gestion automatique."""
    error = AthaliaError(error_code, message, details, context)
    get_error_handler().handle_error(error)
    raise error


# Décorateur pour gestion automatique d'erreurs
def error_handler(error_code: ErrorCode = ErrorCode.UNKNOWN_ERROR):
    """Décorateur pour gestion automatique d'erreurs."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if isinstance(e, AthaliaError):
                    raise
                else:
                    raise_athalia_error(
                        error_code, f"Erreur dans {func.__name__}", str(e)
                    )

        return wrapper

    return decorator


# Context manager pour gestion d'erreurs
class ErrorContext:
    """Context manager pour gestion d'erreurs dans un bloc de code."""

    def __init__(
        self,
        error_code: ErrorCode = ErrorCode.UNKNOWN_ERROR,
        context: dict[str, Any] = None,
    ):
        self.error_code = error_code
        self.context = context or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if isinstance(exc_val, AthaliaError):
                return False  # Laisse l'erreur se propager
            else:
                raise_athalia_error(
                    self.error_code,
                    "Erreur dans le contexte",
                    str(exc_val),
                    self.context,
                )
        return True

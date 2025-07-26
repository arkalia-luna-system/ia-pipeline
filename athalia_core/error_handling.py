#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de gestion d'erreurs pour Athalia
Améliore la robustesse du système avec gestion d'erreurs complète
"""

import logging
import traceback
import time
from typing import Dict, Any, Optional, Callable, Type
from functools import wraps
from .error_codes import ErrorCode, ErrorMessages

logger = logging.getLogger(__name__)

class AthaliaError(Exception):
    """Classe de base pour toutes les erreurs Athalia"""
    
    def __init__(self, message: str, code: str = ErrorCode.SYSTEM_INTERNAL_ERROR.value, 
                 details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}
        self.timestamp = time.time()
        
    def to_dict(self) -> Dict[str, Any]:
        """Convertit l'erreur en dictionnaire"""
        return {
            "error_type": self.__class__.__name__,
            "code": self.code,
            "message": self.message,
            "details": self.details,
            "timestamp": self.timestamp
        }

class ConfigurationError(AthaliaError):
    """Erreur de configuration"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.CONFIG_FILE_NOT_FOUND.value, details)

class FileSystemError(AthaliaError):
    """Erreur de système de fichiers"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.FILE_NOT_FOUND.value, details)

class NetworkError(AthaliaError):
    """Erreur réseau"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.NETWORK_CONNECTION_FAILED.value, details)

class ValidationError(AthaliaError):
    """Erreur de validation"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.VALIDATION_INVALID_INPUT.value, details)

class ProcessingError(AthaliaError):
    """Erreur de traitement"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.PROCESSING_FAILED.value, details)

class SystemError(AthaliaError):
    """Erreur système"""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, ErrorCode.SYSTEM_INTERNAL_ERROR.value, details)

class ErrorRecovery:
    """Gestionnaire de récupération d'erreurs"""
    
    def __init__(self, max_retries: int = 3, retry_delay: float = 1.0):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.retry_count = 0
        
    def retry_operation(self, operation: Callable, *args, **kwargs) -> Any:
        """Répète une opération en cas d'échec"""
        last_exception = None
        
        for attempt in range(self.max_retries + 1):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                last_exception = e
                self.retry_count += 1
                
                if attempt < self.max_retries:
                    logger.warning(f"Tentative {attempt + 1} échouée: {e}. Nouvelle tentative dans {self.retry_delay}s...")
                    time.sleep(self.retry_delay)
                    # Augmenter le délai exponentiellement
                    self.retry_delay *= 2
                else:
                    logger.error(f"Toutes les tentatives ont échoué après {self.max_retries + 1} essais")
                    break
        
        # Si toutes les tentatives ont échoué, lever l'exception
        if last_exception:
            raise last_exception
    
    def reset(self):
        """Réinitialise le compteur de tentatives"""
        self.retry_count = 0
        self.retry_delay = 1.0

class ErrorLogger:
    """Gestionnaire de logging des erreurs"""
    
    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file or "logs/errors.log"
        self.setup_logging()
    
    def setup_logging(self):
        """Configure le logging des erreurs"""
        import os
        
        # Créer le dossier logs s'il n'existe pas
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        
        # Configurer le handler pour les erreurs
        error_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        
        # Formatter pour les erreurs
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )
        error_handler.setFormatter(formatter)
        
        # Ajouter le handler au logger
        logger.addHandler(error_handler)
    
    def log_error(self, error: Exception, context: Optional[str] = None):
        """Enregistre une erreur avec contexte"""
        error_info = {
            "error_type": type(error).__name__,
            "message": str(error),
            "context": context,
            "traceback": traceback.format_exc()
        }
        
        if isinstance(error, AthaliaError):
            error_info.update(error.to_dict())
        
        logger.error(f"Erreur enregistrée: {error_info}")
    
    def get_error_summary(self) -> Dict[str, Any]:
        """Récupère un résumé des erreurs récentes"""
        # Cette méthode pourrait analyser le fichier de log
        # pour fournir des statistiques d'erreurs
        return {
            "total_errors": 0,  # À implémenter
            "error_types": {},  # À implémenter
            "last_error": None  # À implémenter
        }

class ErrorHandler:
    """Gestionnaire principal d'erreurs"""
    
    def __init__(self, enable_recovery: bool = True, enable_logging: bool = True):
        self.enable_recovery = enable_recovery
        self.enable_logging = enable_logging
        self.recovery = ErrorRecovery() if enable_recovery else None
        self.logger = ErrorLogger() if enable_logging else None
        
    def handle_error(self, error: Exception, context: Optional[str] = None) -> Dict[str, Any]:
        """Gère une erreur de manière centralisée"""
        
        # Enregistrer l'erreur
        if self.logger:
            self.logger.log_error(error, context)
        
        # Formater l'erreur
        if isinstance(error, AthaliaError):
            error_info = error.to_dict()
        else:
            error_info = {
                "error_type": type(error).__name__,
                "code": ErrorCode.SYSTEM_INTERNAL_ERROR.value,
                "message": str(error),
                "details": {"traceback": traceback.format_exc()},
                "timestamp": time.time()
            }
        
        # Ajouter le contexte
        if context:
            error_info["context"] = context
        
        # Vérifier si l'erreur est récupérable
        from .error_codes import ErrorHandler as ErrorCodeHandler
        error_info["recoverable"] = ErrorCodeHandler.is_recoverable(error_info["code"])
        
        # Ajouter une suggestion si disponible
        suggestion = ErrorCodeHandler.get_suggestion(error_info["code"])
        if suggestion:
            error_info["suggestion"] = suggestion
        
        return error_info
    
    def safe_execute(self, operation: Callable, *args, **kwargs) -> Any:
        """Exécute une opération de manière sécurisée"""
        try:
            if self.enable_recovery and self.recovery:
                return self.recovery.retry_operation(operation, *args, **kwargs)
            else:
                return operation(*args, **kwargs)
        except Exception as e:
            error_info = self.handle_error(e, f"Operation: {operation.__name__}")
            raise AthaliaError(
                f"Échec de l'opération {operation.__name__}: {str(e)}",
                error_info["code"],
                error_info
            )

def error_handler(enable_recovery: bool = True, enable_logging: bool = True):
    """Décorateur pour gérer les erreurs automatiquement"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            handler = ErrorHandler(enable_recovery, enable_logging)
            return handler.safe_execute(func, *args, **kwargs)
        return wrapper
    return decorator

def validate_input(data: Any, required_fields: list, data_type: Type = dict) -> None:
    """Valide les données d'entrée"""
    if not isinstance(data, data_type):
        raise ValidationError(f"Type de données invalide. Attendu: {data_type}, Reçu: {type(data)}")
    
    if isinstance(data, dict):
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValidationError(
                f"Champs requis manquants: {missing_fields}",
                details={"missing_fields": missing_fields, "required_fields": required_fields}
            )

def safe_file_operation(operation: Callable, file_path: str, *args, **kwargs) -> Any:
    """Exécute une opération sur fichier de manière sécurisée"""
    import os
    
    # Vérifier que le fichier existe
    if not os.path.exists(file_path):
        raise FileSystemError(f"Fichier non trouvé: {file_path}")
    
    # Vérifier les permissions
    if not os.access(file_path, os.R_OK):
        raise FileSystemError(f"Permission refusée pour le fichier: {file_path}")
    
    try:
        return operation(file_path, *args, **kwargs)
    except PermissionError as e:
        raise FileSystemError(f"Erreur de permission: {e}")
    except OSError as e:
        raise FileSystemError(f"Erreur système de fichier: {e}")

def handle_network_errors(func: Callable) -> Callable:
    """Décorateur pour gérer les erreurs réseau"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            raise NetworkError(f"Erreur de connexion: {e}")
        except TimeoutError as e:
            raise NetworkError(f"Délai d'attente dépassé: {e}")
        except Exception as e:
            # Vérifier si c'est une erreur réseau
            if "network" in str(e).lower() or "connection" in str(e).lower():
                raise NetworkError(f"Erreur réseau: {e}")
            else:
                raise
    return wrapper

# Instance globale du gestionnaire d'erreurs
global_error_handler = ErrorHandler()

def get_global_error_handler() -> ErrorHandler:
    """Récupère l'instance globale du gestionnaire d'erreurs"""
    return global_error_handler

def set_global_error_handler(handler: ErrorHandler):
    """Définit l'instance globale du gestionnaire d'erreurs"""
    global global_error_handler
    global_error_handler = handler

# Exemple d'utilisation
if __name__ == "__main__":
    # Test du gestionnaire d'erreurs
    handler = ErrorHandler()
    
    # Test d'une erreur de validation
    try:
        validate_input({"name": "test"}, ["name", "email"])
    except ValidationError as e:
        error_info = handler.handle_error(e, "Test validation")
        print(f"Erreur de validation: {error_info}")
    
    # Test d'une erreur de fichier
    try:
        safe_file_operation(open, "fichier_inexistant.txt")
    except FileSystemError as e:
        error_info = handler.handle_error(e, "Test fichier")
        print(f"Erreur de fichier: {error_info}")
    
    # Test avec le décorateur
    @error_handler(enable_recovery=True, enable_logging=True)
    def test_operation():
        raise ValueError("Test d'erreur")
    
    try:
        test_operation()
    except AthaliaError as e:
        print(f"Erreur gérée: {e.to_dict()}") 
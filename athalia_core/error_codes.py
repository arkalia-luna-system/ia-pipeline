#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codes d'erreur centralisés pour Athalia
Standardise tous les codes d'erreur avec des messages cohérents
"""

from enum import Enum
from typing import Dict, Optional, Any

class ErrorCategory(Enum):
    """Catégories d'erreurs"""
    CONFIGURATION = "E001-E099"
    FILESYSTEM = "E100-E199"
    PERMISSIONS = "E200-E299"
    NETWORK = "E300-E399"
    SYSTEM = "E400-E499"
    VALIDATION = "E500-E599"
    PROCESSING = "E600-E699"

class ErrorCode(Enum):
    """Codes d'erreur standardisés"""
    
    # Erreurs de configuration (E001-E099)
    CONFIG_FILE_NOT_FOUND = "E001"
    CONFIG_INVALID_FORMAT = "E002"
    CONFIG_MISSING_REQUIRED = "E003"
    CONFIG_INVALID_VALUE = "E004"
    CONFIG_PERMISSION_DENIED = "E005"
    
    # Erreurs de fichiers (E100-E199)
    FILE_NOT_FOUND = "E100"
    FILE_ACCESS_DENIED = "E101"
    FILE_ALREADY_EXISTS = "E102"
    FILE_CORRUPTED = "E103"
    FILE_TOO_LARGE = "E104"
    FILE_INVALID_FORMAT = "E105"
    DIRECTORY_NOT_FOUND = "E110"
    DIRECTORY_ACCESS_DENIED = "E111"
    DIRECTORY_NOT_EMPTY = "E112"
    
    # Erreurs de permissions (E200-E299)
    PERMISSION_DENIED = "E200"
    INSUFFICIENT_PRIVILEGES = "E201"
    USER_NOT_AUTHORIZED = "E202"
    GROUP_ACCESS_DENIED = "E203"
    
    # Erreurs réseau (E300-E399)
    NETWORK_CONNECTION_FAILED = "E300"
    NETWORK_TIMEOUT = "E301"
    NETWORK_HOST_UNREACHABLE = "E302"
    NETWORK_PORT_CLOSED = "E303"
    NETWORK_SSL_ERROR = "E304"
    NETWORK_DNS_ERROR = "E305"
    
    # Erreurs système (E400-E499)
    SYSTEM_OUT_OF_MEMORY = "E400"
    SYSTEM_DISK_FULL = "E401"
    SYSTEM_PROCESS_FAILED = "E402"
    SYSTEM_SERVICE_UNAVAILABLE = "E403"
    SYSTEM_RESOURCE_EXHAUSTED = "E404"
    SYSTEM_INTERNAL_ERROR = "E405"
    
    # Erreurs de validation (E500-E599)
    VALIDATION_INVALID_INPUT = "E500"
    VALIDATION_MISSING_REQUIRED = "E501"
    VALIDATION_INVALID_FORMAT = "E502"
    VALIDATION_OUT_OF_RANGE = "E503"
    VALIDATION_CONSTRAINT_VIOLATION = "E504"
    
    # Erreurs de traitement (E600-E699)
    PROCESSING_FAILED = "E600"
    PROCESSING_TIMEOUT = "E601"
    PROCESSING_INVALID_STATE = "E602"
    PROCESSING_DEPENDENCY_MISSING = "E603"
    PROCESSING_RESOURCE_UNAVAILABLE = "E604"

class WarningCode(Enum):
    """Codes d'avertissement standardisés"""
    
    # Avertissements généraux (W001-W099)
    GENERAL_WARNING = "W001"
    DEPRECATED_FEATURE = "W002"
    PERFORMANCE_ISSUE = "W003"
    SECURITY_WARNING = "W004"
    
    # Avertissements de configuration (W100-W199)
    CONFIG_DEFAULT_USED = "W100"
    CONFIG_OPTIONAL_MISSING = "W101"
    CONFIG_VALUE_OVERRIDDEN = "W102"
    
    # Avertissements de fichiers (W200-W299)
    FILE_BACKUP_CREATED = "W200"
    FILE_TEMPORARY_CLEANED = "W201"
    FILE_SIZE_LARGE = "W202"
    
    # Avertissements de performance (W300-W399)
    PERFORMANCE_SLOW_OPERATION = "W300"
    PERFORMANCE_HIGH_MEMORY = "W301"
    PERFORMANCE_HIGH_CPU = "W302"

class InfoCode(Enum):
    """Codes d'information standardisés"""
    
    # Informations générales (I001-I099)
    GENERAL_INFO = "I001"
    OPERATION_STARTED = "I002"
    OPERATION_COMPLETED = "I003"
    OPERATION_SKIPPED = "I004"
    
    # Informations de configuration (I100-I199)
    CONFIG_LOADED = "I100"
    CONFIG_VALIDATED = "I101"
    CONFIG_SAVED = "I102"
    
    # Informations de fichiers (I200-I299)
    FILE_CREATED = "I200"
    FILE_UPDATED = "I201"
    FILE_DELETED = "I202"
    FILE_COPIED = "I203"
    FILE_MOVED = "I204"

class ErrorMessages:
    """Messages d'erreur standardisés"""
    
    _messages: Dict[str, str] = {
        # Erreurs de configuration
        ErrorCode.CONFIG_FILE_NOT_FOUND.value: "Fichier de configuration non trouvé",
        ErrorCode.CONFIG_INVALID_FORMAT.value: "Format de configuration invalide",
        ErrorCode.CONFIG_MISSING_REQUIRED.value: "Paramètre de configuration requis manquant",
        ErrorCode.CONFIG_INVALID_VALUE.value: "Valeur de configuration invalide",
        ErrorCode.CONFIG_PERMISSION_DENIED.value: "Permission refusée pour le fichier de configuration",
        
        # Erreurs de fichiers
        ErrorCode.FILE_NOT_FOUND.value: "Fichier non trouvé",
        ErrorCode.FILE_ACCESS_DENIED.value: "Accès au fichier refusé",
        ErrorCode.FILE_ALREADY_EXISTS.value: "Le fichier existe déjà",
        ErrorCode.FILE_CORRUPTED.value: "Fichier corrompu",
        ErrorCode.FILE_TOO_LARGE.value: "Fichier trop volumineux",
        ErrorCode.FILE_INVALID_FORMAT.value: "Format de fichier invalide",
        ErrorCode.DIRECTORY_NOT_FOUND.value: "Répertoire non trouvé",
        ErrorCode.DIRECTORY_ACCESS_DENIED.value: "Accès au répertoire refusé",
        ErrorCode.DIRECTORY_NOT_EMPTY.value: "Le répertoire n'est pas vide",
        
        # Erreurs de permissions
        ErrorCode.PERMISSION_DENIED.value: "Permission refusée",
        ErrorCode.INSUFFICIENT_PRIVILEGES.value: "Privilèges insuffisants",
        ErrorCode.USER_NOT_AUTHORIZED.value: "Utilisateur non autorisé",
        ErrorCode.GROUP_ACCESS_DENIED.value: "Accès au groupe refusé",
        
        # Erreurs réseau
        ErrorCode.NETWORK_CONNECTION_FAILED.value: "Échec de connexion réseau",
        ErrorCode.NETWORK_TIMEOUT.value: "Délai d'attente réseau dépassé",
        ErrorCode.NETWORK_HOST_UNREACHABLE.value: "Hôte réseau inaccessible",
        ErrorCode.NETWORK_PORT_CLOSED.value: "Port réseau fermé",
        ErrorCode.NETWORK_SSL_ERROR.value: "Erreur SSL/TLS",
        ErrorCode.NETWORK_DNS_ERROR.value: "Erreur de résolution DNS",
        
        # Erreurs système
        ErrorCode.SYSTEM_OUT_OF_MEMORY.value: "Mémoire système insuffisante",
        ErrorCode.SYSTEM_DISK_FULL.value: "Espace disque insuffisant",
        ErrorCode.SYSTEM_PROCESS_FAILED.value: "Échec du processus système",
        ErrorCode.SYSTEM_SERVICE_UNAVAILABLE.value: "Service système indisponible",
        ErrorCode.SYSTEM_RESOURCE_EXHAUSTED.value: "Ressources système épuisées",
        ErrorCode.SYSTEM_INTERNAL_ERROR.value: "Erreur interne du système",
        
        # Erreurs de validation
        ErrorCode.VALIDATION_INVALID_INPUT.value: "Entrée invalide",
        ErrorCode.VALIDATION_MISSING_REQUIRED.value: "Paramètre requis manquant",
        ErrorCode.VALIDATION_INVALID_FORMAT.value: "Format invalide",
        ErrorCode.VALIDATION_OUT_OF_RANGE.value: "Valeur hors limites",
        ErrorCode.VALIDATION_CONSTRAINT_VIOLATION.value: "Violation de contrainte",
        
        # Erreurs de traitement
        ErrorCode.PROCESSING_FAILED.value: "Échec du traitement",
        ErrorCode.PROCESSING_TIMEOUT.value: "Délai de traitement dépassé",
        ErrorCode.PROCESSING_INVALID_STATE.value: "État de traitement invalide",
        ErrorCode.PROCESSING_DEPENDENCY_MISSING.value: "Dépendance manquante",
        ErrorCode.PROCESSING_RESOURCE_UNAVAILABLE.value: "Ressource de traitement indisponible"
    }
    
    @classmethod
    def get_message(cls, code: str) -> str:
        """Récupère le message pour un code d'erreur"""
        return cls._messages.get(code, f"Erreur inconnue: {code}")
    
    @classmethod
    def get_category(cls, code: str) -> Optional[ErrorCategory]:
        """Récupère la catégorie pour un code d'erreur"""
        try:
            code_prefix = code[:1]
            code_number = int(code[1:])
            
            if code_prefix == "E":
                if 1 <= code_number <= 99:
                    return ErrorCategory.CONFIGURATION
                elif 100 <= code_number <= 199:
                    return ErrorCategory.FILESYSTEM
                elif 200 <= code_number <= 299:
                    return ErrorCategory.PERMISSIONS
                elif 300 <= code_number <= 399:
                    return ErrorCategory.NETWORK
                elif 400 <= code_number <= 499:
                    return ErrorCategory.SYSTEM
                elif 500 <= code_number <= 599:
                    return ErrorCategory.VALIDATION
                elif 600 <= code_number <= 699:
                    return ErrorCategory.PROCESSING
        except (ValueError, IndexError):
            pass
        
        return None

class ErrorHandler:
    """Gestionnaire d'erreurs centralisé"""
    
    @staticmethod
    def format_error(code: str, message: Optional[str] = None, details: Optional[Dict] = None) -> Dict:
        """Formate une erreur avec le code et le message"""
        formatted_error: Dict[str, Any] = {
            "code": code,
            "message": message or ErrorMessages.get_message(code),
            "category": ErrorMessages.get_category(code),
            "timestamp": None  # Sera rempli par le CLI
        }
        
        if details:
            formatted_error["details"] = details
            
        return formatted_error
    
    @staticmethod
    def is_recoverable(code: str) -> bool:
        """Détermine si une erreur est récupérable"""
        # Erreurs récupérables
        recoverable_codes = [
            ErrorCode.NETWORK_TIMEOUT.value,
            ErrorCode.NETWORK_CONNECTION_FAILED.value,
            ErrorCode.SYSTEM_RESOURCE_EXHAUSTED.value,
            ErrorCode.PROCESSING_TIMEOUT.value,
            ErrorCode.VALIDATION_INVALID_INPUT.value
        ]
        
        return code in recoverable_codes
    
    @staticmethod
    def get_suggestion(code: str) -> Optional[str]:
        """Récupère une suggestion pour résoudre l'erreur"""
        suggestions = {
            ErrorCode.CONFIG_FILE_NOT_FOUND.value: "Vérifiez le chemin du fichier de configuration",
            ErrorCode.FILE_NOT_FOUND.value: "Vérifiez que le fichier existe et que le chemin est correct",
            ErrorCode.PERMISSION_DENIED.value: "Vérifiez les permissions du fichier ou du répertoire",
            ErrorCode.NETWORK_CONNECTION_FAILED.value: "Vérifiez votre connexion réseau",
            ErrorCode.SYSTEM_OUT_OF_MEMORY.value: "Fermez d'autres applications pour libérer de la mémoire",
            ErrorCode.VALIDATION_INVALID_INPUT.value: "Vérifiez le format des données d'entrée"
        }
        
        return suggestions.get(code)

def get_error_info(code: str) -> Dict:
    """Récupère toutes les informations pour un code d'erreur"""
    return {
        "code": code,
        "message": ErrorMessages.get_message(code),
        "category": ErrorMessages.get_category(code),
        "recoverable": ErrorHandler.is_recoverable(code),
        "suggestion": ErrorHandler.get_suggestion(code)
    }

# Exemple d'utilisation
if __name__ == "__main__":
    # Test des codes d'erreur
    test_codes = [
        ErrorCode.CONFIG_FILE_NOT_FOUND.value,
        ErrorCode.FILE_NOT_FOUND.value,
        ErrorCode.NETWORK_CONNECTION_FAILED.value,
        ErrorCode.SYSTEM_OUT_OF_MEMORY.value
    ]
    
    print("=== Test des codes d'erreur ===")
    for code in test_codes:
        info = get_error_info(code)
        print(f"Code: {info['code']}")
        print(f"Message: {info['message']}")
        print(f"Catégorie: {info['category']}")
        print(f"Récupérable: {info['recoverable']}")
        print(f"Suggestion: {info['suggestion']}")
        print("-" * 40) 
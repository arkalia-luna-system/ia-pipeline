#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codes d'erreur standardisés pour Athalia
Centralisation des codes d'erreur pour une gestion cohérente
"""

from enum import Enum, auto
from typing import Dict, Any


class ErrorCode(Enum):
    """Codes d'erreur standardisés pour Athalia."""

    # Erreurs générales (1000-1999)
    UNKNOWN_ERROR = 1000
    INVALID_INPUT = 1001
    MISSING_REQUIRED_PARAMETER = 1002
    INVALID_CONFIGURATION = 1003
    PERMISSION_DENIED = 1004

    # Erreurs de fichiers (2000-2999)
    FILE_NOT_FOUND = 2000
    FILE_ACCESS_DENIED = 2001
    FILE_CORRUPTED = 2002
    DIRECTORY_NOT_FOUND = 2003
    INSUFFICIENT_DISK_SPACE = 2004

    # Erreurs de modules (3000-3999)
    MODULE_NOT_FOUND = 3000
    MODULE_IMPORT_ERROR = 3001
    MODULE_INITIALIZATION_FAILED = 3002
    MODULE_DEPENDENCY_MISSING = 3003

    # Erreurs d'IA et modèles (4000-4999)
    AI_MODEL_NOT_AVAILABLE = 4000
    AI_MODEL_LOAD_FAILED = 4001
    AI_RESPONSE_TIMEOUT = 4002
    AI_RESPONSE_INVALID = 4003
    AI_PROVIDER_UNAVAILABLE = 4004

    # Erreurs de génération (5000-5999)
    GENERATION_FAILED = 5000
    BLUEPRINT_INVALID = 5001
    TEMPLATE_NOT_FOUND = 5002
    GENERATION_TIMEOUT = 5003

    # Erreurs de tests (6000-6999)
    TEST_FAILED = 6000
    TEST_TIMEOUT = 6001
    TEST_ENVIRONMENT_INVALID = 6002
    COVERAGE_BELOW_THRESHOLD = 6003

    # Erreurs de CI/CD (7000-7999)
    CI_PIPELINE_FAILED = 7000
    BUILD_FAILED = 7001
    DEPLOYMENT_FAILED = 7002
    CONFIGURATION_INVALID = 7003

    # Erreurs de sécurité (8000-8999)
    SECURITY_VIOLATION = 8000
    AUTHENTICATION_FAILED = 8001
    AUTHORIZATION_DENIED = 8002
    VULNERABILITY_DETECTED = 8003

    # Erreurs de performance (9000-9999)
    PERFORMANCE_DEGRADED = 9000
    MEMORY_EXHAUSTED = 9001
    CPU_OVERLOAD = 9002
    TIMEOUT_EXCEEDED = 9003


class ErrorSeverity(Enum):
    """Niveaux de sévérité des erreurs."""
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


# Mapping des codes d'erreur vers leurs descriptions
ERROR_DESCRIPTIONS: Dict[ErrorCode, str] = {
    ErrorCode.UNKNOWN_ERROR: "Erreur inconnue",
    ErrorCode.INVALID_INPUT: "Données d'entrée invalides",
    ErrorCode.MISSING_REQUIRED_PARAMETER: "Paramètre requis manquant",
    ErrorCode.INVALID_CONFIGURATION: "Configuration invalide",
    ErrorCode.PERMISSION_DENIED: "Permission refusée",
    ErrorCode.FILE_NOT_FOUND: "Fichier introuvable",
    ErrorCode.FILE_ACCESS_DENIED: "Accès au fichier refusé",
    ErrorCode.FILE_CORRUPTED: "Fichier corrompu",
    ErrorCode.DIRECTORY_NOT_FOUND: "Répertoire introuvable",
    ErrorCode.INSUFFICIENT_DISK_SPACE: "Espace disque insuffisant",
    ErrorCode.MODULE_NOT_FOUND: "Module introuvable",
    ErrorCode.MODULE_IMPORT_ERROR: "Erreur d'importation du module",
    ErrorCode.MODULE_INITIALIZATION_FAILED: "Échec d'initialisation du module",
    ErrorCode.MODULE_DEPENDENCY_MISSING: "Dépendance du module manquante",
    ErrorCode.AI_MODEL_NOT_AVAILABLE: "Modèle IA non disponible",
    ErrorCode.AI_MODEL_LOAD_FAILED: "Échec du chargement du modèle IA",
    ErrorCode.AI_RESPONSE_TIMEOUT: "Timeout de la réponse IA",
    ErrorCode.AI_RESPONSE_INVALID: "Réponse IA invalide",
    ErrorCode.AI_PROVIDER_UNAVAILABLE: "Fournisseur IA indisponible",
    ErrorCode.GENERATION_FAILED: "Échec de la génération",
    ErrorCode.BLUEPRINT_INVALID: "Blueprint invalide",
    ErrorCode.TEMPLATE_NOT_FOUND: "Template introuvable",
    ErrorCode.GENERATION_TIMEOUT: "Timeout de génération",
    ErrorCode.TEST_FAILED: "Test échoué",
    ErrorCode.TEST_TIMEOUT: "Timeout de test",
    ErrorCode.TEST_ENVIRONMENT_INVALID: "Environnement de test invalide",
    ErrorCode.COVERAGE_BELOW_THRESHOLD: "Couverture de tests insuffisante",
    ErrorCode.CI_PIPELINE_FAILED: "Pipeline CI échoué",
    ErrorCode.BUILD_FAILED: "Build échoué",
    ErrorCode.DEPLOYMENT_FAILED: "Déploiement échoué",
    ErrorCode.CONFIGURATION_INVALID: "Configuration invalide",
    ErrorCode.SECURITY_VIOLATION: "Violation de sécurité",
    ErrorCode.AUTHENTICATION_FAILED: "Échec d'authentification",
    ErrorCode.AUTHORIZATION_DENIED: "Autorisation refusée",
    ErrorCode.VULNERABILITY_DETECTED: "Vulnérabilité détectée",
    ErrorCode.PERFORMANCE_DEGRADED: "Performance dégradée",
    ErrorCode.MEMORY_EXHAUSTED: "Mémoire épuisée",
    ErrorCode.CPU_OVERLOAD: "Surcharge CPU",
    ErrorCode.TIMEOUT_EXCEEDED: "Timeout dépassé",
}


def get_error_description(error_code: ErrorCode) -> str:
    """Récupère la description d'un code d'erreur."""
    return ERROR_DESCRIPTIONS.get(error_code, "Description non disponible")


def get_error_severity(error_code: ErrorCode) -> ErrorSeverity:
    """Détermine la sévérité d'un code d'erreur."""
    severity_mapping = {
        # Erreurs critiques
        ErrorCode.UNKNOWN_ERROR: ErrorSeverity.CRITICAL,
        ErrorCode.FILE_CORRUPTED: ErrorSeverity.CRITICAL,
        ErrorCode.MODULE_INITIALIZATION_FAILED: ErrorSeverity.CRITICAL,
        ErrorCode.AI_MODEL_LOAD_FAILED: ErrorSeverity.CRITICAL,
        ErrorCode.SECURITY_VIOLATION: ErrorSeverity.CRITICAL,
        ErrorCode.MEMORY_EXHAUSTED: ErrorSeverity.CRITICAL,

        # Erreurs importantes
        ErrorCode.INVALID_CONFIGURATION: ErrorSeverity.ERROR,
        ErrorCode.PERMISSION_DENIED: ErrorSeverity.ERROR,
        ErrorCode.FILE_ACCESS_DENIED: ErrorSeverity.ERROR,
        ErrorCode.MODULE_DEPENDENCY_MISSING: ErrorSeverity.ERROR,
        ErrorCode.AI_PROVIDER_UNAVAILABLE: ErrorSeverity.ERROR,
        ErrorCode.GENERATION_FAILED: ErrorSeverity.ERROR,
        ErrorCode.TEST_FAILED: ErrorSeverity.ERROR,
        ErrorCode.CI_PIPELINE_FAILED: ErrorSeverity.ERROR,
        ErrorCode.BUILD_FAILED: ErrorSeverity.ERROR,
        ErrorCode.DEPLOYMENT_FAILED: ErrorSeverity.ERROR,
        ErrorCode.AUTHENTICATION_FAILED: ErrorSeverity.ERROR,
        ErrorCode.AUTHORIZATION_DENIED: ErrorSeverity.ERROR,
        ErrorCode.VULNERABILITY_DETECTED: ErrorSeverity.ERROR,
        ErrorCode.PERFORMANCE_DEGRADED: ErrorSeverity.ERROR,
        ErrorCode.CPU_OVERLOAD: ErrorSeverity.ERROR,

        # Avertissements
        ErrorCode.INVALID_INPUT: ErrorSeverity.WARNING,
        ErrorCode.MISSING_REQUIRED_PARAMETER: ErrorSeverity.WARNING,
        ErrorCode.FILE_NOT_FOUND: ErrorSeverity.WARNING,
        ErrorCode.DIRECTORY_NOT_FOUND: ErrorSeverity.WARNING,
        ErrorCode.INSUFFICIENT_DISK_SPACE: ErrorSeverity.WARNING,
        ErrorCode.MODULE_NOT_FOUND: ErrorSeverity.WARNING,
        ErrorCode.MODULE_IMPORT_ERROR: ErrorSeverity.WARNING,
        ErrorCode.AI_MODEL_NOT_AVAILABLE: ErrorSeverity.WARNING,
        ErrorCode.AI_RESPONSE_TIMEOUT: ErrorSeverity.WARNING,
        ErrorCode.AI_RESPONSE_INVALID: ErrorSeverity.WARNING,
        ErrorCode.BLUEPRINT_INVALID: ErrorSeverity.WARNING,
        ErrorCode.TEMPLATE_NOT_FOUND: ErrorSeverity.WARNING,
        ErrorCode.GENERATION_TIMEOUT: ErrorSeverity.WARNING,
        ErrorCode.TEST_TIMEOUT: ErrorSeverity.WARNING,
        ErrorCode.TEST_ENVIRONMENT_INVALID: ErrorSeverity.WARNING,
        ErrorCode.COVERAGE_BELOW_THRESHOLD: ErrorSeverity.WARNING,
        ErrorCode.CONFIGURATION_INVALID: ErrorSeverity.WARNING,
        ErrorCode.TIMEOUT_EXCEEDED: ErrorSeverity.WARNING,
    }

    return severity_mapping.get(error_code, ErrorSeverity.INFO)


def format_error_message(error_code: ErrorCode, details: str = "", context: Dict[str, Any] = None) -> str:
    """Formate un message d'erreur complet."""
    description = get_error_description(error_code)
    severity = get_error_severity(error_code)

    message = (f"[{severity.name}] {error_code.name} ({error_code.value}): "
               f"{description}")

    if details:
        message += f" - {details}"

    if context:
        context_str = ", ".join([f"{k}={v}" for k, v in context.items()])
        message += f" [Context: {context_str}]"

    return message
#!/usr/bin/env python3
"""
Module utilitaire pour l'exécution sécurisée de commandes subprocess
Remplace les appels subprocess non sécurisés par des versions sécurisées
"""

import logging
import subprocess
from typing import Any, Optional

logger = logging.getLogger(__name__)


def secure_subprocess_run(
    command: list[str], **kwargs: Any
) -> subprocess.CompletedProcess[Any]:
    """
    Exécute une commande de manière sécurisée.

    Args:
        command: Liste de commandes à exécuter
        **kwargs: Arguments supplémentaires pour subprocess.run

    Returns:
        CompletedProcess: Résultat de l'exécution

    Raises:
        ValueError: Si la commande contient des caractères dangereux
        subprocess.TimeoutExpired: Si la commande dépasse le timeout
    """
    # Paramètres de sécurité par défaut (typé Any pour compatibilité subprocess.run)
    safe_kwargs: dict[str, Any] = {
        "shell": False,  # Toujours False pour éviter l'injection de shell
        "check": False,
        "capture_output": True,
        "text": True,
        "timeout": 30,  # Timeout par défaut
    }

    # Fusion avec les kwargs fournis, en préservant la sécurité
    safe_kwargs.update(kwargs)
    safe_kwargs["shell"] = False  # Force shell=False pour la sécurité

    # Validation que la commande est une liste
    if not isinstance(command, list):
        raise ValueError("La commande doit être une liste pour la sécurité")

    # Vérification que la commande ne contient pas de caractères dangereux
    command_str = " ".join(command)
    dangerous_chars = [";", "&", "|", "`", "$", "(", ")", "{", "}", "[", "]"]
    if any(char in command_str for char in dangerous_chars):
        raise ValueError("La commande contient des caractères dangereux")

    try:
        return subprocess.run(command, **safe_kwargs)
    except subprocess.TimeoutExpired:
        logger.error(f"Timeout lors de l'exécution de la commande: {command}")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution de la commande: {e}")
        raise


def secure_subprocess_popen(
    command: list[str], **kwargs: Any
) -> subprocess.Popen[Any]:
    """
    Crée un processus de manière sécurisée.

    Args:
        command: Liste de commandes à exécuter
        **kwargs: Arguments supplémentaires pour subprocess.Popen

    Returns:
        Popen: Processus créé

    Raises:
        ValueError: Si la commande contient des caractères dangereux
    """
    # Paramètres de sécurité par défaut (typé Any pour compatibilité Popen)
    safe_kwargs_popen: dict[str, Any] = {
        "shell": False,  # Toujours False pour éviter l'injection de shell
        "text": True,
    }

    # Fusion avec les kwargs fournis, en préservant la sécurité
    safe_kwargs_popen.update(kwargs)
    safe_kwargs_popen["shell"] = False  # Force shell=False pour la sécurité

    # Validation que la commande est une liste
    if not isinstance(command, list):
        raise ValueError("La commande doit être une liste pour la sécurité")

    # Vérification que la commande ne contient pas de caractères dangereux
    command_str = " ".join(command)
    dangerous_chars = [";", "&", "|", "`", "$", "(", ")", "{", "}", "[", "]"]
    if any(char in command_str for char in dangerous_chars):
        raise ValueError("La commande contient des caractères dangereux")

    try:
        return subprocess.Popen(command, **safe_kwargs_popen)
    except Exception as e:
        logger.error(f"Erreur lors de la création du processus: {e}")
        raise


def validate_command_safety(command: list[str]) -> bool:
    """
    Valide qu'une commande est sûre à exécuter.

    Args:
        command: Liste de commandes à valider

    Returns:
        bool: True si la commande est sûre, False sinon
    """
    if not isinstance(command, list):
        return False  # type: ignore[unreachable]

    command_str = " ".join(command)
    dangerous_chars = [";", "&", "|", "`", "$", "(", ")", "{", "}", "[", "]"]

    return not any(char in command_str for char in dangerous_chars)


# Alias pour la compatibilité
secure_run = secure_subprocess_run
secure_popen = secure_subprocess_popen

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traductions françaises pour Athalia
"""

translations = {
    "welcome": "Bienvenue dans Athalia / Arkalia !",
    "project_generated": "Projet généré avec succès.",
    "error_occurred": "Une erreur est survenue.",
    "auth_required": "Authentification requise.",
    "invalid_api_key": "Clé API invalide."
}


def get_translation(lang='fr'):
    """Retourne les traductions françaises"""
    return {
        'error': 'Erreur inconnue',
        'ok': 'Opération réussie',
        'success': 'Succès',
        'hello': 'Bonjour',
        'bye': 'Au revoir',
        'welcome': 'Bienvenue',
        'project_generated': 'Projet généré avec succès',
        'error_occurred': 'Une erreur est survenue',
        'auth_required': 'Authentification requise',
        'invalid_api_key': 'Clé API invalide'
    }
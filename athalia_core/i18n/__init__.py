#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module d'internationalisation (i18n) pour Athalia
Gestion des traductions et localisation
"""

from . import fr, en

# Configuration par défaut
DEFAULT_LOCALE = "fr"
SUPPORTED_LOCALES = ["fr", "en"]

def get_translation(locale=DEFAULT_LOCALE):
    """Récupère les traductions pour une locale donnée"""
    if locale == "fr":
        return fr.translations
    elif locale == "en":
        return en.translations
    else:
        return fr.translations  # Fallback vers français

def translate(key, locale=DEFAULT_LOCALE, **kwargs):
    """Traduit une clé dans la locale spécifiée"""
    translations = get_translation(locale)
    text = translations.get(key, key)
    
    # Remplacement des variables
    for k, v in kwargs.items():
        text = text.replace(f"{{{k}}}", str(v))
    
    return text

def get_supported_locales():
    """Retourne la liste des locales supportées"""
    return SUPPORTED_LOCALES.copy() 
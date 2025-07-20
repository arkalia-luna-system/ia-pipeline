#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .en import get_translation as get_translation_en
from .fr import get_translation as get_translation_fr

def get_translation(lang: str = 'fr'):
    """Retourne le dictionnaire de traduction pour la langue donnée, avec fallback sur la clé 'error'."""
    if lang == 'en':
        translations = get_translation_en()
    else:
        translations = get_translation_fr()
    def get(key):
        return translations.get(key, translations.get('error', 'Erreur inconnue' if lang == 'fr' else 'Error unknown'))
    translations['get'] = get
    if 'error' not in translations:
        translations['error'] = 'Erreur inconnue' if lang == 'fr' else 'Error unknown'
    return translations
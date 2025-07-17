def get_translation(lang: str = 'fr'):
    """Retourne le dictionnaire de traduction pour la langue donnée."""
    if lang == 'en':
        from .en import translations
        return translations
    from .fr import translations
    return translations 
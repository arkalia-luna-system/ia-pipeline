def get_user_profile(name: str = 'default') -> dict:
    """Retourne le profil utilisateur (préférences, options par défaut)."""
    profiles = {
        'default': {
            'lang': 'fr',
            'ai_model': 'mistral',
            'auto_audit': True,
            'auto_fix': False,
            'dashboard': True
        },
        'dev': {
            'lang': 'en',
            'ai_model': 'claude',
            'auto_audit': True,
            'auto_fix': True,
            'dashboard': True
        }
    }
    return profiles.get(name, profiles['default']) 
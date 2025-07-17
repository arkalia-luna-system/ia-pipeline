def test_get_translation_fr():
    from athalia_core.i18n import get_translation
    tr = get_translation('fr')
    assert tr["welcome"].startswith("Bienvenue")
    assert tr["error"].startswith("Une erreur")

def test_get_translation_en():
    from athalia_core.i18n import get_translation
    tr = get_translation('en')
    assert tr["welcome"].startswith("Welcome")
    assert tr["error"].startswith("An error") 
from athalia_core.profiles import get_user_profile

def test_get_user_profile_default():
    profile = get_user_profile()
    assert profile['lang'] == 'fr'
    assert profile['ai_model'] == 'mistral'
    assert profile['auto_audit'] is True
    assert profile['auto_fix'] is False

def test_get_user_profile_dev():
    profile = get_user_profile('dev')
    assert profile['lang'] == 'en'
    assert profile['ai_model'] == 'claude'
    assert profile['auto_fix'] is True 
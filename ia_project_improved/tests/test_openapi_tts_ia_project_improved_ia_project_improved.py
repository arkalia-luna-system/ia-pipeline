import yaml
import os

def test_openapi_tts_ia_project_improved():
    path = os.path.join(os.path.dirname(__file__), '../openapi_tts.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert '/api/tts' in data['paths']

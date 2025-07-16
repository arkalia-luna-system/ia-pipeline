import yaml
import os

def test_openapi_ultra():
    path = os.path.join(os.path.dirname(__file__), '../openapi.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert 'ApiKeyAuth' in data['components']['securitySchemes']
    assert 'OAuth2' in data['components']['securitySchemes']
    for path, val in data['paths'].items():
        assert 'post' in val
        assert 'responses' in val['post']
        assert '200' in val['post']['responses']
        assert any(code in val['post']['responses'] for code in ['400','401','404','422'])

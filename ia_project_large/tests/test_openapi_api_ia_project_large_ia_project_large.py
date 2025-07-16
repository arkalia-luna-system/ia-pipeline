import yaml
import os

def test_openapi_api_ia_project_large():
    path = os.path.join(os.path.dirname(__file__), '../openapi_api.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert '/api/api' in data['paths']

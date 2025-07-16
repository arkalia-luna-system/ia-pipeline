import yaml
import os

def test_openapi_memory_ia_project():
    path = os.path.join(os.path.dirname(__file__), '../openapi_memory.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert '/api/memory' in data['paths']

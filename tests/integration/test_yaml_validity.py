import os
import yaml
import glob

def test_all_openapi_yaml_valid():
    # Cherche tous les openapi.yaml et openapi_*.yaml dans le repo
    for root, dirs, files in os.walk('.'):
        for fname in files:
            if fname.startswith('openapi') and fname.endswith('.yaml'):
                path = os.path.join(root, fname)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        data = yaml.safe_load(f)
                        assert isinstance(data, dict)
                    except Exception as e:
                        raise AssertionError(f"YAML invalide dans {path}: {e}") 
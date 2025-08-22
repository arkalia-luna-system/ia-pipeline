# 🔧 Fixtures de Tests
**Dossier :** `tests/fixtures/`
**Objectif :** Données et objets partagés entre les tests

## 📁 Structure

```
tests/fixtures/
├── __init__.py
├── test_data/              # Données de test
└── mock_objects/           # Objets mock
```

## 🎯 Utilisation

### **Données de Test**
Le dossier `test_data/` contient :
- Fichiers de configuration de test
- Données d'exemple
- Templates de test

### **Objets Mock**
Le dossier `mock_objects/` contient :
- Objets mock pour les tests
- Stubs de services
- Mocks de dépendances externes

## 🚀 Exemples

```python
# Utilisation dans les tests
from tests.fixtures.test_data import sample_config
from tests.fixtures.mock_objects import mock_api_client

def test_with_fixture():
    config = sample_config()
    client = mock_api_client()
    # Test avec les fixtures
```

## 📊 Statut

- **Phase** : Structure créée
- **Contenu** : À développer selon les besoins
- **Documentation** : En cours 
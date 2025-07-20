# Documentation API - projet_ia_exemple

## Endpoints

### GET /
Point d'entrée de l'API

**Réponse:**
```json
{
  "message": "Bienvenue sur projet_ia_exemple API"
}
```

## Utilisation

### Avec curl
```bash
curl http://localhost:8000/
```

### Avec Python
```python
import requests

response = requests.get('http://localhost:8000/')
print(response.json())
```

## Développement

Pour lancer l'API en mode développement:

```bash
uvicorn src.main:app --reload
```

L'API sera disponible sur http://localhost:8000
La documentation interactive sera sur http://localhost:8000/docs

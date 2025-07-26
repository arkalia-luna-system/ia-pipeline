# 🎨 Documentation des Templates Athalia

## 📋 Vue d'ensemble

Les templates Athalia sont des modèles de code pré-configurés qui permettent de générer rapidement des projets avec une architecture standardisée et des bonnes pratiques intégrées.

## 🏗️ Architecture des Templates

### Structure des Templates
```
templates/
├── main.py.j2          # Point d'entrée principal
├── memory.py.j2        # Système de mémoire
├── tts.py.j2          # Synthèse vocale
└── api/
    └── main.py.j2     # API REST
```

### Variables Disponibles

#### Variables Globales
- `project_name` : Nom du projet
- `project_description` : Description du projet
- `author` : Auteur du projet
- `version` : Version du projet
- `description` : Description du projet

#### Variables Spécifiques
- `api_framework` : Framework API (flask, fastapi, django)
- `endpoints` : Liste des endpoints API
- `memory_type` : Type de mémoire (redis, sqlite, file)
- `tts_engine` : Moteur TTS (gtts, pyttsx3, azure)

## 🔧 Utilisation des Templates

### Génération de Projet
```python
from athalia_core.templates.base_templates import get_base_templates

templates = get_base_templates()
api_template = templates["api/main.py"]

# Rendu du template
from jinja2 import Template
template = Template(api_template)
result = template.render(
    project_name="mon_projet",
    api_framework="flask",
    endpoints=["users", "products"]
)
```

### Variables Requises
Chaque template nécessite des variables spécifiques :

#### Template API
- `project_name` : Nom du projet
- `api_framework` : Framework utilisé
- `endpoints` : Liste des endpoints

#### Template Memory
- `memory_type` : Type de stockage
- `project_name` : Nom du projet

#### Template TTS
- `tts_engine` : Moteur TTS
- `project_name` : Nom du projet

## 📝 Variables Disponibles

### Variables Globales
| Variable | Type | Description | Exemple |
|----------|------|-------------|---------|
| `project_name` | str | Nom du projet | "mon_projet" |
| `author` | str | Auteur | "John Doe" |
| `version` | str | Version | "1.0.0" |
| `description` | str | Description | "Projet IA" |

### Variables API
| Variable | Type | Description | Exemple |
|----------|------|-------------|---------|
| `api_framework` | str | Framework API | "flask" |
| `endpoints` | list | Endpoints | ["users", "products"] |
| `port` | int | Port API | 8000 |

### Variables Memory
| Variable | Type | Description | Exemple |
|----------|------|-------------|---------|
| `memory_type` | str | Type mémoire | "redis" |
| `max_size` | int | Taille max | 1000 |

### Variables TTS
| Variable | Type | Description | Exemple |
|----------|------|-------------|---------|
| `tts_engine` | str | Moteur TTS | "gtts" |
| `language` | str | Langue | "fr" |

## 🎯 Exemples d'Utilisation

### Exemple 1 : Génération d'API Flask
```python
template = Template(templates["api/main.py"])
api_code = template.render(
    project_name="api_rest",
    api_framework="flask",
    endpoints=["users", "products", "orders"],
    port=8000
)
```

### Exemple 2 : Génération de Gestionnaire Mémoire
```python
template = Template(templates["memory/memory.py"])
memory_code = template.render(
    project_name="smart_memory",
    memory_type="redis",
    max_size=1000
)
```

### Créer un système TTS
```python
template = Template(templates["tts/tts.py"])
tts_code = template.render(
    project_name="voice_assistant",
    tts_engine="gtts",
    language="fr"
)
```

## 🔍 Validation des Templates

### Tests Automatiques
Les templates sont validés automatiquement :
- Syntaxe Jinja2 correcte
- Variables requises définies
- Génération de code valide

### Tests Manuels
```bash
# Tester un template
python -m pytest tests/test_templates_documentation.py -v
```

## 🚨 Dépannage

### Problèmes Courants

### Erreurs Communes

#### Variable Manquante
```
Error: Variable 'project_name' not defined
```
**Solution :** Définir toutes les variables requises

#### Template Non Trouvé
```
Error: Template 'api/main.py' not found
```
**Solution :** Vérifier que le template existe dans `templates/`

#### Rendu Incorrect
```
Error: Template rendering failed
```
**Solution :** Vérifier la syntaxe Jinja2 du template

### Bonnes Pratiques

1. **Toujours définir les variables requises**
2. **Tester les templates avant utilisation**
3. **Documenter les nouvelles variables**
4. **Valider le code généré**

## 📚 Références

- [Documentation Jinja2](https://jinja.palletsprojects.com/)
- [Guide des Templates](https://docs.athalia.dev/templates)
- [Exemples de Projets](https://github.com/athalia/examples) 
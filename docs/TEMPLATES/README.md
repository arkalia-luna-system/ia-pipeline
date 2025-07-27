# 🎨 Documentation des Templates Athalia

## 📋 Vue d'ensemble

Cette section documente tous les templates disponibles dans Athalia pour la génération automatique de code.

## 📁 Structure des Templates

```
templates/
├── api/
│   └── main.py.j2          # Template API Flask
├── web/
│   └── app.py.j2           # Template application web
├── cli/
│   └── main.py.j2          # Template CLI
└── docs/
    └── README.md.j2        # Template documentation
```

## 🔧 Templates Disponibles

### API Templates

#### `templates/api/main.py.j2`
Template pour générer une API Flask complète.

**Variables disponibles :**
- `project_name` : Nom du projet
- `author` : Auteur du projet
- `version` : Version du projet
- `timestamp` : Timestamp de génération

**Fonctionnalités :**
- Points de terminaison de santé
- API REST basique
- Logging configuré
- Gestion d'erreurs

### Web Templates

#### `templates/web/app.py.j2`
Template pour applications web Streamlit.

### CLI Templates

#### `templates/cli/main.py.j2`
Template pour applications CLI avec Click.

## 🚀 Utilisation

```python
from athalia_core.templates import TemplateManager

# Créer une instance
tm = TemplateManager()

# Générer un template
result = tm.generate_template(
    template_name="api/main.py.j2",
    context={
        "project_name": "mon-projet",
        "author": "Alice Developer",
        "version": "1.0.0"
    }
)
```

## 📝 Variables Globales

Tous les templates ont accès aux variables suivantes :

- `project_name` : Nom du projet
- `author` : Auteur
- `version` : Version
- `timestamp` : Timestamp de génération
- `description` : Description du projet

## 🔄 Mise à jour

Pour ajouter un nouveau template :

1. Créer le fichier `.j2` dans le dossier approprié
2. Documenter les variables disponibles
3. Ajouter un exemple d'utilisation
4. Mettre à jour cette documentation

## 📚 Exemples

Voir le dossier `examples/` pour des exemples d'utilisation complets. 
# 🎨 Documentation des Templates Athalia

## 📋 Vue d'ensemble

Cette section documente tous les templates disponibles dans Athalia pour la génération automatique de code.

## 🏗️ Architecture des Templates

L'architecture des templates suit une structure modulaire permettant la génération de différents types de projets.

## 📁 Structure des Templates

```
templates/
├── api/
│   └── main.py.j2          # Template API Flask
├── memory/
│   └── memory.py.j2        # Template système de mémoire
├── tts/
│   └── tts.py.j2           # Template Text-to-Speech
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
- `project_description` : Description du projet

**Fonctionnalités :**
- Points de terminaison de santé
- API REST basique
- Logging configuré
- Gestion d'erreurs

### Memory Templates

#### `templates/memory/memory.py.j2`
Template pour système de mémoire et gestion des données.

### TTS Templates

#### `templates/tts/tts.py.j2`
Template pour système Text-to-Speech.

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
        "version": "11.0.0",
        "project_description": "Description du projet"
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
- `project_description` : Description détaillée du projet

## 🎯 Exemples d'Utilisation

### Exemple 1 : Génération d'API Flask
```python
context = {
    "project_name": "mon-api",
    "author": "Alice Developer",
    "version": "11.0.0",
    "project_description": "API REST pour gestion des utilisateurs"
}
```

### Exemple 2 : Génération de Gestionnaire Mémoire
```python
context = {
    "project_name": "mon-cli",
    "author": "Bob Developer",
    "version": "2.0.0",
    "project_description": "Interface en ligne de commande"
}
```

## 🚨 Dépannage

### Problèmes Courants

1. **Template non trouvé** : Vérifier que le fichier `.j2` existe dans le bon dossier
2. **Variables manquantes** : S'assurer que toutes les variables requises sont fournies
3. **Erreur de syntaxe** : Vérifier la syntaxe Jinja2 dans le template

### Solutions

- Consulter la documentation des variables disponibles
- Vérifier les exemples d'utilisation
- Tester avec un contexte minimal

## 🔄 Mise à jour

Pour ajouter un nouveau template :

1. Créer le fichier `.j2` dans le dossier approprié
2. Documenter les variables disponibles
3. Ajouter un exemple d'utilisation
4. Mettre à jour cette documentation

## 📚 Exemples

Voir le dossier `examples/` pour des exemples d'utilisation complets.

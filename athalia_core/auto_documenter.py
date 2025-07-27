#!/usr/bin/env python3
from pathlib import Path
from typing import Dict, List, Any
import json
import os
import re
import argparse
from datetime import datetime
import ast
import importlib
import logging

logger = logging.getLogger(__name__)

"""
Module de documentation automatique pour Athalia
Génération automatique de README, docs API et guides techniques
"""


class AutoDocumenter:
    """Générateur de documentation automatique"""

    project_info: Dict[str, Any]
    api_docs: Dict[str, Any]

    def __init__(self, project_path: str = None, lang: str = 'fr'):
        self.project_path: Path = Path(
            project_path) if project_path else Path('.')
        self.project_info = {}
        self.api_docs = {}
        self.readme_content = ""
        self.lang = lang
        self.translations = self._load_translations(lang)

    def _load_translations(self, lang: str):
        try:
            mod = importlib.import_module(f"athalia_core.i18n.{lang}")
            return getattr(mod, "translations", {})
        except Exception:
            return {}

    def run(self) -> Dict[str, Any]:
        """Méthode run() pour l'orchestrateur - exécute la documentation"""
        if not self.project_path:
            raise ValueError("project_path doit être défini")
        return self.document_project(str(self.project_path))

    def document_project(self, project_path: str) -> Dict[str, Any]:
        """Documentation complète d'un projet"""
        self.project_path = Path(project_path)

        logger.info(
            f"📚 {self.translations.get('doc_generation', 'Génération de documentation pour')} : "
            f"{self.project_path.name}")

        # Analyse du projet
        self._analyze_project()

        # Génération des documents
        readme = self._generate_readme()
        api_docs = self._generate_api_documentation()
        setup_guide = self._generate_setup_guide()
        usage_guide = self._generate_usage_guide()

        # Sauvegarde des documents
        self._save_documents(readme, api_docs, setup_guide, usage_guide)

        return {
            "readme": readme,
            "api_docs": api_docs,
            "setup_guide": setup_guide,
            "usage_guide": usage_guide,
            "created_files": self._get_created_files()
        }

    def _analyze_project(self):
        """Analyse du projet pour la documentation"""
        if not self.project_path:
            raise ValueError("project_path doit être défini avant l'analyse")

        # Analyser d'abord les modules
        modules = self._analyze_modules()

        self.project_info = {
            "name": self.project_path.name,
            "description": self._extract_description(),
            "version": self._extract_version(),
            "author": self._extract_author(),
            "license": self._extract_license(),
            "dependencies": self._extract_dependencies(),
            "entry_points": self._find_entry_points(),
            "modules": modules,
            "classes": self._analyze_classes(modules),
            "functions": self._analyze_functions(modules)
        }

    def _extract_description(self) -> str:
        """Extrait la description du projet"""
        # Chercher dans README existant
        readme_files = list(self.project_path.glob("README*"))
        if readme_files:
            try:
                with open(readme_files[0], 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extraire la première ligne non vide
                    lines = [line.strip()
                             for line in content.split('\n') if line.strip()]
                    if lines:
                        return lines[0]
            except Exception:
                pass

        # Chercher dans setup.py ou pyproject.toml
        setup_file = self.project_path / "setup.py"
        if setup_file.exists():
            try:
                with open(setup_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(
                        r'description\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        return match.group(1)
            except Exception:
                pass

        return f"Projet {self.project_path.name}"

    def _extract_version(self) -> str:
        """Extrait la version du projet"""
        # Chercher dans __init__.py
        init_file = self.project_path / "__init__.py"
        if init_file.exists():
            try:
                with open(init_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(
                        r'__version__\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        return match.group(1)
            except Exception:
                pass

        # Chercher dans setup.py
        setup_file = self.project_path / "setup.py"
        if setup_file.exists():
            try:
                with open(setup_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(
                        r'version\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        return match.group(1)
            except Exception:
                pass

        return "1.0.0"

    def _extract_author(self) -> str:
        """Extrait l'auteur du projet"""
        # Chercher dans setup.py
        setup_file = self.project_path / "setup.py"
        if setup_file.exists():
            try:
                with open(setup_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(
                        r'author\s*=\s*["\']([^"\']+)["\']', content)
                    if match:
                        return match.group(1)
            except Exception:
                pass

        return "Auteur inconnu"

    def _extract_license(self) -> str:
        """Extrait la licence du projet"""
        license_files = list(self.project_path.glob("LICENSE*"))
        if license_files:
            return "Voir fichier LICENSE"

        return "Licence inconnue"

    def _extract_dependencies(self) -> Dict[str, List[str]]:
        """Extrait les dépendances du projet"""
        dependencies = {}

        # Python
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file, 'r') as f:
                    deps = [line.strip() for line in f if line.strip()
                            and not line.startswith('#')]
                    dependencies['python'] = deps
            except Exception:
                pass

        # Node.js
        package_file = self.project_path / "package.json"
        if package_file.exists():
            try:
                with open(package_file, 'r') as f:
                    data = json.load(f)
                    deps = list(data.get('dependencies', {}).keys())
                    dev_deps = list(data.get('devDependencies', {}).keys())
                    dependencies['nodejs'] = deps + dev_deps
            except Exception:
                pass

        return dependencies

    def _find_entry_points(self) -> List[str]:
        """Trouve les points d'entrée du projet"""
        entry_points = []

        # Chercher les fichiers main
        main_patterns = ["main.py", "app.py", "run.py", "server.py", "cli.py"]
        for pattern in main_patterns:
            main_file = self.project_path / pattern
            if main_file.exists():
                entry_points.append(str(main_file))

        # Chercher dans setup.py
        setup_file = self.project_path / "setup.py"
        if setup_file.exists():
            try:
                with open(setup_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = re.findall(
                        r'entry_points.*?\[(.*?)\]', content, re.DOTALL)
                    for match in matches:
                        entry_points.extend(
                            [ep.strip() for ep in match.split(',') if ep.strip()])
            except Exception:
                pass

        return entry_points

    def _analyze_modules(self) -> List[Dict[str, Any]]:
        """Analyse les modules du projet"""
        modules = []
        for py_file in self.project_path.rglob("*.py"):
            if py_file.name != "__init__.py":
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        tree = ast.parse(f.read())

                    module_info = {
                        "name": py_file.stem,
                        "docstring": ast.get_docstring(tree) or "",
                        "classes": [],  # Initialisé comme liste mutable
                        "functions": []  # Initialisé comme liste mutable
                    }

                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            module_info["classes"].append({
                                "name": node.name,
                                "docstring": ast.get_docstring(node) or "",
                                "methods": [
                                    m.name for m in node.body
                                    if isinstance(m, ast.FunctionDef)
                                ]
                            })
                        elif isinstance(node, ast.FunctionDef):
                            module_info["functions"].append({
                                "name": node.name,
                                "docstring": ast.get_docstring(node) or "",
                                "args": [
                                    arg.arg for arg in node.args.args
                                    if arg.arg != 'self'
                                ]
                            })

                    modules.append(module_info)
                except Exception as e:
                    logger.warning(f"Could not analyze module {py_file}: {e}")
        return modules

    def _analyze_classes(
            self, modules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyse les classes du projet"""
        classes = []

        for module in modules:
            for class_info in module["classes"]:
                classes.append({
                    "name": class_info["name"],
                    "module": module["name"],
                    "docstring": class_info["docstring"],
                    "methods": class_info["methods"]
                })

        return classes

    def _analyze_functions(
            self, modules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyse les fonctions du projet"""
        functions = []

        for module in modules:
            for func_info in module["functions"]:
                functions.append({
                    "name": func_info["name"],
                    "module": module["name"],
                    "docstring": func_info["docstring"],
                    "args": func_info["args"]
                })

        return functions

    def _generate_readme(self) -> str:
        """Génère le README du projet"""
        t = self.translations
        current_date = datetime.now().strftime("%Y-%m-%d")

        readme = """# {project_name}

{description}

## {table_of_contents}

- [{installation}](#installation)
- [{usage}](#utilisation)
- [API](#api)
- [{tests}](#tests)
- [{contribution}](#contribution)
- [{license}](#licence)

## 🚀 {installation}

### {prerequisites}
"""
        readme = readme.format(
            project_name=self.project_info['name'],
            description=self.project_info['description'],
            table_of_contents=t.get(
                'table_of_contents',
                '📋 Table des matières'),
            installation=t.get(
                'installation',
                'Installation'),
            usage=t.get(
                'usage',
                'Utilisation'),
            tests=t.get(
                'tests',
                'Tests'),
            contribution=t.get(
                'contribution',
                'Contribution'),
            license=t.get(
                'license',
                'Licence'),
            prerequisites=t.get(
                'prerequisites',
                'Prérequis'))

        # Dépendances
        if self.project_info["dependencies"].get("python"):
            readme += "**Python :**\n"
            for dep in self.project_info["dependencies"]["python"][:5]:
                readme += f"- {dep}\n"
            readme += "\n"
        if self.project_info["dependencies"].get("nodejs"):
            readme += "**Node.js :**\n"
            for dep in self.project_info["dependencies"]["nodejs"][:5]:
                readme += f"- {dep}\n"
            readme += "\n"

        readme += """### {installation_step}

```bash
# Cloner le repository
git clone <repository - url>
cd {project_name}

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 {usage}
""".format(
            installation_step=t.get('installation_step', 'Installation'),
            project_name=self.project_info['name'],
            usage=t.get('usage', 'Utilisation')
        )

        # Points d'entrée
        if self.project_info["entry_points"]:
            readme += "### Lancement\n\n"
            for entry_point in self.project_info["entry_points"]:
                readme += f"```bash\npython {entry_point}\n```\n\n"

        readme += """### Exemple d'utilisation

```python
# Utilisation basique
main()
```

## 🔧 API
"""

        # Classes principales
        if self.project_info["classes"]:
            readme += "### Classes principales\n\n"
            for class_info in self.project_info["classes"][:3]:
                readme += f"#### {class_info['name']}\n\n"
                if class_info["docstring"]:
                    readme += f"{class_info['docstring']}\n\n"
                readme += f"**Méthodes :** {', '.join(class_info['methods'][:5])}\n\n"

        # Fonctions principales
        if self.project_info["functions"]:
            readme += "### Fonctions principales\n\n"
            for func_info in self.project_info["functions"][:5]:
                readme += f"#### {func_info['name']}\n\n"
                if func_info["docstring"]:
                    readme += f"{func_info['docstring']}\n\n"
                if func_info["args"]:
                    readme += f"**Paramètres :** {', '.join(func_info['args'])}\n\n"

        readme += """## 🧪 {tests}

```bash
# Lancer les tests
python -m pytest

# Avec couverture
python -m pytest --cov={project_name}
```

## 🤝 {contribution}

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature / AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature / AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 {license}

{license_content}

---
""".format(
            tests=t.get('tests', 'Tests'),
            project_name=self.project_info['name'],
            contribution=t.get('contribution', 'Contribution'),
            license=t.get('license', 'Licence'),
            license_content=self.project_info['license']
        )
        readme += "*Généré automatiquement par Athalia* - {}\n".format(
            current_date)
        return readme

    def _generate_api_documentation(self) -> str:
        """Génère la documentation API du projet"""
        t = self.translations
        api_title = (
            f"# {t.get('api_documentation', 'API Documentation')} - "
            f"{self.project_info['name']}"
        )
        api_docs = f"""{api_title}

## Vue d'ensemble

Cette documentation décrit l'API de {self.project_info['name']}.

## Modules

"""

        for module in self.project_info["modules"]:
            api_docs += f"### {module['name']}\n\n"
            if module["docstring"]:
                api_docs += f"{module['docstring']}\n\n"

            # Classes du module
            if module["classes"]:
                api_docs += "#### Classes\n\n"
                for class_info in module["classes"]:
                    api_docs += f"##### {class_info['name']}\n\n"
                    if class_info["docstring"]:
                        api_docs += f"{class_info['docstring']}\n\n"

                    if class_info["methods"]:
                        api_docs += "**Méthodes :**\n\n"
                        for method in class_info["methods"]:
                            api_docs += f"- `{method}()`\n"
                        api_docs += "\n"

            # Fonctions du module
            if module["functions"]:
                api_docs += "#### Fonctions\n\n"
                for func_info in module["functions"]:
                    api_docs += f"##### {func_info['name']}\n\n"
                    if func_info["docstring"]:
                        api_docs += f"{func_info['docstring']}\n\n"

                    if func_info["args"]:
                        api_docs += "**Paramètres :**\n\n"
                        for arg in func_info["args"]:
                            api_docs += f"- `{arg}`\n"
                        api_docs += "\n"

            api_docs += "---\n\n"

        return api_docs

    def _generate_setup_guide(self) -> str:
        """Génère le guide d'installation du projet"""
        t = self.translations
        current_date = datetime.now().strftime("%Y-%m-%d")

        setup_guide = """# {setup_guide} - {project_name}

## Vue d'ensemble

Ce guide explique comment installer et configurer {project_name}.

## Prérequis

- Python >= 3.8
- Dépendances listées dans requirements.txt

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Le projet utilise un fichier de configuration YAML :

```yaml
# config.yml
app:
  name: {project_name}
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Lancement rapide

```bash
python main.py
```

---
""".format(
            setup_guide=t.get('setup_guide', 'Guide d\'installation'),
            project_name=self.project_info['name']
        )
        setup_guide += "*Généré automatiquement par Athalia* - {}\n".format(
            current_date)
        return setup_guide

    def _generate_usage_guide(self) -> str:
        """Génère le guide d'utilisation du projet"""
        t = self.translations
        current_date = datetime.now().strftime("%Y-%m-%d")

        usage_guide = """# {usage_guide} - {project_name}

## Vue d'ensemble

Ce guide explique comment utiliser {project_name}.

## Configuration

```yaml
name: {project_name}
version: {version}
description: {description}
```

### Lancement rapide

```bash
# Mode développement
python main.py

# Mode production
python main.py --production
```

### Configuration

Le projet utilise un fichier de configuration YAML :

```yaml
# config.yml
app:
  name: {project_name}
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Fonctionnalités principales

""".format(
            usage_guide=t.get('usage_guide', 'Guide d\'utilisation'),
            project_name=self.project_info['name'],
            version=self.project_info['version'],
            description=self.project_info['description']
        )

        # Décrire les classes principales
        if self.project_info["classes"]:
            usage_guide += "### Classes principales\n\n"
            for class_info in self.project_info["classes"][:3]:
                usage_guide += f"#### {class_info['name']}\n\n"
                if class_info["docstring"]:
                    usage_guide += f"{class_info['docstring']}\n\n"
                usage_guide += "**Exemple d'utilisation :**\n\n"
                usage_guide += "```python\n"
                usage_guide += f"from {self.project_info['name']} import {class_info['name']}\n\n"
                usage_guide += "# Créer une instance\n"
                usage_guide += f"instance = {class_info['name']}()\n"
                if class_info["methods"]:
                    usage_guide += (
                        f"# Utiliser une méthode\n"
                        f"result = instance.{class_info['methods'][0]}()\n"
                    )
                usage_guide += "```\n\n"

        # Décrire les fonctions principales
        if self.project_info["functions"]:
            usage_guide += "### Fonctions utilitaires\n\n"
            for func_info in self.project_info["functions"][:5]:
                usage_guide += f"#### {func_info['name']}\n\n"
                if func_info["docstring"]:
                    usage_guide += f"{func_info['docstring']}\n\n"
                usage_guide += "**Exemple d'utilisation :**\n\n"
                usage_guide += "```python\n"
                usage_guide += f"from {self.project_info['name']} import {func_info['name']}\n\n"
                if func_info["args"]:
                    args_str = ", ".join(
                        (f"{arg}" for arg in func_info["args"]))
                    usage_guide += f"result = {func_info['name']}({args_str})\n"
                else:
                    usage_guide += f"result = {func_info['name']}()\n"
                usage_guide += "```\n\n"

        usage_guide += """
## Cas d'usage avancés

### Intégration avec d'autres outils

```python
# Exemple d'intégration

# Configuration personnalisée
config = {
    'option1': 'value1',
    'option2': 'value2'
}

# Utilisation
app = main_class(config)
app.run()
```

### Gestion des erreurs

```python
try:
    result = some_function()
except Exception as e:
    logger.info(f"Erreur: {e}")
    # Gestion de l'erreur
```

## Bonnes pratiques

1. **Toujours utiliser un environnement virtuel**
2. **Vérifier la configuration avant le lancement**
3. **Utiliser les logs pour le débogage**
4. **Tester les nouvelles fonctionnalités**

## Support et assistance

- Documentation API complète
- Signaler un bug
- Proposer une amélioration
- Contact : support@example.com

---
"""
        usage_guide += "*Généré automatiquement par Athalia* - {}\n".format(
            current_date)
        return usage_guide

    def _save_documents(
            self,
            readme: str,
            api_docs: str,
            setup_guide: str,
            usage_guide: str):
        """Sauvegarde les documents générés"""
        current_date = datetime.now().strftime('%Y-%m-%d')
        t = self.translations

        docs_dir = self.project_path / "docs"
        docs_dir.mkdir(exist_ok=True)

        # README principal
        readme_file = self.project_path / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme)

        # Documentation API
        api_file = docs_dir / "API.md"
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write(api_docs)

        # Guide d'installation
        setup_file = docs_dir / "INSTALLATION.md"
        with open(setup_file, 'w', encoding='utf-8') as f:
            f.write(setup_guide)

        # Guide d'utilisation
        usage_file = docs_dir / "USAGE.md"
        with open(usage_file, 'w', encoding='utf-8') as f:
            f.write(usage_guide)

        # Index de documentation
        setup_guide_text = t.get('setup_guide', 'Guide d\'installation')
        usage_guide_text = t.get('usage_guide', 'Guide d\'utilisation')
        api_doc_text = t.get('api_documentation', 'Documentation API')
        setup_desc = t.get(
            'setup_guide_description',
            'Comment installer et configurer le projet')
        usage_desc = t.get(
            'usage_guide_description',
            'Comment utiliser les fonctionnalités')
        api_desc = t.get(
            'api_documentation_description',
            'Référence complète de l\'API')
        doc_index = t.get('documentation_index', 'Index de documentation')

        index_content = f"""# {doc_index} - {self.project_info['name']}

## 📚 Guides disponibles

- [{setup_guide_text}](INSTALLATION.md) - {setup_desc}
- [{usage_guide_text}](USAGE.md) - {usage_desc}
- [{api_doc_text}](API.md) - {api_desc}

## 🚀 Démarrage rapide

1. Suivez le [{setup_guide_text}](INSTALLATION.md)
2. Consultez le [{usage_guide_text}](USAGE.md)
3. Explorez l'[{api_doc_text}](API.md) pour les fonctionnalités avancées

---
*Généré automatiquement par Athalia* - {current_date}
"""

        index_file = docs_dir / "README.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)

    def _get_created_files(self) -> List[str]:
        files = [
            "README.md",
            "docs/API.md",
            "docs/INSTALLATION.md",
            "docs/USAGE.md"
        ]
        return [str(self.project_path / f) for f in files]


def main():
    """Point d'entrée du script"""

    parser = argparse.ArgumentParser(
        description="Génération automatique de documentation")
    parser.add_argument("project_path", help="Chemin du projet à documenter")
    parser.add_argument(
        "--lang",
        default="fr",
        help="Langue pour la génération de la documentation (fr, en, es, etc.)")

    args = parser.parse_args()

    if not os.path.exists(args.project_path):
        logger.info(f"❌ Le chemin {args.project_path} n'existe pas")
        return

    documenter = AutoDocumenter(args.project_path, args.lang)
    result = documenter.run()

    logger.info("✅ Documentation générée avec succès !")
    logger.info("\n📄 Fichiers créés :")
    for file_path in result["created_files"]:
        logger.info(f"   • {file_path}")


if __name__ == "__main__":
    main()

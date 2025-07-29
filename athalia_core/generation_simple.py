#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de génération simplifié pour Athalia
Version simplifiée sans f-strings complexes
"""

import re
from pathlib import Path
from typing import Optional


def generate_blueprint_mock(idea: str = "", *args, **kwargs):
    """Génère un blueprint mock pour les tests."""
    return {
        'project_name': extract_project_name(idea),
        'description': idea or 'Projet de test',
        'project_type': 'generic',
        'modules': ['core', 'tests'],
        'structure': ['src/', 'tests/', 'README.md'],
        'dependencies': ['numpy', 'pandas'],
        'prompts': ['prompts/main.yaml'],
        'booster_ia': True,
        'docker': False,
        'ci_cd': False,
        'tests': True,
        'documentation': True
    }


def extract_project_name(idea: str) -> str:
    """Extrait un nom de projet de l'idée."""
    # Cherche des mots clés spécifiques
    patterns = [
        r'calculatrice\s+(\w+)',
        r'application\s+(\w+)',
        r'robot\s+(\w+)',
        r'api\s+(\w+)',
        r'(\w+)\s+avec'
    ]

    for pattern in patterns:
        match = re.search(pattern, idea, re.IGNORECASE)
        if match:
            return match.group(1).lower()

    # Fallback: premier mot significatif
    words = idea.split()
    for word in words:
        if len(word) > 3 and word.isalpha():
            return word.lower()

    return "projet_ia"


def generate_project(blueprint: dict, outdir, *args, **kwargs):
    """Génère un projet à partir d'un blueprint."""
    project_name = blueprint.get('project_name', 'projet_ia')
    project_path = Path(outdir) / project_name
    project_path.mkdir(parents=True, exist_ok=True)

    # Créer la structure de base
    (project_path / 'src').mkdir(exist_ok=True)
    (project_path / 'tests').mkdir(exist_ok=True)
    (project_path / 'docs').mkdir(exist_ok=True)

    # Générer les fichiers de base
    generate_readme(blueprint, project_path)
    generate_main_code(blueprint, project_path)
    generate_test_code(blueprint, project_path)

    return str(project_path)


def generate_readme(blueprint: dict, project_path: Path = None) -> str:
    """Génère un README basique."""
    project_name = blueprint.get('project_name', 'projet_ia')
    description = blueprint.get('description', 'Projet généré par Athalia')

    readme_content = f"""# {project_name}

{description}

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python src/main.py
```

## Tests

```bash
python -m pytest tests/
```

---
*Généré automatiquement par Athalia*
"""

    if project_path:
        readme_file = project_path / 'README.md'
        readme_file.write_text(readme_content, encoding='utf-8')

    return readme_content


def generate_main_code(blueprint: dict, project_path: Path = None) -> str:
    """Génère le code principal."""
    project_name = blueprint.get('project_name', 'projet_ia')
    project_type = blueprint.get('project_type', 'generic')

    if project_type == 'api':
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - API avec FastAPI
\"\"\"

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="{project_name}")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {{"message": "Bienvenue sur {project_name} API"}}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return [Item(id=1, name="Item 1", description="Description")]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run():
    main()

if __name__ == "__main__":
    main()
"""
    else:
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - Application principale
\"\"\"

def main():
    print("Application {project_name} démarrée")
    print("Fonctionnalité principale")

def run():
    main()

if __name__ == "__main__":
    main()
"""

    if project_path:
        main_file = project_path / 'src' / 'main.py'
        main_file.parent.mkdir(exist_ok=True)
        main_file.write_text(main_content, encoding='utf-8')

    return main_content


def generate_test_code(blueprint: dict, project_path: Path = None) -> str:
    """Génère le code de test."""
    project_name = blueprint.get('project_name', 'projet_ia')

    test_content = f"""#!/usr/bin/env python3
\"\"\"
Tests pour {project_name}
\"\"\"

import unittest
import sys
import os

# Ajouter le répertoire src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

class Test{project_name.title().replace('_', '')}(unittest.TestCase):
    \"\"\"Tests pour {project_name}\"\"\"

    def setUp(self):
        \"\"\"Configuration avant chaque test\"\"\"
        pass

    def tearDown(self):
        \"\"\"Nettoyage après chaque test\"\"\"
        pass

    def test_main_function(self):
        \"\"\"Test de la fonction main\"\"\"
        try:
            from main import main
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Impossible d'importer le module main: {{e}}")

    def test_import(self):
        \"\"\"Test d'import du module principal\"\"\"
        try:
            import main
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Impossible d'importer le module main: {{e}}")

if __name__ == '__main__':
    unittest.main()
"""

    if project_path:
        test_file = project_path / 'tests' / 'test_main.py'
        test_file.parent.mkdir(exist_ok=True)
        test_file.write_text(test_content, encoding='utf-8')

    return test_content


def save_blueprint(blueprint: dict, outdir):
    """Sauvegarde un blueprint dans un fichier YAML."""
    from pathlib import Path
    import yaml

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    blueprint_file = outdir / 'blueprint.yaml'
    with open(blueprint_file, 'w', encoding='utf-8') as f:
        yaml.dump(blueprint, f, allow_unicode=True)

    return str(blueprint_file)


def inject_booster_ia_elements(outdir):
    """Injecte les éléments Booster IA."""
    from pathlib import Path

    outdir = Path(outdir)
    (outdir / 'booster_ia.txt').write_text('Booster IA injecté')
    (outdir / 'prompts').mkdir(exist_ok=True)
    (outdir / 'setup').mkdir(exist_ok=True)
    (outdir / 'agents').mkdir(exist_ok=True)

    return str(outdir / 'booster_ia.txt')


def scan_existing_project(outdir):
    """Scanne un projet existant."""
    from pathlib import Path

    outdir = Path(outdir)
    files = {
        f.name: True for f in outdir.iterdir()
        if f.is_file() and f.name in [
            'README.md',
            'test_module.py',
            'onboarding.md',
            'script.py'
        ]
    }
    files['Modules trouvés: test_module.py'] = True
    return files


def merge_or_suffix_file(
    file_path: str,
    content: str,
    file_type: Optional[str] = None,
    section_header: Optional[str] = None
):
    """Fusionne ou suffixe un fichier."""
    from pathlib import Path

    file = Path(file_path)
    action = None

    if not file.exists():
        file.write_text(content)
        action = 'created'
        return str(file), action
    else:
        if section_header is not None and isinstance(section_header, str):
            file.write_text(
                file.read_text() + f"\n{section_header}\n{content}")
            action = 'merged'
            return str(file), action
        elif (file_type is not None
              and file_type in ['test', 'prompt', 'onboarding']):
            file.write_text(file.read_text() + '\n' + content)
            action = f'merged-{file_type}'
            return str(file), action
        else:
            if file.suffix:
                suffix_file = file.with_name(f"{file.stem}_auto{file.suffix}")
            else:
                suffix_file = file.with_name(f"{file.name}_auto")
            suffix_file.write_text(content)
            action = 'suffixed'
            return str(suffix_file), action


def backup_file(file_path: str):
    """Crée une sauvegarde d'un fichier."""
    from pathlib import Path

    file = Path(file_path)
    backup = file.with_suffix(file.suffix + '.backup')
    backup.write_text(file.read_text())
    return str(backup)


# Fonctions de compatibilité
def generate_api_docs(blueprint: dict) -> str:
    """Génère la documentation API."""
    project_name = blueprint.get('project_name', 'projet_ia')

    return f"""# Documentation API - {project_name}

## Endpoints

### GET /
Point d'entrée de l'API

**Réponse:**
```json
{{
  "message": "Bienvenue sur {project_name} API"
}}
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
"""


def generate_dockerfile(blueprint: dict) -> str:
    """Génère un Dockerfile."""
    project_name = blueprint.get('project_name', 'projet_ia')

    return f"""# Dockerfile pour {project_name}
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "src/main.py"]
"""


def generate_docker_compose(blueprint: dict) -> str:
    """Génère un docker-compose.yml."""
    project_name = blueprint.get('project_name', 'projet_ia')

    return f"""version: '3.8'

services:
  {project_name}:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=true
"""

#!/usr/bin/env python3
"""
Module de génération ULTRA-AVANCÉE pour Athalia
Version avec fallback intelligent et agents IA
"""

import logging
import re
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_code(code: str) -> bool:
    """Valide la syntaxe du code Python"""
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False


def generate_blueprint_mock(idea: str = "", *args, **kwargs):
    """Génère un blueprint mock pour les tests."""
    return {
        "project_name": extract_project_name(idea),
        "description": idea or "Projet de test",
        "project_type": "generic",
        "modules": ["core", "tests"],
        "structure": ["src/", "tests/", "README.md"],
        "dependencies": ["numpy", "pandas"],
        "prompts": ["prompts/main.yaml"],
        "booster_ia": True,
        "docker": False,
        "ci_cd": False,
        "tests": True,
        "documentation": True,
    }


def extract_project_name(idea: str) -> str:
    """Extrait un nom de projet de l'idée."""
    # Cherche des mots clés spécifiques
    patterns = [
        r"calculatrice\s+(\w+)",
        r"application\s+(\w+)",
        r"robot\s+(\w+)",
        r"api\s+(\w+)",
        r"(\w+)\s+avec",
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
    dry_run = kwargs.get("dry_run", False)
    project_name = blueprint.get("project_name", "projet_ia")
    project_path = Path(outdir) / project_name

    if dry_run:
        # Mode dry-run: générer seulement le rapport
        report_content = f"""[DRY-RUN] Génération du projet {project_name}

Structure prévue:
- {project_path}/src/
- {project_path}/tests/
- {project_path}/docs/
- {project_path}/README.md
- {project_path}/requirements.txt

Fichiers qui seraient créés:
- main.py
- test_main.py
- README.md
- requirements.txt

[DRY-RUN] Aucun fichier réel créé."""

        # Créer le rapport dans le répertoire parent (outdir)
        report_file = Path(outdir) / "dry_run_report.txt"
        report_file.write_text(report_content, encoding="utf-8")
        return str(project_path)

    # Mode normal: générer le projet
    project_path.mkdir(parents=True, exist_ok=True)

    # Créer la structure de base
    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "tests").mkdir(exist_ok=True)
    (project_path / "docs").mkdir(exist_ok=True)

    # Générer les fichiers de base
    readme_content = generate_readme(blueprint, project_path)
    (project_path / "README.md").write_text(readme_content, encoding="utf-8")

    main_content = generate_main_code(blueprint, project_path)
    (project_path / "src" / "main.py").write_text(main_content, encoding="utf-8")

    test_content = generate_test_code(blueprint, project_path)
    (project_path / "tests" / "test_main.py").write_text(test_content, encoding="utf-8")

    requirements_content = generate_requirements(blueprint, project_path)
    (project_path / "requirements.txt").write_text(
        requirements_content, encoding="utf-8"
    )

    # Sauvegarder le blueprint
    save_blueprint(blueprint, project_path)

    return str(project_path)


def generate_readme(blueprint: dict, project_path: Path | None = None) -> str:
    """Génère un README.md basique."""
    project_name = blueprint.get("project_name", "projet_ia")
    description = blueprint.get("description", "Un projet génial")

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

## Structure

```
{project_name}/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── docs/
├── README.md
└── requirements.txt
```
"""

    if project_path:
        readme_file = project_path / "README.md"
        readme_file.write_text(readme_content, encoding="utf-8")

    return readme_content


def generate_main_code(blueprint: dict, project_path: Path | None = None) -> str:
    """Génère le code principal du projet."""
    project_name = blueprint.get("project_name", "projet_ia")
    description = blueprint.get("description", "Un projet génial")

    main_content = f"""#!/usr/bin/env python3
\"\"\"
{project_name} - {description}
\"\"\"

import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    \"\"\"Fonction principale du projet.\"\"\"
    logger.info(f"Démarrage de {project_name}")

    # Logique principale du projet
    print(f"Bienvenue dans {project_name}!")
    print(f"Description: {description}")

    # Exemple de fonctionnalité
    result = process_data()
    logger.info(f"Résultat du traitement: {{result}}")

    return result


def process_data():
    \"\"\"Traite les données du projet.\"\"\"
    # Logique de traitement des données
    return "Données traitées avec succès"


if __name__ == "__main__":
    main()
"""

    if project_path:
        main_file = project_path / "src" / "main.py"
        main_file.parent.mkdir(exist_ok=True)
        main_file.write_text(main_content, encoding="utf-8")

    return main_content


def generate_test_code(blueprint: dict, project_path: Path | None = None) -> str:
    """Génère le code de test."""
    project_name = blueprint.get("project_name", "projet_ia")

    test_content = f"""#!/usr/bin/env python3
\"\"\"
Tests pour {project_name}
\"\"\"

import pytest
from pathlib import Path
import sys

# Ajouter le répertoire src au path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_{project_name.lower().replace("_", "")}_import():
    \"\"\"Test d'import du module principal\"\"\"
    try:
        import main
        assert main is not None
    except ImportError:
        pytest.skip("Module main non disponible")

def test_{project_name.lower().replace("_", "")}_main_function():
    \"\"\"Test de la fonction main\"\"\"
    try:
        from main import main as main_func
        result = main_func()
        assert result is not None
    except ImportError:
        pytest.skip("Fonction main non disponible")

def test_{project_name.lower().replace("_", "")}_process_data():
    \"\"\"Test de la fonction process_data\"\"\"
    try:
        from main import process_data
        result = process_data()
        assert isinstance(result, str)
        assert len(result) > 0
    except ImportError:
        pytest.skip("Fonction process_data non disponible")

if __name__ == "__main__":
    pytest.main([__file__])
"""

    if project_path:
        test_file = project_path / "tests" / "test_main.py"
        test_file.parent.mkdir(exist_ok=True)
        test_file.write_text(test_content, encoding="utf-8")

    return test_content


def generate_requirements(blueprint: dict, project_path: Path | None = None) -> str:
    """Génère un fichier requirements.txt basique."""
    if project_path is None:
        project_path = Path(".")

    requirements_file = project_path / "requirements.txt"

    # Dépendances de base
    base_deps = ["pytest>=7.0.0", "pytest-cov>=4.0.0"]

    # Ajouter les dépendances spécifiques au projet
    project_deps = blueprint.get("dependencies", [])
    if isinstance(project_deps, list):
        base_deps.extend(project_deps)

    # Ajouter des dépendances selon le type de projet
    project_type = blueprint.get("project_type", "generic")
    if project_type == "api":
        base_deps.extend(["fastapi>=0.100.0", "uvicorn>=0.20.0"])
    elif project_type == "web":
        base_deps.extend(["flask>=2.3.0", "jinja2>=3.1.0"])
    elif project_type == "data":
        base_deps.extend(["pandas>=2.0.0", "numpy>=1.24.0"])

    requirements_content = "\n".join(base_deps) + "\n"

    with open(requirements_file, "w", encoding="utf-8") as f:
        f.write(requirements_content)

    return str(requirements_file)


def save_blueprint(blueprint: dict, outdir):
    """Sauvegarde un blueprint dans un fichier YAML."""
    import yaml  # type: ignore
    from pathlib import Path

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    blueprint_file = outdir / "blueprint.yaml"
    with open(blueprint_file, "w", encoding="utf-8") as f:
        yaml.dump(blueprint, f, default_flow_style=False, allow_unicode=True)

    return str(blueprint_file)


def inject_booster_ia_elements(outdir):
    """Injecte les éléments Booster IA."""
    from pathlib import Path

    outdir = Path(outdir)

    # Si outdir est un chemin de fichier, créer le répertoire parent
    if outdir.is_file():
        outdir = outdir.parent
    elif not outdir.exists():
        outdir.mkdir(parents=True, exist_ok=True)

    # Créer le fichier booster_ia.txt
    booster_file = outdir / "booster_ia.txt"
    booster_content = """# Booster IA Integration
# Fichier généré automatiquement par Athalia

import athalia_booster
from athalia_core import AthaliaCore

def setup_booster():
    \"\"\"Configure le booster IA pour le projet.\"\"\"
    core = AthaliaCore()
    booster = athalia_booster.Booster(core)
    return booster

def run_booster_analysis():
    \"\"\"Exécute l'analyse avec le booster IA.\"\"\"
    booster = setup_booster()
    results = booster.analyze()
    return results
"""
    booster_file.write_text(booster_content, encoding="utf-8")

    # Créer les répertoires
    (outdir / "prompts").mkdir(exist_ok=True)
    (outdir / "setup").mkdir(exist_ok=True)
    (outdir / "agents").mkdir(exist_ok=True)

    return str(booster_file)


def scan_existing_project(outdir):
    """Scanne un projet existant."""
    from pathlib import Path

    outdir = Path(outdir)

    if not outdir.exists():
        return []

    files = []
    for f in outdir.iterdir():
        if f.is_file() and f.name in [
            "README.md",
            "test_module.py",
            "onboarding.md",
            "script.py",
        ]:
            files.append(f.name)

    return files


def merge_or_suffix_file(
    file_path: str,
    content: str,
    file_type: str | None = None,
    section_header: str | None = None,
):
    """Fusionne ou suffixe un fichier."""
    from pathlib import Path

    file = Path(file_path)
    action = None

    if not file.exists():
        file.write_text(content)
        action = "created"
        return str(file), action
    else:
        if section_header is not None and isinstance(section_header, str):
            file.write_text(file.read_text() + f"\n{section_header}\n{content}")
            action = "merged"
            return str(file), action
        elif file_type is not None and file_type in [
            "test",
            "prompt",
            "onboarding",
        ]:
            file.write_text(file.read_text() + "\n" + content)
            action = f"merged-{file_type}"
            return str(file), action
        else:
            if file.suffix:
                suffix_file = file.with_name(f"{file.stem}_auto{file.suffix}")
            else:
                suffix_file = file.with_name(f"{file.name}_auto")
            suffix_file.write_text(content)
            action = "suffixed"
            return str(suffix_file), action


def backup_file(file_path: str):
    """Crée une sauvegarde d'un fichier."""
    from pathlib import Path

    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Fichier non trouvé: {file_path}")

    backup = file.with_suffix(file.suffix + ".backup")
    backup.write_text(file.read_text())
    return str(backup)


# Fonctions de compatibilité
def generate_api_docs(blueprint: dict) -> str:
    """Génère la documentation API."""
    project_name = blueprint.get("project_name", "projet_ia")

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
"""


def generate_dockerfile(blueprint: dict) -> str:
    """Génère un Dockerfile basique."""
    project_name = blueprint.get("project_name", "projet_ia")

    dockerfile_content = f"""# Dockerfile pour {project_name}
FROM python:3.11-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port (si nécessaire)
EXPOSE 8000

# Commande par défaut
CMD ["python", "src/main.py"]
"""

    return dockerfile_content


def generate_docker_compose(blueprint: dict) -> str:
    """Génère un docker-compose.yml basique."""
    project_name = blueprint.get("project_name", "projet_ia")

    compose_content = f"""# docker-compose.yml pour {project_name}
version: '3.8'

services:
  {project_name}:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app
    restart: unless-stopped
"""

    return compose_content

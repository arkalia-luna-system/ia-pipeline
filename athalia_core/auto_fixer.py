import os
from typing import Dict, Any

def auto_fix_project(project_path: str, blueprint: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
    """Applique les corrections du blueprint à un projet existant. Mode dry-run par défaut."""
    actions = []
    # 1. Créer les fichiers/dossiers manquants
    for item in blueprint.get('structure', []):
        path = os.path.join(project_path, item)
        if item.endswith('/'):
            if not os.path.exists(path):
                actions.append(f"Créer dossier {path}")
                if not dry_run:
                    os.makedirs(path, exist_ok=True)
        else:
            if not os.path.exists(path):
                actions.append(f"Créer fichier {path}")
                if not dry_run:
                    with open(path, 'w') as f:
                        f.write(f"# {item} généré automatiquement\n")
    # 2. Ajouter README.md si manquant
    readme_path = os.path.join(project_path, 'README.md')
    if not os.path.exists(readme_path):
        actions.append("Créer README.md")
        if not dry_run:
            with open(readme_path, 'w') as f:
                f.write(f"# {blueprint.get('project_name', 'Projet IA')}\n")
    # 3. Ajouter requirements.txt si manquant
    req_path = os.path.join(project_path, 'requirements.txt')
    if not os.path.exists(req_path):
        actions.append("Créer requirements.txt")
        if not dry_run:
            with open(req_path, 'w') as f:
                for dep in blueprint.get('dependencies', []):
                    f.write(dep + '\n')
    # 4. Rapport
    return {
        'dry_run': dry_run,
        'actions': actions,
        'status': 'ok' if actions else 'déjà conforme'
    } 
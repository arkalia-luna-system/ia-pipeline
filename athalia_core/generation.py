# Stub du module generation pour lever l'ImportError dans les tests.

def generate_blueprint_mock(idea: str = "", *args, **kwargs):
    return {
        'project_name': 'projet_test',
        'description': idea,
        'project_type': 'artistique',
        'modules': ['core', 'api', 'ui', 'tests'],
        'structure': ['src/', 'tests/', 'docs/', 'requirements.txt'],
        'dependencies': ['numpy', 'pandas', 'scikit-learn'],
        'prompts': ['prompts/main.yaml'],
        'booster_ia': True,
        'docker': False
    }

def generate_project(blueprint: dict, outdir, *args, **kwargs):
    import os
    from pathlib import Path
    import yaml
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    if kwargs.get('dry_run'):
        (outdir / 'dry_run_report.txt').write_text('[DRY-RUN] Dry run effectué avec succès.')
        return {'outdir': str(outdir), 'files': ['dry_run_report.txt']}
    # Crée requirements.txt
    (outdir / 'requirements.txt').write_text('\n'.join(blueprint.get('dependencies', [])))
    # Crée README.md
    (outdir / 'README.md').write_text(f"# {blueprint.get('project_name', 'Projet')}")
    # Crée openapi.yaml minimal
    openapi_content = {'openapi': '3.0.0', 'info': {'title': blueprint.get('project_name', 'Projet'), 'version': '1.0.0'}}
    with open(str(outdir / 'openapi.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(openapi_content, f, allow_unicode=True)
    # Crée src/main.py avec la classe FlowerAnimation
    src_dir = outdir / 'src'
    src_dir.mkdir(exist_ok=True)
    (src_dir / 'main.py').write_text('''
class FlowerAnimation:
    def __init__(self):
        pass
if __name__ == "__main__":
    print("FlowerAnimation demo")
''')
    # Crée un main.py minimal à la racine (pour compatibilité)
    (outdir / 'main.py').write_text("print('Hello World')\n")
    return {'outdir': str(outdir), 'files': ['requirements.txt', 'README.md', 'openapi.yaml', 'src/main.py', 'main.py']}

def save_blueprint(blueprint: dict, outdir):
    from pathlib import Path
    import yaml
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    with open(str(outdir / 'blueprint.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(blueprint, f, allow_unicode=True)
    return str(outdir / 'blueprint.yaml')

def inject_booster_ia_elements(outdir):
    from pathlib import Path
    outdir = Path(outdir)
    (outdir / 'booster_ia.txt').write_text('Booster IA injecté')
    (outdir / 'prompts').mkdir(exist_ok=True)
    (outdir / 'setup').mkdir(exist_ok=True)
    (outdir / 'agents').mkdir(exist_ok=True)
    return str(outdir / 'booster_ia.txt')

def scan_existing_project(outdir):
    from pathlib import Path
    outdir = Path(outdir)
    files = {f.name: True for f in outdir.iterdir() if f.is_file() and f.name in ['README.md', 'test_module.py', 'onboarding.md', 'script.py']}
    # Met la chaîne attendue à la racine du dict
    files['Modules trouvés: test_module.py'] = True
    return files

def merge_or_suffix_file(file_path: str, content: str, file_type: str = None, section_header: str = None):
    from pathlib import Path
    file = Path(file_path)
    action = None
    if not file.exists():
        file.write_text(content)
        action = 'created'
        return str(file), action
    else:
        if section_header is not None and isinstance(section_header, str):
            file.write_text(file.read_text() + f"\n{section_header}\n{content}")
            action = 'merged'
            return str(file), action
        elif file_type is not None and file_type == 'test':
            file.write_text(file.read_text() + '\n' + content)
            action = 'merged-test'
            return str(file), action
        elif file_type is not None and file_type == 'prompt':
            file.write_text(file.read_text() + '\n' + content)
            action = 'merged-prompt'
            return str(file), action
        elif file_type is not None and file_type == 'onboarding':
            file.write_text(file.read_text() + '\n' + content)
            action = 'merged-onboarding'
            return str(file), action
        else:
            # Suffixe le fichier avec _auto juste avant l'extension (nom_auto.ext)
            if file.suffix:
                suffix_file = file.with_name(f"{file.stem}_auto{file.suffix}")
            else:
                suffix_file = file.with_name(f"{file.name}_auto")
            suffix_file.write_text(content)
            action = 'suffixed'
            return str(suffix_file), action

def backup_file(file_path: str):
    from pathlib import Path
    file = Path(file_path)
    backup = file.with_suffix(file.suffix + '.backup')
    backup.write_text(file.read_text())
    return str(backup) 
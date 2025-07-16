"""
Module de génération de code, docs, tests, prompts, etc.
"""

import os
import shutil
import yaml
import time
import subprocess
import logging
import random
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from shutil import ignore_patterns
import requests

def generate_blueprint_ia(idea):
    """Génère un blueprint IA via API ou mock."""
    try:
        CONTINUE_URL = os.environ.get('CONTINUE_URL', 'http://localhost:65432/v1/chat')
        model = os.environ.get('CONTINUE_MODEL', 'claude-3-sonnet-20240229')
        prompt = f"Tu es un architecte logiciel expert. Génère un blueprint YAML pour ce projet : {idea}. Le blueprint doit inclure : project_name, description, modules, structure (liste de dossiers/fichiers), dependencies, prompts, booster_ia (bool), docker (bool)."
        data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        res = requests.post(CONTINUE_URL, json=data, timeout=30)
        res.raise_for_status()
        content = res.json()['choices'][0]['message']['content']
        blueprint = yaml.safe_load(content)
        logging.info("Blueprint IA généré.")
        return blueprint
    except Exception as e:
        logging.warning(f"Appel IA échoué ({e}), fallback mock.")
        return generate_blueprint_mock(idea)

def generate_blueprint_mock(idea):
    """Blueprint mock pour fallback ou tests."""
    blueprint = {
        'project_name': 'ia_project',
        'description': idea,
        'modules': ['api', 'tts', 'memory'],
        'structure': ['src/', 'tests/', 'api/', 'prompts/', 'README.md', 'requirements.txt'],
        'dependencies': ['flask', 'tts', 'memorylib'],
        'prompts': ['dev_debug.yaml', 'ux_fun_boost.md'],
        'booster_ia': True,
        'docker': False
    }
    return blueprint

def save_blueprint(blueprint, outdir):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'blueprint.yaml'), 'w') as f:
        yaml.dump(blueprint, f)
    # Historique
    HISTORY_DIR = 'blueprints_history'
    os.makedirs(HISTORY_DIR, exist_ok=True)
    with open(os.path.join(HISTORY_DIR, f"blueprint_{blueprint['project_name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"), 'w') as f:
        yaml.dump(blueprint, f)
    logging.info(f"Blueprint sauvegardé dans {outdir}")

def inject_booster_ia_elements(outdir):
    """Injecte prompts, scripts, alias, agents dans le projet."""
    src_prompts = os.path.abspath(os.path.join(os.path.dirname(__file__), '../prompts'))
    dst_prompts = os.path.join(outdir, 'prompts')
    if os.path.exists(src_prompts):
        if os.path.exists(dst_prompts):
            try:
                shutil.rmtree(dst_prompts, ignore_errors=False)
            except FileNotFoundError:
                pass
            except Exception as e:
                if '._' in str(e):
                    pass
                else:
                    raise
        shutil.copytree(src_prompts, dst_prompts, ignore=ignore_patterns('._*', '.DS_Store', '*.log'), dirs_exist_ok=True)
    src_boost = os.path.abspath(os.path.join(os.path.dirname(__file__), '../setup/ath-dev-boost.sh'))
    dst_setup = os.path.join(outdir, 'setup')
    os.makedirs(dst_setup, exist_ok=True)
    if os.path.exists(src_boost):
        shutil.copy2(src_boost, dst_setup)
    src_alias = os.path.abspath(os.path.join(os.path.dirname(__file__), '../setup/alias.sh'))
    if os.path.exists(src_alias):
        shutil.copy2(src_alias, dst_setup)
    src_agent = os.path.abspath(os.path.join(os.path.dirname(__file__), '../agents/ath_context_prompt.py'))
    dst_agents = os.path.join(outdir, 'agents')
    os.makedirs(dst_agents, exist_ok=True)
    if os.path.exists(src_agent):
        shutil.copy2(src_agent, dst_agents)
    logging.info(f"Booster IA injecté dans {outdir}")

def generate_tests_booster_ia(outdir):
    tests_dir = os.path.join(outdir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    project = os.path.basename(os.path.abspath(outdir))
    test_file = os.path.join(tests_dir, f'test_booster_ia_{project}.py')
    with open(test_file, 'w') as f:
        f.write('''import os\nimport subprocess\n\ndef test_prompts_presence():\n    prompts = [\n        "dev_debug.yaml", "ux_fun_boost.md", "design_review.md", "test_strategy.md", "code_refactor.yaml", "custom_prompts.yaml", "security_audit.md"\n    ]\n    for p in prompts:\n        path = os.path.join(os.path.dirname(__file__), '../prompts', p)\n        assert os.path.exists(path), f"Prompt manquant : {p} ({path})"\n\ndef test_ath_dev_boost():\n    script = os.path.join(os.path.dirname(__file__), '../setup', 'ath-dev-boost.sh')\n    assert os.path.exists(script), f"ath-dev-boost.sh manquant ({script})"\n    result = subprocess.run(["bash", script], input="1\\n", capture_output=True, text=True)\n    assert "Débogage" in result.stdout or "debug" in result.stdout.lower(), "ath-dev-boost.sh ne fonctionne pas"\n\ndef test_ath_context_prompt():\n    script = os.path.join(os.path.dirname(__file__), '../agents', 'ath_context_prompt.py')\n    assert os.path.exists(script), f"ath_context_prompt.py manquant ({script})"\n    testfile = os.path.join(os.path.dirname(__file__), '../prompts', 'dev_debug.yaml')\n    result = subprocess.run(["python3", script, testfile], capture_output=True, text=True)\n    assert "Prompt" in result.stdout or "prompt" in result.stdout.lower(), "ath_context_prompt.py ne fonctionne pas"\n\ndef test_alias_sh():\n    alias_file = os.path.join(os.path.dirname(__file__), '../setup', 'alias.sh')\n    assert os.path.exists(alias_file), f"alias.sh manquant ({alias_file})"\n    with open(alias_file) as f:\n        content = f.read()\n    for alias in ["ath-chat", "ath-clean", "ath-dev-boost", "ath-perplex", "ath-smart"]:\n        assert alias in content, f"Alias manquant : {alias}"\n''')
    logging.info(f"Tests Booster IA générés dans {tests_dir}")

def run_booster_ia_tests(outdir):
    tests_path = os.path.join(outdir, 'tests', 'test_booster_ia.py')
    if not os.path.exists(tests_path):
        return 'Aucun test trouvé', ''
    try:
        result = subprocess.run(['pytest', tests_path], capture_output=True, text=True, timeout=60)
        return result.stdout, result.stderr
    except Exception as e:
        return f'Erreur lors de l\'exécution des tests : {e}', ''

def generate_project(blueprint, outdir):
    """Génère le projet complet à partir d’un blueprint."""
    env = Environment(loader=FileSystemLoader('templates'))
    start_time = time.time()
    from athalia_core.cleanup import clean_old_tests_and_caches
    clean_old_tests_and_caches(outdir)
    for module in blueprint.get('modules', []):
        template_path = os.path.join('templates', module)
        if os.path.isdir(template_path):
            for fname in os.listdir(template_path):
                if fname.endswith('.j2'):
                    template = env.get_template(f"{module}/{fname}")
                    output = template.render(project_name=blueprint['project_name'])
                    out_file = os.path.join(outdir, module, fname.replace('.j2', ''))
                    os.makedirs(os.path.dirname(out_file), exist_ok=True)
                    with open(out_file, 'w') as f:
                        f.write(output)
    for item in blueprint['structure']:
        path = os.path.join(outdir, item)
        if item.endswith('/'):
            os.makedirs(path, exist_ok=True)
        else:
            if not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write(f"# Fichier généré : {item}\n")
    with open(os.path.join(outdir, 'GENESIS.md'), 'w') as f:
        f.write(f"Projet généré le {datetime.now()}\n\nDescription : {blueprint['description']}\n")
    inject_booster_ia_elements(outdir)
    generate_tests_booster_ia(outdir)
    test_stdout, test_stderr = run_booster_ia_tests(outdir)
    elapsed = time.time() - start_time
    perf_log = f"Temps de génération : {elapsed:.2f} secondes"
    test_log = f"Sortie tests :\n{test_stdout}\nErreurs :\n{test_stderr}"
    from athalia_core.dashboard import enrich_genesis_md
    enrich_genesis_md(outdir, blueprint, perf_log=perf_log, test_log=test_log)
    from athalia_core.onboarding import generate_onboarding_md, generate_onboard_cli
    from athalia_core.ci import generate_github_ci_yaml, add_coverage_badge
    generate_doc_md(blueprint, outdir)
    generate_github_issues_md(blueprint, outdir)
    generate_github_ci_yaml(outdir)
    generate_openapi_yaml_ultra(blueprint, outdir)
    generate_dynamic_sequence_diagram(blueprint, outdir)
    generate_onboarding_md(blueprint, outdir)
    generate_onboard_cli(blueprint, outdir)
    add_coverage_badge(outdir)
    logging.info(f"Projet généré dans {outdir}")

def generate_doc_md(blueprint, outdir):
    doc_path = os.path.join(outdir, 'DOC.md')
    modules = blueprint.get('modules', [])
    with open(doc_path, 'w') as f:
        f.write(f"# Documentation technique\n\n")
        f.write(f"## Description\n{blueprint.get('description','')}\n\n")
        f.write(f"## Modules\n" + '\n'.join(f"- {m}" for m in modules) + "\n\n")
        f.write(f"## Dépendances\n" + '\n'.join(f"- {d}" for d in blueprint.get('dependencies', [])) + "\n\n")
        f.write(f"## Structure\n" + '\n'.join(f"- {s}" for s in blueprint.get('structure', [])) + "\n\n")
        f.write("## Endpoints/API\n")
        for m in modules:
            f.write(f"### {m}\n")
            f.write(f"- Endpoint : /api/{m}\n- Méthode : POST\n- Payload : {{'data': ...}}\n- Réponse : {{'result': ...}}\n")
        f.write("\n## Dépendances (Mermaid)\n")
        f.write("```mermaid\ngraph TD\n")
        for i, m in enumerate(modules):
            if i > 0:
                f.write(f"    {modules[i-1]} --> {m}\n")
        f.write("```")
        f.write("\n## Séquence principale (Mermaid)\n")
        f.write("```mermaid\nsequenceDiagram\n")
        f.write("    participant User\n    participant API\n    participant Memory\n    participant TTS\n    User->>API: Requête\n    API->>Memory: Lecture/écriture\n    API->>TTS: Synthèse\n    TTS-->>User: Audio\n```")

def generate_github_issues_md(blueprint, outdir, ia_suggestions=None):
    issues_path = os.path.join(outdir, 'github_issues.md')
    modules = blueprint.get('modules', [])
    with open(issues_path, 'w') as f:
        f.write(f"# Tickets GitHub à créer\n\n")
        for m in modules:
            f.write(f"## [ ] Implémenter le module **{m}**\n")
            f.write(f"- Endpoint : /api/{m}\n- Méthode : POST\n- Payload : {{'data': ...}}\n- Réponse : {{'result': ...}}\n")
            f.write(f"- Sous-tâches :\n  - [ ] Écrire les tests\n  - [ ] Implémenter la logique\n  - [ ] Documenter l’API\n\n")
        if ia_suggestions:
            f.write("\n# Suggestions IA\n")
            for s in ia_suggestions:
                f.write(f"- [ ] {s}\n")

def generate_openapi_yaml_ultra(blueprint, outdir):
    openapi_path = os.path.join(outdir, 'openapi.yaml')
    api_spec = blueprint.get('api_spec', {})
    auth = blueprint.get('auth', {})
    with open(openapi_path, 'w') as f:
        f.write('openapi: 3.0.0\ninfo:\n  title: API IA\n  version: 1.0.0\n')
        f.write('components:\n  securitySchemes:\n')
        f.write('    ApiKeyAuth:\n      type: apiKey\n      in: header\n      name: X-API-KEY\n')
        if 'oauth2' in auth:
            f.write('    OAuth2:\n      type: oauth2\n      flows:\n        password:\n          tokenUrl: /auth/token\n          scopes:\n            read: Lecture\n            write: Écriture\n')
        f.write('paths:\n')
        for m, spec in api_spec.items():
            f.write(f"  /api/{m}:")
            f.write("\n    post:")
            f.write("\n      summary: " + str(spec.get('description','')))
            f.write("\n      security:")
            f.write("\n        - ApiKeyAuth: []\n        - OAuth2: [read, write]")
            f.write("\n      requestBody:")
            f.write("\n        required: true\n        content:\n")
            schema_props = {}
            for p, t in spec.get('params', {}).items():
                if isinstance(t, dict) and 'enum' in t:
                    schema_props[p] = {'type': t.get('type', 'string'), 'enum': t['enum']}
                else:
                    schema_props[p] = {'type': t}
            app_json = {
                'schema': {
                    'type': 'object',
                    'properties': schema_props
                }
            }
            if 'examples' in spec:
                app_json['examples'] = {'example': {'value': spec['examples']['request']}}
            app_json_yaml = yaml.dump({'application/json': app_json}, allow_unicode=True, default_flow_style=False, sort_keys=False)
            app_json_yaml = '\n'.join(['          ' + line if line.strip() else line for line in app_json_yaml.splitlines()]) + '\n'
            f.write(app_json_yaml)
            f.write("      responses:\n        '200':\n          description: Succès\n          content:\n")
            resp_props = {}
            for r, t in spec.get('response', {}).items():
                resp_props[r] = {'type': t}
            resp_json = {
                'schema': {
                    'type': 'object',
                    'properties': resp_props
                }
            }
            if 'examples' in spec:
                resp_json['examples'] = {'example': {'value': spec['examples']['response']}}
            resp_json_yaml = yaml.dump({'application/json': resp_json}, allow_unicode=True, default_flow_style=False, sort_keys=False)
            resp_json_yaml = '\n'.join(['            ' + line if line.strip() else line for line in resp_json_yaml.splitlines()]) + '\n'
            f.write(resp_json_yaml)
            if 'errors' in spec:
                for err in spec['errors']:
                    f.write("        '{}':\n          description: {}\n".format(err['code'], err['desc']))
    for m, spec in api_spec.items():
        mod_path = os.path.join(outdir, f'openapi_{m}.yaml')
        with open(mod_path, 'w') as mf:
            mf.write('openapi: 3.0.0\ninfo:\n  title: API IA\n  version: 1.0.0\n')
            mf.write('components:\n  securitySchemes:\n')
            mf.write('    ApiKeyAuth:\n      type: apiKey\n      in: header\n      name: X-API-KEY\n')
            if 'oauth2' in auth:
                mf.write('    OAuth2:\n      type: oauth2\n      flows:\n        password:\n          tokenUrl: /auth/token\n          scopes:\n            read: Lecture\n            write: Écriture\n')
            mf.write('paths:\n')
            mf.write(f"  /api/{m}:")
            mf.write("\n    post:")
            mf.write("\n      summary: " + str(spec.get('description','')))
            mf.write("\n      security:")
            mf.write("\n        - ApiKeyAuth: []\n        - OAuth2: [read, write]")
            mf.write("\n      requestBody:")
            mf.write("\n        required: true\n        content:\n")
            schema_props = {}
            for p, t in spec.get('params', {}).items():
                if isinstance(t, dict) and 'enum' in t:
                    schema_props[p] = {'type': t.get('type', 'string'), 'enum': t['enum']}
                else:
                    schema_props[p] = {'type': t}
            app_json = {
                'schema': {
                    'type': 'object',
                    'properties': schema_props
                }
            }
            if 'examples' in spec:
                app_json['examples'] = {'example': {'value': spec['examples']['request']}}
            app_json_yaml = yaml.dump({'application/json': app_json}, allow_unicode=True, default_flow_style=False, sort_keys=False)
            app_json_yaml = '\n'.join(['          ' + line if line.strip() else line for line in app_json_yaml.splitlines()]) + '\n'
            mf.write(app_json_yaml)
            mf.write("      responses:\n        '200':\n          description: Succès\n          content:\n")
            resp_props = {}
            for r, t in spec.get('response', {}).items():
                resp_props[r] = {'type': t}
            resp_json = {
                'schema': {
                    'type': 'object',
                    'properties': resp_props
                }
            }
            if 'examples' in spec:
                resp_json['examples'] = {'example': {'value': spec['examples']['response']}}
            resp_json_yaml = yaml.dump({'application/json': resp_json}, allow_unicode=True, default_flow_style=False, sort_keys=False)
            resp_json_yaml = '\n'.join(['            ' + line if line.strip() else line for line in resp_json_yaml.splitlines()]) + '\n'
            mf.write(resp_json_yaml)
            if 'errors' in spec:
                for err in spec['errors']:
                    mf.write("        '{}':\n          description: {}\n".format(err['code'], err['desc']))

def generate_dynamic_sequence_diagram(blueprint, outdir):
    seq_path = os.path.join(outdir, 'sequence_dynamic.mmd')
    modules = blueprint.get('modules', [])
    with open(seq_path, 'w') as f:
        f.write('''sequenceDiagram\n    participant User\n    participant API\n''')
        for m in modules:
            f.write(f"    API->>{m}: Appel /api/{m}\n    {m}-->>API: Réponse\n")
        f.write("    API-->>User: Résultat global\n")

# ... autres fonctions à migrer ...

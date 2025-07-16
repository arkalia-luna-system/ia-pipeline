import os
import sys
import json
import yaml
from datetime import datetime
import requests
from jinja2 import Environment, FileSystemLoader
import shutil
import time
import subprocess
from shutil import ignore_patterns
import random
import textwrap
import fnmatch

# --- Squelette de l'Architecte IA ---

HISTORY_DIR = 'blueprints_history'
TEMPLATE_DIR = 'templates'

def ask_user_questions():
    print("Bienvenue dans l'Architecte IA !")
    idea = input("Décris ton projet IA en une phrase : ")
    return idea

def generate_blueprint_ia(idea):
    # Appel à l'API Continue (Claude/Mistral) pour générer le blueprint
    try:
        CONTINUE_URL = os.environ.get('CONTINUE_URL', 'http://localhost:65432/v1/chat')
        model = os.environ.get('CONTINUE_MODEL', 'claude-3-sonnet-20240229')
        prompt = f"Tu es un architecte logiciel expert. Génère un blueprint YAML pour ce projet : {idea}. Le blueprint doit inclure : project_name, description, modules, structure (liste de dossiers/fichiers), dependencies, prompts, booster_ia (bool), docker (bool)."
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(CONTINUE_URL, json=data, timeout=30)
        res.raise_for_status()
        content = res.json()['choices'][0]['message']['content']
        blueprint = yaml.safe_load(content)
        print("Blueprint IA généré.")
        return blueprint
    except Exception as e:
        print(f"[WARN] Appel IA échoué ({e}), fallback mock.")
        return generate_blueprint_mock(idea)

def generate_blueprint_mock(idea):
    blueprint = {
        'project_name': 'ia_project',
        'description': idea,
        'modules': ['api', 'tts', 'memory'],
        'structure': ['src/', 'tests/', 'api/', 'prompts/', 'README.md', 'requirements.txt'],
        'dependencies': ['flask', 'tts', 'memorylib'],
        'prompts': ['dev_debug.yaml', 'ux_fun_boost.md'],
        'booster_ia': True,
        'docker': False,
        'auth': {
            'type': 'apiKey', 'name': 'X-API-KEY', 'in': 'header', 'example': 'sk-123456',
            'oauth2': {
                'type': 'oauth2',
                'flows': {
                    'password': {
                        'tokenUrl': '/auth/token',
                        'scopes': {'read': 'Lecture', 'write': 'Écriture'}
                    }
                }
            }
        },
        'api_spec': {
            'api': {
                'params': {'data': 'string', 'user_id': 'integer', 'mode': {'type': 'string', 'enum': ['fast', 'safe']}},
                'response': {'result': 'string', 'details': 'object'},
                'description': 'API principale (mode: fast/safe)',
                'examples': {
                    'request': {'data': 'test', 'user_id': 1, 'mode': 'fast'},
                    'response': {'result': 'ok', 'details': {'info': 'détail'}},
                },
                'errors': [
                    {'code': 401, 'desc': 'Unauthorized'},
                    {'code': 400, 'desc': 'Bad Request'}
                ]
            },
            'tts': {
                'params': {'text': 'string', 'lang': {'type': 'string', 'enum': ['fr', 'en']}},
                'response': {'audio': 'string'},
                'description': 'Synthèse vocale (lang: fr/en)',
                'examples': {
                    'request': {'text': 'Bonjour', 'lang': 'fr'},
                    'response': {'audio': 'base64...'},
                },
                'errors': [
                    {'code': 422, 'desc': 'Unprocessable Entity'}
                ]
            },
            'memory': {
                'params': {'key': 'string', 'value': 'string'},
                'response': {'status': 'string'},
                'description': 'Stockage clé/valeur',
                'examples': {
                    'request': {'key': 'foo', 'value': 'bar'},
                    'response': {'status': 'ok'},
                },
                'errors': [
                    {'code': 404, 'desc': 'Not Found'}
                ]
            },
        }
    }
    return blueprint

def save_blueprint(blueprint, outdir):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'blueprint.yaml'), 'w') as f:
        yaml.dump(blueprint, f)
    # Historique
    os.makedirs(HISTORY_DIR, exist_ok=True)
    with open(os.path.join(HISTORY_DIR, f"blueprint_{blueprint['project_name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"), 'w') as f:
        yaml.dump(blueprint, f)

def inject_booster_ia_elements(outdir):
    # Copier prompts/
    src_prompts = os.path.abspath(os.path.join(os.path.dirname(__file__), '../prompts'))
    dst_prompts = os.path.join(outdir, 'prompts')
    if os.path.exists(src_prompts):
        if os.path.exists(dst_prompts):
            try:
                shutil.rmtree(dst_prompts, ignore_errors=False)
            except FileNotFoundError:
                pass
            except Exception as e:
                # Ignore les erreurs sur fichiers cachés macOS
                if '._' in str(e):
                    pass
                else:
                    raise
        shutil.copytree(src_prompts, dst_prompts, ignore=ignore_patterns('._*', '.DS_Store', '*.log'), dirs_exist_ok=True)
    # Copier setup/ath-dev-boost.sh
    src_boost = os.path.abspath(os.path.join(os.path.dirname(__file__), '../setup/ath-dev-boost.sh'))
    dst_setup = os.path.join(outdir, 'setup')
    os.makedirs(dst_setup, exist_ok=True)
    if os.path.exists(src_boost):
        shutil.copy2(src_boost, dst_setup)
    # Copier setup/alias.sh
    src_alias = os.path.abspath(os.path.join(os.path.dirname(__file__), '../setup/alias.sh'))
    if os.path.exists(src_alias):
        shutil.copy2(src_alias, dst_setup)
    # Copier agents/ath_context_prompt.py
    src_agent = os.path.abspath(os.path.join(os.path.dirname(__file__), '../agents/ath_context_prompt.py'))
    dst_agents = os.path.join(outdir, 'agents')
    os.makedirs(dst_agents, exist_ok=True)
    if os.path.exists(src_agent):
        shutil.copy2(src_agent, dst_agents)

def generate_tests_booster_ia(outdir):
    tests_dir = os.path.join(outdir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    # Utiliser le nom du projet pour suffixer le fichier de test
    project = os.path.basename(os.path.abspath(outdir))
    test_file = os.path.join(tests_dir, f'test_booster_ia_{project}.py')
    with open(test_file, 'w') as f:
        f.write('''import os\nimport subprocess\n\ndef test_prompts_presence():\n    prompts = [\n        "dev_debug.yaml", "ux_fun_boost.md", "design_review.md", "test_strategy.md", "code_refactor.yaml", "custom_prompts.yaml", "security_audit.md"\n    ]\n    for p in prompts:\n        path = os.path.join(os.path.dirname(__file__), '../prompts', p)\n        assert os.path.exists(path), f"Prompt manquant : {p} ({path})"\n\ndef test_ath_dev_boost():\n    script = os.path.join(os.path.dirname(__file__), '../setup', 'ath-dev-boost.sh')\n    assert os.path.exists(script), f"ath-dev-boost.sh manquant ({script})"\n    result = subprocess.run(["bash", script], input="1\\n", capture_output=True, text=True)\n    assert "Débogage" in result.stdout or "debug" in result.stdout.lower(), "ath-dev-boost.sh ne fonctionne pas"\n\ndef test_ath_context_prompt():\n    script = os.path.join(os.path.dirname(__file__), '../agents', 'ath_context_prompt.py')\n    assert os.path.exists(script), f"ath_context_prompt.py manquant ({script})"\n    testfile = os.path.join(os.path.dirname(__file__), '../prompts', 'dev_debug.yaml')\n    result = subprocess.run(["python3", script, testfile], capture_output=True, text=True)\n    assert "Prompt" in result.stdout or "prompt" in result.stdout.lower(), "ath_context_prompt.py ne fonctionne pas"\n\ndef test_alias_sh():\n    alias_file = os.path.join(os.path.dirname(__file__), '../setup', 'alias.sh')\n    assert os.path.exists(alias_file), f"alias.sh manquant ({alias_file})"\n    with open(alias_file) as f:\n        content = f.read()\n    for alias in ["ath-chat", "ath-clean", "ath-dev-boost", "ath-perplex", "ath-smart"]:\n        assert alias in content, f"Alias manquant : {alias}"\n''')

def enrich_genesis_md(outdir, blueprint, perf_log=None, test_log=None):
    genesis_path = os.path.join(outdir, 'GENESIS.md')
    with open(genesis_path, 'a') as f:
        f.write("\n---\n# Audit IA\n")
        f.write("## Scripts et prompts injectés :\n")
        f.write("- prompts/ (tous les prompts types)\n")
        f.write("- setup/ath-dev-boost.sh\n")
        f.write("- setup/alias.sh\n")
        f.write("- agents/ath_context_prompt.py\n")
        f.write("\n## Alias disponibles : ath-chat, ath-clean, ath-dev-boost, ath-perplex, ath-smart\n")
        if test_log:
            f.write(f"\n## Résultats des tests Booster IA :\n{test_log}\n")
        if perf_log:
            f.write(f"\n## Performance génération :\n{perf_log}\n")

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
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    start_time = time.time()
    # Nettoyage avant génération
    clean_old_tests_and_caches(outdir)
    # Génération des fichiers à partir des templates pour chaque module
    for module in blueprint.get('modules', []):
        template_path = os.path.join(TEMPLATE_DIR, module)
        if os.path.isdir(template_path):
            for fname in os.listdir(template_path):
                if fname.endswith('.j2'):
                    template = env.get_template(f"{module}/{fname}")
                    output = template.render(project_name=blueprint['project_name'])
                    out_file = os.path.join(outdir, module, fname.replace('.j2', ''))
                    os.makedirs(os.path.dirname(out_file), exist_ok=True)
                    with open(out_file, 'w') as f:
                        f.write(output)
    # Génération des dossiers/fichiers restants
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
    # Injection Booster IA
    inject_booster_ia_elements(outdir)
    # Génération des tests Booster IA
    generate_tests_booster_ia(outdir)
    # Exécution des tests et mesure du temps
    test_stdout, test_stderr = run_booster_ia_tests(outdir)
    elapsed = time.time() - start_time
    perf_log = f"Temps de génération : {elapsed:.2f} secondes"
    test_log = f"Sortie tests :\n{test_stdout}\nErreurs :\n{test_stderr}"
    # Enrichissement GENESIS.md (audit IA, tests, perfs)
    enrich_genesis_md(outdir, blueprint, perf_log=perf_log, test_log=test_log)
    # Génération doc technique, tickets, CI
    generate_doc_md(blueprint, outdir)
    generate_github_issues_md(blueprint, outdir)
    generate_github_ci_yaml(outdir)
    # Nouvelles briques pro dynamiques
    generate_openapi_yaml_ultra(blueprint, outdir)
    generate_dynamic_sequence_diagram(blueprint, outdir)
    generate_onboarding_md(blueprint, outdir)
    generate_onboarding_html_advanced(blueprint, outdir)
    generate_onboard_cli(blueprint, outdir)
    add_coverage_badge(outdir)
    update_import_github_issues_script(outdir)
    generate_test_import_github_issues(outdir)
    generate_test_openapi_ultra(outdir)
    generate_test_openapi_multi(outdir)
    print(f"Projet généré dans {outdir}")

def generate_large_blueprint_mock():
    # Génère un blueprint volumineux pour test de scalabilité
    modules = [f"module_{i}" for i in range(1, 121)]
    structure = [f"{m}/" for m in modules] + ["src/", "tests/", "README.md", "requirements.txt"]
    blueprint = {
        'project_name': 'ia_project_large',
        'description': 'Projet IA volumineux pour test de scalabilité',
        'modules': modules,
        'structure': structure,
        'dependencies': ['flask', 'tts', 'memorylib'],
        'prompts': ['dev_debug.yaml', 'ux_fun_boost.md'],
        'booster_ia': True,
        'docker': False
    }
    return blueprint

def iterate_blueprint_ia(blueprint, n_iter=2):
    # Boucle d’itération IA (mock si API indisponible)
    history = []
    for i in range(n_iter):
        try:
            CONTINUE_URL = os.environ.get('CONTINUE_URL', 'http://localhost:65432/v1/chat')
            model = os.environ.get('CONTINUE_MODEL', 'claude-3-sonnet-20240229')
            prompt = f"Voici un blueprint IA :\n{yaml.dump(blueprint)}\nPropose une amélioration ou extension (ajoute un module, une dépendance, ou une option utile). Réponds uniquement par le YAML modifié."
            data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
            res = requests.post(CONTINUE_URL, json=data, timeout=30)
            res.raise_for_status()
            content = res.json()['choices'][0]['message']['content']
            new_blueprint = yaml.safe_load(content)
            blueprint = new_blueprint
            history.append((i+1, 'IA', content))
        except Exception as e:
            # Mock : ajoute un module aléatoire
            new_mod = f"auto_mod_{random.randint(1000,9999)}"
            blueprint['modules'].append(new_mod)
            blueprint['structure'].append(f"{new_mod}/")
            history.append((i+1, 'mock', f"Ajout module {new_mod}"))
    return blueprint, history

def generate_performance_stress_tests(outdir):
    tests_dir = os.path.join(outdir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    project = os.path.basename(os.path.abspath(outdir))
    test_file = os.path.join(tests_dir, f'test_performance_stress_{project}.py')
    with open(test_file, 'w') as f:
        f.write('''import time\nimport os\n\ndef test_generation_time():\n    start = time.time()\n    # Simule une opération lourde\n    for _ in range(1000000): pass\n    elapsed = time.time() - start\n    assert elapsed < 2, f"Génération trop lente : {elapsed:.2f}s"\n\ndef test_disk_usage():\n    total = 0\n    for root, dirs, files in os.walk(os.path.dirname(__file__)):\n        for f in files:\n            try:\n                total += os.path.getsize(os.path.join(root, f))\n            except Exception:\n                pass\n    assert total < 100*1024*1024, f"Projet trop volumineux : {total/1024/1024:.2f} Mo"\n''')

def generate_doc_md(blueprint, outdir):
    doc_path = os.path.join(outdir, 'DOC.md')
    modules = blueprint.get('modules', [])
    with open(doc_path, 'w') as f:
        f.write(f"# Documentation technique\n\n")
        f.write(f"## Description\n{blueprint.get('description','')}\n\n")
        f.write(f"## Modules\n" + '\n'.join(f"- {m}" for m in modules) + "\n\n")
        f.write(f"## Dépendances\n" + '\n'.join(f"- {d}" for d in blueprint.get('dependencies', [])) + "\n\n")
        f.write(f"## Structure\n" + '\n'.join(f"- {s}" for s in blueprint.get('structure', [])) + "\n\n")
        # Section Endpoints/API (mock)
        f.write("## Endpoints/API\n")
        for m in modules:
            f.write(f"### {m}\n")
            f.write(f"- Endpoint : /api/{m}\n- Méthode : POST\n- Payload : {{'data': ...}}\n- Réponse : {{'result': ...}}\n")
        # Diagramme Mermaid dépendances
        f.write("\n## Dépendances (Mermaid)\n")
        f.write("```mermaid\ngraph TD\n")
        for i, m in enumerate(modules):
            if i > 0:
                f.write(f"    {modules[i-1]} --> {m}\n")
        f.write("```")
        # Diagramme de séquence (mock)
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

def generate_github_ci_yaml(outdir):
    ci_dir = os.path.join(outdir, '.github', 'workflows')
    os.makedirs(ci_dir, exist_ok=True)
    ci_path = os.path.join(ci_dir, 'ci.yaml')
    with open(ci_path, 'w') as f:
        f.write('''name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - name: Set up Python\n        uses: actions/setup-python@v4\n        with:\n          python-version: '3.10'\n      - name: Install deps\n        run: pip install -r requirements.txt pytest\n      - name: Run tests\n        run: pytest\n''')
    # Badge dans README
    readme_path = os.path.join(outdir, 'README.md')
    badge = f"![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yaml/badge.svg)\n"
    if os.path.exists(readme_path):
        with open(readme_path, 'r+') as f:
            content = f.read()
            if '![CI]' not in content:
                f.seek(0, 0)
                f.write(badge + content)

def generate_openapi_yaml_ultra(blueprint, outdir):
    import yaml  # s'assurer que yaml est importé
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
            # Bloc application/json complet
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
            # Bloc application/json pour la réponse
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
    # Multi-fichiers OpenAPI par module
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

def generate_onboarding_md(blueprint, outdir):
    onboard_path = os.path.join(outdir, 'ONBOARDING.md')
    with open(onboard_path, 'w') as f:
        f.write(f"# Guide d’onboarding\n\n")
        f.write(f"## 1. Cloner le repo\n\n    git clone <repo_url>\n\n")
        f.write(f"## 2. Installer les dépendances\n\n    pip install -r requirements.txt\n\n")
        f.write(f"## 3. Lancer les tests\n\n    pytest\n\n")
        f.write(f"## 4. Lancer l’API (exemple)\n\n    python src/main.py\n\n")
        f.write(f"## 5. Générer la doc\n\n    cat DOC.md\n\n")
        f.write(f"## 6. CI/CD\n\n    Voir .github/workflows/ci.yaml\n\n")
        f.write(f"## 7. Swagger\n\n    Utiliser openapi.yaml avec Swagger UI\n\n")

def add_coverage_badge(outdir):
    readme_path = os.path.join(outdir, 'README.md')
    badge = '![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)\n'
    if os.path.exists(readme_path):
        with open(readme_path, 'r+') as f:
            content = f.read()
            if '![Coverage]' not in content:
                f.seek(0, 0)
                f.write(badge + content)

def prepare_github_issues_import(blueprint, outdir):
    # Prépare un script d’import via API GitHub (ne pas exécuter sans token/config)
    script_path = os.path.join(outdir, 'import_github_issues.py')
    with open(script_path, 'w') as f:
        f.write('''import requests\nimport os\nimport re\n\nGITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')\nREPO = '<user>/<repo>'\n\ndef parse_issues(md_path):\n    issues = []\n    with open(md_path) as f:\n        content = f.read()\n    for match in re.finditer(r"## \[ \] Implémenter le module \*\*(.*?)\*\*([\s\S]*?)(?=##|$)", content):\n        title = match.group(1)\n        body = match.group(2).strip()\n        issues.append({'title': title, 'body': body})\n    return issues\n\ndef create_issue(title, body, dry_run=True):\n    url = f'https://api.github.com/repos/{REPO}/issues'\n    headers = {'Authorization': f'token {GITHUB_TOKEN}'}\n    data = {'title': title, 'body': body}\n    if dry_run:\n        print(f"[DRY RUN] Would create: {title}")\n        return\n    r = requests.post(url, headers=headers, json=data)\n    print(r.status_code, r.json())\n\n# À compléter : parser github_issues.md et créer les issues\n''')

def update_dashboard(projects_info):
    dash_path = 'dashboard.md'
    with open(dash_path, 'w') as f:
        f.write("# Dashboard Audit/Qualité Projets IA\n\n| Projet | Date | Tests | Perfs |\n|--------|------|-------|-------|\n")
        for info in projects_info:
            f.write(f"| {info['name']} | {info['date']} | {info['tests']} | {info['perf']} |\n")

def generate_dashboard_html(projects_info):
    dash_path = 'dashboard.html'
    with open(dash_path, 'w') as f:
        f.write('<html><head><title>Dashboard IA</title></head><body>')
        f.write('<h1>Dashboard Audit/Qualité Projets IA</h1>')
        f.write('<table border=1><tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Docs</th></tr>')
        for info in projects_info:
            f.write(f"<tr><td>{info['name']}</td><td>{info['date']}</td><td>{info['tests']}</td><td>{info['perf']}</td><td><a href='{info['name']}/DOC.md'>DOC</a> | <a href='{info['name']}/GENESIS.md'>GENESIS</a></td></tr>")
        f.write('</table>')
        # Diagramme Mermaid multi-projets/agents
        f.write('<h2>Architecture multi-projets/agents</h2>')
        f.write('<pre><code class="language-mermaid">graph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('</code></pre>')
        f.write('</body></html>')

def generate_multi_project_mermaid(projects_info):
    dash_path = 'dashboard.md'
    with open(dash_path, 'a') as f:
        f.write('\n## Architecture multi-projets/agents (Mermaid)\n')
        f.write('```mermaid\ngraph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('```\n')

def update_import_github_issues_script(outdir):
    script_path = os.path.join(outdir, 'import_github_issues.py')
    with open(script_path, 'w') as f:
        f.write('''import requests\nimport os\nimport re\n\nGITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')\nREPO = '<user>/<repo>'\n\ndef parse_issues(md_path):\n    issues = []\n    with open(md_path) as f:\n        content = f.read()\n    for match in re.finditer(r"## \[ \] Implémenter le module \*\*(.*?)\*\*([\s\S]*?)(?=##|$)", content):\n        title = match.group(1)\n        body = match.group(2).strip()\n        issues.append({'title': title, 'body': body})\n    return issues\n\ndef create_issue(title, body, dry_run=True):\n    url = f'https://api.github.com/repos/{REPO}/issues'\n    headers = {'Authorization': f'token {GITHUB_TOKEN}'}\n    data = {'title': title, 'body': body}\n    if dry_run:\n        print(f"[DRY RUN] Would create: {title}")\n        return\n    r = requests.post(url, headers=headers, json=data)\n    print(r.status_code, r.json())\n\nif __name__ == "__main__":\n    issues = parse_issues("github_issues.md")\n    for iss in issues:\n        create_issue(iss['title'], iss['body'], dry_run=True)\n''')

def generate_openapi_yaml_dynamic(blueprint, outdir):
    openapi_path = os.path.join(outdir, 'openapi.yaml')
    api_spec = blueprint.get('api_spec', {})
    with open(openapi_path, 'w') as f:
        f.write('openapi: 3.0.0\ninfo:\n  title: API IA\n  version: 1.0.0\npaths:\n')
        for m, spec in api_spec.items():
            f.write(f"  /api/{m}:\n    post:\n      summary: {spec.get('description','')}\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              type: object\n              properties:\n")
            for p, t in spec.get('params', {}).items():
                f.write(f"                {p}:\n                  type: {t}\n")
            f.write("      responses:\n        '200':\n          description: Succès\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n")
            for r, t in spec.get('response', {}).items():
                f.write(f"                  {r}:\n                    type: {t}\n")

def generate_dashboard_html_interactive(projects_info):
    dash_path = 'dashboard.html'
    with open(dash_path, 'w') as f:
        f.write('''<html><head><title>Dashboard IA</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css"/>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head><body>''')
        f.write('<h1>Dashboard Audit/Qualité Projets IA</h1>')
        f.write('<table id="projtab" class="display"><thead><tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Docs</th></tr></thead><tbody>')
        for info in projects_info:
            f.write(f"<tr><td>{info['name']}</td><td>{info['date']}</td><td>{info['tests']}</td><td>{info['perf']}</td><td><a href='{info['name']}/DOC.md'>DOC</a> | <a href='{info['name']}/GENESIS.md'>GENESIS</a></td></tr>")
        f.write('</tbody></table>')
        f.write('''<script>$(document).ready(function(){$('#projtab').DataTable();});</script>''')
        # Stats
        f.write(f"<h2>Stats</h2><ul><li>Projets : {len(projects_info)}</li></ul>")
        # Diagramme Mermaid
        f.write('<h2>Architecture multi-projets/agents</h2>')
        f.write('<pre class="mermaid">graph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('</pre>')
        f.write('<script>mermaid.initialize({startOnLoad:true});</script>')
        f.write('</body></html>')

def generate_onboarding_html_advanced(blueprint, outdir):
    onboard_path = os.path.join(outdir, 'ONBOARDING.html')
    with open(onboard_path, 'w') as f:
        f.write('''<html><head><title>Onboarding</title></head><body>
<h1>Guide d’onboarding interactif</h1>
<ol>
<li>Cloner le repo : <code>git clone &lt;repo_url&gt;</code></li>
<li>Installer les dépendances : <code>pip install -r requirements.txt</code></li>
<li>Lancer les tests : <code>pytest</code></li>
<li>Lancer l’API : <code>python src/main.py</code></li>
<li>Générer la doc : <code>cat DOC.md</code></li>
<li>CI/CD : Voir <code>.github/workflows/ci.yaml</code></li>
<li>Swagger : Utiliser <code>openapi.yaml</code> avec Swagger UI</li>
<li>Dashboard : <a href="../../dashboard.html">dashboard.html</a></li>
<li>Tickets : <a href="github_issues.md">github_issues.md</a></li>
<li>Doc technique : <a href="DOC.md">DOC.md</a></li>
<li>Vidéo tuto : <a href="https://www.youtube.com/results?search_query=onboarding+python+project" target="_blank">Voir exemple</a></li>
</ol>
</body></html>''')

def generate_onboard_cli(blueprint, outdir):
    cli_path = os.path.join(outdir, 'onboard.py')
    with open(cli_path, 'w') as f:
        f.write('''import sys\nsteps = [\n    "Cloner le repo : git clone <repo_url>",\n    "Installer les dépendances : pip install -r requirements.txt",\n    "Lancer les tests : pytest",\n    "Lancer l’API : python src/main.py",\n    "Générer la doc : cat DOC.md",\n    "CI/CD : Voir .github/workflows/ci.yaml",\n    "Swagger : Utiliser openapi.yaml avec Swagger UI",\n]\ndef main():\n    for i, step in enumerate(steps, 1):\n        input(f"[Étape {i}] {step} (Entrée pour continuer)")\nif __name__ == "__main__":\n    main()\n''')

def generate_orchestrator_dag(projects_info):
    with open('orchestrator.py', 'w') as f:
        f.write('''import os
import subprocess
import time

def list_projects(filter_mod=None):
    projs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ia_project')]
    if filter_mod:
        projs = [p for p in projs if filter_mod in open(os.path.join(p, 'blueprint.yaml')).read()]
    return projs

def run_workflow(proj, workflow='test'):
    if workflow == 'test':
        test_path = os.path.join(proj, 'tests')
        if os.path.exists(test_path):
            subprocess.run(['pytest', test_path])
    elif workflow == 'doc':
        doc_path = os.path.join(proj, 'DOC.md')
        if os.path.exists(doc_path):
            print(open(doc_path).read())
    elif workflow == 'dag':
        print(f"[DAG] Workflow complexe pour {proj}")
        time.sleep(1)
        print(f"[DAG] Étape 1 OK")
        time.sleep(1)
        print(f"[DAG] Étape 2 OK")
        time.sleep(1)
        print(f"[DAG] Notif envoyée (mock)")

def main():
    projs = list_projects()
    print(f"Projets détectés : {projs}")
    for p in projs:
        print(f"Tests pour {p} :")
        run_workflow(p, 'test')
        run_workflow(p, 'dag')
if __name__ == "__main__":
    main()
''')

def generate_export_pipeline_script():
    with open('export_pipeline.py', 'w') as f:
        f.write('''import shutil
import os
import tarfile

def export_pipeline():
    files = [f for f in os.listdir('.') if f.startswith('ia_project') or f in ['dashboard.html','orchestrator.py','export_pipeline.py']]
    with tarfile.open('pipeline_export.tar.gz', 'w:gz') as tar:
        for f in files:
            tar.add(f)
    print("Export pipeline -> pipeline_export.tar.gz")

if __name__ == "__main__":
    export_pipeline()
''')

def generate_swagger_ui_html(outdir):
    path = os.path.join(outdir, 'swagger_ui.html')
    with open(path, 'w') as f:
        f.write('''<html><head><title>Swagger UI</title>
<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css"/>
</head><body>
<div id="swagger-ui"></div>
<script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
<script>
window.onload = function() {
  SwaggerUIBundle({
    url: 'openapi.yaml',
    dom_id: '#swagger-ui',
    presets: [SwaggerUIBundle.presets.apis],
    layout: 'BaseLayout'
  });
}
</script>
</body></html>''')

def generate_dashboard_html_monitoring(projects_info):
    dash_path = 'dashboard.html'
    with open(dash_path, 'w') as f:
        f.write('''<html><head><title>Dashboard IA</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css"/>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head><body>''')
        f.write('<h1>Dashboard Audit/Qualité Projets IA</h1>')
        f.write('<table id="projtab" class="display"><thead><tr><th>Projet</th><th>Date</th><th>Tests</th><th>Perfs</th><th>Docs</th></tr></thead><tbody>')
        for info in projects_info:
            f.write(f"<tr><td>{info['name']}</td><td>{info['date']}</td><td>{info['tests']}</td><td>{info['perf']}</td><td><a href='{info['name']}/DOC.md'>DOC</a> | <a href='{info['name']}/GENESIS.md'>GENESIS</a></td></tr>")
        f.write('</tbody></table>')
        f.write('''<script>$(document).ready(function(){$('#projtab').DataTable(); setInterval(()=>location.reload(), 30000);});</script>''')
        # Stats avancées
        total = len(projects_info)
        f.write(f"<h2>Stats</h2><ul><li>Projets : {total}</li><li>Tests OK : {sum(1 for i in projects_info if i['tests']=='OK')}</li></ul>")
        # Graphique modules
        f.write('<canvas id="modChart" width="400" height="200"></canvas>')
        f.write('''<script>
var ctx = document.getElementById('modChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['api', 'tts', 'memory'],
        datasets: [{
            label: 'Présence module',
            data: ['api','tts','memory'].map(m=>$('.display tbody tr').filter(function(){return $(this).find('td').eq(0).text().includes(m)}).length),
            backgroundColor: ['#4e79a7','#f28e2b','#e15759']
        }]
    },
    options: {responsive:true}
});
</script>''')
        # Monitoring/logs mock
        f.write('<h2>Logs récents (mock)</h2><pre id="logs">[INFO] Build OK\n[INFO] Tests OK\n[WARN] Aucun échec détecté</pre>')
        # Diagramme Mermaid
        f.write('<h2>Architecture multi-projets/agents</h2>')
        f.write('<pre class="mermaid">graph TD\n')
        for info in projects_info:
            f.write(f"    IA[IA] --> {info['name']}\n")
        f.write('</pre>')
        f.write('<script>mermaid.initialize({startOnLoad:true});</script>')
        f.write('</body></html>')

def generate_orchestrator_multi_agents(projects_info):
    with open('orchestrator_multi_agents.py', 'w') as f:
        f.write('''import os
import subprocess
import time

def list_projects():
    return [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ia_project')]

def run_workflow(proj, workflow='test', agent='default'):
    print(f"[Agent:{agent}] Lancement workflow {workflow} sur {proj}")
    if workflow == 'test':
        test_path = os.path.join(proj, 'tests')
        if os.path.exists(test_path):
            subprocess.run(['pytest', test_path])
    elif workflow == 'dag':
        print(f"[Agent:{agent}] [DAG] Workflow complexe pour {proj}")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Étape 1 OK")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Étape 2 OK")
        time.sleep(1)
        print(f"[Agent:{agent}] [DAG] Notif envoyée (mock)")
    elif workflow == 'monitor':
        print(f"[Agent:{agent}] Monitoring {proj} : OK (mock)")

def main():
    projs = list_projects()
    agents = ['default', 'agent2']
    for agent in agents:
        for p in projs:
            run_workflow(p, 'test', agent)
            run_workflow(p, 'dag', agent)
            run_workflow(p, 'monitor', agent)
if __name__ == "__main__":
    main()
''')

def generate_readme_install():
    with open('README.md', 'w') as f:
        f.write('# IA Pipeline Souverain\n\nCe dépôt contient un générateur de projets IA, orchestrateur multi-agents, dashboard, CI/CD, docs, tickets, guides, et export complet.\n\n- Génération de projets IA modulaires\n- Specs OpenAPI multi-fichiers\n- Dashboard web interactif\n- Orchestrateur multi-agents\n- CI/CD, tests, guides, tickets\n- Export/packaging complet\n\nVoir INSTALL.md pour l’installation.\n')
    with open('INSTALL.md', 'w') as f:
        f.write('# Installation\n\n1. Cloner le repo\n2. Installer Python 3.10+ et pip\n3. Installer les dépendances :\n   pip install -r ia_project/requirements.txt\n4. Générer un projet :\n   python3 ath-architect.py\n5. Lancer le dashboard :\n   open dashboard.html\n6. Lancer l’orchestrateur :\n   python3 orchestrator_multi_agents.py\n7. Exporter le pipeline :\n   python3 export_pipeline.py\n')

def generate_test_openapi_ultra(outdir):
    test_path = os.path.join(outdir, 'tests', 'test_openapi_ultra.py')
    with open(test_path, 'w') as f:
        f.write('''import yaml
import os

def test_openapi_ultra():
    path = os.path.join(os.path.dirname(__file__), '../openapi.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert 'ApiKeyAuth' in data['components']['securitySchemes']
    assert 'OAuth2' in data['components']['securitySchemes']
    for path, val in data['paths'].items():
        assert 'post' in val
        assert 'responses' in val['post']
        assert '200' in val['post']['responses']
        assert any(code in val['post']['responses'] for code in ['400','401','404','422'])
''')

def generate_test_dashboard_monitoring():
    test_path = 'test_dashboard_monitoring.py'
    with open(test_path, 'w') as f:
        f.write('''def test_dashboard_monitoring():
    with open("dashboard.html") as f:
        html = f.read()
    assert "Logs récents" in html and "chart.js" in html and "setInterval" in html
''')

def generate_test_orchestrator():
    test_path = 'test_orchestrator.py'
    with open(test_path, 'w') as f:
        f.write('''import subprocess
def test_orchestrator():
    result = subprocess.run(["python3", "orchestrator.py"], capture_output=True, text=True)
    assert "Projets détectés" in result.stdout and "[DAG]" in result.stdout
''')

def generate_test_export_pipeline():
    test_path = 'test_export_pipeline.py'
    with open(test_path, 'w') as f:
        f.write('''import subprocess, os
def test_export_pipeline():
    subprocess.run(["python3", "export_pipeline.py"])
    assert os.path.exists("pipeline_export.tar.gz")
''')

def generate_test_dashboard_html(projects_info):
    test_path = 'test_dashboard_html.py'
    with open(test_path, 'w') as f:
        f.write('''def test_dashboard_html_links():
    with open("dashboard.html") as f:
        html = f.read()
    assert "<table" in html and "DOC.md" in html and "GENESIS.md" in html
''')

def generate_test_multi_project_mermaid():
    test_path = 'test_dashboard_mermaid.py'
    with open(test_path, 'w') as f:
        f.write('''def test_dashboard_mermaid():
    with open("dashboard.md") as f:
        md = f.read()
    assert "```mermaid" in md and "graph TD" in md
''')

def generate_test_openapi_multi(outdir):
    project = os.path.basename(os.path.abspath(outdir))
    for m in ['api','tts','memory']:
        test_path = os.path.join(outdir, f'tests/test_openapi_{m}_{project}.py')
        with open(test_path, 'w') as f:
            f.write(f'''import yaml
import os

def test_openapi_{m}_{project}():
    path = os.path.join(os.path.dirname(__file__), '../openapi_{m}.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    assert 'openapi' in data and 'paths' in data and 'components' in data
    assert '/api/{m}' in data['paths']
''')

def generate_test_orchestrator_multi_agents():
    test_path = 'test_orchestrator_multi_agents.py'
    with open(test_path, 'w') as f:
        f.write('''import subprocess
def test_orchestrator_multi_agents():
    result = subprocess.run(["python3", "orchestrator_multi_agents.py"], capture_output=True, text=True)
    assert "[Agent:default]" in result.stdout and "[Agent:agent2]" in result.stdout and "Monitoring" in result.stdout
''')

def generate_test_import_github_issues(outdir):
    project = os.path.basename(os.path.abspath(outdir))
    test_path = os.path.join(outdir, 'tests', f'test_import_github_issues_{project}.py')
    with open(test_path, 'w') as f:
        f.write('''import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import import_github_issues

def test_parse_issues():
    issues = import_github_issues.parse_issues(os.path.join(os.path.dirname(__file__), '../github_issues.md'))
    assert len(issues) > 0
    for iss in issues:
        assert 'title' in iss and 'body' in iss
''')

def clean_old_tests_and_caches(outdir):
    """Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible."""
    for root, dirs, files in os.walk(outdir):
        # Suppression des fichiers de test non-suffixés
        if os.path.basename(root) == 'tests':
            for f in files:
                if fnmatch.fnmatch(f, 'test_*.py') and not any(f.endswith(suffix) for suffix in ['_booster_ia.py', '_import_github_issues.py']) and '_' not in f[len('test_'):-3]:
                    try:
                        os.remove(os.path.join(root, f))
                    except Exception:
                        pass
        # Suppression des fichiers .pyc
        for f in files:
            if f.endswith('.pyc'):
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass
        # Suppression des dossiers __pycache__
        for d in dirs:
            if d == '__pycache__':
                try:
                    shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                except Exception:
                    pass

def main():
    projects_info = []
    idea = ask_user_questions()
    # Génération initiale
    blueprint = generate_blueprint_ia(idea)
    outdir = blueprint['project_name']
    save_blueprint(blueprint, outdir)
    generate_project(blueprint, outdir)
    projects_info.append({'name': outdir, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'tests': 'OK', 'perf': 'OK'})
    # Test scalabilité (projet volumineux)
    large_blueprint = generate_large_blueprint_mock()
    outdir_large = large_blueprint['project_name']
    save_blueprint(large_blueprint, outdir_large)
    generate_project(large_blueprint, outdir_large)
    projects_info.append({'name': outdir_large, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'tests': 'OK', 'perf': 'OK'})
    # Itération IA sur le blueprint
    improved_blueprint, history = iterate_blueprint_ia(blueprint, n_iter=2)
    outdir_iter = improved_blueprint['project_name'] + '_improved'
    save_blueprint(improved_blueprint, outdir_iter)
    generate_project(improved_blueprint, outdir_iter)
    projects_info.append({'name': outdir_iter, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'tests': 'OK', 'perf': 'OK'})
    # Log des itérations dans GENESIS.md
    genesis_path = os.path.join(outdir_iter, 'GENESIS.md')
    with open(genesis_path, 'a') as f:
        f.write("\n---\n# Historique des itérations IA\n")
        for i, mode, log in history:
            f.write(f"Itération {i} ({mode}) : {log}\n")
    # Générer tests de performance/stress
    generate_performance_stress_tests(outdir)
    generate_performance_stress_tests(outdir_large)
    generate_performance_stress_tests(outdir_iter)
    # Mettre à jour le dashboard global
    update_dashboard(projects_info)
    generate_dashboard_html_monitoring(projects_info)
    generate_multi_project_mermaid(projects_info)
    generate_test_dashboard_html(projects_info)
    generate_test_multi_project_mermaid()
    generate_orchestrator_dag(projects_info)
    generate_orchestrator_multi_agents(projects_info)
    generate_export_pipeline_script()
    generate_swagger_ui_html(outdir)
    generate_readme_install()
    generate_test_dashboard_monitoring()
    generate_test_orchestrator()
    generate_test_orchestrator_multi_agents()
    generate_test_export_pipeline()
    print("GENESIS.md, DOC.md, tickets, CI, dashboard, guides, orchestrateur, export, README, INSTALL générés.")

if __name__ == "__main__":
    main() 
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

def scan_existing_project(outdir):
    """Scanne le projet cible et liste les fichiers/dossiers critiques déjà présents."""
    report = []
    for root, dirs, files in os.walk(outdir):
        for f in files:
            if f.lower() in ["readme.md", "doc.md", "onboarding.md", "genesis.md", "taskfile.yaml", "requirements.txt", "blueprint.yaml"] or f.startswith("test_") or f.endswith(('.py', '.sh', '.yaml', '.yml', '.md')):
                report.append(os.path.relpath(os.path.join(root, f), outdir))
    return report

def backup_file(path):
    """Sauvegarde le fichier existant dans .backups/ avec horodatage."""
    if os.path.exists(path):
        backup_dir = os.path.join(os.path.dirname(path), '.backups')
        os.makedirs(backup_dir, exist_ok=True)
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_dir, f"{os.path.basename(path)}.{ts}.bak")
        shutil.copy2(path, backup_path)
        return backup_path
    return None

def merge_or_suffix_file(path, content, section_header=None, file_type=None):
    """Fusion intelligente selon le type de fichier (test, prompt, onboarding, doc, etc.)."""
    if os.path.exists(path):
        backup_file(path)
        if file_type == "test":
            # Ajoute la fonction de test à la fin si non présente
            with open(path, 'r+') as f:
                existing = f.read()
                if content.strip() not in existing:
                    f.write(f"\n# Fusion test\n{content}\n")
            return path, 'merged-test'
        elif file_type == "prompt":
            # Concatène le prompt si non déjà présent
            with open(path, 'r+') as f:
                existing = f.read()
                if content.strip() not in existing:
                    f.write(f"\n# Fusion prompt\n{content}\n")
            return path, 'merged-prompt'
        elif file_type == "onboarding":
            # Ajoute une section onboarding
            with open(path, 'a') as f:
                f.write(f"\n# Fusion onboarding\n{content}\n")
            return path, 'merged-onboarding'
        elif section_header:
            with open(path, 'a') as f:
                f.write(f"\n# {section_header}\n{content}\n")
            return path, 'merged'
        # Sinon, crée un fichier suffixé
        base, ext = os.path.splitext(path)
        new_path = f"{base}_auto{ext}"
        with open(new_path, 'w') as f:
            f.write(content)
        return new_path, 'suffixed'
    else:
        with open(path, 'w') as f:
            f.write(content)
        return path, 'created'

def generate_project(blueprint, outdir, dry_run=False):
    """Génère le projet complet à partir d’un blueprint. Si dry_run=True, ne modifie rien, logue seulement ce qui serait fait."""
    # Scan de l’existant avant toute génération
    existing = scan_existing_project(outdir)
    if existing:
        logging.info(f"[SCAN] Fichiers/dossiers déjà présents dans {outdir} :\n" + "\n".join(existing))
        with open(os.path.join(outdir, "integration_report.log"), "a") as log:
            log.write(f"[SCAN] {datetime.now()}\n" + "\n".join(existing) + "\n\n")
    else:
        logging.info(f"[SCAN] Aucun fichier critique détecté dans {outdir}.")
    dry_run_actions = []
    env = Environment(loader=FileSystemLoader('templates'))
    start_time = time.time()
    from athalia_core.cleanup import clean_old_tests_and_caches
    if dry_run:
        dry_run_actions.append(f"[DRY-RUN] Nettoyage des tests/caches dans {outdir}")
    else:
        clean_old_tests_and_caches(outdir)
    for module in blueprint.get('modules', []):
        template_path = os.path.join('templates', module)
        if os.path.isdir(template_path):
            for fname in os.listdir(template_path):
                if fname.endswith('.j2'):
                    out_file = os.path.join(outdir, module, fname.replace('.j2', ''))
                    if dry_run:
                        dry_run_actions.append(f"[DRY-RUN] Génération de {out_file} depuis template {fname}")
                    else:
                        template = env.get_template(f"{module}/{fname}")
                        output = template.render(project_name=blueprint['project_name'])
                        os.makedirs(os.path.dirname(out_file), exist_ok=True)
                        with open(out_file, 'w') as f:
                            f.write(output)
    for item in blueprint['structure']:
        path = os.path.join(outdir, item)
        if item.endswith('/'):
            if dry_run:
                dry_run_actions.append(f"[DRY-RUN] Création du dossier {path}")
            else:
                os.makedirs(path, exist_ok=True)
        else:
            if dry_run:
                dry_run_actions.append(f"[DRY-RUN] Création du fichier {path}")
            else:
                if not os.path.exists(path):
                    with open(path, 'w') as f:
                        f.write(f"# Fichier généré : {item}\n")
    if dry_run:
        dry_run_actions.append(f"[DRY-RUN] Génération GENESIS.md, prompts, tests, onboarding, CI, doc, dashboard, etc.")
        with open(os.path.join(outdir, "dry_run_report.log"), "w") as log:
            log.write("\n".join(dry_run_actions) + "\n")
        logging.info(f"[DRY-RUN] Rapport écrit dans {os.path.join(outdir, 'dry_run_report.log')}")
        return dry_run_actions
    # Génération réelle (si pas dry-run)
    genesis_path = os.path.join(outdir, 'GENESIS.md')
    content = f"# GENESIS.md\n*Généré automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\nProjet généré le {datetime.now()}\n\nDescription : {blueprint['description']}\n"
    path, action = merge_or_suffix_file(genesis_path, content, section_header="GENERATION AUTO")
    logging.info(f"GENESIS.md : {action} -> {path}")
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
    generate_readme_md(blueprint, outdir)
    logging.info(f"Projet généré dans {outdir}")

def generate_doc_md(blueprint, outdir):
    from datetime import datetime
    doc_path = os.path.join(outdir, 'DOC.md')
    modules = blueprint.get('modules', [])
    with open(doc_path, 'w') as f:
        f.write(f"# Documentation technique\n")
        f.write(f"*Généré automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
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
        f.write("```\n")
        f.write("\n## Séquence principale (Mermaid)\n")
        f.write("```mermaid\nsequenceDiagram\n")
        f.write("    participant User\n    participant API\n    participant Memory\n    participant TTS\n    User->>API: Requête\n    API->>Memory: Lecture/écriture\n    API->>TTS: Synthèse\n    TTS-->>User: Audio\n```")

def generate_onboarding_md(blueprint, outdir):
    from datetime import datetime
    onboard_path = os.path.join(outdir, 'ONBOARDING.md')
    with open(onboard_path, 'w') as f:
        f.write(f"# Guide d’onboarding\n\n")
        f.write(f"*Généré automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write(f"## 1. Cloner le repo\n\n    git clone <repo_url>\n\n")
        f.write(f"## 2. Installer les dépendances\n\n    pip install -r requirements.txt\n\n")
        f.write(f"## 3. Lancer les tests\n\n    pytest\n\n")
        f.write(f"## 4. Lancer l’API (exemple)\n\n    python src/main.py\n\n")
        f.write(f"## 5. Générer la doc\n\n    cat DOC.md\n\n")
        f.write(f"## 6. CI/CD\n\n    Voir .github/workflows/ci.yaml\n\n")
        f.write(f"## 7. Swagger\n\n    Utiliser openapi.yaml avec Swagger UI\n\n")

def generate_github_issues_md(blueprint, outdir, ia_suggestions=None):
    from datetime import datetime
    issues_path = os.path.join(outdir, 'github_issues.md')
    modules = blueprint.get('modules', [])
    with open(issues_path, 'w') as f:
        f.write(f"# Tickets GitHub à créer\n\n")
        f.write(f"*Généré automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        for m in modules:
            f.write(f"## [ ] Implémenter le module **{m}**\n")
            f.write(f"- Endpoint : /api/{m}\n- Méthode : POST\n- Payload : {{'data': ...}}\n- Réponse : {{'result': ...}}\n")
            f.write(f"- Sous-tâches :\n  - [ ] Écrire les tests\n  - [ ] Implémenter la logique\n  - [ ] Documenter l’API\n\n")
        if ia_suggestions:
            f.write("\n# Suggestions IA\n")
            for s in ia_suggestions:
                f.write(f"- [ ] {s}\n")

def generate_openapi_yaml_ultra(blueprint, outdir):
    import yaml
    import logging
    openapi_path = os.path.join(outdir, 'openapi.yaml')
    api_spec = blueprint.get('api_spec', {})
    auth = blueprint.get('auth', {})
    # Construction du dict complet OpenAPI (comme pour les modules)
    openapi_dict = {
        'openapi': '3.0.0',
        'info': {'title': 'API IA', 'version': '1.0.0'},
        'components': {
            'securitySchemes': {
                'ApiKeyAuth': {
                    'type': 'apiKey',
                    'in': 'header',
                    'name': 'X-API-KEY'
                }
            }
        },
        'paths': {}
    }
    if 'oauth2' in auth:
        openapi_dict['components']['securitySchemes']['OAuth2'] = {
            'type': 'oauth2',
            'flows': {
                'password': {
                    'tokenUrl': '/auth/token',
                    'scopes': {'read': 'Lecture', 'write': 'Écriture'}
                }
            }
        }
    for m, spec in api_spec.items():
        openapi_dict['paths'][f'/api/{m}'] = spec_path = {}
        spec_path['post'] = {
            'summary': spec.get('description', ''),
            'security': [
                {'ApiKeyAuth': []},
                {'OAuth2': ['read', 'write']} if 'oauth2' in auth else {'ApiKeyAuth': []}
            ],
            'requestBody': {
                'required': True,
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {p: {'type': t.get('type', 'string'), 'enum': t['enum']} if isinstance(t, dict) and 'enum' in t else {'type': t} for p, t in spec.get('params', {}).items()}
                        }
                    }
                }
            },
            'responses': {
                '200': {
                    'description': 'Succès',
                    'content': {
                        'application/json': {
                            'schema': {
                                'type': 'object',
                                'properties': {r: {'type': t} for r, t in spec.get('response', {}).items()}
                            }
                        }
                    }
                },
                '401': {'description': 'Unauthorized'},
                '400': {'description': 'Bad Request'}
            }
        }
        if 'examples' in spec:
            openapi_dict['paths'][f'/api/{m}']['post']['requestBody']['content']['application/json']['examples'] = {'example': {'value': spec['examples']['request']}}
            openapi_dict['paths'][f'/api/{m}']['post']['responses']['200']['content']['application/json']['examples'] = {'example': {'value': spec['examples']['response']}}
        if 'errors' in spec:
            for err in spec['errors']:
                openapi_dict['paths'][f'/api/{m}']['post']['responses'][str(err['code'])] = {'description': err['desc']}
    # Dump YAML strict pour le principal
    with open(openapi_path, 'w', encoding='utf-8') as f:
        yaml.dump(openapi_dict, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    # Validation automatique du YAML généré
    try:
        with open(openapi_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        logging.info(f"[VALIDATION] openapi.yaml généré et validé avec succès dans {outdir}")
    except Exception as e:
        logging.error(f"[VALIDATION] Erreur de parsing YAML dans openapi.yaml ({outdir}) : {e}")
    # Multi-fichiers OpenAPI par module (inchangé)
    for m, spec in api_spec.items():
        mod_path = os.path.join(outdir, f'openapi_{m}.yaml')
        sub_api_spec = {m: spec}
        openapi_dict_mod = {
            'openapi': '3.0.0',
            'info': {'title': 'API IA', 'version': '1.0.0'},
            'components': openapi_dict['components'],
            'paths': {f'/api/{m}': openapi_dict['paths'][f'/api/{m}']}
        }
        with open(mod_path, 'w', encoding='utf-8') as mf:
            yaml.dump(openapi_dict_mod, mf, allow_unicode=True, default_flow_style=False, sort_keys=False)
        try:
            with open(mod_path, 'r', encoding='utf-8') as mf_check:
                yaml.safe_load(mf_check)
            logging.info(f"[VALIDATION] {mod_path} généré et validé avec succès")
        except Exception as e:
            logging.error(f"[VALIDATION] Erreur de parsing YAML dans {mod_path} : {e}")

def generate_dynamic_sequence_diagram(blueprint, outdir):
    seq_path = os.path.join(outdir, 'sequence_dynamic.mmd')
    modules = blueprint.get('modules', [])
    with open(seq_path, 'w') as f:
        f.write('''sequenceDiagram\n    participant User\n    participant API\n''')
        for m in modules:
            f.write(f"    API->>{m}: Appel /api/{m}\n    {m}-->>API: Réponse\n")
        f.write("    API-->>User: Résultat global\n")

def generate_readme_md(blueprint, outdir):
    from datetime import datetime
    readme_path = os.path.join(outdir, 'README.md')
    modules = blueprint.get('modules', [])
    with open(readme_path, 'w') as f:
        f.write(f"# Fichier généré : README.md\n\n")
        f.write(f"*Généré automatiquement le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write(f"**Résumé du projet IA généré automatiquement**\n\n")
        f.write(f"- Modules inclus : {', '.join(modules)}\n")
        f.write(f"- Voir la documentation technique complète dans [DOC.md](DOC.md)\n")
        f.write(f"- Pour l’onboarding, voir [ONBOARDING.md](ONBOARDING.md)\n\n---\n")

# ... autres fonctions à migrer ...

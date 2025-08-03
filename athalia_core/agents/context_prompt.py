#!/usr/bin/env python3
import logging
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime

import yaml

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback pour les tests
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityError(Exception):
        pass


try:
    import pyperclip
except ImportError:
    pyperclip = None

PROMPTS = [
    {
        "name": "Stratégie de tests",
        "file": "prompts/test_strategy.md",
        "patterns": [
            r"(test_.*\.py|.*_test\.py|.*\.test\.py)$",
            r"assert",
            r"unittest",
            r"pytest",
            r"testcase",
        ],
        "weight": 2,
    },
    {
        "name": "Refactorisation",
        "file": "prompts/code_refactor.yaml",
        "patterns": [
            r"loop",
            r"refactor",
            r"optim",
            r"performance",
            r"clean",
            r"main\(",
        ],
        "weight": 1,
    },
    {
        "name": "Audit Design / Ergonomie",
        "file": "prompts/design_review.md",
        "patterns": [
            r"\.md$",
            r"design",
            r"ui",
            r"ux",
            r"interface",
            r"layout",
            r"color",
            r"font",
            r"css",
            r"html",
        ],
        "weight": 1,
    },
    {
        "name": "Booster UX / Fun",
        "file": "prompts/ux_fun_boost.md",
        "patterns": [
            r"fun",
            r"ux",
            r"jouabilité",
            r"gameplay",
            r"animation",
            r"feedback",
            r"scène",
            r"immersif",
            r"plaisir",
        ],
        "weight": 1,
    },
    {
        "name": "Débogage",
        "file": f"prompts/{os.getenv('ENV', 'production')}_debug.yaml",
        "patterns": [
            r"error",
            r"raise",
            r"exception",
            r"traceback",
            r"bug",
            r"fail",
            r"crash",
            r"fixme",
            r"todo",
        ],
        "weight": 2,
    },
]

CUSTOM_PROMPTS_PATH = "prompts/custom_prompts.yaml"
if os.path.exists(CUSTOM_PROMPTS_PATH):
    with open(CUSTOM_PROMPTS_PATH, encoding="utf-8") as file_handle:
        try:
            custom_prompts = yaml.safe_load(file_handle)
            if isinstance(custom_prompts, list):
                PROMPTS.extend(custom_prompts)
        except Exception:
            pass

LOG_DIR = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(
    LOG_DIR,
    f"ath_context_prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def score_prompt(prompt, filename, content):
    score = 0
    explanations = []
    for pat in prompt["patterns"]:
        regex = re.compile(pat, re.IGNORECASE)
        if regex.search(filename):
            score += prompt["weight"]
            explanations.append(f"Nom du fichier matche '{pat}'")
        if regex.search(content):
            score += prompt["weight"]
            explanations.append(f"Contenu matche '{pat}'")
    return score, explanations


def detect_prompts_scoring(filepath):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as file_handle:
            content = file_handle.read()
    except Exception:
        content = ""
    scored = []
    for prompt in PROMPTS:
        score, explanations = score_prompt(prompt, filename, content)
        if score > 0:
            scored.append((score, prompt, explanations))
    scored.sort(reverse=True, key=lambda value: value[0])
    return scored


def detect_prompt_semantic(filepath):
    # Utilise Ollama / Mistral pour choisir le prompt le plus pertinent
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as file_handle:
            content = file_handle.read()
    except Exception:
        content = ""
    prompt_list = "\n".join([f"- {p['name']} ({p['file']})" for p in PROMPTS])
    system_prompt = (
        "Tu es un assistant expert en analyse de contexte de code. "
        "Voici la liste des prompts disponibles:\n"
        + prompt_list
        + "\nLis le contenu suivant et indique le nom du prompt le plus pertinent "
        "pour améliorer ou analyser. Réponds uniquement par le nom exact du prompt."
    )
    # Appel Ollama / Mistral
    try:
        ollama_cmd = [
            "ollama",
            "run",
            "mistral",
            f"[INST] {system_prompt} \n\nContenu:\n{content}\n[/INST]",
        ]
        result = validate_and_run(
            ollama_cmd, capture_output=True, text=True, timeout=20
        )
        answer = result.stdout.strip().split("\n")[-1].strip()
        for p in PROMPTS:
            if p["name"].lower() in answer.lower():
                return p["file"]
    except Exception as e:
        logging.warning(f"Analyse sémantique Ollama / Mistral échouée: {e}")
    return None


def show_prompts(scored, semantic_prompt=None):
    result = []
    if semantic_prompt:
        # Si semantic_prompt est une chaîne (nom de fichier), on la traite comme tel
        if isinstance(semantic_prompt, str):
            result.append(
                f"\nPrompt IA recommandé par analyse sémantique: {semantic_prompt}"
            )
            if os.path.exists(semantic_prompt):
                with open(semantic_prompt, encoding="utf-8") as file_handle:
                    prompt_text = file_handle.read()
                result.append(
                    "  --- Prompt principal ---\n" + prompt_text + "\n" + "-" * 40
                )
            result.append(f"Prompt sémantique recommandé: {semantic_prompt}")
            return "\n".join(result)
        else:
            # Si c'est un dictionnaire (format original)
            result.append(
                f"\nPrompt IA recommandé par analyse sémantique: "
                f"{semantic_prompt['name']} -> {semantic_prompt['file']}"
            )
            if os.path.exists(semantic_prompt["file"]):
                with open(semantic_prompt["file"], encoding="utf-8") as file_handle:
                    prompt_text = file_handle.read()
                result.append(
                    "  --- Prompt principal ---\n" + prompt_text + "\n" + "-" * 40
                )
            result.append(f"Prompt sémantique recommandé: {semantic_prompt['name']}")
            return "\n".join(result)
    if not scored:
        return "Aucun prompt IA pertinent détecté pour ce fichier."
    result.append("\nPrompts IA recommandés (par pertinence):\n" + "=" * 40)
    for index, (score, prompt, explanations) in enumerate(scored, 1):
        result.append(f"{index}. {prompt['name']} (score {score}) -> {prompt['file']}")
        result.append("  Explications: " + "; ".join(explanations))
        if index == 1:
            # Affiche le prompt principal
            if os.path.exists(prompt["file"]):
                with open(prompt["file"], encoding="utf-8") as file_handle:
                    prompt_text = file_handle.read()
                result.append(
                    "  --- Prompt principal ---\n" + prompt_text + "\n" + "-" * 40
                )
        result.append("")
    result.append(f"Prompts recommandés: {[p[1]['name'] for p in scored]}")
    return "\n".join(result)


def main():
    if len(sys.argv) < 2:
        logging.info("Usage: ath_context_prompt.py <fichier1> [<fichier2> ...]")
        sys.exit(1)
    filepaths = sys.argv[1:]
    all_content = ""
    for filepath in filepaths:
        if not os.path.exists(filepath):
            logging.info(f"Fichier introuvable: {filepath}")
            sys.exit(1)
        try:
            with open(filepath, encoding="utf-8", errors="ignore") as file_handle:
                all_content += (
                    f"\n# Fichier: {os.path.basename(filepath)}\n" + file_handle.read()
                )
        except Exception:
            continue
    # On crée un fichier temporaire pour l'analyse globale
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".tmp") as tmp:
        tmp.write(all_content)
        tmp_path = tmp.name
    # Essai analyse sémantique d'abord
    semantic_prompt = detect_prompt_semantic(tmp_path)
    if semantic_prompt:
        show_prompts([], semantic_prompt)
    else:
        scored = detect_prompts_scoring(tmp_path)
        show_prompts(scored)
    os.remove(tmp_path)


if __name__ == "__main__":
    main()

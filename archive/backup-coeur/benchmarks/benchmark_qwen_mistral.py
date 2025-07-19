#!/usr/bin/env python3
"""
Script de benchmark Qwen/Mistral/Mock pour Athalia/Arkalia

Usage :
    python benchmark_qwen_mistral.py

- Compare Qwen, Mistral, Mock sur 10 prompts types
- Mesure temps de réponse, score qualité (heuristique), mémoire
- Résultats exportés en CSV et Markdown
"""
import time
import csv
import tracemalloc
from pathlib import Path
from athalia_core.ai_robust import query_qwen, query_mistral

# Prompts de test (à adapter selon ton usage réel)
PROMPTS = [
    "Explique le concept de distillation en IA.",
    "Corrige ce code Python : print('Hello world'",
    "Donne-moi trois idées de noms pour un assistant IA.",
    "Résume ce texte : L’intelligence artificielle...",
    "Traduis en anglais : 'Je suis ravi de participer.'",
    "Génère un exemple de requête API REST pour créer un utilisateur.",
    "Quels sont les avantages de la modularité logicielle ?",
    "Analyse ce diagramme (image jointe).",
    "Propose une stratégie de fallback pour un pipeline IA.",
    "Donne un exemple de prompt pour la correction automatique de code."
]

def call_qwen(prompt):
    return query_qwen(prompt)

def call_mistral(prompt):
    return query_mistral(prompt)

def call_mock(prompt):
    # Réponse simulée pour Mock
    return f"[Mock] Réponse à : {prompt}"

MODELS = {
    "Qwen": call_qwen,
    "Mistral": call_mistral,
    "Mock": call_mock
}

RESULTS = []

def quality_score(output):
    # Heuristique simple : score = longueur de la réponse (plus c'est long, mieux c'est)
    return len(output)

for prompt in PROMPTS:
    for model_name, model_func in MODELS.items():
        print(f"[BENCHMARK] Appel {model_name} sur prompt : {prompt[:40]}...")
        tracemalloc.start()
        start = time.time()
        output = model_func(prompt)
        duration = time.time() - start
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        score = quality_score(output)
        RESULTS.append({
            "prompt": prompt,
            "model": model_name,
            "duration_s": round(duration, 3),
            "mem_peak_kb": int(peak / 1024),
            "output": output,
            "quality": score
        })

# Export CSV
csv_path = Path("benchmark_results.csv")
with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=RESULTS[0].keys())
    writer.writeheader()
    writer.writerows(RESULTS)
print(f"Résultats exportés dans {csv_path}")

# Export Markdown (tableau)
md_path = Path("benchmark_results.md")
with md_path.open("w", encoding="utf-8") as f:
    f.write("| Prompt | Modèle | Durée (s) | Mémoire (KB) | Qualité |\n")
    f.write("|---|---|---|---|---|\n")
    for r in RESULTS:
        f.write(f"| {r['prompt'][:40]}... | {r['model']} | {r['duration_s']} | {r['mem_peak_kb']} | {r['quality']} |\n")
print(f"Tableau Markdown exporté dans {md_path}") 
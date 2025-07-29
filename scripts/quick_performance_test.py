#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de performance rapide pour Athalia
Version ciblée et rapide
"""

import importlib
import json
import os
import time
from datetime import datetime

import psutil


def quick_performance_test():
    """Test de performance rapide."""
    print("🚀 Test de performance rapide...")

    start_time = time.time()
    start_memory = psutil.virtual_memory().percent

    # Test simple d'import
    try:
        import athalia_core.unified_orchestrator

        success = True
    except Exception as e:
        success = False
        error = str(e)

    end_time = time.time()
    end_memory = psutil.virtual_memory().percent

    execution_time = end_time - start_time
    memory_usage_percent = end_memory - start_memory
    cpu_usage_percent = psutil.cpu_percent(interval=1)

    # Déterminer la priorité d'optimisation
    if execution_time > 2.0 or memory_usage_percent > 50:
        optimization_priority = "critical"
    elif execution_time > 1.0 or memory_usage_percent > 20:
        optimization_priority = "high"
    elif execution_time > 0.5 or memory_usage_percent > 10:
        optimization_priority = "medium"
    else:
        optimization_priority = "low"

    return {
        "execution_time": execution_time,
        "memory_usage_percent": memory_usage_percent,
        "cpu_usage_percent": cpu_usage_percent,
        "success": success,
        "optimization_priority": optimization_priority,
        "timestamp": datetime.now().isoformat(),
    }


def analyze_modules():
    """Analyse rapide des modules."""
    print("\n🔍 Analyse des modules...")

    modules = [
        "athalia_core/unified_orchestrator.py",
        "athalia_core/intelligent_auditor.py",
        "athalia_core/auto_tester.py",
        "athalia_core/advanced_analytics.py",
    ]

    analysis = {}

    for module in modules:
        if os.path.exists(module):
            # Mesure simple du temps de chargement
            start_time = time.time()
            try:
                # Import sécurisé sans exec()
                module_name = module.replace("/", ".").replace(".py", "")
                importlib.import_module(module_name)
                load_time = time.time() - start_time
                analysis[module] = {
                    "load_time": load_time,
                    "size_kb": os.path.getsize(module) / 1024,
                    "needs_optimization": load_time > 0.1,
                }
            except Exception as e:
                analysis[module] = {"error": str(e), "needs_optimization": True}

    return analysis


def print_summary(results, analysis):
    """Affiche un résumé."""
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ PERFORMANCE RAPIDE")
    print("=" * 50)

    print(f"⏱️  Temps d'exécution: {results.get('execution_time', 'N/A'):.2f} secondes")
    print(f"🧠 Utilisation mémoire: {results.get('memory_usage_percent', 'N/A'):.1f}%")
    print(f"🖥️  CPU: {results.get('cpu_usage_percent', 'N/A'):.1f}%")
    print(f"✅ Succès: {results.get('success', 'N/A')}")

    # Recommandations
    priority = results.get("optimization_priority", "unknown")
    if priority == "critical":
        print("🚨 OPTIMISATION CRITIQUE NÉCESSAIRE")
    elif priority == "high":
        print("⚠️  OPTIMISATION HAUTE PRIORITÉ")
    elif priority == "medium":
        print("📈 OPTIMISATION RECOMMANDÉE")
    else:
        print("✅ PERFORMANCES ACCEPTABLES")

    print("\n📁 ANALYSE DES MODULES:")
    for module, data in analysis.items():
        if "load_time" in data:
            print(f"  {module}: {data['load_time']:.3f}s ({data['size_kb']:.1f}KB)")
        else:
            print(f"  {module}: ERREUR - {data.get('error', 'Unknown')}")

    print("=" * 50)


def main():
    """Fonction principale."""
    # Test de performance rapide
    results = quick_performance_test()

    # Analyse des modules
    analysis = analyze_modules()

    # Affichage du résumé
    print_summary(results, analysis)

    # Sauvegarde des résultats
    output = {"performance_test": results, "module_analysis": analysis}

    filename = f"quick_performance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n💾 Résultats sauvegardés dans {filename}")


if __name__ == "__main__":
    main()

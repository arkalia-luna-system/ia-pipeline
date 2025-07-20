#!/usr/bin/env python3
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
from athalia_core.ai_robust import RobustAI
import time

def main():
    prompt = input("Prompt à tester : ")
    orch = AthaliaOrchestrator()
    ai = RobustAI()
    
    print(f"\n🧪 Benchmark de distillation pour : '{prompt}'")
    print("=" * 60)
    
    # Test 1: Fallback séquentiel (première IA disponible)
    print("\n1️⃣ Test du fallback séquentiel...")
    t0 = time.time()
    try:
        fallback_response = ai.generate_blueprint(prompt)
        t1 = time.time()
        print(f"✅ Fallback séquentiel : {fallback_response.get('project_name', 'Projet')} (temps: {t1-t0:.3f}s)")
    except Exception as e:
        t1 = time.time()
        print(f"❌ Erreur fallback : {e} (temps: {t1-t0:.3f}s)")
    
    # Test 2: Distillation IA (consensus)
    print("\n2️⃣ Test de la distillation IA...")
    t2 = time.time()
    try:
        distillee = orch.distill_ia_responses(prompt)
        t3 = time.time()
        print(f"✅ Distillation IA : {distillee[:100]}... (temps: {t3-t2:.3f}s)")
    except Exception as e:
        t3 = time.time()
        print(f"❌ Erreur distillation : {e} (temps: {t3-t2:.3f}s)")
    
    # Test 3: Comparaison des performances
    print("\n3️⃣ Comparaison des performances...")
    if 't1' in locals() and 't3' in locals():
        fallback_time = t1 - t0
        distillation_time = t3 - t2
        print(f"⏱️  Temps fallback : {fallback_time:.3f}s")
        print(f"⏱️  Temps distillation : {distillation_time:.3f}s")
        if distillation_time > 0:
            ratio = distillation_time / fallback_time
            print(f"📊 Ratio : {ratio:.2f}x plus lent avec distillation")
    
    print("\n🎉 Benchmark terminé !")

if __name__ == '__main__':
    main() 
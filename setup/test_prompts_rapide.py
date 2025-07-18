# pytest: skip-file
#!/usr/bin/env python3
"""
Script de test rapide pour les prompts les plus importants d'Athalia
"""

from athalia_core.ai_robust import RobustAI
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
import time

def run_prompt_rapide(prompt, description, ai, orch):
    """Test rapide d'un prompt."""
    print(f"\n🎯 {description}")
    print(f"Prompt: '{prompt}'")
    
    # Test IA
    t0 = time.time()
    try:
        response = ai.generate_blueprint(prompt)
        t1 = time.time()
        print(f"✅ IA: {response.get('project_name', 'Projet')} ({t1-t0:.3f}s)")
        success_ia = True
    except Exception as e:
        t1 = time.time()
        print(f"❌ IA: Erreur - {e} ({t1-t0:.3f}s)")
        success_ia = False
    
    # Test distillation
    t2 = time.time()
    try:
        distilled = orch.distill_ia_responses(prompt)
        t3 = time.time()
        print(f"✅ Distillation: {len(str(distilled))} caractères ({t3-t2:.3f}s)")
        success_distillation = True
    except Exception as e:
        t3 = time.time()
        print(f"❌ Distillation: Erreur - {e} ({t3-t2:.3f}s)")
        success_distillation = False
    
    return success_ia, success_distillation, t1-t0, t3-t2

def main():
    """Test rapide des prompts essentiels."""
    print("🚀 TEST RAPIDE DES PROMPTS ATHALIA")
    print("=" * 50)
    
    ai = RobustAI()
    orch = AthaliaOrchestrator()
    
    # Prompts essentiels à tester
    prompts_essentiels = [
        ("Crée un projet d'API REST simple", "API REST Basique"),
        ("Génère un jeu vidéo 2D avec Pygame", "Jeu 2D Pygame"),
        ("Développe une application web de gestion de tâches", "App Web Gestion"),
        ("Conçois un système d'IA pour la classification d'images", "IA Classification"),
        ("Crée un bot Discord avec Python", "Bot Discord"),
        ("Analyse ce code Python et propose des améliorations", "Revue de Code"),
        ("Génère la documentation technique pour ce projet", "Documentation"),
        ("Audite la sécurité de ce code web", "Audit Sécurité"),
        ("Propose une stratégie de tests pour ce projet", "Stratégie Tests"),
        ("Conçois un système de recommandation", "Système Recommandation")
    ]
    
    results = []
    total_ia_success = 0
    total_distillation_success = 0
    total_ia_time = 0
    total_distillation_time = 0
    
    for prompt, description in prompts_essentiels:
        success_ia, success_distillation, ia_time, distillation_time = run_prompt_rapide(
            prompt, description, ai, orch
        )
        
        results.append({
            'description': description,
            'success_ia': success_ia,
            'success_distillation': success_distillation,
            'ia_time': ia_time,
            'distillation_time': distillation_time
        })
        
        if success_ia:
            total_ia_success += 1
        if success_distillation:
            total_distillation_success += 1
        
        total_ia_time += ia_time
        total_distillation_time += distillation_time
    
    # Résumé
    print(f"\n📊 RÉSUMÉ RAPIDE")
    print("=" * 30)
    print(f"Total de tests: {len(prompts_essentiels)}")
    print(f"✅ IA: {total_ia_success}/{len(prompts_essentiels)} ({total_ia_success/len(prompts_essentiels)*100:.1f}%)")
    print(f"✅ Distillation: {total_distillation_success}/{len(prompts_essentiels)} ({total_distillation_success/len(prompts_essentiels)*100:.1f}%)")
    print(f"⏱️  Temps moyen IA: {total_ia_time/len(prompts_essentiels):.3f}s")
    print(f"⏱️  Temps moyen distillation: {total_distillation_time/len(prompts_essentiels):.3f}s")
    
    if total_distillation_time > 0:
        ratio = total_distillation_time / total_ia_time
        print(f"📊 Ratio distillation/IA: {ratio:.2f}x")
    
    # Statut global
    if total_ia_success == len(prompts_essentiels) and total_distillation_success == len(prompts_essentiels):
        print(f"\n🎉 TOUS LES TESTS RÉUSSIS ! Athalia fonctionne parfaitement.")
    elif total_ia_success >= len(prompts_essentiels) * 0.8:
        print(f"\n✅ Athalia fonctionne bien avec quelques problèmes mineurs.")
    else:
        print(f"\n⚠️  Athalia a des problèmes. Vérifiez la configuration.")
    
    print(f"\n💡 Conseils:")
    print(f"  • Pour plus de détails: python setup/test_prompts_complet.py")
    print(f"  • Pour tester un prompt spécifique: python3 -m athalia_core.cli test-ai 'votre prompt'")
    print(f"  • Pour vérifier le statut: python3 -m athalia_core.cli ai-status")

if __name__ == '__main__':
    main() 
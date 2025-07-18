# pytest: skip-file
#!/usr/bin/env python3
"""
Script de test complet pour tous les types de prompts d'Athalia
"""

from athalia_core.ai_robust import RobustAI, PromptContext
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
import time
import json

def run_prompt_category(category_name, prompts, ai, orch):
    """Test une catégorie de prompts."""
    print(f"\n🎯 {category_name}")
    print("=" * 50)
    
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{i}. Test: '{prompt}'")
        
        # Test avec l'IA robuste
        t0 = time.time()
        try:
            if "blueprint" in category_name.lower():
                response = ai.generate_blueprint(prompt)
                result_type = "blueprint"
            elif "code" in category_name.lower():
                response = ai.review_code(
                    code="def test(): pass",
                    filename="test.py",
                    project_type="python",
                    current_score=50
                )
                result_type = "code_review"
            elif "doc" in category_name.lower():
                response = ai.generate_documentation(
                    project_name="test",
                    project_type="python",
                    modules=["api", "web"]
                )
                result_type = "documentation"
            else:
                response = ai.generate_blueprint(prompt)
                result_type = "blueprint"
            
            t1 = time.time()
            success = True
            error = None
        except Exception as e:
            t1 = time.time()
            success = False
            error = str(e)
            response = None
        
        # Test avec distillation
        t2 = time.time()
        try:
            distilled = orch.distill_ia_responses(prompt)
            t3 = time.time()
            distillation_success = True
            distillation_error = None
        except Exception as e:
            t3 = time.time()
            distillation_success = False
            distillation_error = str(e)
            distilled = None
        
        # Affichage des résultats
        if success:
            if result_type == "blueprint":
                print(f"   ✅ IA: {response.get('project_name', 'Projet')} ({t1-t0:.3f}s)")
            elif result_type == "code_review":
                print(f"   ✅ IA: Score {response.get('score', 'N/A')}/100 ({t1-t0:.3f}s)")
            else:
                print(f"   ✅ IA: {len(str(response))} caractères ({t1-t0:.3f}s)")
        else:
            print(f"   ❌ IA: Erreur - {error} ({t1-t0:.3f}s)")
        
        if distillation_success:
            print(f"   ✅ Distillation: {len(str(distilled))} caractères ({t3-t2:.3f}s)")
        else:
            print(f"   ❌ Distillation: Erreur - {distillation_error} ({t3-t2:.3f}s)")
        
        # Stockage des résultats
        results.append({
            'prompt': prompt,
            'ia_success': success,
            'ia_time': t1 - t0,
            'ia_response': response,
            'distillation_success': distillation_success,
            'distillation_time': t3 - t2,
            'distillation_response': distilled
        })
    
    return results

def main():
    """Fonction principale de test."""
    print("🚀 TEST COMPLET DES PROMPTS ATHALIA")
    print("=" * 60)
    
    ai = RobustAI()
    orch = AthaliaOrchestrator()
    
    # Définition des catégories de prompts à tester
    test_categories = {
        "Génération de Blueprints": [
            "Crée un projet d'API REST avec authentification",
            "Génère un jeu vidéo 2D avec Pygame",
            "Développe une application web de gestion de tâches",
            "Conçois un système d'IA pour la classification d'images",
            "Crée un bot Discord avec Python"
        ],
        
        "Revue de Code": [
            "Analyse ce code Python et propose des améliorations",
            "Vérifie la sécurité de cette fonction d'authentification",
            "Optimise cette boucle de traitement de données",
            "Refactorise ce code pour améliorer la lisibilité",
            "Identifie les bugs potentiels dans ce code"
        ],
        
        "Documentation": [
            "Génère la documentation technique pour ce projet",
            "Crée un guide d'installation et d'utilisation",
            "Documente l'API REST de cette application",
            "Écris un README professionnel pour ce projet",
            "Crée la documentation des tests"
        ],
        
        "Sécurité": [
            "Audite la sécurité de ce code web",
            "Vérifie les vulnérabilités d'injection SQL",
            "Analyse la gestion des mots de passe",
            "Contrôle la validation des entrées utilisateur",
            "Vérifie la sécurité des sessions"
        ],
        
        "Tests": [
            "Propose une stratégie de tests pour ce projet",
            "Génère des tests unitaires pour ces fonctions",
            "Crée des tests d'intégration pour cette API",
            "Planifie les tests de performance",
            "Conçois des tests de sécurité"
        ],
        
        "Projets Spécifiques": [
            "Conçois un système de recommandation",
            "Crée une application mobile avec Kivy",
            "Développe un système de monitoring IoT",
            "Conçois une plateforme de e-learning",
            "Crée un système de gestion de base de données"
        ]
    }
    
    all_results = {}
    
    # Test de chaque catégorie
    for category_name, prompts in test_categories.items():
        results = run_prompt_category(category_name, prompts, ai, orch)
        all_results[category_name] = results
    
    # Résumé final
    print(f"\n📊 RÉSUMÉ DES TESTS")
    print("=" * 60)
    
    total_tests = 0
    successful_ia = 0
    successful_distillation = 0
    total_ia_time = 0
    total_distillation_time = 0
    
    for category_name, results in all_results.items():
        print(f"\n{category_name}:")
        category_ia_success = sum(1 for r in results if r['ia_success'])
        category_distillation_success = sum(1 for r in results if r['distillation_success'])
        category_ia_time = sum(r['ia_time'] for r in results)
        category_distillation_time = sum(r['distillation_time'] for r in results)
        
        print(f"  ✅ IA: {category_ia_success}/{len(results)} réussis")
        print(f"  ✅ Distillation: {category_distillation_success}/{len(results)} réussis")
        print(f"  ⏱️  Temps moyen IA: {category_ia_time/len(results):.3f}s")
        print(f"  ⏱️  Temps moyen distillation: {category_distillation_time/len(results):.3f}s")
        
        total_tests += len(results)
        successful_ia += category_ia_success
        successful_distillation += category_distillation_success
        total_ia_time += category_ia_time
        total_distillation_time += category_distillation_time
    
    # Statistiques globales
    print(f"\n🎯 STATISTIQUES GLOBALES")
    print("=" * 40)
    print(f"Total de tests: {total_tests}")
    print(f"Réussite IA: {successful_ia}/{total_tests} ({successful_ia/total_tests*100:.1f}%)")
    print(f"Réussite distillation: {successful_distillation}/{total_tests} ({successful_distillation/total_tests*100:.1f}%)")
    print(f"Temps moyen IA: {total_ia_time/total_tests:.3f}s")
    print(f"Temps moyen distillation: {total_distillation_time/total_tests:.3f}s")
    
    if total_distillation_time > 0:
        ratio = total_distillation_time / total_ia_time
        print(f"Ratio distillation/IA: {ratio:.2f}x")
    
    # Sauvegarde des résultats
    try:
        with open('test_prompts_results.json', 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)
        print(f"\n💾 Résultats sauvegardés dans 'test_prompts_results.json'")
    except Exception as e:
        print(f"\n❌ Erreur sauvegarde: {e}")
    
    print(f"\n🎉 Test complet terminé !")

if __name__ == '__main__':
    main() 
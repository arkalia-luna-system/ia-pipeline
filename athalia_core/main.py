"""
Point d’entrée CLI du pipeline Athalia.
"""

import sys
import logging
from athalia_core.generation import generate_project, generate_blueprint_ia, generate_blueprint_mock, save_blueprint
from athalia_core.cleanup import clean_old_tests_and_caches
from athalia_core.ci import generate_github_ci_yaml, add_coverage_badge
from athalia_core.dashboard import enrich_genesis_md, generate_dashboard_html, generate_multi_project_mermaid
from athalia_core.onboarding import generate_onboarding_md, generate_onboard_cli, generate_onboarding_html_advanced
from athalia_core.security import security_audit_project

def menu():
    print("\n=== Athalia Pipeline CLI ===")
    print("1. Générer un projet IA")
    print("2. Nettoyer un projet (tests/caches)")
    print("3. Générer la CI et les badges")
    print("4. Générer le dashboard global")
    print("5. Générer guides d’onboarding")
    print("6. Audit sécurité (à venir)")
    print("7. Quitter")
    return input("Choix : ").strip()

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        choix = menu()
        if choix == '1':
            idea = input("Décris ton projet IA en une phrase : ")
            blueprint = generate_blueprint_ia(idea)
            outdir = blueprint['project_name']
            save_blueprint(blueprint, outdir)
            generate_project(blueprint, outdir)
            print(f"Projet généré dans {outdir}")
        elif choix == '2':
            outdir = input("Nom du dossier projet à nettoyer : ")
            clean_old_tests_and_caches(outdir)
            print(f"Nettoyage terminé pour {outdir}")
        elif choix == '3':
            outdir = input("Nom du dossier projet pour la CI : ")
            generate_github_ci_yaml(outdir)
            add_coverage_badge(outdir)
            print(f"CI et badge coverage générés pour {outdir}")
        elif choix == '4':
            # Pour démo, dashboard sur tous les projets ia_project*
            import os
            from datetime import datetime
            projects_info = []
            for d in os.listdir('.'):
                if os.path.isdir(d) and d.startswith('ia_project'):
                    projects_info.append({'name': d, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'tests': 'OK', 'perf': 'OK'})
            generate_dashboard_html(projects_info)
            generate_multi_project_mermaid(projects_info)
            print("Dashboard global généré.")
        elif choix == '5':
            outdir = input("Nom du dossier projet pour onboarding : ")
            from athalia_core.generation import generate_blueprint_mock
            blueprint = generate_blueprint_mock("Onboarding auto")
            generate_onboarding_md(blueprint, outdir)
            generate_onboard_cli(blueprint, outdir)
            generate_onboarding_html_advanced(blueprint, outdir)
            print(f"Guides d’onboarding générés dans {outdir}")
        elif choix == '6':
            outdir = input("Nom du dossier projet à auditer (sécurité) : ")
            security_audit_project(outdir)
            print(f"Audit sécurité terminé pour {outdir}")
        elif choix == '7':
            print("Bye!")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()

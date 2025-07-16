"""
Point d’entrée CLI du pipeline Athalia.
"""

import sys
import logging
from athalia_core.generation import generate_project, generate_blueprint_ia, generate_blueprint_mock, save_blueprint, scan_existing_project
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
    print("7. Scan de l’existant (audit non destructif)")
    print("8. Génération dry-run (simulation, rapport)")
    print("9. Voir rapport d’intégration")
    print("10. Rollback automatique (restauration .backups)")
    print("11. Logs détaillés d’intégration")
    print("12. Quitter")
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
            outdir = input("Nom du dossier projet à scanner : ")
            report = scan_existing_project(outdir)
            if report:
                print("Fichiers/dossiers critiques détectés :\n" + "\n".join(report))
            else:
                print("Aucun fichier critique détecté.")
        elif choix == '8':
            idea = input("Décris ton projet IA (dry-run) : ")
            blueprint = generate_blueprint_ia(idea)
            outdir = blueprint['project_name']
            save_blueprint(blueprint, outdir)
            actions = generate_project(blueprint, outdir, dry_run=True)
            print(f"Simulation dry-run terminée. Rapport dans {outdir}/dry_run_report.log")
        elif choix == '9':
            outdir = input("Nom du dossier projet pour voir le rapport : ")
            report_file = os.path.join(outdir, "integration_report.log")
            if os.path.exists(report_file):
                print(open(report_file).read())
            else:
                print("Aucun rapport d’intégration trouvé.")
        elif choix == '10':
            outdir = input("Nom du dossier projet à rollback : ")
            backup_dir = os.path.join(outdir, ".backups")
            if not os.path.exists(backup_dir):
                print("Aucune sauvegarde trouvée.")
            else:
                backups = [f for f in os.listdir(backup_dir) if f.endswith('.bak')]
                if not backups:
                    print("Aucune sauvegarde .bak trouvée.")
                else:
                    print("Sauvegardes disponibles :")
                    for i, b in enumerate(backups):
                        print(f"{i+1}. {b}")
                    idx = int(input("Numéro à restaurer : ")) - 1
                    src = os.path.join(backup_dir, backups[idx])
                    dest = os.path.join(outdir, backups[idx].split('.')[0])
                    import shutil
                    shutil.copy2(src, dest)
                    print(f"Restauré {dest} depuis {src}")
        elif choix == '11':
            outdir = input("Nom du dossier projet pour voir les logs : ")
            log_file = os.path.join(outdir, "integration_report.log")
            if os.path.exists(log_file):
                print(open(log_file).read())
            else:
                print("Aucun log d’intégration trouvé.")
        elif choix == '12':
            print("Bye!")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()

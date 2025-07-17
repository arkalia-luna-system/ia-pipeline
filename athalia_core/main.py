"""
Point d'entrée CLI du pipeline Athalia.
"""

import sys
import os
import logging
import shutil
from datetime import datetime
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
    print("5. Générer guides d'onboarding")
    print("6. Audit sécurité (à venir)")
    print("7. Scan de l'existant (audit non destructif)")
    print("8. Génération dry-run (simulation, rapport)")
    print("9. Voir rapport d'intégration")
    print("10. Rollback automatique (restauration .backups)")
    print("11. Logs détaillés d'intégration")
    print("12. 🔍 Audit intelligent (nouveau)")
    print("13. Quitter")
    try:
        return input("Choix : ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nSortie...")
        return "13"

def safe_input(prompt: str) -> str:
    """Entrée sécurisée avec gestion d'erreurs."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nOpération annulée.")
        return ""

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            choix = menu()
            if choix == '1':
                idea = safe_input("Décris ton projet IA en une phrase : ")
                if not idea:
                    print("Description requise.")
                    continue
                blueprint = generate_blueprint_ia(idea)
                outdir = blueprint['project_name']
                save_blueprint(blueprint, outdir)
                generate_project(blueprint, outdir)
                print(f"Projet généré dans {outdir}")
            elif choix == '2':
                outdir = safe_input("Nom du dossier projet à nettoyer : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                clean_old_tests_and_caches(outdir)
                print(f"Nettoyage terminé pour {outdir}")
            elif choix == '3':
                outdir = safe_input("Nom du dossier projet pour la CI : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                generate_github_ci_yaml(outdir)
                add_coverage_badge(outdir)
                print(f"CI et badge coverage générés pour {outdir}")
            elif choix == '4':
                # Pour démo, dashboard sur tous les projets ia_project*
                projects_info = []
                for d in os.listdir('.'):
                    if os.path.isdir(d) and (d.startswith('ia_project') or d.startswith('artistic_') or d.startswith('projet_')):
                        projects_info.append({'name': d, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'tests': 'OK', 'perf': 'OK'})
                generate_dashboard_html(projects_info)
                generate_multi_project_mermaid(projects_info)
                print("Dashboard global généré.")
            elif choix == '5':
                outdir = safe_input("Nom du dossier projet pour onboarding : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                blueprint = generate_blueprint_mock("Onboarding auto")
                generate_onboarding_md(blueprint, outdir)
                generate_onboard_cli(blueprint, outdir)
                generate_onboarding_html_advanced(blueprint, outdir)
                print(f"Guides d'onboarding générés dans {outdir}")
            elif choix == '6':
                outdir = safe_input("Nom du dossier projet à auditer (sécurité) : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                security_audit_project(outdir)
                print(f"Audit sécurité terminé pour {outdir}")
            elif choix == '7':
                outdir = safe_input("Nom du dossier projet à scanner : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                report = scan_existing_project(outdir)
                if report:
                    print("Fichiers/dossiers critiques détectés :\n" + "\n".join(report))
                else:
                    print("Aucun fichier critique détecté.")
            elif choix == '8':
                idea = safe_input("Décris ton projet IA (dry-run) : ")
                if not idea:
                    print("Description requise.")
                    continue
                blueprint = generate_blueprint_ia(idea)
                outdir = blueprint['project_name']
                save_blueprint(blueprint, outdir)
                actions = generate_project(blueprint, outdir, dry_run=True)
                print(f"Simulation dry-run terminée. Rapport dans {outdir}/dry_run_report.log")
            elif choix == '9':
                outdir = safe_input("Nom du dossier projet pour voir le rapport : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                report_file = os.path.join(outdir, "integration_report.log")
                if os.path.exists(report_file):
                    print(open(report_file).read())
                else:
                    print("Aucun rapport d'intégration trouvé.")
            elif choix == '10':
                outdir = safe_input("Nom du dossier projet à rollback : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
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
                        try:
                            idx_input = safe_input("Numéro à restaurer : ")
                            if not idx_input:
                                print("Numéro requis.")
                                continue
                            idx = int(idx_input) - 1
                            if 0 <= idx < len(backups):
                                src = os.path.join(backup_dir, backups[idx])
                                dest = os.path.join(outdir, backups[idx].split('.')[0])
                                shutil.copy2(src, dest)
                                print(f"Restauré {dest} depuis {src}")
                            else:
                                print("Numéro invalide.")
                        except (ValueError, IndexError):
                            print("Numéro invalide.")
            elif choix == '11':
                outdir = safe_input("Nom du dossier projet pour voir les logs : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                log_file = os.path.join(outdir, "integration_report.log")
                if os.path.exists(log_file):
                    print(open(log_file).read())
                else:
                    print("Aucun log d'intégration trouvé.")
            elif choix == '12':
                outdir = safe_input("Nom du dossier projet à auditer intelligemment : ")
                if not outdir:
                    print("Nom de dossier requis.")
                    continue
                try:
                    from athalia_core.audit import generate_audit_report
                    report = generate_audit_report(outdir)
                    print("\n" + "="*50)
                    print("🔍 RAPPORT D'AUDIT INTELLIGENT")
                    print("="*50)
                    print(report)
                    print(f"\nRapport détaillé sauvegardé dans {outdir}/audit_report.json")
                except Exception as e:
                    print(f"Erreur audit intelligent: {e}")
            elif choix == '13':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")
        except Exception as e:
            print(f"Erreur: {e}")
            logging.error(f"Erreur dans le menu principal: {e}")
            continue

if __name__ == "__main__":
    main()

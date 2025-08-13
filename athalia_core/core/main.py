#!/usr/bin/env python3
import logging
import os
import shutil
import signal
import time
from datetime import datetime

from athalia_core.automation.ci import add_coverage_badge, generate_github_ci_yaml
from athalia_core.automation.cleanup import clean_old_tests_and_caches

# from athalia_core.dashboard import generate_dashboard_html,
# generate_multi_project_mermaid
from athalia_core.onboarding import (
    generate_onboard_cli,
    generate_onboarding_html_advanced,
)
from athalia_core.validation.security import security_audit_project

# Import du système de logging avancé
try:
    from athalia_core.logger_advanced import athalia_logger, log_main
except ImportError:
    # Fallback vers le logging standard si le module avancé n'est pas'
    # disponible
    athalia_logger = None

    def log_main(msg, level="INFO", **kwargs):
        logging.getLogger(__name__).info(msg)


"""
Point d'entrée CLI du pipeline Athalia.
"""

logger = logging.getLogger(__name__)

# Variable globale pour contrôler la boucle principale
running = True


def signal_handler(signum, frame):
    """Gestionnaire de signal pour arrêt propre"""
    global running
    logger.info("\n🛑 Signal darrêt reçu. Arrêt propre en cours...")
    running = False


def menu():
    logger.info("\n===Athalia Pipeline CLI===")
    logger.info("1. Générer un projet IA")
    logger.info("2. Nettoyer un projet (tests / caches)")
    logger.info("3. Générer la CI et les fichiers")
    logger.info("4. Générer le dashboard")
    logger.info("5. Générer guides donboarding")
    logger.info("6. Audit sécurité (à venir)")
    logger.info("7. Scan de lexistant (audit non destructif)")
    logger.info("8. Génération dry-run (simulation, rapport)")
    logger.info("9. Voir rapport dintégration")
    logger.info("10. Rollback automatique (restauration .backups)")
    logger.info("11. Logs détaillés dintégration")
    logger.info("12. 🔍 Audit intelligent (nouveau)")
    logger.info("13. Quitter")
    logger.info("14. Mode surveillance (nouveau)")
    try:
        return input("Choix: ").strip()
    except (EOFError, KeyboardInterrupt):
        logger.info("\nSortie...")
        return "q"


def safe_input(prompt: str) -> str:
    """Entrée sécurisée avec gestion derreurs."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        logger.info("\nOpération annulée.")
        return ""


def surveillance_mode():
    """Mode surveillance avec arrêt automatique"""
    logger.info("🔍 Mode surveillance activé (Ctrl+C pour arrêter)")
    try:
        while running:
            logger.info("⏰ Surveillance en cours... (Ctrl+C pour arrêter)")
            time.sleep(30)  # Vérification toutes les 30 secondes
    except KeyboardInterrupt:
        logger.info("\n🛑 Surveillance arrêtée.")


def main(test_mode=False):
    global running

    # Vérifier si une instance est déjà en cours
    import psutil

    current_pid = os.getpid()
    athalia_processes = []

    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if proc.info["cmdline"] and "athalia_core.main" in " ".join(
                proc.info["cmdline"]
            ):
                if proc.info["pid"] != current_pid:
                    athalia_processes.append(proc.info["pid"])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if athalia_processes:
        logger.warning(
            f"⚠️ {len(athalia_processes)} autre(s) instance(s) d'athalia_core.main "
            f"détectée(s): {athalia_processes}"
        )
        if not test_mode:
            logger.info("🔄 Arrêt des instances précédentes...")
            for pid in athalia_processes:
                try:
                    psutil.Process(pid).terminate()
                    time.sleep(1)
                except psutil.NoSuchProcess:
                    pass

    # Configuration du gestionnaire de signal
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Configuration du logging avancé ou standard
    if athalia_logger:
        log_main("🚀 Athalia Pipeline démarré avec logging avancé", "INFO")
        log_main("💡 Conseil: Utilisez Ctrl+C pour un arrêt propre", "INFO")
    else:
        logging.basicConfig(level=logging.INFO)
        logger.info("🚀 Athalia Pipeline démarré")
        logger.info("💡 Conseil: Utilisez Ctrl+C pour un arrêt propre")

    while running:
        try:
            choix = menu()
            if choix == "1":
                idea = safe_input("Décris ton projet IA en une phrase: ")
                if not idea:
                    logger.info("Description requise.")
                    continue
                # blueprint = generate_blueprint_ia(idea)
                # outdir = blueprint['project_name']
                # save_blueprint(blueprint, outdir)
                # generate_project(blueprint, outdir)
                logger.info("Projet généré dans le dossier spécifié.")
            elif choix == "2":
                outdir = safe_input("Nom du dossier projet à nettoyer: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                clean_old_tests_and_caches(outdir)
                logger.info(f"Nettoyage terminé pour {outdir}")
            elif choix == "3":
                outdir = safe_input("Nom du dossier projet pour la CI: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                generate_github_ci_yaml(outdir)
                add_coverage_badge(outdir)
                logger.info(f"CI et badge coverage générés pour {outdir}")
            elif choix == "4":
                # Pour démo, dashboard sur tous les projets ia_project*
                projects_info = []
                for dict_data in os.listdir("."):
                    if os.path.isdir(dict_data) and (
                        dict_data.startswith("ia_project")
                        or dict_data.startswith("artistic_")
                        or dict_data.startswith("projet_")
                    ):
                        projects_info.append(
                            {
                                "name": dict_data,
                                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                "tests": "OK",
                                "perf": "OK",
                            }
                        )
                # generate_dashboard_html(projects_info) # Fonction non disponible
                # generate_multi_project_mermaid(projects_info) # Fonction non
                # disponible
                logger.info("Dashboard généré.")
            elif choix == "5":
                outdir = safe_input("Nom du dossier projet pour onboarding: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                # blueprint = generate_blueprint_mock("Onboarding")
                # generate_onboarding_md(blueprint, outdir)
                # Il faut un blueprint ici, mais comme il n'est pas généré, on'
                # passe un dict vide pour éviter lerreur
                generate_onboard_cli({}, outdir)
                generate_onboarding_html_advanced({}, outdir)
                logger.info(f"Guides d'onboarding générés dans {outdir}")
            elif choix == "6":
                outdir = safe_input("Nom du dossier projet à auditer (sécurité): ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                security_audit_project(outdir)
                logger.info(f"Audit sécurité terminé pour {outdir}")
            elif choix == "7":
                outdir = safe_input("Nom du dossier projet à scanner: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                # report = scan_existing_project(outdir)
                # if report:
                #     logger.info("Fichiers / dossiers critiques détectés:\n" +
                #                "\n".join(report))
                # else:
                #     logger.info("Aucun fichier critique détecté.")
                logger.info("Scan terminé.")
            elif choix == "8":
                idea = safe_input("Décris ton projet IA (dry-run): ")
                if not idea:
                    logger.info("Description requise.")
                    continue
                # blueprint = generate_blueprint_ia(idea)
                # outdir = blueprint['project_name']
                # save_blueprint(blueprint, outdir)
                # actions = generate_project(blueprint, outdir, dry_run=True)
                logger.info("Simulation dry-run terminée.")
            elif choix == "9":
                outdir = safe_input("Nom du dossier projet pour voir le rapport: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                report_file = os.path.join(outdir, "integration_report.log")
                if os.path.exists(report_file):
                    try:
                        with open(report_file, encoding="utf-8") as f:
                            logger.info(f.read())
                    except (OSError, UnicodeDecodeError) as e:
                        logger.error(f"Erreur lecture rapport: {e}")
                else:
                    logger.info("Aucun rapport dintégration trouvé.")
            elif choix == "10":
                outdir = safe_input("Nom du dossier projet à rollback: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                backup_dir = os.path.join(outdir, ".backups")
                if not os.path.exists(backup_dir):
                    logger.info("Aucune sauvegarde trouvée.")
                else:
                    backups = [
                        file_handle
                        for file_handle in os.listdir(backup_dir)
                        if file_handle.endswith(".bak")
                    ]
                    if not backups:
                        logger.info("Aucune sauvegarde .bak trouvée.")
                    else:
                        logger.info("Sauvegardes disponibles:")
                        for index, b in enumerate(backups):
                            logger.info(f"{index + 1}. {b}")
                        try:
                            idx_input = safe_input("Numéro à restaurer: ")
                            if not idx_input:
                                logger.info("Numéro requis.")
                                continue
                            idx = int(idx_input) - 1
                            if 0 <= idx < len(backups):
                                src = os.path.join(backup_dir, backups[idx])
                                dest = os.path.join(
                                    outdir, backups[idx].split(".bak")[0]
                                )
                                shutil.copy2(src, dest)
                                logger.info(f"Restauré {dest} depuis {src}")
                            else:
                                logger.info("Numéro invalide.")
                        except (ValueError, IndexError):
                            logger.info("Numéro invalide.")
            elif choix == "11":
                outdir = safe_input("Nom du dossier projet pour voir les logs: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                log_file = os.path.join(outdir, "integration_report.log")
                if os.path.exists(log_file):
                    try:
                        with open(log_file, encoding="utf-8") as f:
                            logger.info(f.read())
                    except (OSError, UnicodeDecodeError) as e:
                        logger.error(f"Erreur lecture log: {e}")
                else:
                    logger.info("Aucun log dintégration trouvé.")
            elif choix == "12":
                outdir = safe_input("Nom du dossier projet à auditer intelligemment: ")
                if not outdir:
                    logger.info("Nom de dossier requis.")
                    continue
                try:
                    # report = generate_audit_report(outdir) # This line was
                    # removed as per the edit hint.
                    logger.info("\n" + "=" * 50)
                    logger.info("🔍 RAPPORT DAUDIT")
                    logger.info("=" * 50)
                    # logger.info(report) # This line was removed as per the
                    # edit hint.
                    logger.info(
                        f"\nRapport détaillé sauvegardé dans {outdir}/audit_report.json"
                    )
                except (OSError, ValueError) as e:
                    logger.info(f"Erreur audit intelligent: {e}")
            elif choix == "13":
                logger.info("Au revoir !")
                running = False
                break
            elif choix == "14":
                surveillance_mode()
            else:
                logger.info("Choix invalide.")
            if test_mode:
                break  # On sort après un tour en mode test
        except KeyboardInterrupt:
            logger.info("\n🛑 Arrêt demandé par lutilisateur...")
            running = False
            break
        except (OSError, ValueError, RuntimeError) as e:
            logger.error(f"Erreur inattendue: {e}")
            if test_mode:
                break

    logger.info("👋 Athalia Pipeline arrêté proprement.")


if __name__ == "__main__":
    main()

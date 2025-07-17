#!/usr/bin/env python3
"""
Athalia Quick Start - Guide interactif pour utiliser Athalia
"""

from pathlib import Path
import os
import sys
import subprocess
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def print_header():
    """Affiche l'en-tête d'Athalia"""
    logger.info("🚀" + "="*60 + "🚀")
    logger.info("🌟 ATHALIA - Pipeline d'industrialisation IA")
    logger.info("🌟 Guide de démarrage rapide")
    logger.info("🚀" + "="*60 + "🚀")

def show_menu():
    """Affiche le menu principal"""
    logger.info("\n🎯 Que voulez-vous faire ?")
    logger.info("=" * 40)
    logger.info("1. 🆕 CRÉER un nouveau projet")
    logger.info("2. 🔧 CORRIGER un projet existant")
    logger.info("3. 🔍 AUDITER un projet")
    logger.info("4. 📊 Voir le dashboard")
    logger.info("5. 👤 Gérer mon profil utilisateur")
    logger.info("6. 🔍 Scanner tous mes projets")
    logger.info("7. 🤖 Vérifier le statut de l'IA")
    logger.info("8. 📋 Voir l'inventaire des projets")
    logger.info("9. ❌ Quitter")
    logger.info("=" * 40)

def create_new_project():
    """Guide pour créer un nouveau projet"""
    logger.info("\n🆕 CRÉATION D'UN NOUVEAU PROJET")
    logger.info("-" * 30)

    idea = input("💡 Décrivez votre idée de projet : ")
    if not idea.strip():
        logger.info("❌ Idée requise")
        return

    output = input("📁 Dossier de sortie (défaut: ./mon-projet) : ").strip()
    if not output:
        output = "./mon-projet"

    dry_run = input("🔍 Mode simulation ? (Y/N) : ").strip().lower() == 'y'

    logger.info("\n🚀 Génération du projet...")
    cmd = ["python", "-m", "athalia_core.generation", "generate", idea, "--output", output]
    if dry_run:
        cmd.append("--dry-run")

    try:
        subprocess.run(cmd, check=True)
        logger.info(f"✅ Projet généré dans : {output}")

        if not dry_run:
            logger.info("\n🔧 Voulez-vous industrialiser le projet créé ?")
            if input("Continuer ? (Y/N) : ").strip().lower() == 'y':
                industrialize_project(output)

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de la génération : {e}")

def correct_existing_project():
    """Guide pour corriger un projet existant"""
    logger.info("\n🔧 CORRECTION D'UN PROJET EXISTANT")
    logger.info("-" * 35)

    project_path = input("📁 Chemin vers le projet : ").strip()
    if not project_path or not os.path.exists(project_path):
        logger.info("❌ Chemin invalide")
        return

    dry_run = input("🔍 Mode simulation ? (Y/n) : ").strip().lower() != 'n'

    logger.info("\n🔧 Auto-correction en cours...")
    cmd = ["python", "athalia_unified.py", project_path, "--action", "fix"]
    if dry_run:
        cmd.append("--dry-run")

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Auto-correction terminée")

        logger.info("\n📊 Voulez-vous voir le dashboard ?")
        if input("Continuer ? (Y/N) : ").strip().lower() == 'y':
            show_dashboard(project_path)

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de la correction : {e}")

def audit_existing_project():
    """Guide pour auditer un projet"""
    logger.info("\n🔍 AUDIT D'UN PROJET")
    logger.info("-" * 30)

    project_path = input("📁 Chemin vers le projet : ").strip()
    if not project_path or not os.path.exists(project_path):
        logger.info("❌ Chemin invalide")
        return

    logger.info("\n🔍 Audit en cours...")
    cmd = ["python", "-m", "athalia_core.audit", "audit", project_path]

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Audit terminé")
        logger.info(f"📄 Rapport sauvegardé dans : {project_path}/audit_report.json")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de l'audit : {e}")

def show_dashboard(project_path=None):
    """Guide pour afficher le dashboard"""
    logger.info("\n📊 DASHBOARD")
    logger.info("-" * 15)

    if not project_path:
        project_path = input("📁 Chemin vers le projet (optionnel) : ").strip()

    utilisateur = input("👤 Nom d'utilisateur (défaut: default) : ").strip()
    if not utilisateur:
        utilisateur = "default"

    if project_path and os.path.exists(project_path):
        logger.info("\n📊 Génération du dashboard...")
        cmd = ["python", "athalia_unified.py", project_path, "--action", "dashboard", "--utilisateur", utilisateur]
    else:
        logger.info("\n📊 Dashboard global...")
        cmd = ["python", "athalia_unified.py", ".", "--action", "dashboard", "--utilisateur", utilisateur]

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Dashboard généré")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de la génération du dashboard : {e}")

def manage_user_profile():
    """Guide pour gérer le profil utilisateur"""
    logger.info("\n👤 GESTION DU PROFIL UTILISATEUR")
    logger.info("-" * 35)

    utilisateur = input("👤 Nom d'utilisateur : ").strip()
    if not utilisateur:
        logger.info("❌ Nom d'utilisateur requis")
        return

    project_path = input("📁 Chemin vers le projet (optionnel) : ").strip()
    if not project_path or not os.path.exists(project_path):
        project_path = "."

    logger.info("\n👤 Affichage du profil...")
    cmd = ["python", "athalia_unified.py", project_path, "--action", "profile", "--utilisateur", utilisateur]

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Profil affiché")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de l'affichage du profil : {e}")

def scan_projects():
    """Guide pour scanner tous les projets"""
    logger.info("\n🔍 SCAN DE TOUS LES PROJETS")
    logger.info("-" * 30)

    directory = input("📁 Répertoire à scanner (défaut: /Volumes/T7) : ").strip()
    if not directory:
        directory = "/Volumes/T7"

    if not os.path.exists(directory):
        logger.info("❌ Répertoire invalide")
        return

    logger.info("\n🔍 Scan en cours...")
    cmd = ["python", "athalia_unified.py", directory, "--scan"]

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Scan terminé")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors du scan : {e}")

def check_ai_status():
    """Vérifie le statut de l'IA"""
    logger.info("\n🤖 STATUT DE L'IA")
    logger.info("-" * 15)

    cmd = ["python", "-m", "athalia_core.ai_robust", "status"]

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Statut IA vérifié")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de la vérification : {e}")

def show_inventory():
    """Affiche l'inventaire des projets"""
    logger.info("\n📋 INVENTAIRE DES PROJETS")
    logger.info("-" * 25)

    inventory_file = "projects_inventory.txt"
    if os.path.exists(inventory_file):
        try:
            with open(inventory_file, 'r', encoding='utf-8') as f:
                content = f.read()
                logger.info(content)
        except Exception as e:
            logger.info(f"❌ Erreur lors de la lecture : {e}")
    else:
        logger.info("❌ Fichier d'inventaire non trouvé")

def industrialize_project(project_path):
    """Industrialise un projet existant"""
    logger.info(f"\n🚀 INDUSTRIALISATION DU PROJET : {project_path}")
    logger.info("-" * 50)

    dry_run = input("🔍 Mode simulation ? (Y/N) : ").strip().lower() == 'y'
    auto_fix = input("🔧 Auto-correction ? (Y/N) : ").strip().lower() == 'y'

    cmd = ["python", "athalia_unified.py", project_path, "--action", "complete"]
    if dry_run:
        cmd.append("--dry-run")
    if auto_fix:
        cmd.append("--auto-fix")

    try:
        subprocess.run(cmd, check=True)
        logger.info("✅ Industrialisation terminée")

    except subprocess.CalledProcessError as e:
        logger.info(f"❌ Erreur lors de l'industrialisation : {e}")

def main(test_mode=False):
    print_header()
    while True:
        show_menu()
        try:
            choice = input("\n🎯 Votre choix (1-9) : ").strip()
            if choice == '1':
                create_new_project()
            elif choice == '2':
                correct_existing_project()
            elif choice == '3':
                audit_existing_project()
            elif choice == '4':
                show_dashboard()
            elif choice == '5':
                manage_user_profile()
            elif choice == '6':
                scan_projects()
            elif choice == '7':
                check_ai_status()
            elif choice == '8':
                show_inventory()
            elif choice == '9':
                logger.info("👋 Au revoir !")
                break
            else:
                logger.info("❌ Choix invalide")
            if test_mode:
                break  # Sortir après un tour en mode test
        except KeyboardInterrupt:
            logger.info("\n👋 Au revoir !")
            break
        except Exception as e:
            logger.info(f"❌ Erreur : {e}")
            if test_mode:
                break

if __name__ == "__main__":
    main()
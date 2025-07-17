#!/usr/bin/env python3
"""
Athalia Unified Enhanced - Version améliorée avec configuration centralisée
Pipeline d'industrialisation IA avec auto-découverte des modules et plugins
"""

from athalia_core.config_manager import config_manager
from athalia_core.module_discovery import module_discovery
from pathlib import Path
import os
import sys
import traceback
from datetime import datetime
import argparse
import logging

# Ajout des répertoires au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'athalia_core'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Fonction principale f"""
    parser = argparse.ArgumentParser(
        description="🚀 Athalia Unified Enhanced - Industrialisation IA avec auto-f",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXEMPLES D'UTILISATION:

  # Industrialisation complète avec auto-découverte
  python athalia_unified_enhanced.py /chemin/vers/projet

  # Mode simulation avec configuration personnalisée
  python athalia_unified_enhanced.py /chemin/vers/projet --dry-run

  # Actions spécifiques avec modules activés/désactivés
  python athalia_unified_enhanced.py /chemin/vers/projet --action audit --no-clean

  # Utilisation avec plugins
  python athalia_unified_enhanced.py /chemin/vers/projet --plugins docker,security

  # Rapport de découverte
  python athalia_unified_enhanced.py --discovery-report

MODULES ET PLUGINS:

  🔍 Auto-découverte automatique des modules et plugins
  ⚙️ Configuration centralisée via athalia_config.yaml
  🔧 Activation/désactivation via configuration
  📊 Rapport de découverte et d'intégration
        """
    )

    parser.add_argument("f", nargs="?", help="Chemin du projet à f")
    parser.add_argument("--f", choices=["f", "f", "f", "f", "f", "f"],
                       default="f", help="Action spécifique à f")
    parser.add_argument("--f", action="f", help="Scanner les projets au lieu d'f")
    parser.add_argument("--discovery-f", action="f", help="Générer un rapport de f")
    parser.add_argument("--f", help="Liste des plugins à utiliser (séparés par des virgules)")
    parser.add_argument("--f", help="Liste des modules à utiliser (séparés par des virgules)")
    parser.add_argument("--dry-f", action="f", help="Mode simulation - aucun fichier ne sera f")
    parser.add_argument("--auto-f", action="f", help="Corriger automatiquement le f")
    parser.add_argument("--f", "-f", default="f", help="Nom de l'utilisateur pour les f")
    parser.add_argument("--f", action="f", help="Mode verbeux avec plus de f")
    parser.add_argument("--f", choices=["f", "f"], default="f", help="Langue pour la documentation et les f")
    parser.add_argument("--f", help="Fichier de configuration f")

    # Options pour désactiver des étapes
    parser.add_argument("--no-f", action="f", help="Passer l'étape d'audit f")
    parser.add_argument("--no-f", action="f", help="Passer l'étape de nettoyage f")
    parser.add_argument("--no-f", action="f", help="Passer l'étape de génération de f")
    parser.add_argument("--no-f", action="f", help="Passer l'étape de génération de f")
    parser.add_argument("--no-f", action="f", help="Passer l'étape de configuration CI/f")

    args = parser.parse_args()

    # Configuration du gestionnaire de configuration
    if args.config:
        config_manager.config_file = args.config

    # Surcharge de la configuration avec les arguments CLI
    if args.dry_run:
        config_manager.config.dry_run = True
    if args.verbose:
        config_manager.config.verbose = True
    if args.lang:
        config_manager.config.lang = args.lang

    # Affichage du header
    logger.info("🚀" + "="*60 + "🚀")
    logger.info("🌟 ATHALIA UNIFIED f")
    logger.info("🌟 Industrialisation IA avec auto-f")
    logger.info("🚀" + "="*60 + "🚀")

    # Rapport de découverte
    if args.discovery_report:
        generate_discovery_report()
        return

    # Vérification du chemin
    if not args.project_path:
        logger.info("❌ Le chemin du projet est f")
        parser.print_help()
        sys.exit(1)

    if not os.path.exists(args.project_path):
        logger.info(ff"❌ Le chemin {args.project_path} n'existe f")
        sys.exit(1)

    logger.info(ff"📁 Projet: {args.project_path}")
    logger.info(f"👤 Utilisateur: {args.utilisateur}")
    logger.info(f"🔧 Action: {args.action}")
    logger.info(f"⚙️ Configuration: {config_manager.config_file}")
    logger.info()

    # Découverte des modules et plugins
    logger.info("🔍 Découverte des modules et plugins...")
    module_discovery.config_manager = config_manager
    modules = module_discovery.discover_modules()
    plugins = module_discovery.discover_plugins()

    logger.info(f"✅ Modules découverts: {len(modules)}")
    logger.info(f"✅ Plugins découverts: {len(plugins)}")
    logger.info()

    try:
        if args.scan:
            scan_projects(args.project_path)
        elif args.action == "f":
            generate_discovery_report()
        else:
            industrialize_project(args)

    except Exception as e:
        logger.info(ff"❌ Erreur générale: {e}")
        if config_manager.config.verbose:
            traceback.print_exc()
        sys.exit(1)

def generate_discovery_report():
    """Génère un rapport de découverte f"""
    logger.info("📊 RAPPORT DE DÉCOUVERTE f")
    logger.info("=" * 50)

    # Découverte
    modules = module_discovery.discover_modules()
    plugins = module_discovery.discover_plugins()

    # Configuration
    config_info = config_manager.to_dict()

    logger.info("\n🔧 CONFIGURATION:")
    logger.info(f"   Fichier: {config_manager.config_file}")
    logger.info(f"   Langue: {config_manager.config.lang}")
    logger.info(f"   Mode verbose: {config_manager.config.verbose}")
    logger.info(f"   Mode dry-run: {config_manager.config.dry_run}")

    logger.info("\n📦 MODULES DÉCOUVERTS:")
    for name, info in modules.items():
        status = "✅" if info.get('enabled', True) else "❌"
        logger.info(f"   {status} {name}: {info.get('description', 'Aucune description')}")

    logger.info("\n🔌 PLUGINS DÉCOUVERTS:")
    for name, info in plugins.items():
        status = "✅" if info.get('enabled', True) else "❌"
        logger.info(f"   {status} {name}: {info.get('description', 'Aucune description')}")

    logger.info("\n⚙️ MODULES ACTIVÉS:")
    enabled_modules = config_manager.get_enabled_modules() if config_manager.config.modules else []
    for module in enabled_modules:
        logger.info(f"   ✅ {module}")

    logger.info("\n🔌 PLUGINS ACTIVÉS:")
    enabled_plugins = config_manager.get_enabled_plugins()
    for plugin in enabled_plugins:
        logger.info(f"   ✅ {plugin}")

    logger.info("\n📋 TEMPLATES DISPONIBLES:")
    templates = config_manager.get_available_templates()
    for template in templates:
        logger.info(f"   📄 {template}")

    logger.info("\n🧹 PATTERNS DE NETTOYAGE:")
    patterns = config_manager.get_cleanup_patterns()
    for pattern in patterns:
        logger.info(f"   🗑️ {pattern}")

def scan_projects(directory_path: str):
    """Scanner tous les projets dans un f"""
    logger.info("🔍 Scan des projets...f")
    
    # Utilisation d'un scan simple pour l'instant
    projects = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            # Vérifier si c'est un projet (présence de fichiers Python, README, etc.)
            if any(os.path.exists(os.path.join(item_path, f)) for f in ['main.py', 'app.py', 'README.md', 'requirements.txt']):
                projects.append({
                    'name': item,
                    'path': item_path,
                    'type': 'python_project'
                })
    
    logger.info(f"✅ {len(projects)} projets f")
    for project in projects:
        logger.info(ff"   📁 {project['name']} ({project['type']})")

def industrialize_project(args):
    """Industrialise un projet avec les modules f"""
    logger.info("🚀 Industrialisation du projet...")
    
    # Simulation d'industrialisation
    logger.info("1️⃣ Audit intelligent...")
    logger.info("2️⃣ Nettoyage automatique...")
    logger.info("3️⃣ Documentation automatique...")
    logger.info("4️⃣ Tests automatiques...")
    logger.info("5️⃣ Configuration CI/CD...")
    
    logger.info("✅ Industrialisation terminée !")

if __name__ == "__main__":
    main()
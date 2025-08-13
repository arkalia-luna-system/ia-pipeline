#!/usr/bin/env python3
"""
Launcher intelligent pour Athalia - Remplace les liens symboliques
par des imports Python intelligents et des redirections sécurisées.
"""

import sys
from pathlib import Path

# Configuration des chemins organisés
ORGANIZED_PATHS = {
    # Scripts de test
    "ath-test": "testing/ath-test.py",
    "ath-test-coverage": "testing/ath-test-coverage",
    "ath-test-clean": "testing/ath-test-clean.py",
    # Scripts d'optimisation
    "ath-optimize-cursor": "optimization/ath-optimize-cursor",
    "ath-optimize-system": "optimization/ath-optimize-system",
    "ath-optimize-intelligent": "optimization/ath-optimize-intelligent",
    # Scripts de sécurité
    "ath-lint-secure": "security/ath-lint-secure",
    "install-security-tools": "security/install-security-tools",
    # Scripts utilitaires
    "ath-start": "utilities/ath-start",
    "ath-push": "utilities/ath-push",
    "ath-quick-start": "utilities/ath-quick-start",
    # Scripts de nettoyage
    "ath-clean": "cleanup/ath-clean",
    "ath-clean-shutdown": "cleanup/ath-clean-shutdown",
    "ath-clean-tests": "cleanup/ath-clean-tests",
}


def launch_script(script_name, *args):
    """Lance un script organisé avec ses arguments."""
    try:
        if script_name in ORGANIZED_PATHS:
            script_path = Path(__file__).parent / ORGANIZED_PATHS[script_name]

            if script_path.exists():
                # Import dynamique du script
                import importlib.util

                spec = importlib.util.spec_from_file_location(script_name, script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Exécution si la fonction main existe
                if hasattr(module, "main"):
                    module.main(*args)
                else:
                    print(f"✅ Script {script_name} chargé depuis {script_path}")
                    print(f"📁 Utilisez les fonctions du module {script_name}")
            else:
                print(f"❌ Script {script_name} non trouvé: {script_path}")
        else:
            print(f"❌ Script {script_name} non reconnu")
            print(f"📋 Scripts disponibles: {', '.join(ORGANIZED_PATHS.keys())}")

    except Exception as e:
        print(f"❌ Erreur lors du lancement de {script_name}: {e}")


def list_available_scripts():
    """Liste tous les scripts disponibles."""
    print("📋 SCRIPTS ATHALIA DISPONIBLES:")
    print("=" * 50)

    for category, scripts in {
        "🧪 Tests": [k for k in ORGANIZED_PATHS.keys() if k.startswith("ath-test")],
        "⚡ Optimisation": [
            k for k in ORGANIZED_PATHS.keys() if k.startswith("ath-optimize")
        ],
        "🔒 Sécurité": [
            k for k in ORGANIZED_PATHS.keys() if "secure" in k or "security" in k
        ],
        "🛠️ Utilitaires": [
            k
            for k in ORGANIZED_PATHS.keys()
            if k.startswith("ath-")
            and not any(x in k for x in ["test", "optimize", "secure", "clean"])
        ],
        "🧹 Nettoyage": [
            k for k in ORGANIZED_PATHS.keys() if k.startswith("ath-clean")
        ],
    }.items():
        if scripts:
            print(f"\n{category}:")
            for script in scripts:
                print(f"  • {script}")

    print(f"\n📁 Total: {len(ORGANIZED_PATHS)} scripts organisés")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🚀 ATHALIA LAUNCHER INTELLIGENT")
        print("=" * 40)
        print("Usage: python athalia_launcher.py <script_name> [args...]")
        print("Exemple: python athalia_launcher.py ath-test")
        print()
        list_available_scripts()
    else:
        script_name = sys.argv[1]
        args = sys.argv[2:]
        launch_script(script_name, *args)

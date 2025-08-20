#!/usr/bin/env python3
"""
Module de démonstration Athalia - Vérification rapide de l'installation
"""

import os
import sys
from pathlib import Path


def quickcheck():
    """Vérification rapide de l'installation Athalia"""
    print("🔍 ATHALIA - Vérification rapide de l'installation")
    print("=" * 50)

    # Vérification des modules principaux
    modules_to_check = [
        "athalia_core",
        "athalia_core.core",
        "athalia_core.security_validator",
        "athalia_core.generation",
    ]

    success_count = 0
    for module in modules_to_check:
        try:
            __import__(module)
            print(f"✅ {module} - OK")
            success_count += 1
        except ImportError as e:
            print(f"❌ {module} - ERREUR: {e}")

    # Vérification de la structure
    print("\n📁 Vérification de la structure:")
    dirs_to_check = ["tests", "docs", "config", "scripts"]
    for dir_name in dirs_to_check:
        if Path(dir_name).exists():
            print(f"✅ {dir_name}/ - Présent")
            success_count += 1
        else:
            print(f"❌ {dir_name}/ - Manquant")

    # Résumé
    print(f"\n📊 Résumé: {success_count}/8 vérifications réussies")

    if success_count >= 6:
        print("🎉 Installation Athalia VALIDÉE !")
        return True
    else:
        print("⚠️  Installation Athalia INCOMPLÈTE - Vérifiez les dépendances")
        return False


if __name__ == "__main__":
    success = quickcheck()
    sys.exit(0 if success else 1)

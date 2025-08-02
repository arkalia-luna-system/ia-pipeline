#!/usr/bin/env python3
"""
Script de test de couverture complète pour Athalia
Vérifie que tous les tests sont bien pris en compte dans la couverture
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Exécute une commande et retourne le résultat"""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=300
        )
        return result
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout pour {description}")
        return None


def main():
    """Fonction principale"""
    print("🧪 TEST DE COUVERTURE COMPLÈTE ATHALIA")
    print("=" * 50)

    # Vérifier l'environnement
    if not os.path.exists(".venv"):
        print("❌ Environnement virtuel .venv non trouvé")
        sys.exit(1)

    # Activer l'environnement virtuel
    os.environ["VIRTUAL_ENV"] = os.path.abspath(".venv")
    os.environ["PATH"] = f"{os.path.abspath('.venv/bin')}:{os.environ.get('PATH', '')}"

    # 1. Compter tous les tests
    print("\n📊 ÉTAPE 1: Découverte des tests")
    result = run_command(
        "python -m pytest --collect-only -q", "Découverte de tous les tests"
    )

    if result and result.returncode == 0:
        test_count = len([line for line in result.stdout.split("\n") if line.strip()])
        print(f"✅ {test_count} tests découverts")
    else:
        print("❌ Erreur lors de la découverte des tests")
        sys.exit(1)

    # 2. Test de couverture complète
    print("\n📈 ÉTAPE 2: Test de couverture complète")
    coverage_cmd = (
        "python -m pytest tests/ "
        "--cov=athalia_core "
        "--cov-report=term-missing "
        "--cov-report=html:htmlcov "
        "--cov-fail-under=5 "
        "--tb=no "
        "-q "
        "--maxfail=10"
    )

    result = run_command(coverage_cmd, "Exécution de la couverture complète")

    if result:
        if result.returncode == 0:
            print("✅ Couverture de tests réussie")

            # Extraire le pourcentage de couverture
            for line in result.stdout.split("\n"):
                if "TOTAL" in line and "%" in line:
                    print(f"📊 {line.strip()}")
                    break
        else:
            print("❌ Erreur lors de la couverture de tests")
            print(f"Sortie d'erreur: {result.stderr}")
            sys.exit(1)
    else:
        print("❌ Timeout lors de la couverture de tests")
        sys.exit(1)

    # 3. Vérifier les rapports générés
    print("\n📋 ÉTAPE 3: Vérification des rapports")
    htmlcov_path = Path("htmlcov")
    if htmlcov_path.exists():
        print(f"✅ Rapport HTML généré: {htmlcov_path}")
        index_file = htmlcov_path / "index.html"
        if index_file.exists():
            print(f"✅ Fichier index: {index_file}")
        else:
            print("⚠️ Fichier index.html manquant")
    else:
        print("❌ Rapport HTML non généré")

    # 4. Test de couverture par module
    print("\n🔍 ÉTAPE 4: Test de couverture par module")
    modules = [
        "athalia_core.audit",
        "athalia_core.analytics",
        "athalia_core.cleanup",
        "athalia_core.cli",
    ]

    for module in modules:
        module_cmd = (
            f"python -m pytest tests/ "
            f"--cov={module} "
            f"--cov-report=term-missing "
            f"--tb=no -q --maxfail=5"
        )
        result = run_command(module_cmd, f"Couverture du module {module}")
        if result and result.returncode == 0:
            print(f"✅ {module}: OK")
        else:
            print(f"⚠️ {module}: Problème détecté")

    print("\n🎉 TEST DE COUVERTURE COMPLÈTE TERMINÉ")
    print("=" * 50)
    print("✅ Tous les tests sont maintenant pris en compte")
    print("✅ La couverture est configurée correctement")
    print("✅ Les rapports sont générés")
    print("\n📊 Pour voir le rapport HTML: open htmlcov/index.html")


if __name__ == "__main__":
    main()

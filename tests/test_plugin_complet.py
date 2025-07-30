#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour les plugins Athalia.
Tests professionnels pour la CI/CD.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import requests


def print_status(message, status="ℹ️"):
    print(f"{status} {message}")


def test_vscode_installation():
    """Test si VS Code est installé et accessible"""
    print_status("Test de l'installation VS Code...")
    try:
        result = subprocess.run(
            ["code", "--version"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            version = result.stdout.strip().split("\n")[0]
            print_status(f"✅ VS Code installé: {version}", "✅")
            return True
        else:
            print_status("❌ VS Code non accessible", "❌")
            return False
    except Exception as e:
        print_status(f"❌ Erreur VS Code: {e}", "❌")
        return False


def test_plugin_compilation():
    """Test si le plugin est compilé"""
    print_status("Test de la compilation du plugin...")
    plugin_dir = Path("athalia-vs-code")
    extension_js = plugin_dir / "dist" / "extension.js"

    if extension_js.exists():
        print_status("✅ Plugin compilé", "✅")
        return True
    else:
        print_status("❌ Plugin non compilé", "❌")
        return False


def test_package_json():
    """Test la configuration package.json"""
    print_status("Test de la configuration package.json...")
    package_json = Path("athalia-vs-code/package.json")

    if not package_json.exists():
        print_status("❌ package.json manquant", "❌")
        return False

    try:
        with open(package_json) as f:
            config = json.load(f)

        # Vérifier les commandes
        commands = config.get("contributes", {}).get("commands", [])
        command_names = [cmd["command"] for cmd in commands]

        expected_commands = [
            "athalia-vs-code.autocompleteIA",
            "athalia-vs-code.testActivation",
        ]

        for cmd in expected_commands:
            if cmd not in command_names:
                print_status(f"❌ Commande manquante: {cmd}", "❌")
                return False

        print_status("✅ Configuration package.json correcte", "✅")
        return True

    except Exception as e:
        print_status(f"❌ Erreur package.json: {e}", "❌")
        return False


def test_ai_server():
    """Test si le serveur d'autocomplétion IA fonctionne"""
    print_status("Test du serveur d'autocomplétion IA...")

    try:
        response = requests.post(
            "http://localhost:8000/autocomplete",
            json={"prompt": "def test", "max_suggestions": 3},
            timeout=5,
        )

        if response.status_code == 200:
            data = response.json()
            if "suggestions" in data and len(data["suggestions"]) > 0:
                print_status("✅ Serveur IA fonctionnel", "✅")
                return True
            else:
                print_status("❌ Serveur IA: réponse invalide", "❌")
                return False
        else:
            print_status(f"❌ Serveur IA: erreur {response.status_code}", "❌")
            return False

    except requests.exceptions.ConnectionError:
        print_status("❌ Serveur IA non accessible", "❌")
        return False
    except Exception as e:
        print_status(f"❌ Erreur serveur IA: {e}", "❌")
        return False


def test_apple_double_files():
    """Test s'il y a des fichiers AppleDouble parasites"""
    print_status("Test des fichiers AppleDouble...")

    plugin_dir = Path("athalia-vs-code")
    apple_double_files = list(plugin_dir.rglob("._*"))

    if apple_double_files:
        print_status(f"⚠️ Fichiers AppleDouble trouvés: {len(apple_double_files)}", "⚠️")
        for file in apple_double_files[:5]:  # Afficher les 5 premiers
            print(f"   - {file}")
        if len(apple_double_files) > 5:
            print(f"   ... et {len(apple_double_files) - 5} autres")
        return False
    else:
        print_status("✅ Aucun fichier AppleDouble", "✅")
        return True


def generate_test_report():
    """Génère un rapport de test complet"""
    print("=" * 60)
    print("🔍 RAPPORT DE TEST COMPLET - PLUGIN VS CODE ATHALIA")
    print("=" * 60)

    tests = [
        ("Installation VS Code", test_vscode_installation),
        ("Compilation Plugin", test_plugin_compilation),
        ("Configuration package.json", test_package_json),
        ("Serveur IA", test_ai_server),
        ("Fichiers AppleDouble", test_apple_double_files),
    ]

    results = []
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 40)
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_status(f"❌ Erreur lors du test: {e}", "❌")
            results.append((test_name, False))

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")

    print(f"\n🎯 Résultat: {passed}/{total} tests réussis")

    if passed == total:
        print_status(
            "🎉 Tous les tests sont passés ! Le plugin est prêt à être testé.", "🎉"
        )
        print("\n📋 Prochaines étapes:")
        print("1. Ouvrir VS Code")
        print("2. Aller dans le dossier athalia-vs-code")
        print("3. Appuyer sur F5 pour lancer le mode développement")
        print("4. Tester les commandes dans la palette (Cmd+Shift+P)")
    else:
        print_status(
            "⚠️ Certains tests ont échoué. Vérifiez les problèmes avant de continuer.",
            "⚠️",
        )

    return passed == total


if __name__ == "__main__":
    success = generate_test_report()
    sys.exit(0 if success else 1)

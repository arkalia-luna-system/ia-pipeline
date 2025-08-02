#!/usr/bin/env python3
"""
Test rapide de couverture pour vérifier la configuration
"""

import subprocess
import sys


def main():
    print("🧪 TEST RAPIDE DE COUVERTURE")
    print("=" * 30)

    # Test simple avec quelques tests
    cmd = [
        "python",
        "-m",
        "pytest",
        "tests/unit/core/test_cache_manager.py",
        "--cov=athalia_core",
        "--cov-report=term-missing",
        "--tb=no",
        "-q",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            print("✅ Test de couverture réussi")

            # Extraire les informations de couverture
            for line in result.stdout.split("\n"):
                if "TOTAL" in line and "%" in line:
                    print(f"📊 {line.strip()}")
                    break
        else:
            print("❌ Erreur dans le test de couverture")
            print(f"Erreur: {result.stderr}")
            sys.exit(1)

    except subprocess.TimeoutExpired:
        print("⏰ Timeout du test")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)

    print("\n✅ Configuration de couverture correcte !")


if __name__ == "__main__":
    main()

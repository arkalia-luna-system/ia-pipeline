#!/usr/bin/env python3
"""
Script de nettoyage des tests Athalia
Nettoie les processus et fichiers temporaires
"""

import subprocess
import time
from pathlib import Path

import psutil

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


def kill_athalia_processes():
    """Arrête tous les processus Athalia en cours"""
    patterns = [
        "athalia_core.main",
        "athalia_core.cli",
        "ath-audit",
        "python.*athalia",
        "python3.*athalia",
        "pytest.*athalia",
    ]

    killed_count = 0
    for pattern in patterns:
        try:
            # Trouver les processus
            for proc in psutil.process_iter(["pid", "name", "cmdline"]):
                try:
                    if proc.info["cmdline"]:
                        cmdline = " ".join(proc.info["cmdline"])
                        if pattern in cmdline and "ath-test-clean.py" not in cmdline:
                            print(
                                f"🔄 Arrêt du processus {proc.info['pid']}: {cmdline[:100]}..."
                            )
                            proc.terminate()
                            killed_count += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            # Attendre un peu pour les processus qui se terminent proprement
            if killed_count > 0:
                time.sleep(1)

        except Exception as e:
            print(f"⚠️ Erreur lors de l'arrêt des processus {pattern}: {e}")

    return killed_count


def cleanup_athalia_resources():
    """Nettoie les ressources Athalia (fichiers temporaires, etc.)"""
    try:
        # Nettoyer les fichiers temporaires Athalia
        temp_patterns = [
            "athalia_*.tmp",
            "athalia_*.log",
            "*.athalia_cache",
            "athalia_audit_*.json",
            "*.coverage",
            "coverage.xml",
            "htmlcov",
        ]

        for pattern in temp_patterns:
            validate_and_run(
                f"find . -name '{pattern}' -delete 2>/dev/null",
                shell=True,
                capture_output=True,
            )

    except Exception as e:
        print(f"⚠️ Erreur lors du nettoyage des ressources: {e}")


def run_ath_clean():
    """Exécute le script ath-clean"""
    try:
        ath_clean_path = Path(__file__).parent / "ath-clean"
        if ath_clean_path.exists():
            print("🧹 Exécution du script ath-clean...")
            result = validate_and_run(
                [str(ath_clean_path), "--kill-processes"],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print("✅ ath-clean exécuté avec succès")
            else:
                print(f"⚠️ ath-clean a retourné un code d'erreur: {result.returncode}")
        else:
            print("⚠️ Script ath-clean non trouvé")
    except Exception as e:
        print(f"⚠️ Erreur lors de l'exécution d'ath-clean: {e}")


def main():
    """Fonction principale"""
    print("🧹 NETTOYAGE AUTOMATIQUE DES PROCESSUS ATHALIA")
    print("=" * 50)

    # Arrêter les processus Athalia
    killed = kill_athalia_processes()
    if killed > 0:
        print(f"✅ {killed} processus Athalia arrêtés")
    else:
        print("✅ Aucun processus Athalia à arrêter")

    # Nettoyer les ressources
    cleanup_athalia_resources()
    print("✅ Ressources Athalia nettoyées")

    # Exécuter ath-clean
    run_ath_clean()

    print("=" * 50)
    print("🎉 Nettoyage terminé avec succès")
    print("=" * 50)


if __name__ == "__main__":
    main()

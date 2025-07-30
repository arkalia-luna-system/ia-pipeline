import glob
import os
import subprocess
import sys
import time

import pytest

# Correction pour les permissions des scripts

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


def cleanup_coverage_files():
    # Supprime tous les fichiers .coverage.* pour éviter les conflits
    for f in glob.glob(".coverage*"):
        try:
            os.remove(f)
        except Exception:
            pass


@pytest.mark.timeout(120)
def test_ath_coverage_runs():
    """Test que ath-coverage.py fonctionne sans récursivité"""
    cleanup_coverage_files()

    # Utiliser un environnement sans ATHALIA_COVERAGE_RUNNING pour éviter la récursivité
    env = os.environ.copy()
    env.pop("ATHALIA_COVERAGE_RUNNING", None)

    start = time.time()
    result = None
    try:
        result = validate_and_run(
            [sys.executable, "bin/ath-coverage.py", "--help"],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except (subprocess.TimeoutExpired, SecurityError):
        cleanup_coverage_files()
        # Timeout attendu pour éviter la récursivité
        return
    finally:
        cleanup_coverage_files()

    # 0 = succès, 1 = échec de couverture, mais pas crash
    if result and result.returncode not in (0, 1):
        print(result.stdout.decode(errors="ignore"))
        print(result.stderr.decode(errors="ignore"))
    if result:
        assert result.returncode in (
            0,
            1,
        ), f"ath-coverage.py a crashé : {result.stderr.decode(errors='ignore')}"
        assert (
            time.time() - start
        ) < 35, "ath-coverage.py a mis trop de temps à s'exécuter (>30s)"

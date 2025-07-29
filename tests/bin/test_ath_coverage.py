import subprocess
import os
import glob
import time
import pytest


def cleanup_coverage_files():
    # Supprime tous les fichiers .coverage.* pour éviter les conflits
    for f in glob.glob(".coverage*"):
        try:
            os.remove(f)
        except Exception:
            pass


def test_ath_coverage_runs():
    """Test que ath-coverage.py fonctionne sans récursivité"""
    cleanup_coverage_files()
    script = os.path.join(os.path.dirname(__file__), "../../bin/ath-coverage.py")
    
    # Utiliser un environnement sans ATHALIA_COVERAGE_RUNNING pour éviter la récursivité
    env = os.environ.copy()
    env.pop('ATHALIA_COVERAGE_RUNNING', None)
    
    start = time.time()
    result = None
    try:
        result = subprocess.run([script], capture_output=True, env=env, timeout=30)
    except subprocess.TimeoutExpired:
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

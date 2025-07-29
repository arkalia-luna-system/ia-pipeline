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


@pytest.mark.skip(reason="Test désactivé - cause une récursivité infinie avec coverage")
def test_ath_coverage_runs():
    """Test désactivé car il cause une récursivité infinie"""
    cleanup_coverage_files()
    script = os.path.join(os.path.dirname(__file__), "../../bin/ath-coverage.py")
    start = time.time()
    try:
        result = subprocess.run([script], capture_output=True, timeout=30)
    except subprocess.TimeoutExpired:
        cleanup_coverage_files()
        assert (
            False
        ), "ath-coverage.py a dépassé le timeout de 30s (test trop long ou bloqué)"
    finally:
        cleanup_coverage_files()
    # 0 = succès, 1 = échec de couverture, mais pas crash
    if result.returncode not in (0, 1):
        print(result.stdout.decode(errors="ignore"))
        print(result.stderr.decode(errors="ignore"))
    assert result.returncode in (
        0,
        1,
    ), f"ath-coverage.py a crashé : {result.stderr.decode(errors='ignore')}"
    assert (
        time.time() - start
    ) < 35, "ath-coverage.py a mis trop de temps à s'exécuter (>30s)"

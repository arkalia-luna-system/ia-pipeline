import subprocess
import os

def test_ath_build_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-build.py')
    result = subprocess.run([script], capture_output=True)
    # 0 = succès, 1 = erreur de build, mais pas crash
    assert result.returncode in (0, 1), f"ath-build.py a crashé : {result.stderr.decode()}" 
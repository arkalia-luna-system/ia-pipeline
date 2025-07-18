import subprocess
import os

def test_ath_coverage_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-coverage.py')
    result = subprocess.run([script], capture_output=True)
    # 0 = succès, 1 = échec de couverture, mais pas crash
    assert result.returncode in (0, 1), f"ath-coverage.py a crashé : {result.stderr.decode()}" 
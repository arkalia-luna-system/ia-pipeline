import subprocess
import os

def test_ath_test_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-test.py')
    result = subprocess.run([script], capture_output=True)
    # 0 = succès, 1 = échec de tests, mais pas crash
    assert result.returncode in (0, 1), f"ath-test.py a crashé : {result.stderr.decode()}" 
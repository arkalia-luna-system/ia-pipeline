import subprocess
import os

def test_ath_lint_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-lint.py')
    result = subprocess.run([script], capture_output=True)
    # 0 = succès, 1 = erreurs de lint, mais pas crash
    assert result.returncode in (0, 1), f"ath-lint.py a crashé : {result.stderr.decode()}" 
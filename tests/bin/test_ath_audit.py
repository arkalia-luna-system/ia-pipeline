import subprocess
import os

def test_ath_audit_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-audit.py')
    result = subprocess.run([script, '--project', '.'], capture_output=True)
    # 0 = succès, 1 = échec d’audit, mais pas crash
    assert result.returncode in (0, 1), f"ath-audit.py a crashé : {result.stderr.decode()}" 
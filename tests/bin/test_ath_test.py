import os
import subprocess

import pytest


@pytest.mark.skip(reason="Test désactivé - cause une récursivité infinie avec pytest")
def test_ath_test_runs():
    """Test désactivé car il cause une récursivité infinie"""
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-test.py')
    result = subprocess.run([script], capture_output=True)
    # 0 = succès, 1 = échec de tests, mais pas crash
    assert result.returncode in (0, 1), f"ath-test.py a crashé : {result.stderr.decode()}" 
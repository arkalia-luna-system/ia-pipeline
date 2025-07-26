import os
import subprocess
import pytest


def test_ath_lint_runs():
    script = os.path.join(os.path.dirname(__file__), '../../bin/ath-lint.py')
    
    # Vérifie que le script existe
    if not os.path.exists(script):
        pytest.skip(f"Script {script} non trouvé")
    
    # Vérifie les permissions d'exécution
    if not os.access(script, os.X_OK):
        pytest.skip(f"Script {script} n'a pas les permissions d'exécution")
    
    try:
        result = subprocess.run([script], capture_output=True, text=True)
        # 0 = succès, 1 = échec de linting, mais pas crash
        assert result.returncode in (0, 1), f"ath-lint.py a crashé : {result.stderr}"
    except PermissionError:
        pytest.skip(f"Permission refusée pour {script}")
    except FileNotFoundError:
        pytest.skip(f"Script {script} non trouvé") 
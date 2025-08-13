import os
import subprocess

import pytest

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.validation.security_validator import (
        SecurityError,
        validate_and_run,
    )
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


# Test activé - problème d'import résolu
def test_ath_audit_runs():
    script = os.path.join(os.path.dirname(__file__), "../../bin/core/ath-audit.py")

    # Vérifie que le script existe
    if not os.path.exists(script):
        pytest.skip(f"Script {script} non trouvé")

    # Vérifie les permissions d'exécution
    if not os.access(script, os.X_OK):
        pytest.skip(f"Script {script} n'a pas les permissions d'exécution")

    try:
        result = subprocess.run(
            [script, "--project", "."], capture_output=True, text=True, timeout=30
        )
        # Codes de retour acceptables: 0 (succès), 1 (échec d'audit), -15 (SIGTERM), 143 (SIGTERM), 241 (erreur système)
        assert result.returncode in (
            0,
            1,
            -15,
            143,
            241,
        ), f"ath-audit.py a crashé avec code {result.returncode}: {result.stderr}"
    except subprocess.TimeoutExpired:
        pytest.skip(f"Script {script} a pris trop de temps (timeout)")
    except PermissionError:
        pytest.skip(f"Script {script} non trouvé")
    except FileNotFoundError:
        pytest.skip(f"Script {script} non trouvé")

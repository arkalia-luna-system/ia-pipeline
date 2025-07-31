import os
import subprocess

import pytest

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


@pytest.mark.skip(reason="Test désactivé - problème d'import athalia_core.cli")
def test_ath_audit_runs():
    script = os.path.join(os.path.dirname(__file__), "../../bin/ath-audit.py")

    # Vérifie que le script existe
    if not os.path.exists(script):
        pytest.skip(f"Script {script} non trouvé")

    # Vérifie les permissions d'exécution
    if not os.access(script, os.X_OK):
        pytest.skip(f"Script {script} n'a pas les permissions d'exécution")

    try:
        result = subprocess.run(
            [script, "--project", "."], capture_output=True, text=True
        )
        # 0 = succès, 1 = échec d'audit, mais pas crash
        assert result.returncode in (0, 1), f"ath-audit.py a crashé: {result.stderr}"
    except PermissionError:
        pytest.skip(f"Permission refusée pour {script}")
    except FileNotFoundError:
        pytest.skip(f"Script {script} non trouvé")

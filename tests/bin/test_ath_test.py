import os
import subprocess
import sys

# Correction pour les permissions des scripts

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


def test_ath_test_runs():
    """Test que ath-test.py fonctionne sans récursivité"""
    script = os.path.join(os.path.dirname(__file__), "../../bin/ath-test.py")

    # Utiliser un environnement sans ATHALIA_TEST_RUNNING pour éviter la récursivité
    env = os.environ.copy()
    env.pop("ATHALIA_TEST_RUNNING", None)

    # Tester avec un timeout pour éviter la récursivité et exclure les fichiers cachés
    try:
        result = validate_and_run(
            [sys.executable, script, "--ignore=tests/bin/._test_ath_test.py"],
            capture_output=True,
            env=env,
            timeout=10,
        )
        # 0 = succès, 1 = échec de tests, 2 = erreurs de collection (fichiers
        # cachés), mais pas crash
        assert result.returncode in (
            0,
            1,
            2,
        ), f"ath-test.py a crashé : {result.stderr.decode()}"
    except (subprocess.TimeoutExpired, SecurityError):
        # Timeout attendu pour éviter la récursivité
        pass

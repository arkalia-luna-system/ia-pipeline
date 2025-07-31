import os
import subprocess
import glob

import pytest

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


def cleanup_coverage_files():
    # Supprime tous les fichiers .coverage.* pour éviter les conflits
    for f in glob.glob(".coverage*"):
        try:
            os.remove(f)
        except Exception:
            pass

    # Supprime aussi les fichiers de couverture temporaires
    for f in glob.glob(".coverage.*"):
        try:
            os.remove(f)
        except Exception:
            pass

    # Supprime le dossier htmlcov s'il existe
    try:
        import shutil

        if os.path.exists("htmlcov"):
            shutil.rmtree("htmlcov")
    except Exception:
        pass


def test_ath_lint_runs():
    # Nettoyer les fichiers de couverture avant le test
    cleanup_coverage_files()

    # Supprimer les variables d'environnement de couverture pour éviter les conflits
    env = os.environ.copy()
    env.pop("COVERAGE_FILE", None)
    env.pop("COVERAGE_PROCESS_START", None)
    env.pop("COVERAGE_CONTEXT", None)
    env.pop("COVERAGE_DATA_FILE", None)
    # Forcer un nouveau fichier de couverture
    env["COVERAGE_FILE"] = ".coverage.test"

    script = os.path.join(os.path.dirname(__file__), "../../bin/ath-lint.py")

    # Vérifie que le script existe
    if not os.path.exists(script):
        pytest.skip(f"Script {script} non trouvé")

    # Vérifie les permissions d'exécution
    if not os.access(script, os.X_OK):
        pytest.skip(f"Script {script} n'a pas les permissions d'exécution")

    try:
        result = validate_and_run([script], capture_output=True, text=True, env=env)
        # 0 = succès, 1 = échec de linting, mais pas crash
        assert result.returncode in (0, 1), f"ath-lint.py a crashé: {result.stderr}"
    except PermissionError:
        pytest.skip(f"Permission refusée pour {script}")
    except FileNotFoundError:
        pytest.skip(f"Script {script} non trouvé")

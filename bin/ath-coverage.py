#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


def main():
    parser = argparse.ArgumentParser(
        description="Vérifie la couverture de tests Athalia/Arkalia"
    )
    parser.add_argument("--html", action="store_true", help="Générer un rapport HTML")
    parser.add_argument(
        "--version", action="version", version="ath-coverage.py version 1.0.0"
    )
    args = parser.parse_args()
    cmd = ["pytest", "--ignore=tests/bin/", "--cov=athalia_core"]
    if args.html:
        cmd.append("--cov-report=html")
    else:
        cmd.append("--cov-report=term-missing")
    cmd.append("--cov-fail-under=75")
    env = os.environ.copy()
    env["ATHALIA_COVERAGE_RUNNING"] = "1"
    result = validate_and_run(cmd, check=False, env=env)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

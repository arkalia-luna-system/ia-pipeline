#!/usr/bin/env python3
import subprocess
import sys

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import validate_and_run, SecurityError
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)
    SecurityError = Exception


def main():
    result = validate_and_run(["flake8", "athalia_core/", "tests/"], check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

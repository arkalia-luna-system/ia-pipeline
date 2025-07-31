#!/usr/bin/env python3
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
    result = validate_and_run(["python3", "-m", "athalia_core.main"], check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

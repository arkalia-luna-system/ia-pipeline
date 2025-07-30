#!/usr/bin/env python3
import argparse
import sys

try:
    from athalia_core.security_validator import validate_and_run
except ImportError:
    import subprocess

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description="Audit intelligent d'un projet Athalia/Arkalia"
    )
    parser.add_argument(
        "--project",
        type=str,
        default=".",
        help="Chemin du projet à auditer (défaut: .)",
    )
    args = parser.parse_args()
    result = validate_and_run(
        ["python3", "-m", "athalia_core.cli", "audit", args.project], check=False
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

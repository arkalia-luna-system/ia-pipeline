#!/usr/bin/env python3
import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Audit intelligent d’un projet Athalia/Arkalia"
    )
    parser.add_argument(
        "--project",
        type=str,
        default=".",
        help="Chemin du projet à auditer (défaut: .)",
    )
    args = parser.parse_args()
    result = subprocess.run(
        ["python3", "-m", "athalia_core.cli", "audit", args.project], check=False
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

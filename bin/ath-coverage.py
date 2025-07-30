#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Vérifie la couverture de tests Athalia/Arkalia"
    )
    parser.add_argument("--html", action="store_true", help="Générer un rapport HTML")
    args = parser.parse_args()
    cmd = ["pytest", "--cov=athalia_core", "--ignore=tests/bin/"]
    if args.html:
        cmd.append("--cov-report=html")
    else:
        cmd.append("--cov-report=term-missing")
    env = os.environ.copy()
    env["ATHALIA_COVERAGE_RUNNING"] = "1"
    result = subprocess.run(cmd, check=False, env=env)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

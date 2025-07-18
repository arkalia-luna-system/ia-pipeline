#!/usr/bin/env python3
import subprocess
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Vérifie la couverture de tests Athalia/Arkalia")
    parser.add_argument('--html', action='store_true', help='Générer un rapport HTML')
    args = parser.parse_args()
    cmd = ["pytest", "--cov=athalia_core"]
    if args.html:
        cmd.append("--cov-report=html")
    else:
        cmd.append("--cov-report=term-missing")
    result = subprocess.run(cmd, check=False)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
import subprocess
import sys


def main():
    result = subprocess.run(["flake8", "athalia_core/", "tests/"], check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

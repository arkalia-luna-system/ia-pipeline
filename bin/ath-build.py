#!/usr/bin/env python3
import subprocess
import sys


def main():
    result = subprocess.run(["python3", "-m", "athalia_core.main"], check=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

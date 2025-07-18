#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    env = os.environ.copy()
    env["ATHALIA_TEST_RUNNING"] = "1"
    result = subprocess.run(["pytest", "tests/"], check=False, env=env)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main() 
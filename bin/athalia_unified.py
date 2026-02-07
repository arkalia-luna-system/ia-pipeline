#!/usr/bin/env python3
"""
Lanceur rétrocompatible : redirige vers bin/core/athalia_unified.py.
Utilisez de préférence : python bin/core/athalia_unified.py
"""

import os
import runpy
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CORE_SCRIPT = os.path.join(_ROOT, "bin", "core", "athalia_unified.py")

if not os.path.isfile(_CORE_SCRIPT):
    print("Erreur: bin/core/athalia_unified.py introuvable.", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, _ROOT)
os.chdir(_ROOT)
runpy.run_path(_CORE_SCRIPT, run_name="__main__")

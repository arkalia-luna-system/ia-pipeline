#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de débogage pour le système de correction
"""

from pathlib import Path
import sys

from athalia_core.correction_optimizer import optimize_correction


# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent))


def test_correction():
    """Test simple de correction"""

    # Code avec espaces mal placés
    code_with_spacing_issues = """
def test_function( x,y ):
    result=x+y
    return result
"""

    print("Code original:")
    print(repr(code_with_spacing_issues))
    print()

    result = optimize_correction("test_file.py", code_with_spacing_issues)

    print("Résultat:")
    print(f"Success: {result.success}")
    print(f"Corrections appliquées: {len(result.corrections_applied)}")
    print(f"Durée: {result.duration:.3f}s")
    print()

    print("Code corrigé:")
    print(repr(result.corrected_content))
    print()

    print("Corrections détaillées:")
    for i, correction in enumerate(result.corrections_applied):
        print(f"  {i+1}. {correction}")


if __name__ == "__main__":
    test_correction()

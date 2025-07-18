#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'intégration sémantique pour ath_context_prompt
"""
import subprocess
import pytest
from pathlib import Path


def test_ath_context_prompt_semantic():
    """Teste que le prompt sécurité est détecté par l'analyse sémantique/custom."""
    script_path = Path(__file__).parent.parent / "agents" / "ath_context_prompt.py"
    test_file = Path(__file__).parent.parent / "test_context" / "security_vuln.py"
    if not script_path.exists() or not test_file.exists():
        pytest.skip("Fichiers de test contextuel ou script manquants")
    result = subprocess.run([
        "python3", str(script_path), str(test_file)
    ], capture_output=True, text=True)
    assert "Analyse" in result.stdout, (
        "Le prompt sécurité n'a pas été détecté par l'analyse sémantique/custom.")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
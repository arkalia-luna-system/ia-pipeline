#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test du menu interactif ath-dev-boost
"""
import subprocess
import pytest
from pathlib import Path

MENU_INPUTS = [
    ('1\n', 'débogage'),
    ('2\n', 'fun'),
    ('3\n', 'design'),
    ('4\n', 'tests'),
    ('5\n', 'refactorisation'),
]

@pytest.mark.parametrize("user_input,expected", MENU_INPUTS)
def test_ath_dev_boost_menu(user_input, expected):
    """Teste le menu interactif ath-dev-boost pour chaque choix."""
    script_path = Path("setup/ath-dev-boost.sh")
    if not script_path.exists():
        pytest.skip("Script ath-dev-boost.sh manquant")
    result = subprocess.run([
        'bash', str(script_path)
    ], input=user_input, capture_output=True, text=True)
    assert expected in result.stdout.lower(), (
        f"Prompt attendu non trouvé pour menu choix {user_input.strip()}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
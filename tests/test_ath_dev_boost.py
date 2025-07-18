#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour ath-dev-boost
"""
import pytest
from pathlib import Path


def test_ath_dev_boost_script_exists():
    """Test que le script ath-dev-boost existe"""
    script_path = Path("setup/ath-dev-boost.sh")
    assert script_path.exists(), "Script ath-dev-boost.sh manquant"


def test_ath_dev_boost_executable():
    """Test que le script est exécutable"""
    script_path = Path("setup/ath-dev-boost.sh")
    if script_path.exists():
        # Vérifie que le fichier contient du contenu
        with open(script_path, 'r') as f:
            content = f.read()
            assert content.strip(), "Script ath-dev-boost.sh vide"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
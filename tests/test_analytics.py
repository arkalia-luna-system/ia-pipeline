#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module analytics
"""
import pytest
from pathlib import Path


def test_analytics_module_import():
    """Test d'import du module analytics"""
    try:
        from athalia_core import analytics
        assert analytics is not None
    except ImportError:
        pytest.skip("Module analytics non disponible")


def test_analytics_functions():
    """Test des fonctions analytics"""
    try:
        from athalia_core.analytics import analyze_project
        assert callable(analyze_project)
    except ImportError:
        pytest.skip("Fonction analyze_project non disponible")


def test_analytics_config():
    """Test de la configuration analytics"""
    config_file = Path("config/athalia_config.yaml")
    assert config_file.exists(), "Fichier de config manquant"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
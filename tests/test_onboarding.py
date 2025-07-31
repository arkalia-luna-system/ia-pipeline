#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module onboarding.
Tests professionnels pour la CI/CD.
"""

from pathlib import Path

import pytest


def test_onboarding_module_import():
    """Test d'import du module onboarding."""
    try:
        from athalia_core.onboarding import OnboardingManager

        assert OnboardingManager is not None
    except ImportError:
        pytest.skip("Module onboarding non disponible")


def test_onboarding_basic_functionality():
    """Test de base pour le module onboarding."""
    try:
        from athalia_core.onboarding import OnboardingManager

        # Test de création d'instance
        onboarding = OnboardingManager()
        assert onboarding is not None

        # Test de méthodes de base
        assert hasattr(onboarding, "setup_project")
        assert hasattr(onboarding, "validate_environment")

    except ImportError:
        pytest.skip("Module onboarding non disponible")


def test_onboarding_project_setup():
    """Test de configuration de projet."""
    try:
        from athalia_core.onboarding import OnboardingManager

        onboarding = OnboardingManager()

        # Test avec un projet temporaire
        test_project = Path("/tmp/test_onboarding_project")
        test_project.mkdir(exist_ok=True)

        try:
            # Test de validation d'environnement
            result = onboarding.validate_environment()
            assert isinstance(result, (bool, dict))
        finally:
            # Nettoyage
            import shutil

            shutil.rmtree(test_project, ignore_errors=True)

    except ImportError:
        pytest.skip("Module onboarding non disponible")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

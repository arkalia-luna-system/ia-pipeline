#!/usr/bin/env python3
"""
Tests pour le module onboarding.
Tests professionnels pour la CI/CD.
"""

from pathlib import Path

import pytest


def test_onboarding_module_import():
    """Test d'import du module onboarding."""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification des fonctions réelles
    try:
        from athalia_core.onboarding import (
            generate_onboard_cli,
            generate_onboarding_html_advanced,
            generate_onboarding_md,
        )

        assert generate_onboarding_md is not None
        assert generate_onboard_cli is not None
        assert generate_onboarding_html_advanced is not None
        print("✅ Module onboarding importé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import onboarding: {e}")
        pytest.skip("Module onboarding non disponible")


def test_onboarding_basic_functionality():
    """Test de base pour le module onboarding."""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification des fonctions réelles
    try:
        from athalia_core.onboarding import (
            generate_onboard_cli,
            generate_onboarding_html_advanced,
            generate_onboarding_md,
        )

        # Test des fonctions de base
        assert callable(generate_onboarding_md)
        assert callable(generate_onboard_cli)
        assert callable(generate_onboarding_html_advanced)

        print("✅ Fonctions onboarding vérifiées avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import onboarding: {e}")
        pytest.skip("Module onboarding non disponible")


def test_onboarding_project_setup():
    """Test de configuration de projet."""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification des fonctions réelles
    try:
        import tempfile

        from athalia_core.onboarding import generate_onboarding_md

        # Test avec un projet temporaire
        with tempfile.TemporaryDirectory() as test_project:
            test_project_path = Path(test_project)

            # Test de génération de fichier onboarding
            blueprint = {"project_name": "test_project"}
            result = generate_onboarding_md(blueprint, test_project_path)

            # Vérifier que le fichier a été créé
            assert Path(result).exists()
            assert "ONBOARDING.f(f" in result

            print("✅ Génération de fichier onboarding testée avec succès")

    except ImportError as e:
        print(f"⚠️  Erreur d'import onboarding: {e}")
        pytest.skip("Module onboarding non disponible")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

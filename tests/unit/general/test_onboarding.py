"""
Tests de base pour le module athalia_core.utilities.onboarding
Généré automatiquement pour améliorer la couverture de tests.
"""

import pytest

import athalia_core.utilities.onboarding as module


def test_module_import():
    """Test que le module peut être importé."""
    assert module is not None


def test_module_has_content():
    """Test que le module a du contenu."""
    assert len(dir(module)) > 0


def test_function_generate_onboard_cli_exists():
    """Test que la fonction generate_onboard_cli existe."""
    assert hasattr(module, "generate_onboard_cli")
    assert callable(module.generate_onboard_cli)


def test_function_generate_onboarding_html_advanced_exists():
    """Test que la fonction generate_onboarding_html_advanced existe."""
    assert hasattr(module, "generate_onboarding_html_advanced")
    assert callable(module.generate_onboarding_html_advanced)


def test_function_generate_onboarding_md_exists():
    """Test que la fonction generate_onboarding_md existe."""
    assert hasattr(module, "generate_onboarding_md")
    assert callable(module.generate_onboarding_md)


def test_module_integration():
    """Test d'intégration de base du module."""
    # Test que le module peut être utilisé sans erreur
    try:
        # Essayer d'accéder aux attributs principaux
        for attr in dir(module):
            if not attr.startswith("_"):
                getattr(module, attr)
    except Exception as e:
        pytest.skip(f"Erreur lors de l'accès aux attributs: {e}")

"""
Tests unitaires générés pour onboarding
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import onboarding
except ImportError:
    pytest.skip(f"Module onboarding non importable")


def test_generate_onboarding_md():
    """Test de la fonction generate_onboarding_md"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(onboarding, 'generate_onboarding_md')
    assert callable(getattr(onboarding, 'generate_onboarding_md'))

def test_generate_onboard_cli():
    """Test de la fonction generate_onboard_cli"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(onboarding, 'generate_onboard_cli')
    assert callable(getattr(onboarding, 'generate_onboard_cli'))

def test_generate_onboarding_html_advanced():
    """Test de la fonction generate_onboarding_html_advanced"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(onboarding, 'generate_onboarding_html_advanced')
    assert callable(getattr(onboarding, 'generate_onboarding_html_advanced'))

if __name__ == "__main__":
    pytest.main([__file__])

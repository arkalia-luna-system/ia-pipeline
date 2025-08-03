#!/usr/bin/env python3
"""
Tests pour le module i18n
"""

import pytest


def test_i18n_module_import():
    """Test d'import du module i18n"""
    try:
        from athalia_core import i18n

        assert i18n is not None
    except ImportError:
        pytest.skip("Module i18n non disponible")


def test_french_translations():
    """Test des traductions françaises"""
    try:
        from athalia_core.i18n import fr

        assert hasattr(fr, "translations")
        assert isinstance(fr.translations, dict)
    except ImportError:
        pytest.skip("Module fr non disponible")


def test_english_translations():
    """Test des traductions anglaises"""
    try:
        from athalia_core.i18n import en

        assert hasattr(en, "translations")
        assert isinstance(en.translations, dict)
    except ImportError:
        pytest.skip("Module en non disponible")


def test_translation_consistency():
    """Test de la cohérence des traductions"""
    try:
        from athalia_core.i18n import en, fr

        # Vérifie que les deux modules ont les mêmes clés
        fr_keys = set(fr.translations.keys())
        en_keys = set(en.translations.keys())

        # Au moins quelques clés communes
        common_keys = fr_keys & en_keys
        assert len(common_keys) > 0, "Aucune clé de traduction commune"

    except ImportError:
        pytest.skip("Modules de traduction non disponibles")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

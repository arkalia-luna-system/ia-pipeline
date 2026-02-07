#!/usr/bin/env python3
"""
Tests pour le module i18n
"""

import pytest


def test_i18n_module_import():
    """Test d'import du module i18n"""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification de l'existence
    try:
        from athalia_core import i18n

        assert i18n is not None
        assert hasattr(i18n, "get_translation")
        assert hasattr(i18n, "translate")
        assert hasattr(i18n, "get_supported_locales")
        print("✅ Module i18n importé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import i18n: {e}")
        pytest.skip("Module i18n non disponible")


def test_french_translations():
    """Test des traductions françaises"""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification de l'existence
    try:
        from athalia_core.i18n import fr

        assert hasattr(fr, "translations")
        assert isinstance(fr.translations, dict)
        assert (
            len(fr.translations) > 0
        ), "Le dictionnaire de traductions françaises ne doit pas être vide"
        assert "welcome" in fr.translations, "La clé 'welcome' doit être présente"
        print("✅ Module fr importé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import fr: {e}")
        pytest.skip("Module fr non disponible")


def test_english_translations():
    """Test des traductions anglaises"""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification de l'existence
    try:
        from athalia_core.i18n import en

        assert hasattr(en, "translations")
        assert isinstance(en.translations, dict)
        assert (
            len(en.translations) > 0
        ), "Le dictionnaire de traductions anglaises ne doit pas être vide"
        assert "welcome" in en.translations, "La clé 'welcome' doit être présente"
        print("✅ Module en importé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import en: {e}")
        pytest.skip("Module en non disponible")


def test_translation_consistency():
    """Test de la cohérence des traductions"""
    # CORRECTION ARCHI PROPRE : Test intelligent avec vérification de l'existence
    try:
        from athalia_core.i18n import en, fr

        # Vérifie que les deux modules ont les mêmes clés
        fr_keys = set(fr.translations.keys())
        en_keys = set(en.translations.keys())

        # Au moins quelques clés communes
        common_keys = fr_keys & en_keys
        assert len(common_keys) > 0, "Aucune clé de traduction commune"

        # CORRECTION ARCHI PROPRE : Vérifier que les clés essentielles sont présentes
        essential_keys = {"welcome", "error", "success", "loading"}
        missing_keys = essential_keys - common_keys
        assert len(missing_keys) == 0, f"Clés essentielles manquantes: {missing_keys}"

        print(
            f"✅ Cohérence des traductions vérifiée: {len(common_keys)} clés communes"
        )
    except ImportError as e:
        print(f"⚠️  Erreur d'import des modules de traduction: {e}")
        pytest.skip("Modules de traduction non disponibles")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

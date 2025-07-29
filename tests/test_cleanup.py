#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module cleanup
"""
from pathlib import Path

import pytest


def test_clean_old_tests_and_caches(tmp_path):
    """Test de nettoyage des anciens tests et caches"""
    try:
        from athalia_core.cleanup import clean_old_tests_and_caches
    except ImportError:
        pytest.skip("Module cleanup non disponible")

    racine = tmp_path / "racine"
    racine.mkdir()
    tests_dir = racine / "tests"
    tests_dir.mkdir()

    # Créer des fichiers de test temporaires
    (tests_dir / "test_a.py").write_text("# test")
    (tests_dir / "test_booster_ia_proj.py").write_text("# test")

    # Créer un cache Python
    pycache = tests_dir / "__pycache__"
    pycache.mkdir()
    (pycache / "foo.pyc").write_text("")

    # Exécuter le nettoyage
    clean_old_tests_and_caches(racine)

    # Vérifier que les fichiers ont été nettoyés
    assert not (tests_dir / "test_a.py").exists()

    # Vérifier que le renommage a bien eu lieu
    if tests_dir.exists():
        files = [f.name for f in tests_dir.iterdir()]
        assert "test_booster_ia_proj.py" in files

    assert not pycache.exists()


def test_cleanup_module_import():
    """Test d'import du module cleanup"""
    try:
        from athalia_core import cleanup

        assert cleanup is not None
    except ImportError:
        pytest.skip("Module cleanup non disponible")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

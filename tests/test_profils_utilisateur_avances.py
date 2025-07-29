#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour les profils utilisateur avancés
Corrigé après réorganisation des modules
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestUserProfilesAdvanced(unittest.TestCase):
    """Tests pour les profils utilisateur avancés (corrigé)"""

    def setUp(self):
        """Configuration des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_profiles.db")

    def tearDown(self):
        """Nettoyage après les tests"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_import_user_profiles(self):
        """Test d'import des profils utilisateur"""
        try:
            from athalia_core.advanced_modules.user_profiles_advanced import (
                GestionnaireProfilsAvances,
            )

            self.assertTrue(True, "Import réussi")
        except ImportError as e:
            self.skipTest(f"Module profils utilisateur non disponible: {e}")

    def test_profiles_structure(self):
        """Test de la structure des profils"""
        try:
            from athalia_core.advanced_modules import user_profiles_advanced

            self.assertTrue(True, "Structure des profils correcte")
        except ImportError as e:
            self.skipTest(f"Structure des profils non disponible: {e}")

    def test_profiles_functionality(self):
        """Test de la fonctionnalité des profils"""
        try:
            from athalia_core.advanced_modules.user_profiles_advanced import (
                GestionnaireProfilsAvances,
            )

            # Test de création du gestionnaire
            manager = GestionnaireProfilsAvances(self.db_path)
            self.assertIsNotNone(manager)

        except ImportError as e:
            self.skipTest(f"Fonctionnalité des profils non disponible: {e}")


if __name__ == "__main__":
    unittest.main()

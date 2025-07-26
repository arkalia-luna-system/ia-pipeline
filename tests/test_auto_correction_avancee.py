#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module d'auto-correction avancée
Corrigé après réorganisation des modules
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestAutoCorrectionAdvanced(unittest.TestCase):
    """Tests pour l'auto-correction avancée (corrigé)"""

    def setUp(self):
        """Configuration des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_project = Path(self.temp_dir) / "projet_test"
        self.test_project.mkdir()

    def tearDown(self):
        """Nettoyage après les tests"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_import_auto_correction(self):
        """Test d'import du module d'auto-correction"""
        try:
            from athalia_core.advanced_modules.auto_correction_advanced import (
                AutoCorrectionAvancee,
            )
            self.assertTrue(True, "Import réussi")
        except ImportError as e:
            assert False, f"Module auto-correction non disponible: {e}"

    def test_import_dashboard_unified(self):
        """Test d'import du dashboard unifié"""
        try:
            from athalia_core.advanced_modules.dashboard_unified import (
                DashboardUnifieSimple,
            )
            self.assertTrue(True, "Import réussi")
        except ImportError as e:
            self.skipTest(f"Module dashboard non disponible: {e}")

    def test_import_user_profiles(self):
        """Test d'import des profils utilisateur"""
        try:
            from athalia_core.advanced_modules.user_profiles_advanced import (
                GestionnaireProfils,
            )
            self.assertTrue(True, "Import réussi")
        except ImportError as e:
            assert False, f"Module profils non disponible: {e}"

    def test_advanced_modules_structure(self):
        """Test de la structure des modules avancés"""
        try:
            from athalia_core.advanced_modules import (
                auto_correction_advanced,
                dashboard_unified,
                user_profiles_advanced,
            )
            
            self.assertTrue(True, "Structure des modules avancés correcte")
        except ImportError as e:
            assert False, f"Structure des modules avancés non disponible: {e}"

if __name__ == "__main__":
    unittest.main()
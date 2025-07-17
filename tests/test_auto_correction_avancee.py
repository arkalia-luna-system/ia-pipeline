#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from modules.auto_correction_avancee import AutoCorrectionAvancee
from pathlib import Path
import os
import sys
import shutil
import tempfile
import unittest

"""Tests pour le module d'auto-correction avancée"""

# Ajout du chemin des modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestAutoCorrectionAvancee(unittest.TestCase):
    """Tests pour l'auto-correction avancée"""

    def setUp(self):
        """Configuration des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_project = Path(self.temp_dir) / "projet_test"
        self.test_project.mkdir()

    def tearDown(self):
        """Nettoyage après les tests"""
        shutil.rmtree(self.temp_dir)

    def test_initialisation(self):
        """Test de l'initialisation du module"""
        auto_corr = AutoCorrectionAvancee(str(self.test_project))
        self.assertIsNotNone(auto_corr)
        self.assertEqual(str(auto_corr.project_path), str(self.test_project))

    def test_analyse_dry_run(self):
        """Test de l'analyse en mode dry-run"""
        # Création d'un fichier de test avec des erreurs
        test_file = self.test_project / "test.py"
        with open(test_file, 'w') as file_handle:
            file_handle.write("""
def test_function():
    value = 1+2
    if value:
        print('Erreur')
    return value
""")
        auto_corr = AutoCorrectionAvancee(str(self.test_project))
        resultats = auto_corr.analyser_et_corriger(dry_run=True)
        self.assertIsInstance(resultats, dict)
        self.assertIn("resultats", resultats)

    def test_generation_rapport(self):
        """Test de génération de rapport"""
        auto_corr = AutoCorrectionAvancee(str(self.test_project))
        resultats = {"resultats": [], "details": []}
        rapport = auto_corr.generer_rapport(resultats)
        self.assertIsInstance(rapport, str)
        self.assertIn("Rapport d'Auto-Correction", rapport)

if __name__ == "__main__":
    unittest.main()
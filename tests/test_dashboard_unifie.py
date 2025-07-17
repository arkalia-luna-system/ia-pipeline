#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import os
import sys
import shutil
import unittest
try:
    from modules.dashboard_unifie import DashboardUnifie
except ModuleNotFoundError:
    DashboardUnifie = None

"""Tests pour le module de dashboard unifié"""

# Ajout du chemin des modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@unittest.skipIf(DashboardUnifie is None, "Module dashboard_unifie manquant")
class TestDashboardUnifie(unittest.TestCase):
    """Tests pour le dashboard unifié"""

    def setUp(self):
        """Configuration des tests"""
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_dashboard.db")

    def tearDown(self):
        """Nettoyage après les tests"""
        shutil.rmtree(self.temp_dir)

    def test_initialisation(self):
        """Test de l'initialisation du dashboard"""
        dashboard = DashboardUnifie(self.db_path)
        self.assertIsNotNone(dashboard)
        self.assertEqual(dashboard.db_path, self.db_path)

    def test_enregistrement_metrique(self):
        """Test de l'enregistrement d'une métrique"""
        dashboard = DashboardUnifie(self.db_path)
        dashboard.enregistrer_metrique("latence", 85.5, "ms")
        metriques = dashboard.obtenir_metriques_temps_reel()
        self.assertIsInstance(metriques, dict)

    def test_enregistrement_evenement(self):
        """Test de l'enregistrement d'un événement"""
        dashboard = DashboardUnifie(self.db_path)
        dashboard.enregistrer_evenement("erreur", "connexion", "timeout")
        metriques = dashboard.obtenir_metriques_temps_reel()
        self.assertIsInstance(metriques, dict)

    def test_generation_rapport(self):
        """Test de génération de rapport consolidé"""
        dashboard = DashboardUnifie(self.db_path)
        # Ajout de données de test
        dashboard.enregistrer_metrique("latence", 90.0, "ms")
        dashboard.enregistrer_evenement("erreur", "connexion", "timeout")
        dashboard.enregistrer_rapport("erreur", "connexion", "Rapport de test", 85, 90)
        rapport = dashboard.generer_rapport_consolide()
        self.assertIsInstance(rapport, str)
        self.assertIn("Dashboard Unifié", rapport)

    def test_generation_html(self):
        """Test de génération du dashboard HTML"""
        dashboard = DashboardUnifie(self.db_path)
        # Ajout de données de test
        dashboard.enregistrer_metrique("latence", 90.0, "ms")
        dashboard.enregistrer_evenement("erreur", "connexion", "timeout")
        html_file = dashboard.generer_dashboard_html("test_dashboard.html")
        self.assertTrue(os.path.exists(html_file))

if __name__ == "__main__":
    unittest.main()